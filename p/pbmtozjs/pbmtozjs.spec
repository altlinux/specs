Name: pbmtozjs
Version: 0
Release: alt1
License: GPL
Group: System/Configuration/Printing

Url: http://www.linuxprinting.org/download/printing/pbmtozjs.c
Source: %name-%version.tar

BuildRequires: libjbig-devel

Summary: Driver for the HP LaserJet 1000 GDI printers
%description
Driver for the HP LaserJet 1000 GDI printers. Perhaps it also works with some
other GDI printers made by QMS and Minolta (these manufacturer names appear in
the driver's source code).

%prep
%setup
head -34 pbmtozjs.c | tail -33 > pbmtozjs.txt

%build
gcc %optflags -o pbmtozjs pbmtozjs.c -ljbig

%install
install -d %buildroot%_bindir/
install -m0755 pbmtozjs %buildroot%_bindir/

%files
%doc pbmtozjs.txt
%_bindir/pbmtozjs

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0-alt1
- Initial build for ALT

