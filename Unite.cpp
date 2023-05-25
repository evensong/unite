#include "PDFWriter.h"
#include "PDFModifiedPage.h"
#include "AbstractContentContext.h"

#include <iostream>
#include <fstream>
#include <string>
#include <map>

void test(std::map<std::string, std::string> &dict) { // test that dictionary is correctly formatted and outputs correct translations

	std::string userPhrase = "";
	while (userPhrase != "quit") {
		std::cout << "Enter an English phrase or type \"quit\" to exit: ";
		std::cin >> userPhrase;
		std::cout << std::endl;
		if (userPhrase == "quit") {
			std::cout << "Goodbye!" << std::endl;
		}
		else {
			try {
				std::cout << dict[userPhrase] << std::endl;
			}
			catch (std::out_of_range) {
				std::cout << "Phrase not found in dictionary." << std::endl;
			}

		}
	}
	
}

int main() {

	std::map<std::string, std::string> dict; //this will hold our mapping of english words/phrases to spanish

	try {
		std::ifstream inputFile;
		inputFile.open("dictionary.txt");

		while (!inputFile.eof()) {
			char english[256], spanish[256];

			inputFile.getline(english, 256, ':');
			inputFile.getline(spanish, 256);

			dict[english] = spanish;

			if (!inputFile.good() && !inputFile.eof()) {
				throw(inputFile.rdstate());
			}
		}
		inputFile.close();
	}
	catch (std::ios_base::iostate error) {
		std::cout << "Enountered an error setting up dictionary. Error code: " << error << std::endl;
		return error;
	}

	//Get filepaths from user
	char inPath[256], outPath[256]; // buffers for user input

	std::cout << "Enter document filepath: ";
	std::cin.getline(inPath, 256);
	std::cout << std::endl; 

	std::cout << "Enter output filepath: ";
	std::cin.getline(outPath, 256);
	std::cout << std::endl;



	
	PDFWriter pdfWriter;
	pdfWriter.ModifyPDF(inPath, ePDFVersion13, outPath);

	pdfWriter.EndPDF();
	

	test(dict);
	
	return 0;
}
