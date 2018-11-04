cidade = str(input('Digite uma cidade entre as opções abaixo:\nCuritiba\nMaringá\nLondrina\nPinhais\nChapecó\nJoinville\nBlumenau\nFlorianópolis\nPorto Alegre\nGramado\n ')).strip().lower()
if 'curitiba' in cidade:
    print('É do estado do PR.\nÉ capital.')
else:
    if 'maringá' in cidade:
        print('É do estado do PR.\nNão é capital.')
    else:
        if 'londrina' in cidade:
            print('É do estado do PR.\nNão é capital.')
        else:
            if 'pinhais' in cidade:
                print('É do estado do PR.\nNão é capital.')
            else:
                if 'chapecó' in cidade:
                    print('É do estado de SC.\nNão é capital.')
                else:
                    if 'joinville' in cidade:
                        print('É do estado de SC.\nNão é capital.')
                    else:
                        if 'blumenau' in cidade:
                            print('É do estado de SC.\nNão é capital.')
                        else:
                            if 'florianópolis' in cidade:
                                print('É do estado de SC.\nÉ capital.')
                            else:
                                if 'porto alegre' in cidade:
                                    print('É do estado do RS.\nÉ capital.')
                                else:
                                    if 'gramado' in cidade:
                                        print('É do estado do RS.\nNão é capital.')
                                    else:
                                        print('Verifique a grafia.')
                                        print('obs: é necessário colocar acentos.')


