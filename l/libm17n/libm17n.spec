%define oname m17n-lib
Name: libm17n
Version: 1.6.2
Release: alt2

Summary: Multilingual text processing library

Group: Text tools
License: LGPL
Url: http://www.m17n.org/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: http://www.m17n.org/m17n-lib-download/%oname-%version.tar.bz2

# $ freetype-config --libs
# -lfreetype -lz
BuildRequires: zlib-devel

# Automatically added by buildreq on Mon Dec 28 2009
BuildRequires: glibc-devel-static imake libXaw-devel libXft-devel libxml2-devel xorg-cf-files
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libm17n-db = %version

%description
The m17n library is a multilingual text processing library for the C
language.

%package -n m17n-utils
Summary: Multilingual text processing utilities
Group: Development/C

%description -n m17n-utils
Multilingual text processing utilities.

%package -n libm17n-gui
Summary: Multilingual text processing library GUI level APIs
Group: Development/C

%description -n libm17n-gui
The m17n library is a multilingual text processing library for the C
language.

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries/include files for development with %name.

%prep
%setup -q -n %oname-%version

%build
%autoreconf
%configure \
	--with-fontconfig \
	--disable-rpath \
	--disable-static
%make

%install
%makeinstall

%files
%doc AUTHORS NEWS
%_libdir/libm17n.so.*
%_libdir/libm17n-core.so.*
%_libdir/libm17n-flt.so.*

%files -n libm17n-gui
%_libdir/m17n
%_libdir/libm17n-gui.so.*

%files -n m17n-utils
%_bindir/*
%exclude %_bindir/m17n-config

%files devel
%doc README TODO ChangeLog
%_bindir/m17n-config
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*

%changelog
* Mon Sep 12 2011 Alexey Gladkov <legion@altlinux.ru> 1.6.2-alt2
- Fix buildrequires (workaround).

* Fri Dec 17 2010 Alexey Gladkov <legion@altlinux.ru> 1.6.2-alt1
- New version (1.6.2).

* Mon Dec 28 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.5-alt1
- new version (1.5.5).

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.2
- build without gui, unresolved=relaxed

* Fri Mar 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.1
- new version (1.3.3)

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1
- initial build for ALT Linux Sisyphus
