import tkinter as tk
import matplotlib.pyplot as plt

class Contract:
    def __init__(self, _buysell = 1, _callput = 1, _strike_price = -1, _contract_price = -1.0):
        self.buysell = _buysell  # buy = 1, sell = -1
        self.callput = _callput  # call = 1, put = -1
        self.strike_price = _strike_price
        self.contract_price = _contract_price
    def __attrs(self):
        return (self.buysell, self.callput, self.strike_price, self.contract_price)
    def __hash__(self):
        return hash(self.__attrs())
    def __repr__(self):
        return f"{('Buy' if self.buysell == 1 else 'Sell')} {self.strike_price} {('C' if self.callput == 1 else 'P')}, ${self.contract_price}"
    def __str__(self):
        return f"{('Buy' if self.buysell == 1 else 'Sell')} {self.strike_price} {('C' if self.callput == 1 else 'P')}, ${self.contract_price}"
    def __lt__(self, other):
        if self.buysell != other.buysell:
            return self.buysell > other.buysell
        if self.callput != other.callput:
            return self.callput > other.callput
        return self.strike_price < other.strike_price
    def __eq__(self, other):
        if self.buysell != other.buysell:       
            return False
        if self.callput != other.callput:
            return False
        if self.strike_price != other.strike_price:
            return False
        if self.contract_price != other.contract_price:
            return False
        return True
            

contract_dict = {}  #[Contract(1, 1, 100, 10), Contract(-1, -1, 200, 100)]

def plot_result():
    mn = 100000000
    mx = -100000000
    final_prices = []
    profit = []
    pay, get = 0, 0
    for each_contract in contract_dict:
        if each_contract.buysell == 1:
            pay += each_contract.contract_price
        else:
            get += each_contract.contract_price
        
        if mn > each_contract.strike_price:
            mn = each_contract.strike_price
        if mx < each_contract.strike_price:
            mx = each_contract.strike_price
    
    diff = (max(pay, get)-3)//50+1
    mn = max(mn//50-diff-1, 0) * 50
    mx = (mx//50+diff+1) * 50
    
    while mn <= mx:
        final_prices.append(mn)
        mn += 50
        
    for each_price in final_prices:
        profit_at_price = 0
        for each_contract in contract_dict:
            if each_contract.buysell == 1 and each_contract.callput == 1:
                profit_at_price += max(each_price - each_contract.strike_price, 0) * contract_dict[each_contract]
            elif each_contract.buysell == 1 and each_contract.callput == -1:
                profit_at_price += max(each_contract.strike_price - each_price, 0) * contract_dict[each_contract]
            elif each_contract.buysell == -1 and each_contract.callput == 1:
                profit_at_price -= max(each_price - each_contract.strike_price, 0) * contract_dict[each_contract]
            elif each_contract.buysell == -1 and each_contract.callput == -1:
                profit_at_price -= max(each_contract.strike_price - each_price, 0) * contract_dict[each_contract]
            profit_at_price += (each_contract.buysell * (-1) * each_contract.contract_price * contract_dict[each_contract])
        profit.append(profit_at_price*50)
    plt.figure(figsize= [5.375, 4.375], dpi = 128)
    plt.plot(final_prices, [0 for i in range(len(profit))], "--")
    plt.plot(final_prices, profit, "bo-")
    plt.savefig("plot_img.png", format = "png")
    #plt.show()

def info_canvas_redraw(canvas : tk.Canvas):
    canvas.delete("all")
    
    # format of table
    column_width = [57, 57, 57, 57, 57]
    sum_width = [0]
    for i in range(5):
        sum_width.append(sum_width[i] + column_width[i] + 1)
    title_height = 40
    
    global contract_dict
    contract_dict = dict(sorted(contract_dict.items()))
    
    canvas.create_rectangle(0, 2, sum_width[5]-1, title_height, width = 0, fill = "#F70")
    canvas.create_text((sum_width[0]+sum_width[1])/2-1, title_height/2+1, text = "Buy/Sell", anchor = "center", font = ("Consolas", 9))
    canvas.create_text((sum_width[1]+sum_width[2])/2-1, title_height/2+1, text = "Call/Put", anchor = "center", font = ("Consolas", 9))
    canvas.create_text((sum_width[2]+sum_width[3])/2-1, title_height/2+1, text = "口數", anchor = "center", font = ("Consolas", 10))
    canvas.create_text((sum_width[3]+sum_width[4])/2-1, title_height/2+1, text = "履約價", anchor = "center", font = ("Consolas", 10))
    canvas.create_text((sum_width[4]+sum_width[5])/2-1, title_height/2+1, text = " 選擇權 \n當前價位", anchor = "center", font = ("Consolas", 10))
    
    sz = len(contract_dict)
    cnt = 0
    for each_contract in contract_dict:
        if cnt % 2 == 0:
            canvas.create_rectangle(0, cnt*20+title_height+1, sum_width[5]-1, cnt*20+title_height+19, width = 0, fill = "#FFF")
        else:
            canvas.create_rectangle(0, cnt*20+title_height+1, sum_width[5]-1, cnt*20+title_height+19, width = 0, fill = "#FED")
        text_to_print = ""
        if each_contract.buysell == 1:
            text_to_print = "Buy"
            canvas.create_rectangle(10, cnt*20+title_height+1, sum_width[1]-11, cnt*20+title_height+19, width = 0, fill = "#F77")
        else:
            text_to_print = "Sell"
            canvas.create_rectangle(10, cnt*20+title_height+1, sum_width[1]-11, cnt*20+title_height+19, width = 0, fill = "#7F7")
        canvas.create_text((sum_width[0]+sum_width[1])/2-1, cnt*20+title_height+10, text = text_to_print, anchor = "center", font = ("Consolas", 10))
        
        if each_contract.callput == 1:
            text_to_print = "Call"
            canvas.create_rectangle(sum_width[1]+10, cnt*20+title_height+1, sum_width[2]-11, cnt*20+title_height+19, width = 0, fill = "#F77")
        else:
            text_to_print = "Put"
            canvas.create_rectangle(sum_width[1]+10, cnt*20+title_height+1, sum_width[2]-11, cnt*20+title_height+19, width = 0, fill = "#7F7")
        canvas.create_text((sum_width[1]+sum_width[2])/2-1, cnt*20+title_height+10, text = text_to_print, anchor = "center", font = ("Consolas", 10))
        
        text_to_print = str(contract_dict[each_contract])
        canvas.create_text((sum_width[2]+sum_width[3])/2-1, cnt*20+title_height+10, text = text_to_print, anchor = "center", font = ("Consolas", 10))
        
        text_to_print = str(each_contract.strike_price)
        canvas.create_text((sum_width[3]+sum_width[4])/2-1, cnt*20+title_height+10, text = text_to_print, anchor = "center", font = ("Consolas", 10))
        
        text_to_print = str(each_contract.contract_price)
        canvas.create_text((sum_width[4]+sum_width[5])/2-1, cnt*20+title_height+10, text = text_to_print, anchor = "center", font = ("Consolas", 10))
        
        cnt += 1
    
    for i in range(1, 5):
        canvas.create_line(sum_width[i]-1, 2, sum_width[i]-1, sz*20+title_height-1)
    
    canvas.config(scrollregion = (0, 0, 229, sz*20+title_height))
        

def add_contract(_buysell, _callput, _strike_price, _contract_price, _amnt = 1) -> bool:
    if _buysell != 1 and _buysell != -1:
        tk.messagebox.showwarning("Add contract failed", "Invalid value \"buysell\"!")
        return False
    if _callput != 1 and _callput != -1:
        tk.messagebox.showwarning("Add contract failed", "Invalid value \"callput\"!")
        return False
    if _strike_price % 50 != 0:
        tk.messagebox.showwarning("Add contract failed", "Invalid value! (strike_price%50 != 0)")
        return False
    if _contract_price < 0:
        tk.messagebox.showwarning("Add contract failed", "Invalid value! (contract_price < 0)!")
        return False
    c = Contract(_buysell, _callput, _strike_price, _contract_price)
    if c in contract_dict:
        if contract_dict[c] + _amnt < 0:
            tk.messagebox.showwarning("Add contract failed", "Invalid value! (total amnt <= 0)!")
            return False
        contract_dict[c] += _amnt
    else:
        if _amnt <= 0:
            tk.messagebox.showwarning("Add contract failed", "Invalid value! (amnt <= 0)!")
            return False
        contract_dict[c] = _amnt
    #tk.messagebox.showinfo("Add contract succeeded", f"Add contract ({Contract(_buysell, _callput, _strike_price, _contract_price)}) * {_amnt} succeeded.")
    if contract_dict[c] == 0:
        contract_dict.pop(c)
    return True


def main():
    main_window = tk.Tk()
    main_window.title("選擇權組合單損益試算程式")
    window_length, window_width = 1000, 750
    main_window.geometry(f"{window_length}x{window_width}+30+30")
    main_window.minsize(1000, 750)
    main_window.resizable(True, True)
    
    # frame 1 : contract info of options(buy/sell, call/put, strike price, price)
    frame_L = tk.Frame(main_window, width = 310, height = 562, bg = "#FFF")
    
    info_canvas = tk.Canvas(frame_L, width = 289, height = 562, bg = "#FFF", scrollregion = (0, 0, 229, 562))
    
    info_canvas_redraw(info_canvas)
    
    info_scrollbar = tk.Scrollbar(frame_L, orient = "vertical")    # 建立滾動條
    info_scrollbar.pack(side='right', fill='y')  # 將滾動條加在右側，垂直填滿
    info_scrollbar.config(command=info_canvas.yview)    # 設定 scrollbar 綁定 text 的 yview
    def _on_mousewheel(event):
        event.widget.yview_scroll(int(-1*(event.delta/120)), "units")
    info_canvas.bind("<MouseWheel>", _on_mousewheel)
    info_canvas.pack()
    #info_canvas.pack_propagate(0)
    
    frame_L.grid(row = 0, column = 0)
    frame_L.grid_propagate(0)
    
    # frame 2 : chart
    frame_R = tk.Frame(main_window, width = 690, height = 562, bg = "#BBB")
    img_canvas = tk.Canvas(frame_R, width = 688, height = 560)
    img_canvas.pack()
    frame_R.grid(row = 0, column = 1)
    frame_R.grid_propagate(0)
    
    # frame 3 : add/remove contracts
    frame_D = tk.Frame(main_window, width = 1000, height = 188, bg = "#666")
    
    buysell_label = tk.Label(frame_D, text = "買進/賣出：", font = ("Consolas", 10))
    buysell_entry = tk.Entry(frame_D, width = 25)
    buysell_label.place(relx = 0.05, rely = 0.1, anchor = "w")
    buysell_entry.place(relx = 0.25, rely = 0.1, anchor = "center")
    callput_label = tk.Label(frame_D, text = "買權/賣權：", font = ("Consolas", 10))
    callput_entry = tk.Entry(frame_D, width = 25)
    callput_label.place(relx = 0.05, rely = 0.3, anchor = "w")
    callput_entry.place(relx = 0.25, rely = 0.3, anchor = "center")
    strike_price_label = tk.Label(frame_D, text = "履約價：", font = ("Consolas", 10))
    strike_price_entry = tk.Entry(frame_D, width = 25)
    strike_price_label.place(relx = 0.05, rely = 0.5, anchor = "w")
    strike_price_entry.place(relx = 0.25, rely = 0.5, anchor = "center")
    contract_price_label = tk.Label(frame_D, text = "選擇權價格：", font = ("Consolas", 10))
    contract_price_entry = tk.Entry(frame_D, width = 25)
    contract_price_label.place(relx = 0.05, rely = 0.7, anchor = "w")
    contract_price_entry.place(relx = 0.25, rely = 0.7, anchor = "center")
    amnt_label = tk.Label(frame_D, text = "口數：", font = ("Consolas", 10))
    amnt_entry = tk.Entry(frame_D, width = 25)
    amnt_label.place(relx = 0.05, rely = 0.9, anchor = "w")
    amnt_entry.place(relx = 0.25, rely = 0.9, anchor = "center")
    
    def clear_text():
        buysell_entry.delete(0, tk.END)
        callput_entry.delete(0, tk.END)
        amnt_entry.delete(0, tk.END)
        strike_price_entry.delete(0, tk.END)
        contract_price_entry.delete(0, tk.END)
    clear_button = tk.Button(frame_D, text = "清除填寫", font = ("Consolas", 10), command = clear_text)
    clear_button.place(relx = 0.4, rely = 0.5)
    
    def confirm_text():
        try:
            buysell_val = buysell_entry.get()
            if buysell_val.lower() == "buy" or buysell_val.lower() == "b":
                buysell_val = 1
            elif buysell_val.lower() == "sell" or buysell_val.lower() == "s":
                buysell_val = -1
            elif buysell_val == "0":
                buysell_val = -1
            elif buysell_val == "-1" or buysell_val == "1":
                buysell_val = int(buysell_val)
            else:
                raise ValueError("buysell")
            callput_val = callput_entry.get()
            if callput_val.lower() == "call" or callput_val.lower() == "c":
                callput_val = 1
            elif callput_val.lower() == "put" or callput_val.lower() == "p":
                callput_val = -1
            elif callput_val == "0":
                callput_val = -1
            elif callput_val == "-1" or callput_val == "1":
                callput_val = int(callput_val)
            else:
                raise ValueError("callput")
            
            amnt_val = amnt_entry.get()
            if amnt_val == "":
                amnt_val = 1
            else:
                amnt_val = int(amnt_val)
            strike_price_val = int(strike_price_entry.get())
            contract_price_val = int(contract_price_entry.get())
        except ValueError as e:
            tk.messagebox.showwarning("Invalid num", e)
            return
        if add_contract(buysell_val, callput_val, strike_price_val, contract_price_val, amnt_val):
            clear_text()
            info_canvas_redraw(info_canvas)
            plot_result()
            plot_img = tk.PhotoImage(file = "plot_img.png")
            img_canvas.create_image(0, 0, anchor = "nw", image = plot_img)
            img_canvas.image = plot_img
            
    confirm_button = tk.Button(frame_D, text = "確認輸入", font = ("Consolas", 10), command = confirm_text)
    confirm_button.place(relx = 0.4, rely = 0.25)
    confirm_button.bind_all("<Return>", lambda _ : confirm_text())
    
    # clear all button
    def clear_all():
        clear_text()
        contract_dict.clear()
        info_canvas_redraw(info_canvas)
        plot_result()
        plot_img = tk.PhotoImage(file = "plot_img.png")
        img_canvas.create_image(0, 0, anchor = "nw", image = plot_img)
        img_canvas.image = plot_img
    clear_all_button = tk.Button(frame_D, text = "清除全部", font = ("Consolas", 10), command = clear_all)
    clear_all_button.place(relx = 0.7, rely = 0.5)
    
    
    
    frame_D.grid(row = 1, column = 0, columnspan = 2)
    
    main_window.mainloop()


if __name__ == "__main__":
    main()