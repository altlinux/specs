Summary: Konica Minolta magicolor 2300W and 2400W Printer Driver

Name: m2300w
Version: 0.51
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

License: GPL
Group: Publishing
URL: http://sourceforge.net/projects/m2300w/
Source:	http://downloads.sourceforge.net/m2300w/%name-%version.tar

Requires: foomatic-db-engine

# Automatically added by buildreq on Tue Nov 06 2007
BuildRequires: foomatic-db-engine foomatic-filters ghostscript

%description
The m2300w driver is a Linux printer driver for the Konica Minolta magicolor
2300W and 2400W color laser printers. It is intended for being used in
conjunction with ghostscript, foomatic and CUPS.

This package contains CUPS drivers (PPD) for the following printers:

 o Minolta magicolor 2300W
 o Minolta magicolor 2400W

%prep

%setup -q

%build
%configure
%make

%install
%makeinstall INSTROOT=%buildroot

%clean

%files
%doc COPYING INSTALL README README.ghostscript
%_datadir/cups/model/*
%_datadir/%name
%exclude %_datadir/%name/*/foomatic
%_bindir/*


%changelog
* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.51-alt1
- Initial build

