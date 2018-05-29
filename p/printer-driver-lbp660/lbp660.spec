%define rname lbp660

Summary: Linux Canon LBP-460/660 driver
Name: printer-driver-%rname
Version: 0.3.1
Release: alt1
License: GPLv2
Group: System/Configuration/Printing
URL: http://www.boichat.ch/nicolas/lbp660/
Source: %rname-%version.tar

ExclusiveArch: %ix86 x86_64
BuildRequires: cups-devel
Requires: cups

%description
In this package there is a linux driver for the Canon LBP-660 and
LBP-460 printers.

This package contains CUPS drivers (PPD) for the following printers:

- Canon-LBP-460
- Canon-LBP-660

%prep
%setup -n %rname-%version

%build
%add_optflags -fgnu89-inline
%make_build CFLAGS="%optflags"

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/cups/model/%rname

install -m0755 lbp[46]60 %buildroot%_bindir/
install -m0755 lbp[46]60-* %buildroot%_bindir/
install -m0644 ppd/*.ppd %buildroot%_datadir/cups/model/%rname/

%files
%doc COPYING NEWS README THANKS TODO
%attr(4710,root,sys) %_bindir/%rname
%attr(4710,root,sys) %_bindir/lbp460
%_bindir/lbp[46]60-*
%_datadir/cups/model/%rname/

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.3.1-alt1
- Ini8tial build for ALT

