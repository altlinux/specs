%define rname foo2kyo

Summary: Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux
Name: printer-driver-%rname
Version: 0.1.0
Release: alt1.a
License: GPLv2
Group: System/Configuration/Printing
URL: http://sourceforge.net/projects/kyo-fs1016mfp/
Source: %rname-%version.tar

BuildRequires: cups-devel
Requires: cups

%description
Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux.

This package contains foomatic and cups Drivers for the Kyocera Mita FS-1016
MFP.

%prep
%setup -n %rname-%version

%build
%make

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/foomatic/db/source/{driver,opt,printer}
install -d %buildroot%_datadir/cups/model/%rname

install -m0755 foo2kyo %buildroot%_bindir
install -m0755 foo2kyo-wrapper %buildroot%_bindir

for dir in driver opt printer; do
  install -c -m0644 foomatic-db/$dir/*.xml %buildroot%_datadir/foomatic/db/source/$dir/
done

#install -m0644 ppd/Kyocera-FS-1016MFP-foo2kyo.ppd %%buildroot%%_datadir/cups/model/%%rname/

%files
%doc COPYING
%_bindir/foo2kyo
%_bindir/foo2kyo-wrapper
%_datadir/foomatic/db/source/*/*.xml

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.1.0-alt1.a
- Initial build for ALT

