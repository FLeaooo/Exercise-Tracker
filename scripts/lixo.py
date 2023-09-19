"""
[sg.Frame('Volume de exercicios (3x) semanal', [
    [sg.Text('Total exercicios semanais das costas: '), sg.Input(size=(6, 1), key='-IN_VOL_BASE_COSTA-'),
     sg.Button('Inserir', expand_x=True, key='-BUT_VOL_BASE_COSTA-')],
    [sg.Table(headings=volume_base[0], values=volume_base[1:], expand_x=True, key='-TABLE_VOL_BASE-')]
], expand_x=True)],


    if event == '-BUT_VOL_BASE_COSTA-':
        volume_base = atribui_volumes_base_costas(values['-IN_VOL_BASE_COSTA-'])
        window['-TABLE_VOL_BASE-'].update(values=volume_base[1:])

def atribui_volumes_base_costas(volume_costas):
    # Cria uma lista para ser (musculo e volume)
    musc_volume = []
    volume_base_aux = volume_base[:]
    for musculo in lista_musculos:
        # adiciona o musculo na lista
        musc_volume.append(musculo)

        # adiciona o volume com base no musculo
        if musculo == 'Costas':
            musc_volume.append(int(volume_costas))
        elif musculo == 'Perna':
            musc_volume.append(int(volume_costas) + 1)
        elif musculo in ['Peito', 'Ombros']:
            musc_volume.append(int(volume_costas) - 1)
        elif musculo in ['Bíceps', 'Tríceps', 'Antebraço', 'Panturilha', 'Abdômen']:
            musc_volume.append(int(volume_costas) - 2)

        volume_base_aux.append(musc_volume[:])
        musc_volume.clear()

    return volume_base_aux


"""