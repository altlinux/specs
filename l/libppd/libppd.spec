%define soversion 2
Name: libppd
Version: 2.0.0
Release: alt1
Summary: Library for retro-fitting legacy printer drivers
License: Apache-2.0 WITH LLVM-exception
Url: https://github.com/OpenPrinting/libppd
Group: System/Libraries
Source0: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: ghostscript
BuildRequires: git-core
BuildRequires: libtool
BuildRequires: pkg-config
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(libcupsfilters) >= 2.0
BuildRequires: pkgconfig(zlib)
BuildRequires: poppler-utils

%description
Libppd provides all PPD related function/API which is going
to be removed from CUPS 3.X, but are still required for retro-fitting
support of legacy printers. The library is meant only for retro-fitting
printer applications, any new printer drivers have to be written as
native printer application without libppd.

%package -n %name%soversion
Group: System/Libraries
Summary: Library for retro-fitting legacy printer drivers
Requires: ghostscript
Requires: poppler-utils

%description -n %name%soversion
Libppd provides all PPD related function/API which is going
to be removed from CUPS 3.X, but are still required for retro-fitting
support of legacy printers. The library is meant only for retro-fitting
printer applications, any new printer drivers have to be written as
native printer application without libppd.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soversion = %EVR
Requires: cups-devel
Requires: libcupsfilters-devel

%description devel
The %name-devel package contains libraries and header files for
developing retro-fitting printer applications.

%package tools
Group: System/Configuration/Printing
Summary: PPD compiler tools and definition files
Requires: %name%soversion = %EVR
Conflicts: libcups-devel < 3.0

%description tools
The package contains PPD compiler and definition files needed for generating
PPD files from *.drv files.

%prep
%setup

%build
./autogen.sh
%configure\
  --disable-acroread \
  --disable-mutool \
  --disable-rpath \
  --disable-silent-rules \
  --disable-static \
  --enable-ppdc-utils \
  --enable-testppdfile \
  --with-pdftops=hybrid \
  --with-cups-rundir=/run/cups/ \
  #

%make_build

%check
make check

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%name

%files -n %name%soversion
%doc LICENSE NOTICE COPYING
%doc ABOUT-NLS AUTHORS CHANGES.md README.md
%_libdir/libppd.so.%soversion.*
%_libdir/libppd.so.%soversion

%files devel
%doc CONTRIBUTING.md DEVELOPING.md
%dir %_includedir/ppd
%_includedir/ppd/ppd-filter.h
%_includedir/ppd/ppdc.h
%_includedir/ppd/ppd.h
%_libdir/libppd.so
%_libdir/pkgconfig/libppd.pc

%files tools
%_bindir/ppdc
%_bindir/ppdhtml
%_bindir/ppdi
%_bindir/ppdmerge
%_bindir/ppdpo
%_bindir/testppdfile
%dir %_datadir/ppdc/
%_datadir/ppdc/epson.h
%_datadir/ppdc/font.defs
%_datadir/ppdc/hp.h
%_datadir/ppdc/label.h
%_datadir/ppdc/media.defs
%_datadir/ppdc/raster.defs

%changelog
* Fri Sep 29 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0 (Fixes: CVE-2023-4504)

* Mon Jul 24 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc2
- update to 2.0rc2

* Mon Jun 19 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc1
- first build for ALT
