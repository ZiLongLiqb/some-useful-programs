from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def mergePdf(infilelist,outfile):
	pdfFileWriter=PdfFileWriter()
	for infile in infilelist:
		pdfReader=PdfFileReader(open(infile,"rb"))
		numpages=pdfReader.getNumPages()
		for index in range(0,numpages):
			pageobj=pdfReader.getPage(index)
			pdfFileWriter.addPage(pageobj)
		pdfFileWriter.write(open(outfile,"wb"))

rootdir=r'your dir'
'''list_=os.listdir(rootdir)
path=[]
for i in range(len(list_)):
	path.append(os.path.join(rootdir,"%d.pdf"%(i+1)))
out_=os.path.join(rootdir,"out.pdf")

print(out_,path)'''

path=[]
path.append(os.path.join(rootdir,"AQM.pdf"))
path.append(os.path.join(rootdir,"16.pdf"))
out_=os.path.join(rootdir,"out2.pdf")
mergePdf(path,out_)