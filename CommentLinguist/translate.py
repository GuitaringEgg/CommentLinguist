import azure_translate_api

class translate():
  def __init__(self, client_id, client_secret):
    self.bing = azure_translate_api.MicrosoftTranslatorClient('pythontest',  # make sure to replace client_id with your client id
                                                              'y32l8f0X5rq1G+5O9ayNk7p7zI1hHUh57VaoHXYMEzU=a') # replace the client secret with the client secret for you app.

    if self.bing.TranslateText("This is just a test", 'en', 'en').find("TranslateApiException") != -1:
      print "Well shit. It's not translating again."
      exit()

  # Translate a pythono file's comment from source_lang to target_lang, and save as .translate.py
  def translate_py(self, file_name, source_lang, target_lang):
    # Open files
    f = open(file_name, "r")
    o = open(file_name[:file_name.rfind(".")]+".translated" + file_name[file_name.rfind("."):], "w")

    # Inialise some variables
    translation = ""
    in_comment_block = False

    for line in f:
      # If we are already in a comment block, continue translating
      # If we find the end of the block, just write the line
      if in_comment_block:
        if line.find('"""') != -1:
            in_comment_block = False
            o.write(line)
        else:
          if line.isspace():
            o.write(line)
          else:
            translation = self.bing.TranslateText(line[:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
            o.write(translation + "\n")

      else:
        # If we find a block comment line, start translating if we are not already in a block
        if line.find('"""') != -1:
          if not in_comment_block:
            in_comment_block = True
            translation = self.bing.TranslateText(line[line.find('"""')+3:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
            o.write(line[0: line.find('"""')+3] + translation + "\n")

        # If we find a single line comment, translate the comment bit and print out the
        # line with the newly translated bit
        elif line.find("#") != -1:
          translation = self.bing.TranslateText(line[line.find("#")+1:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
          o.write(line[0: line.find("#")+1] + translation + "\n")

        # Otherwise just print the line without translation
        else:
          o.write(line)
    f.close()
    o.close()


  # Translate a c++ file's comments from one language to another, and save it as .translate.cpp
  def translate_cpp(self, file_name, source_lang, target_lang):
    # Open files
    f = open(file_name, "r")
    o = open(file_name[:file_name.rfind(".")]+".translated" + file_name[file_name.rfind("."):], "w")

    # Inialise some variables
    translation = ""
    in_comment_block = False

    for line in f:
      # If we are already in a comment block, continue translating
      # If we find the end of the block, just write the line
      if in_comment_block:
        if line.find('*/') != -1:
            in_comment_block = False
            o.write(line)
        else:
          if line.isspace():
            o.write(line)
          else:
            translation = self.bing.TranslateText(line[:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
            o.write(translation + "\n")

      else:
        # If we find a block comment line, start translating if we are not already in a block
        if line.find('/*') != -1:
          if not in_comment_block:
            in_comment_block = True
            translation = self.bing.TranslateText(line[line.find('/*')+2:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
            o.write(line[0: line.find('/*')+2] + translation + "\n")

        # If we find a single line comment, translate the comment bit and print out the
        # line with the newly translated bit
        elif line.find("//") != -1:
          translation = self.bing.TranslateText(line[line.find("//")+2:-1], source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/")[1:-1]
          o.write(line[0: line.find("//")+2] + translation + "\n")

        # Otherwise just print the line without translation
        else:
          o.write(line)

  # Doesn't really work just now
  def translate_batch_py(self, file_name, source_lang, target_lang):
    # Open files
    f = open(file_name, "r")
    o = open(file_name[:file_name.rfind(".")]+".translated" + file_name[file_name.rfind("."):], "w")

    # Inialise some variables
    in_comment_block = False
    output = []
    needs_translating = []

    for line in f:
      # If we are already in a comment block, continue translating
      # If we find the end of the block, just write the line
      if in_comment_block:
        if line.find('"""') != -1:
            in_comment_block = False
            output.append(line)
        else:
          if line.isspace():
            output.append(line)
          else:
            needs_translating.append(line)
            output.append("")

      else:
        # If we find a block comment line, start translating if we are not already in a block
        if line.find('"""') != -1:
          if not in_comment_block:
            in_comment_block = True
            needs_translating.append(line)
            output.append("")

        # If we find a single line comment, translate the comment bit and print out the
        # line with the newly translated bit
        elif line.find("#") != -1:
          needs_translating.append(line)
          output.append("")

        # Otherwise just print the line without translation
        else:
          output.append(line)

    translation = self.bing.TranslateText(' ^ | ^ '.join(needs_translating), source_lang, target_lang).decode("ascii", "ignore").replace("\/", "/").replace('\\"', '"').replace("\\u000a", '\n')[1:-1].split("^ | ^")
    print translation

    i = 0
    for line in output:
      if line == "":
        o.write(translation[i] + "\n")
        i += 1
      else:
        o.write(line)



    f.close()
    o.close()
