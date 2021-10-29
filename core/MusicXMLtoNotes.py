# from xml.dom import minidom
import xml.etree.ElementTree as ET

# parse an xml file by name
#mydoc = minidom.parse('items.xml')
# mydoc = minidom.parse('SenoritaShort_v1.xml')
# tree = ET.parse('SenoritaShort_v1.xml')
# root = tree.getroot()
#items = mydoc.getElementsByTagName('item')
# measures = mydoc.getElementsByTagName('measure')
# notes = mydoc.getElementsByTagName('note')
# steps = mydoc.getElementsByTagName('step')
# durations = mydoc.getElementsByTagName('duration')
# note_types = mydoc.getElementsByTagName('type')
# note_octaves = mydoc.getElementsByTagName('octave')


# one specific item attribute
#print('Measure #2 attribute:')
#print(measures[1].attributes['number'].value)
# all items data
# for elem in steps:
#     print(elem.firstChild.data)
# for  idx, elem in enumerate(steps):
#     print("["+str(idx)+"]"+elem.firstChild.data)
#     if(elem.firstChild.data == 'E'):
#         result_lyre_song += "q"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'F'):
#         result_lyre_song += "w"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'G'):
#         result_lyre_song += "e"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'A'):
#         result_lyre_song += "r"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'B'):
#         result_lyre_song += "t"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'C'):
#         result_lyre_song += "y"+str(durations[idx].firstChild.data)+" "
#     elif(elem.firstChild.data == 'D'):
#         result_lyre_song += "u"+str(durations[idx].firstChild.data)+" "
#     else:
#         result_lyre_song += ""    
# print('\n Durations:')
# for elem in notes:
#     print(elem.firstChild.data)
    
# print('\n Lyre Song:\n')
# print(result_lyre_song)

## Expansion Genshin Clefs ##
genshin_g_clef = {
    'C5' : 'q',
    'D5' : 'w',
    'E5' : 'e',
    'F5' : 'r',
    'G5' : 't',
    'A5' : 'y',
    'B5' : 'u',
}
genshin_alto_clef = {
    'C4' : 'z',
    'D4' : 'x',
    'E4' : 'c',
    'F4' : 'v',
    'G4' : 'b',
    'A4' : 'n',
    'B4' : 'm',
}
genshin_c_clef = {
    'C3' : 'a',
    'D3' : 's',
    'E3' : 'd',
    'F3' : 'f',
    'G3' : 'g',
    'A3' : 'h',
    'B3' : 'j',
}
genshin_clefs = {
    'C5' : 'q',
    'D5' : 'w',
    'E5' : 'e',
    'F5' : 'r',
    'G5' : 't',
    'A5' : 'y',
    'B5' : 'u',
    'C4' : 'z',
    'D4' : 'x',
    'E4' : 'c',
    'F4' : 'v',
    'G4' : 'b',
    'A4' : 'n',
    'B4' : 'm',
    'C3' : 'a',
    'D3' : 's',
    'E3' : 'd',
    'F3' : 'f',
    'G3' : 'g',
    'A3' : 'h',
    'B3' : 'j',
    'REST' : 'i',
}

def fetchXmlTreeRoot(xml_filename):
    tree_xml = ET.parse(xml_filename)
    tree_root = tree_xml.getroot()
    return tree_root

def createFileWithContent(givenContent, givenOutputName):
    with open(output_file_location+givenOutputName, "w") as text_file:
        print(f"{givenContent}", file=text_file)

def convertRootToNotesSignature(xml_tree_root):
    xml_tree_music_part = xml_tree_root.findall('part')
    sheet_settings = ""
    sheet_clef = "1"
    measure_beat_type = "1"
    result_analyse_sheet = ""
    result_note_song = ""
    for part in xml_tree_music_part:
        xml_tree_measures = part.findall('measure')
        if((xml_tree_measures != [])) :
            for measure in xml_tree_measures:
                current_messure_clef = ""
                print("\n## Measure ##")
                xml_tree_measure_attributes = measure.findall('attributes')
                if((xml_tree_measure_attributes != [])) :
                    # print("xml_tree_measure_attributes")
                    # print(xml_tree_measure_attributes)
                    for idx, attribute in enumerate(xml_tree_measure_attributes):
                        note_duration = attribute.find('duration')
                        xml_tree_measure_attributes_divisions = attribute.find('divisions')
                        if(xml_tree_measure_attributes_divisions != None) :
                            print("[measure_attribute] "+'divisions\t\t= '+ str(xml_tree_measure_attributes_divisions.text))
                            result_analyse_sheet +="\n"+"[measure_attribute] "+'divisions\t\t= '+ str(xml_tree_measure_attributes_divisions.text)
                        xml_tree_measure_attributes_key = attribute.find('key')
                        if(xml_tree_measure_attributes_key != None) :
                            xml_tree_measure_attributes_key_fifths = xml_tree_measure_attributes_key.find('fifths')
                            if(xml_tree_measure_attributes_key_fifths != None) :
                                print("[measure_attribute] "+'key-fifths\t\t= '+ str(xml_tree_measure_attributes_key_fifths.text))
                                result_analyse_sheet +="\n"+"[measure_attribute] "+'key-fifths\t\t= '+ str(xml_tree_measure_attributes_key_fifths.text)
                        xml_tree_measure_attributes_time = attribute.find('time')
                        if(xml_tree_measure_attributes_time != None) :
                            xml_tree_measure_attributes_time_beats = xml_tree_measure_attributes_time.find('beats')
                            if(xml_tree_measure_attributes_time_beats != None) :
                                print("[measure_attribute] "+'time-beats\t\t= '+ str(xml_tree_measure_attributes_time_beats.text))
                                result_analyse_sheet +="\n"+"[measure_attribute] "+'time-beats\t\t= '+ str(xml_tree_measure_attributes_time_beats.text)
                                # sheet_settings += str(xml_tree_measure_attributes_time_beats.text)
                            xml_tree_measure_attributes_time_beat_type = xml_tree_measure_attributes_time.find('beat-type')
                            if(xml_tree_measure_attributes_time_beat_type != None) :
                                print("[measure_attribute] "+'time-beat-type\t= '+str(xml_tree_measure_attributes_time_beat_type.text))
                                result_analyse_sheet +="\n"+"[measure_attribute] "+'time-beat-type\t= '+str(xml_tree_measure_attributes_time_beat_type.text)
                                measure_beat_type = str(xml_tree_measure_attributes_time_beat_type.text)
                                # sheet_settings += "_"+str(xml_tree_measure_attributes_time_beat_type.text)
                        xml_tree_measure_attributes_clef = attribute.find('clef')
                        if(xml_tree_measure_attributes_clef != None) :
                            xml_tree_measure_attributes_clef_sign = xml_tree_measure_attributes_clef.find('sign')
                            if(xml_tree_measure_attributes_clef_sign != None) :
                                print("[measure_attribute] "+'clef-sign\t\t= '+ str(xml_tree_measure_attributes_clef_sign.text))
                                result_analyse_sheet +="\n"+"[measure_attribute] "+'clef-sign\t\t= '+ str(xml_tree_measure_attributes_clef_sign.text)
                                # sheet_settings += str(xml_tree_measure_attributes_clef_sign.text)
                            xml_tree_measure_attributes_clef_line = xml_tree_measure_attributes_clef.find('line')
                            if(xml_tree_measure_attributes_clef_line != None) :
                                print("[measure_attribute] "+'clef-line\t\t= '+str(xml_tree_measure_attributes_clef_line.text))
                                result_analyse_sheet +="\n"+"[measure_attribute] "+'clef-line\t\t= '+str(xml_tree_measure_attributes_clef_line.text)
                xml_tree_measure_notes = measure.findall('note')
                if(xml_tree_measure_notes != []) :

                    for idx, note in enumerate(xml_tree_measure_notes):
                        note_duration = note.find('duration')
                        note_time_signature = round((eval(note_duration.text) / eval(measure_beat_type) ) * 1000)
                        if(note_duration != None) :
                            print("\n["+str(idx)+"]"+'duration\t= '+ str(note_duration.text)+ ' tick')
                            print("["+str(idx)+"]"+'signature\t= '+ str(note_time_signature)+ '')
                            result_analyse_sheet +="\n"+"\n["+str(idx)+"]"+'duration\t= '+ str(note_duration.text)+ ' tick'
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+'signature\t= '+ str(note_time_signature)+ ''
                        xml_tree_rest = note.find('rest')
                        if(xml_tree_rest != None) :
                            print("["+str(idx)+"]"+'rest found')
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+'rest found'
                            print("["+str(idx)+"]"+ str(xml_tree_rest.text))
                            result_note_song += "REST_"+str(note_time_signature)+" "
                        #define note pitch
                        xml_tree_pitch = note.find('pitch')
                        if(xml_tree_pitch != None) :
                            xml_tree_pitch_step = xml_tree_pitch.find('step')
                            if(xml_tree_pitch_step != None) :
                                print("["+str(idx)+"]"+'pitch-step\t= ' + str(xml_tree_pitch_step.text))
                                result_analyse_sheet +="\n"+"["+str(idx)+"]"+'pitch-step\t= ' + str(xml_tree_pitch_step.text)
                                xml_tree_pitch_step_value = str(xml_tree_pitch_step.text)
                            xml_tree_pitch_octave = xml_tree_pitch.find('octave')
                            if(xml_tree_pitch_octave != None) :
                                print("["+str(idx)+"]"+'pitch-octave\t= '+ str(xml_tree_pitch_octave.text))
                                result_analyse_sheet +="\n"+"["+str(idx)+"]"+'pitch-octave\t= '+ str(xml_tree_pitch_octave.text)
                                xml_tree_pitch_octave_value = str(xml_tree_pitch_octave.text)
                            if((xml_tree_pitch_octave != None) & (xml_tree_pitch_step != None)) :
                                result_note_song += str(xml_tree_pitch_step_value)+str(xml_tree_pitch_octave_value)+'_'+str(note_time_signature)+" "
                        #define note type
                        xml_tree_type = note.find('type')
                        if(xml_tree_type != None) :
                            print("["+str(idx)+"]"+'type\t\t= '+ str(xml_tree_type.text))
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+'type\t\t= '+ str(xml_tree_type.text)
                        #define note octave
                        xml_tree_octave = note.find('octave')
                        if(xml_tree_octave != None) :
                            print("["+str(idx)+"]"+'octave found')
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+'octave found'
                            print("["+str(idx)+"]"+ str(xml_tree_octave.text))
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+ str(xml_tree_octave.text)
                        #define note tie
                        xml_tree_tie = note.find('tie')
                        if(xml_tree_tie != None) :
                            print("["+str(idx)+"]"+'tie found')
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+'tie found'
                            print("["+str(idx)+"]"+ str(xml_tree_tie.text))
                            result_analyse_sheet +="\n"+"["+str(idx)+"]"+ str(xml_tree_tie.text)
        createFileWithContent(result_analyse_sheet, 'result_analyse_sheet.txt')
        print('\n \n Converted Sheet Settings: ' + sheet_settings)
    return result_note_song
def convertSongSignatureToGenshin(song_signature) :
    result_sheet_lyre_song = song_signature
    for pitch, lyre_key in genshin_clefs.items():
        result_sheet_lyre_song = result_sheet_lyre_song.replace(pitch.upper(), lyre_key)
    return result_sheet_lyre_song

print('\n\n STARTING CODE \n\n')
#fetchedTreeRoot = fetchXmlTreeRoot('SenoritaShort_v1.xml')
## Global Variables
input_location="sheets_xml/"
input_sheetname="Duet_for_Piano_and_Violin"
input_sheetname="SenoritaShort_v4"
input_sheetname="SenoritaShort_v1"
input_sheetname="SenoritaXML"
input_extension=".xml"
output_file_location = "converted_to_genshin/"
output_file_name = str(input_sheetname)+'.txt'

##UsingCore Methods
fetchedTreeRoot = fetchXmlTreeRoot(input_location+input_sheetname+input_extension)
# fetchedTreeRoot = fetchXmlTreeRoot("sheets_xml/SenoritaShort_v4.xml")
# convertedLyreSong = convertRootToNotesDuration(fetchedTreeRoot)
convertedSheetSongSignature = convertRootToNotesSignature(fetchedTreeRoot)
convertedLyreSongSignature = convertSongSignatureToGenshin(convertedSheetSongSignature)

##Program Ouputs
# print('\n \n Converted Lyre Song: ' + convertedLyreSong)
# createFileWithContent(convertedLyreSong,output_file_name);
# print('\n \n Converted Sheet Signature : ' + convertedSheetSongSignature)
createFileWithContent(convertedSheetSongSignature,(output_file_name+'_full_signature'));
print('\n \n Converted Lyre Signature : ' + convertedLyreSongSignature)
createFileWithContent(convertedLyreSongSignature,(output_file_name+'_lyre'));

##TERMINATION
print('\n\n END OF CODE \n\n')