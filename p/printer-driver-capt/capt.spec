%define rname capt

Summary: CAPT driver for Canon LBP-810 and LBP-1120
Name: printer-driver-%rname
Version: 0.1
Release: alt1
License: GPLv2
Group: System/Configuration/Printing
URL: http://www.boichat.ch/nicolas/capt/
# Source: http://www.boichat.ch/nicolas/capt/capt-%version.tar.gz
Source: capt-%version.tar

BuildRequires: cups-devel
Requires: cups

%description
CAPT driver for Canon LBP-810 and LBP-1120

This package contains CUPS drivers (PPD) for the following printers:
- Canon-LBP-810
- Canon-LBP-1120

%prep
%setup -n %rname-%version

%build
%add_optflags -fgnu89-inline
%make_build CFLAGS="%optflags"

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/cups/model/capt

install -m0755 capt %buildroot%_bindir/
install -m0755 capt-* %buildroot%_bindir/
install -m0644 ppd/*.ppd %buildroot%_datadir/cups/model/capt/

%files
%_bindir/capt
%_bindir/capt-print
%_datadir/cups/model/capt/*.ppd
%doc COPYING TODO NEWS README

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.1-alt1
- Initial build for ALT

