import pypdf

def FindinDict(punctuationds and special characters):
      for key in punctuations.key():
           try:
                 value=punctuations[key]
           except:
                 continue
           if key==special characters:
                 return value
          if insistance(value, dict):
                 x=FindinDict (punctuations,special characters)  
                 if x is not none:
                        return x

pdfobject=open('Data extraction.pdf' , 'rb')
pdf=pypdf.PdfFileReader(pdfobject)
