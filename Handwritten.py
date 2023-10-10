# Make Handwritten assignments- convert text to handwriting using python.
# pip install pywhatkit 
# pip install pywhatkit==4.6 when generate error => Unable to access Pywhatkit api right now
import pywhatkit as pw

t = ("""just wanted to add to the answers, a group of data is expected to be in a sequence, so you can match each section of the grouped data without skipping over a data because if a word is skipped from a sentence, we may not refer to the sentence as one group anymore, see the below example for more clarification, however, the compile method is deprecated.""")
pw.text_to_handwriting(t,"demo2.png",[255,0,0])
print(" END ")

