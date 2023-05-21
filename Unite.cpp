#include "PDFWriter.h"
#include "PDFModifiedPage.h"
#include "AbstractContentContext.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace PDFHummus;

int main() {

	std::string inPath = "";
	std::string outPath = "";
	std::cout << "Enter document filepath: ";
	std::cin >> inPath;
	std::cout << std::endl; 

	std::cout << "Enter output filepath: ";
	std::cin >> outPath;
	std::cout << std::endl;

	PDFWriter pdfWriter;
	pdfWriter.ModifyPDF(inPath, ePDFVersion13, outPath);

	pdfWriter.EndPDF();

	std::cout << "It works!" << std::endl;

	return 0;
}
