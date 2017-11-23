import pyautogui


#Mapa de botoes: onde esta "", colocar key to teclado configurado no emulador (snes9x)
key={"A": pyautogui.press("a"),"B": pyautogui.press("b"),"X": pyautogui.press("x"),
         "Y": pyautogui.press("y"),"Left": pyautogui.press("left"),"Right": pyautogui.press("right"),
         "Up": pyautogui.press("Up"), "Down": pyautogui.press("Down"), "Start": pyautogui.press("i"),
         "Select": pyautogui.press("u"),"Restart": pyautogui.press("f2")}
    
    
key.get("A")
