%define rname lxx74

Summary: A Linux Printer Driver for Lexmark X74 All In One
Name: printer-driver-lxx74
Version: 0.8.4.2
Release: alt1
License: GPLv2
Group: System/Configuration/Printing
Url: http://home.online.no/~enrio/
# site is dead
Source: %rname-%version.tar.gz

BuildRequires: libcups-devel zlib-devel
Requires: cups

%description
A Linux Printer Driver for Lexmark X74 All In One

The driver also works with:
 o Lexmark X75

The driver also should work with:
 o Compaq  - IJ670 Series, Inkjet Printer
 o Lexmark - Inkjet 4104, Inkjet Printer, Lexmark X76, Lexmark Z13,
             Lexmark Z14, Lexmark Z23-Z33, Lexmark Z24-Z34, Lexmark Z25-Z35
 o Samsung - MJC-940_2200_530, MJC-950_2130_530

This package contains CUPS drivers (PPD) for the following printers:

 o Compaq IJ670
 o Compaq Inkjet Printer
 o Lexmark All In One
 o Lexmark Inkjet Printer
 o Lexmark X74
 o Lexmark X75
 o Lexmark X76
 o Lexmark Z13
 o Lexmark Z14
 o Lexmark Z23
 o Lexmark Z24
 o Lexmark Z25
 o Lexmark Z33
 o Lexmark Z34
 o Lexmark Z35
 o Samsung MJC-2130
 o Samsung MJC-2200
 o Samsung MJC-530
 o Samsung MJC-940
 o Samsung MJC-950
 o Lexmark All In One

%prep
%setup -n %rname-%version

%build
%make

gunzip lxx74.ppd.gz
cp lxx74.ppd Compaq-IJ670-lxx74.ppd
perl -p -i -e 's/All In One/IJ670/gi' Compaq-IJ670-lxx74.ppd
cp lxx74.ppd Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/Lexmark/Compaq/gi' Compaq-*-lxx74.ppd
cp lxx74.ppd Lexmark-X74-lxx74.ppd
perl -p -i -e 's/All In One/X74/gi' Lexmark-X74-lxx74.ppd
cp lxx74.ppd Lexmark-X75-lxx74.ppd
perl -p -i -e 's/All In One/X75/gi' Lexmark-X75-lxx74.ppd
cp lxx74.ppd Lexmark-X76-lxx74.ppd
perl -p -i -e 's/All In One/X76/gi' Lexmark-X76-lxx74.ppd
cp lxx74.ppd Lexmark-Z13-lxx74.ppd
perl -p -i -e 's/All In One/Z13/gi' Lexmark-Z13-lxx74.ppd
cp lxx74.ppd Lexmark-Z14-lxx74.ppd
perl -p -i -e 's/All In One/Z14/gi' Lexmark-Z14-lxx74.ppd
cp lxx74.ppd Lexmark-Z23-lxx74.ppd
perl -p -i -e 's/All In One/Z23/gi' Lexmark-Z23-lxx74.ppd
cp lxx74.ppd Lexmark-Z33-lxx74.ppd
perl -p -i -e 's/All In One/Z33/gi' Lexmark-Z33-lxx74.ppd
cp lxx74.ppd Lexmark-Z24-lxx74.ppd
perl -p -i -e 's/All In One/Z24/gi' Lexmark-Z24-lxx74.ppd
cp lxx74.ppd Lexmark-Z34-lxx74.ppd
perl -p -i -e 's/All In One/Z34/gi' Lexmark-Z34-lxx74.ppd
cp lxx74.ppd Lexmark-Z25-lxx74.ppd
perl -p -i -e 's/All In One/Z25/gi' Lexmark-Z25-lxx74.ppd
cp lxx74.ppd Lexmark-Z35-lxx74.ppd
perl -p -i -e 's/All In One/Z35/gi' Lexmark-Z35-lxx74.ppd
cp lxx74.ppd Lexmark-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Lexmark-Inkjet_Printer-lxx74.ppd
cp lxx74.ppd Lexmark-InkJet_4104-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet 4104/gi' Lexmark-Inkjet_4104-lxx74.ppd
cp lxx74.ppd Samsung-MJC-940-lxx74.ppd
perl -p -i -e 's/All In One/MJC-940/gi' Samsung-MJC-940-lxx74.ppd
cp lxx74.ppd Samsung-MJC-950-lxx74.ppd
perl -p -i -e 's/All In One/MJC-950/gi' Samsung-MJC-950-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2200-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2200/gi' Samsung-MJC-2200-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2130-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2130/gi' Samsung-MJC-2130-lxx74.ppd
cp lxx74.ppd Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/All In One/MJC-530/gi' Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/Lexmark/Samsung/gi' Samsung-*-lxx74.ppd
gzip -9 *.ppd

%install
install -d %buildroot%_sysconfdir/cups
install -d %buildroot%_libdir/cups/filter
install -d %buildroot%_datadir/cups/data
install -d %buildroot%_datadir/cups/model/%rname

install -m0755 rasterto%rname %buildroot%_libdir/cups/filter/rasterto%rname.bin
install -m0644 self-portrait.out.gz %buildroot%_datadir/cups/data/self-portrait.out.gz

cat << EOF > %buildroot%_libdir/cups/filter/rasterto%rname
#!/bin/bash
export self_portrait="%_datadir/cups/data/self-portrait.out.gz"
exec %_libdir/cups/filter/rasterto%rname.bin "\$@"
EOF
chmod 755 %buildroot%_libdir/cups/filter/rasterto%rname

install -m0644 %rname.types %buildroot%_sysconfdir/cups/
install -m0644 %rname.convs %buildroot%_sysconfdir/cups/
install -m0644 *.ppd* %buildroot%_datadir/cups/model/%rname/

%files
%config(noreplace) %_sysconfdir/cups/%rname.convs
%config(noreplace) %_sysconfdir/cups/%rname.types
%_libdir/cups/filter/rasterto%rname.bin
%_libdir/cups/filter/rasterto%rname
%_datadir/cups/data/self-portrait.out*
%dir %_datadir/cups/model/%rname
%_datadir/cups/model/%rname/%rname.ppd*
%_datadir/cups/model/%rname/Compaq-IJ670-%rname.ppd*
%_datadir/cups/model/%rname/Compaq-Inkjet_Printer-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-InkJet_4104-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Inkjet_Printer-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-X74-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-X75-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-X76-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z13-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z14-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z23-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z24-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z25-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z33-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z34-%rname.ppd*
%_datadir/cups/model/%rname/Lexmark-Z35-%rname.ppd*
%_datadir/cups/model/%rname/Samsung-MJC-2130-%rname.ppd*
%_datadir/cups/model/%rname/Samsung-MJC-2200-%rname.ppd*
%_datadir/cups/model/%rname/Samsung-MJC-530-%rname.ppd*
%_datadir/cups/model/%rname/Samsung-MJC-940-%rname.ppd*
%_datadir/cups/model/%rname/Samsung-MJC-950-%rname.ppd*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.8.4.2-alt1
- Initial build for ALT

