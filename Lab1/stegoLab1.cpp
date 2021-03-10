#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

string mainFile = "inp.txt";
string method1 = "1.txt";
string method2 = "2.txt";
string method3 = "3.txt";

void pars(string& s);
string addSpace(string s);
void AtoB(string& chiperText);
void embed(string& text, string s);
void replaceSymbol(string& text, string s);
void OutToFile(string text, string fileName);

int main()
{

    string text1, text2, text3, chiperText = "Безопасност";
    cout << int(chiperText[2]);
     AtoB(chiperText);
     pars(text1);
     pars(text3);
     embed(text1, chiperText);//первый метод
     text2=addSpace(chiperText); // второй метод
     replaceSymbol(text3, chiperText);// третий метод
     OutToFile(text1,method1);
     OutToFile(text2,method2);
     OutToFile(text3,mathod3);

}

void embed(string& text, string s)
{
    int k = 0;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '1')
        {
            k = text.find("е");
            if (k == -1) { cout << "Недостаточно текста для встраивания"; }
            text[k] = 'e';
        }
        else
        {
            k = text.find("с");
            if (k == -1) { cout << "Недостаточно текста для встраивания"; }
            text[k] = 'c';
        }
    }
}
string addSpace(string s)
{
    string a, text;
    int i = 0;
    ifstream file(mainFile.c_str());
    while (!file.eof())
    {
        getline(file, a);
        if (i <= s.size())
        {
            if (s[i] == '1') a += " ";
            else a += "  ";
            i++;
        }
        a += "\n";
        text += a;
    }
    file.close();
    return text;
}
void pars(string& s)
{
    string a, text;
    ifstream file(mainFile.c_str());
    while (!file.eof())
    {
        getline(file, a);
        a += "\n";
        text += a;
    }
    file.close();
    s = text;
}
void replaceSymbol(string& text, string s)
{
    int k = 0;
    char x[2];
    x[0] = char(133);// 133 это код "...";
    string z = x;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '1')
        {
            k = text.find(".");
            if (k == -1) { cout << "Недостаточно текста для встраивания"; break; }
            text.replace(k, 1, z);
        }
        else
        {
            k = text.find(char(45));
            if (k == -1) { cout << "Недостаточно текста для встраивания"; break; }
            text[k] = char(150);
        }
    }
}
void OutToFile(string text, string fileName)
{
    ofstream ff(fileName.c_str());
    ff << text;
    ff.close();
}
void AtoB(string& chiperText)
{
    char x[10];
    string bin;
    for (int i = 0; i < chiperText.size(); i++)
    {
        itoa(int(chiperText[i]), x, 2);
        bin += x;

    }
    chiperText = bin;
}
