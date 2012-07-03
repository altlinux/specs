Summary: CUPS driver for Brother P-touch label printers

%define orig_name ptouch-driver

Name: printer-driver-ptouch
Version: 1.3
Release: alt1

Provides: %orig_name = %version
Obsoletes: %orig_name

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL

URL: http://www.diku.dk/~panic/P-touch/
Source: http://www.diku.dk/~panic/P-touch/%orig_name-%version.tar

Requires: cups

# Automatically added by buildreq on Wed Nov 07 2007
BuildRequires: libcups-devel

%description
This is a CUPS raster filter for Brother P-touch label printers.  It is
meant to be used by the PostScript Description files of the drivers from
the foomatic package.

%prep
%setup -q -n %orig_name-%version

%build
%configure
%make_build

%install
%makeinstall libdir=%buildroot%_prefix/lib


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_prefix/lib/cups/filter/*

%changelog
* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- 1.3

* Fri Nov 21 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt2
- fix build with gcc-4.3
- rename package to printer-driver-ptouch

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- Initial build
