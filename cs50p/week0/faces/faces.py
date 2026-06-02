def convert(cry_out):
    return cry_out.replace(":)", "🙂").replace(":(", "🙁")

cry_out = input()


print(convert(cry_out))
