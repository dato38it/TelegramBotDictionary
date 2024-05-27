from translate import Translator
translator=Translator(from_lang="russian", to_lang="english")
translation=translator.translate("Привет. Как дела?")
print(translation)
