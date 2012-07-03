Name:		XORSearch
Version:	1.6.0
%define		_ver 1_6_0
Release:	alt1
License:	Public domain
Group:		File tools
Summary:	Search for a given string in an XOR, ROL or ROT encoded binary file
URL:		http://blog.didierstevens.com/programs/xorsearch/
Source:		http://www.didierstevens.com/files/software/XORSearch_V%{_ver}.zip

# Automatically added by buildreq on Tue Jul 13 2010
BuildRequires: unzip

%description
XORSearch is a program to search for a given string in an XOR, ROL or ROT  encoded binary file. An XOR encoded binary file is a file where some (or all) bytes have been XORed with a constant value (the key). A ROL (or ROR) encoded file has its bytes rotated by a certain number of bits (the key). A ROT encoded file has its alphabetic characters (A-Z and a-z) rotated by a certain number of positions. XOR and ROL/ROR encoding is used by malware programmers to obfuscate strings like URLs.

XORSearch will try all XOR keys (0 to 255),  ROL keys (1 to 7) and ROT keys (1 to 25) when searching. I programmed XORSearch to include key 0, because this allows to search in an unencoded binary file (X XOR 0 equals X).

If the search string is found, XORSearch will print it until the 0 (byte zero) is encountered or until 50 characters have been printed, which ever comes first. 50 is the default value, it can be changed with option -l. Unprintable characters are replaced by a dot.

%prep
%setup -cq
echo "%description" > o
%build
gcc %name.c -o %name

%install
install -D %name %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Tue Jul 13 2010 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Initial build for ALT

