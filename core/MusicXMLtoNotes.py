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



def fetchXmlTreeRoot(xml_filename):
    tree_xml = ET.parse(xml_filename)
    tree_root = tree_xml.getroot()
    return tree_root

def convertRootToLyre(xml_tree_root):
    xml_tree_music_part = xml_tree_root.findall('part')
    result_lyre_song = ""
    for part in xml_tree_music_part:
        xml_tree_measure = part.findall('measure')
        for measure in xml_tree_measure:
            xml_tree_measure_notes = measure.findall('note')
            for idx, note in enumerate(xml_tree_measure_notes):
                xml_tree_duration = note.find('duration')
                xml_tree_duration_value = "";
                if(xml_tree_duration != None) :
                    if(int(xml_tree_duration.text) >  (3*9)):
                        xml_tree_duration_value = str(int(xml_tree_duration.text)-(3*9)) + " I9 I9 I9"
                    elif(int(xml_tree_duration.text) >  (2*9)):
                        xml_tree_duration_value = str(int(xml_tree_duration.text)-(2*9)) + " I9 I9"
                    elif(int(xml_tree_duration.text) >  (9)):
                        xml_tree_duration_value = str(int(xml_tree_duration.text)-9) + " I9"
                    else : 
                        xml_tree_duration_value = xml_tree_duration.text;
                    print("["+str(idx)+"]"+'duration '+ str(xml_tree_duration.text)+ ' ')
                xml_tree_rest = note.find('rest')
                if(xml_tree_rest != None) :
                    print("["+str(idx)+"]"+'rest found')
                    result_lyre_song += "I"+str(xml_tree_duration_value)+" "
                xml_tree_pitch = note.find('pitch')
                if(xml_tree_pitch != None) :
                    #print("["+str(idx)+"]"+'pitch found')
                    #print("["+str(idx)+"]"+'xml_tree_pitch =>'+str(xml_tree_pitch))
                    xml_tree_pitch_step = xml_tree_pitch.find('step')
                    #xml_tree_pitch_step_value = str(xml_tree_pitch_step.text)
                    
                    if(xml_tree_pitch_step.text == 'E'):
                        result_lyre_song += "q"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'F'):
                        result_lyre_song += "w"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'G'):
                        result_lyre_song += "e"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'A'):
                        result_lyre_song += "r"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'B'):
                        result_lyre_song += "t"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'C'):
                        result_lyre_song += "y"+str(xml_tree_duration_value)+" "
                    elif(xml_tree_pitch_step.text == 'D'):
                        result_lyre_song += "u"+str(xml_tree_duration_value)+" "
                    else:
                        result_lyre_song += ""
                    #print("["+str(idx)+"]"+'xml_tree_pitch_step found')
                    #print("["+str(idx)+"]"+'xml_tree_pitch_step =>'+str(xml_tree_pitch_step))
                    #print("["+str(idx)+"]"+'xml_tree_pitch_step_value =>'+str(xml_tree_pitch_step_value))
                    xml_tree_pitch_octave = xml_tree_pitch.find('octave')
                    xml_tree_pitch_octave_value = str(xml_tree_pitch_octave.text)
                    #result_lyre_song += str(xml_tree_pitch_step_value)+str(xml_tree_duration.text)+" "
                    #print("["+str(idx)+"]"+'xml_tree_pitch_octave found')
                    #print("["+str(idx)+"]"+'xml_tree_pitch_octave =>'+str(xml_tree_pitch_octave))
                    #print("["+str(idx)+"]"+'xml_tree_pitch_octave_value =>'+str(xml_tree_pitch_octave.text))
                xml_tree_type = note.find('type')
                if(xml_tree_type != None) :
                    #print("["+str(idx)+"]"+'type found')
                    print("["+str(idx)+"]"+ str(xml_tree_type.text))
                xml_tree_octave = note.find('octave')
                if(xml_tree_octave != None) :
                    print("["+str(idx)+"]"+'octave found')
                xml_tree_tie = note.find('tie')
                if(xml_tree_tie != None) :
                    print("["+str(idx)+"]"+'tie found')
                xml_tree_rest = note.find('rest')
                if(xml_tree_rest != None) :
                    print("["+str(idx)+"]"+'rest found')
                # if(xml_tree_step.text == 'E'):
                #     result_lyre_song += "q"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'F'):
                #     result_lyre_song += "w"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'G'):
                #     result_lyre_song += "e"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'A'):
                #     result_lyre_song += "r"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'B'):
                #     result_lyre_song += "t"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'C'):
                #     result_lyre_song += "y"+str(xml_tree_duration.text)+" "
                # elif(xml_tree_step.text == 'D'):
                #     result_lyre_song += "u"+str(xml_tree_duration.text)+" "
                # else:
                #     result_lyre_song += ""
    return result_lyre_song
    # segments = []
    # for elem in xml_tree_root: #Access all measurements (segments)
    #     segment = []
    #     for note in elem.findall('note'):
    #         segment.append(note.attrib)
    #     segments.append(segment)
    # return segments

def convertRootToNotesDuration(xml_tree_root):
    xml_tree_music_part = xml_tree_root.findall('part')
    result_note_song = ""
    for part in xml_tree_music_part:
        xml_tree_measures = part.findall('measure')
        if((xml_tree_measures != [])) :
            for measure in xml_tree_measures:
                print("\n## Measure ##")
                xml_tree_measure_attributes = measure.findall('attributes')
                if((xml_tree_measure_attributes != [])) :
                    print("xml_tree_measure_attributes")
                    print(xml_tree_measure_attributes)
                    # xml_tree_measure_clef_sign = xml_tree_measure_clef.find('sign')
                    # if(xml_tree_measure_clef_sign != None) :
                    #         print("["+str(idx)+"]"+'clef-sign\t= '+ str(xml_tree_measure_clef_sign.text))
                    # xml_tree_measure_clef_line = xml_tree_measure_clef.find('line')
                    # if(xml_tree_measure_clef_line != None) :
                    #         print("["+str(idx)+"]"+'clef-line\t= '+str(xml_tree_measure_clef_line.text))
                xml_tree_measure_notes = measure.findall('note')
                if(xml_tree_measure_notes != []) :
                    # print("xml_tree_measure_notes")
                    # print(xml_tree_measure_notes)
                    for idx, note in enumerate(xml_tree_measure_notes):
                        xml_tree_duration = note.find('duration')
                        if(xml_tree_duration != None) :
                            print("\n["+str(idx)+"]"+'duration\t= '+ str(xml_tree_duration.text)+ ' tick')
                        xml_tree_rest = note.find('rest')
                        if(xml_tree_rest != None) :
                            print("["+str(idx)+"]"+'rest found')
                            print("["+str(idx)+"]"+ str(xml_tree_rest.text))
                            result_note_song += "I"+str(xml_tree_duration.text)+" "
                        #define note pitch
                        xml_tree_pitch = note.find('pitch')
                        if(xml_tree_pitch != None) :
                            xml_tree_pitch_step = xml_tree_pitch.find('step')
                            if(xml_tree_pitch_step != None) :
                                print("["+str(idx)+"]"+'pitch-step\t= ' + str(xml_tree_pitch_step.text))
                                xml_tree_pitch_step_value = str(xml_tree_pitch_step.text)
                            xml_tree_pitch_octave = xml_tree_pitch.find('octave')
                            if(xml_tree_pitch_octave != None) :
                                print("["+str(idx)+"]"+'pitch-octave\t= '+ str(xml_tree_pitch_octave.text))
                                xml_tree_pitch_octave_value = str(xml_tree_pitch_octave.text)
                            if((xml_tree_pitch_octave != None) & (xml_tree_pitch_step != None)) :
                                result_note_song += str(xml_tree_pitch_step_value)+str(xml_tree_pitch_octave_value)+'_'+str(xml_tree_duration.text)+" "
                        #define note type
                        xml_tree_type = note.find('type')
                        if(xml_tree_type != None) :
                            print("["+str(idx)+"]"+'type\t\t= '+ str(xml_tree_type.text))
                        #define note octave
                        xml_tree_octave = note.find('octave')
                        if(xml_tree_octave != None) :
                            print("["+str(idx)+"]"+'octave found')
                            print("["+str(idx)+"]"+ str(xml_tree_octave.text))
                        #define note tie
                        xml_tree_tie = note.find('tie')
                        if(xml_tree_tie != None) :
                            print("["+str(idx)+"]"+'tie found')
                            print("["+str(idx)+"]"+ str(xml_tree_tie.text))
    return result_note_song

print('\n\n STARTING CODE \n\n')
#fetchedTreeRoot = fetchXmlTreeRoot('SenoritaShort_v1.xml')
## Global Variables
input_location="sheets_xml/"
input_sheetname="SenoritaShort_v4"
input_extension=".xml"
output_file_location = "converted_to_genshin/"
output_file_name = str(input_sheetname)+'.txt'

##Core Methods
# fetchedTreeRoot = fetchXmlTreeRoot(input_location+input_sheetname+input_extension)
fetchedTreeRoot = fetchXmlTreeRoot("sheets_xml/SenoritaShort_v4.xml")
# convertedLyreSong = convertRootToLyre(fetchedTreeRoot)
convertedLyreSong = convertRootToNotesDuration(fetchedTreeRoot)

##Program Ouputs
print('\n \n Converted Lyre Song: ' + convertedLyreSong)
with open(output_file_location+output_file_name, "w") as text_file:
    print(f"{convertedLyreSong}", file=text_file)

##TERMINATION
print('\n\n END OF CODE \n\n')