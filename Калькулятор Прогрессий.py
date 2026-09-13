import tkinter
from tkinter import ttk

def IsNumber(String):
    String = String.strip()
    try:
        return int(String)
    except ValueError:
        return 0


def GetGeometricProgression(StartNumber, Step, Distans):
    Progression = {}
    for Index in range(1, Distans + 1):
        Progression[Index] = StartNumber * (Step ** (Index - 1))
    return Progression

def GetSumGeometricProgression(StartNumber, Step, Distans):
    if Step == 1:
        return StartNumber * Distans
    return StartNumber * (Step**Distans - 1) / (Step - 1)


def GetArefmeticProgression(StartNumber, Step, Distans):
    Progression = {}
    for Index in  range(1, Distans+1):
        Progression[Index] = StartNumber + Step*(Index-1)
    return Progression

def GetSumArefmeticProgression(StartNumber, Step, Distans):
    return (2*StartNumber + Step*(Distans -1))/2*Distans

def PrintArefmeticProgression(StartNumber, Step, Distans):
    print()
    print("Арифметическая прогрессия:")
    for Index, Object in GetArefmeticProgression(StartNumber, Step, Distans).items():
        print(Index, ": ", Object, sep = "")
    print()
    print("Сумма:", GetSumArefmeticProgression(StartNumber, Step, Distans))

    
def PrintGeometricProgression(StartNumber, Step, Distans):
    print()
    print("Геометрическая прогрессия:")
    for Index, Object in GetGeometricProgression(StartNumber, Step, Distans).items():
        print(Index, ": ", Object, sep = "")
    print()
    print("Сумма:", GetSumGeometricProgression(StartNumber, Step, Distans))

def MonitorArefmeticProgression(StartNumber, Step, Distans):
    OutputText.insert(tkinter.END, "Арифметическая прогрессия:\n")
    for Index, Object in GetArefmeticProgression(
        StartNumber, Step, Distans
    ).items():
        OutputText.insert(tkinter.END, f"{Index}: {Object}\n")
    OutputText.insert(
        tkinter.END,
        f"\nСумма: {GetSumArefmeticProgression(StartNumber, Step, Distans)}\n\n",
    )


def MonitorGeometricProgression(StartNumber, Step, Distans):
    OutputText.insert(tkinter.END, "Геометрическая прогрессия:\n")
    for Index, Object in GetGeometricProgression(
        StartNumber, Step, Distans
    ).items():
        OutputText.insert(tkinter.END, f"{Index}: {Object}\n")
    OutputText.insert(
        tkinter.END,
        f"\nСумма: {GetSumGeometricProgression(StartNumber, Step, Distans)}\n\n",
    )

# Функция обработки кнопки расчёта
def OnCalculate():
    # Очищаем поле вывода перед новым расчетом
    OutputText.delete("1.0", tkinter.END)

    # Считываем данные из полей ввода вашим IsNumber
    StartNumber = IsNumber(EntryStart.get())
    Step = IsNumber(EntryStep.get())
    Distans = int(IsNumber(EntryDistans.get()))

    Progression = ComboProgression.get()

    if Progression == "Арифметическая":
        MonitorArefmeticProgression(StartNumber, Step, Distans)
    elif Progression == "Геометрическая":
        MonitorGeometricProgression(StartNumber, Step, Distans)
    else:
        MonitorArefmeticProgression(StartNumber, Step, Distans)
        MonitorGeometricProgression(StartNumber, Step, Distans)
#создаём окно
Window = tkinter.Tk()
Window.title("Калькулятор прогрессий")
Window.geometry("400x520")

# Выбор типа прогрессии
LabelProg = ttk.Label(Window, text="Выберите прогрессию:")#окно текста
LabelProg.pack(pady=(10, 2))
ComboProgression = ttk.Combobox(Window, values=["Арифметическая", "Геометрическая"], state="readonly") #создаём окно выбора
ComboProgression.current(0)# по умолчанию арефметическая
ComboProgression.pack(fill="x", padx=20)#на всю длинну


# Поле: Начальное число
LabelStart = ttk.Label(Window, text="Начальное число:")#текст с верху
LabelStart.pack(pady=(10, 2))
EntryStart = ttk.Entry(Window)#поле
EntryStart.insert(0, "1")#по умолчанию
EntryStart.pack(fill="x", padx=20)

# Поле: Шаг
LabelStep = ttk.Label(Window, text="Шаг:")
LabelStep.pack(pady=(10, 2))
EntryStep = ttk.Entry(Window)
EntryStep.insert(0, "2")
EntryStep.pack(fill="x", padx=20)

# Поле: Длина
LabelDist = ttk.Label(Window, text="Длина:")
LabelDist.pack(pady=(10, 2))
EntryDistans = ttk.Entry(Window)
EntryDistans.insert(0, "10")
EntryDistans.pack(fill="x", padx=20)

# Кнопка расчета
BtnCalc = ttk.Button(Window, text="Рассчитать", command=OnCalculate)#кнопка
BtnCalc.pack(pady=15, fill="x", padx=20)

# Окно вывода результатов
OutputText = tkinter.Text(Window, height=12, font=("Courier", 9))#поле
OutputText.pack(fill="both", expand=True, padx=20, pady=(0, 15))
Window.mainloop()#чтоб программа не закрывалась