import speech_recognition as sr

import commands

command_list = ['ip','open','calculate','goodbye','volume']
r = sr.Recognizer()
run = True
while(run):
    try:
        with sr.Microphone(0) as source2:
            r.adjust_for_ambient_noise(source2, duration=1)
            
            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            if 'george' in MyText:
                for x in range(len(command_list)):
                    if command_list[x] in MyText:
                        if command_list[x] == 'ip':
                            if 'local' in MyText:
                                commands.get_ip('local')
                                break
                            elif 'global' in MyText:
                                commands.get_ip('global')
                                break

                        elif command_list[x] == 'calculate':
                            splited = MyText.split(" ")
                            for y in range(len(splited)):
                                if splited[y] == 'calculate':
                                    commands.Calculate(int(splited[y+1]),splited[y+2],int(splited[y+3]))
                                    break
                        
                        elif command_list[x] == 'open':
                            if 'google' in MyText or 'chrome' in MyText:
                                commands.open_program('google')
                            elif 'firefox' in MyText:
                                commands.open_program('firefox')
                            elif 'minecraft' in MyText or 'hypixel' in MyText:
                                commands.open_program('minecraft')
                            else:
                                splited = MyText.split(" ")
                                for y in range(len(splited)):
                                    if splited[y] == 'open':
                                        commands.open_program(splited[y+1])
                                        break
                        
                        elif command_list[x] == 'volume':
                            if 'up' in MyText:
                                commands.volume_control('up')
                            elif 'down' in MyText:
                                commands.volume_control('down')
                            elif 'mute' in MyText or 'unmute' in MyText:
                                commands.volume_control('mute')

                        elif command_list[x] == 'goodbye':
                            commands.SpeakText('Goodbye')
                            run = False
                        else:
                            print(MyText)

                    elif 'addiction' in MyText and 'hypixel' in MyText:
                        commands.open_program('minecraft')
            else:
                print(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
