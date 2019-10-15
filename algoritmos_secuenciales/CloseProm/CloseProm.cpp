//
// Created by Santiago Baena Rivera on 14/10/19.
//

#include "CloseProm.h"
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int main(){

  ifstream fin("../../data/Data2017Empresa.csv");

  if(!fin){
    
    cout << "File not open\n";
    return 1;
    
  }

  vector<Stock> stock;

  string line;
  const char delim = ';';

  while(getline(fin, line)){

    istringstream ss(line);
    Stock stock;
    ss >> stock.date;
    cout << stock.date;
    ss.ignore(10, delim);
    //getline(ss, stock, ';');
    ss >> stock.high;
    cout << stock.date;

  }
}



