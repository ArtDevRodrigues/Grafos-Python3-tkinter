
import tkinter as tk
import colorsys
from lista import Lista
from tkinter import messagebox


root = tk.Tk()
root.title("Grafo")
root['bg'] = "gray"
width = int(root.winfo_screenwidth() * 0.6)
height = int(root.winfo_screenheight() * 0.9)

nodeRadius = 30

font = "Notomono 18"
fontNode = "Notomono 16"

nodesColors = Lista()
nodesCoord = Lista()
edges = Lista()

def update():
    canvas.delete("all")
    for edge in edges:
        x0 = nodesCoord[edge[0]]
        y0 = nodesCoord[edge[1]]
        x1 = nodesCoord[edge[0]]
        y1 = nodesCoord[edge[1]]

        canvas.create_line(x0, y0, x1, y1, fill='white', width = 5)

    for i in range(len(nodesCoord)):
        node = nodesCoord[i]
        x = node[0]
        y = node[1]

        canvas.create_oval(x-nodeRadius , y-nodeRadius , x+nodeRadius , y+nodeRadius , fill=nodesColors[i], outline='grey', width=3)
        canvas.create_text(x, y, text=str(i), font = fontNode)
def addNode(event):
    
    x = int(entryNodeX.get())*100
    y = int(entryNodeY.get())*100
    if x != None or y != None: 

        nodesCoord.append([x,y])

        if(len(nodesColors) != 0 and nodesColors[0] != 'white'):
            nodesColors.clear()
            for i in range(len(nodesCoord)):
                nodesColors.append('white')

        else:
            nodesColors.append('white')
            
        update()

        print ("Adicionado um nó por coordenada", x, y)
    else:
        messagebox.showerror('Campos vasios','Preencha todos os campos!')

def addList(event):
    
    positions = entryListPosition.get()
    stringEmpty = ""
    for index, element in enumerate(positions):
        if element == ";":
            change = False
            x = ""
            y = ""
            for elem in stringEmpty:
                if elem == "(" or elem == ")": pass
                elif elem==",":
                    change = True
                else:
                    if change:
                        y += elem
                    else:
                        x += elem
                
            nodesCoord.append([int(x)*100,int(y)*100])

            if(len(nodesColors) != 0 and nodesColors[0] != 'white'):
                nodesColors.clear()
                for i in range(len(nodesCoord)):
                    nodesColors.append('white')

            else:
                nodesColors.append('white')
                
            update()
            print ("Adicionado um nó por coordenada", x, y)
            stringEmpty = ""
        
        else:
            stringEmpty += element
        
        if index == len(str(positions)) -1 and element != ";":
            change = False
            x = ""
            y = ""
            for elem in stringEmpty:
                if elem == "(" or elem == ")": pass
                elif elem==",":
                    change = True
                else:
                    if change:
                        y += elem
                    else:
                        x += elem
                
            nodesCoord.append([int(x)*100,int(y)*100])

            if(len(nodesColors) != 0 and nodesColors[0] != 'white'):
                nodesColors.clear()
                for i in range(len(nodesCoord)):
                    nodesColors.append('white')
            else:
                nodesColors.append('white')
            update()
            print ("Adicionado um nó por coordenada", x, y)

            stringEmpty = ""

def editNode (evento):
    i = int (entryNodeId.get ())
    x = int (entryNodeX.get ())*100
    y = int (entryNodeY.get ())*100


    if x != None or y != None or i != None :
        nodesCoord [i] [0] = x
        nodesCoord [i] [1] = y
        update()
        print ("Nó alterado com ID", i, "por coordenada", x, y)

    else:
        messagebox.showerror('Campos vasios','Preencha todos os campos!')
  
def removeNode (evento):
    i = int (entryNodeId.get ())
    nodesCoord.pop(i)
    nodesColors.pop(i)
    update ()
    print ("Nó removido por ID", int (entryNodeId.get ()))

   
def addEdge (evento):

    fromNode = int(entryEdgeFrom.get ())
    toNode = int(entryEdgeTo.get ())

    if (len(nodesColors) != 0 and nodesColors[0] != 'white'):

        nodesColors.clear ()
        for i in range(len (nodesCoord)):
            nodesColors.append ('branco')
    edges.append ((fromNode, toNode))
    update ()
    print ("Adicionada uma borda entre", fromNode, "e", toNode)
   


def removeEdge(event):
    fromNode = int(entryEdgeFrom.get())
    toNode = int(entryEdgeTo.get())

    try:
        edges.remove((fromNode, toNode))
    except Exception:
        pass
    try:
        edges.remove((toNode, fromNode))
    except Exception:
        pass
    update()
    print ("Removida a borda entre", int (entryEdgeFrom.get ()), "e", int (entryEdgeTo.get ()))
  

def colorIt(event):
    colors = 1

    isFound = False
    countEdges = len(edges)
    nodesIdColors = []
    for i in range(len(nodesCoord)):
        nodesIdColors.append(0)
    if(countEdges == 0):
        isFound = True
    while(not isFound):
        add = 1
        for j in range(len(nodesCoord)):
            nodesIdColors[j] += add
            add = nodesIdColors[j]//colors
            nodesIdColors[j] = nodesIdColors[j]%colors

        if(add == 1):
            colors+=1
            colorStep = 360/colors
            continue

        isFound = True
        for edge in edges:
            if(nodesIdColors[edge[0]] == nodesIdColors[edge[1]]):
                isFound = False

    hueStep = 1/colors
    hue = 0
    saturation = 1
    value = 1
    print(nodesColors)
    print(len(nodesColors))
    colorRGB = [0,0,0]
    for i in range(len(nodesColors)):
        nodeIdColor = nodesIdColors[i]
        red = 0
        green = 0
        blue = 0
        hue = hueStep*nodeIdColor

        colorNorRGB = colorsys.hsv_to_rgb(hue,saturation,value)
        print(colorNorRGB)
        colorStr = ''
        for j in range(3):
            colorRGB[j] = int(255*colorNorRGB[j]+0.4)
        print(colorRGB)
        print(hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2]))
        print(hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2])[2:])
        colorStr += hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2])[2:]
        while(len(colorStr) < 6):
            colorStr = '0' + colorStr
        colorStr = '#' + colorStr
        print(colorStr)
        print(i)
        nodesColors[i] = colorStr
    print(nodesColors)
    update()
    print("Pintado!")
def vanish(event):
    nodesCoord.clear()
    edges.clear()
    update()
    print("Liberado!")



frame = tk.Frame(root, width=int(width * 0.25), height=int(height*0.5), bg='gray', bd=5, relief='ridge')
canvas = tk.Canvas(root, width=int(width * 0.75), height=height, bg='#a3a3a3', bd=5, relief='ridge')

canvas.pack(side=tk.LEFT)
frame.pack(side=tk.RIGHT)

d = 9
labelCoord = tk.Label(frame, text="  Coordenadas  ",font=font)
labelNodeX = tk.Label(frame, text="X:"+" "*d,font=font)
labelNodeY = tk.Label(frame, text="Y:"+" "*d, font=font)
labelNodeId = tk.Label(frame, text="ID:"+" "*d, font=font)
labelEdgeFrom = tk.Label(frame, text="De:"+" "*d, font=font)
labelEdgeTo = tk.Label(frame, text="Para:"+" "*d, font=font)
labelListPosition = tk.Label(frame, text=" Posicoes:"+" "*7, font=font)
label01 = tk.Label(frame,background="gray")
label02 = tk.Label(frame,background="gray")
label03 = tk.Label(frame,background="gray")

buttonAddNode = tk.Button (frame, text = "  Adicionar Nó ", font = font)
buttonEditNode = tk.Button (frame, text = "   Editar Nó   ", font = font)
buttonRemoveNode = tk.Button (frame, text = "   Remover Nó  ", font = font)
buttonAddEdge = tk.Button (frame, text = "Adicionar Borda", font = font)
buttonRemoveEdge = tk.Button (frame, text = " Remover borda ", font = font)
buttonColorIt = tk.Button (frame, text = "     Paint     ", font = font)
buttonVanish = tk.Button (frame, text = "  Limpar campo ", font = font)
buttonAddList = tk.Button(frame,text="Adicionar Lista",font= font)

entryNodeId = tk.Entry(frame, font=font)
entryNodeX = tk.Entry(frame, font=font)
entryNodeY = tk.Entry(frame, font=font)
entryEdgeFrom = tk.Entry(frame, font=font)
entryEdgeTo = tk.Entry(frame, font=font)
entryListPosition = tk.Entry(frame, font=font)

labelCoord.grid(row=1, column=1,columnspan=2)
labelNodeId.grid(row=2, column=1)
labelNodeX.grid(row=3, column=1)
labelNodeY.grid(row=4, column=1)
labelEdgeFrom.grid(row=7, column=1)
labelEdgeTo.grid(row=8, column=1)
labelListPosition.grid(row=14,column=1)
label01.grid(row=6,column=1,columnspan=2)
label02.grid(row=9,column=1,columnspan=2)
label03.grid(row=13,column=1,columnspan=2)

buttonAddNode.grid(row=5, column=2)
buttonEditNode.grid(row=10, column=1)
buttonRemoveNode.grid(row=10, column=2)
buttonAddEdge.grid(row=11, column=1)
buttonRemoveEdge.grid(row=11, column=2)
buttonColorIt.grid(row=12, column=1)
buttonVanish.grid(row=12, column=2)
buttonAddList.grid(row=15,column=2)


entryNodeId.grid(row=2, column=1, columnspan=2)
entryNodeX.grid(row=3, column=1, columnspan=2)
entryNodeY.grid(row=4, column=1, columnspan=2)
entryEdgeFrom.grid(row=7,column=1, columnspan=2)
entryEdgeTo.grid(row=8,column=1, columnspan=2)
entryListPosition.grid(row=14,column=2)

buttonAddNode.bind("<Button-1>", addNode)
buttonEditNode.bind("<Button-1>", editNode)
buttonRemoveNode.bind("<Button-1>", removeNode)
buttonAddEdge.bind("<Button-1>", addEdge)
buttonRemoveEdge.bind("<Button-1>", removeEdge)
buttonColorIt.bind("<Button-1>", colorIt)
buttonVanish.bind("<Button-1>", vanish)
buttonAddList.bind("<Button-1>", addList)

root.mainloop()