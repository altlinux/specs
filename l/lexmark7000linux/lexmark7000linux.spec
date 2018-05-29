Name: lexmark7000linux
Version: 990516
Release: alt1
License: GPL
Group: System/Configuration/Printing

URL: http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/olddrv.html
# site is dead
# Source: http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/%name-%version.tar.bz2
Source: %name-%version.tar

Summary: Lexmark 7xxx and 57zzz printer driver for Linux
%description
This is the printer driver for Lexmark 7000 "GDI" printers.

 * Known to work with Lexmark 7000, 7200 and 5700 printers
 * 600x600 dpi Black & White printing
 * Preliminary 600x600 CMY colour printing for 7000, 7200

%prep
%setup

#fix Makefile
perl -pi -e 's@-o root -g root@@' Makefile

%build
%make_build

%install
%makeinstall

%files
%doc README CHANGES lexmark*-filter lexmarkprotocol.txt *.prn *.pbm
%_bindir/pbm2l7k
%_bindir/pnmraw2cmyk
%_bindir/pbm2lex5700
%_bindir/pnm2lex7000
%_bindir/pnm2lex5700
%_bindir/dbman
%_bindir/psprint
%_bindir/pscprint

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 990516-alt1
- Initial build for ALT

