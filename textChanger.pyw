from pynput import keyboard
import pyperclip


ENG_RU = {
			'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г',
			'i':'ш', 'o':'щ', 'p':'з', '[':'х', ']':'ъ', 'a':'ф', 's':'ы',
			'd':'в', 'f':'а', 'g':'п', 'h':'р', 'j':'о', 'k':'л', 'l':'д',
			';':'ж', "'":"э", 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и',
			'n':'т', 'm':'ь', ',':'б', '.':'ю', '/':'.', '?':',', '<':'б', '>':'ю',
			':':'ж','"':'э','{':'х','}':'ъ'
																		  }
RU_ENG = {v:k for k,v in ENG_RU.items()}

def change(ENG_RU, RU_ENG):
	changed=''
	for i in pyperclip.paste().lower():
		try:
			changed+=ENG_RU[i]
		except KeyError:
			try:
				changed+=RU_ENG[i]
			except KeyError:
				changed+=i
	print(f"Текст изменен на: {changed}")
	pyperclip.copy(changed)



def on_activate_c():
    change(ENG_RU, RU_ENG)

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+c': on_activate_c, 
        '<ctrl>+<alt>+<esc>': exit}) as h:
    h.join()
