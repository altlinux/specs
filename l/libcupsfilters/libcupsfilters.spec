%define soversion 2
Name: libcupsfilters
Version: 2.0.0
Release: alt1
Summary: Library for developing printing filters
License: Apache-2.0 WITH LLVM-exception
Group: System/Libraries
Url: https://github.com/OpenPrinting/libcupsfilters
Source0: %name-%version.tar
Source1: default-testpage.pdf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: ghostscript
BuildRequires: git-core
BuildRequires: libtool
BuildRequires: pkg-config
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libqpdf)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: fonts-ttf-dejavu
Requires: ghostscript
Requires: %name%soversion = %EVR
Conflicts: cups-filters < 2.0.0-alt1

%description
Libcupsfilters provides a library, which implements common functions used
in cups-browsed daemon and printing filters, and additional files
as banner templates and character sets. The filters are used in CUPS daemon
and in printer applications.

%package -n %name%soversion
Summary: Library for developing printing filters
Group: System/Libraries
Requires: %name = %EVR

%description -n %name%soversion
Libcupsfilters%soversion provides a library, which implements common functions
used in cups-browsed daemon and printing filters.

%package devel
Summary: Development files for libcupsfilters]
Group: Development/C
Requires: %name%soversion = %EVR

%description devel
Development files for OpenPrinting cupsfilters library.

%prep
%setup

%build
./autogen.sh
%configure --disable-mutool \
           --disable-rpath \
           --disable-silent-rules \
           --disable-static \
           --enable-dbus \
	   #
%make_build

%check
make check

%install
%makeinstall_std
install -D -m 644 %SOURCE1 %buildroot/%_datadir/cups/data/
rm -rf %buildroot/usr/share/doc/libcupsfilters

%files
%doc COPYING LICENSE NOTICE cupsfilters/fontembed/README
%doc AUTHORS CHANGES.md CHANGES-1.x.md README.md
%dir %_datadir/cups/banners
%_datadir/cups/banners/classified
%_datadir/cups/banners/confidential
%_datadir/cups/banners/form
%_datadir/cups/banners/secret
%_datadir/cups/banners/standard
%_datadir/cups/banners/topsecret
%_datadir/cups/banners/unclassified
%dir %_datadir/cups/charsets
%_datadir/cups/charsets/pdf.utf-8
%_datadir/cups/charsets/pdf.utf-8.heavy
%_datadir/cups/charsets/pdf.utf-8.simple
%_datadir/cups/data/classified.pdf
%_datadir/cups/data/confidential.pdf
%_datadir/cups/data/default-testpage.pdf
%_datadir/cups/data/default.pdf
%_datadir/cups/data/form_english.pdf
%_datadir/cups/data/form_russian.pdf
%_datadir/cups/data/form_english_in.odt
%_datadir/cups/data/form_russian_in.odt
%_datadir/cups/data/secret.pdf
%_datadir/cups/data/standard.pdf
%_datadir/cups/data/testprint
%_datadir/cups/data/topsecret.pdf
%_datadir/cups/data/unclassified.pdf

%files -n %name%soversion
%_libdir/*.so.%{soversion}.*
%_libdir/*.so.%{soversion}

%files devel
%doc CONTRIBUTING.md DEVELOPING.md
%dir %_includedir/cupsfilters
%_includedir/cupsfilters/*
%_libdir/libcupsfilters.so
%_libdir/pkgconfig/libcupsfilters.pc

%changelog
* Fri Sep 29 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0
- added default-testpage.pdf from cups-filters package (Closes: #47646)

* Mon Jul 24 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc2
- update to 2.0rc2

* Mon Jun 19 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc1
- first build for ALT
