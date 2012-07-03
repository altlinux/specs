
Name:     libchipcard
Version:  5.0.2
Release:  alt2

Summary:  A library for easy access to smart cards (chipcards)
License:  LGPL
Group:    System/Libraries
Url:      http://www.libchipcard.de/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   http://dl.sourceforge.net/libchipcard/%name-%version.tar.gz
Source1:  %name.init
Source2:  %name.watch

Patch0:  %name-etc.patch
Patch1:  %name-am18.patch

BuildRequires: gcc-c++ glibc-devel 
BuildRequires: libgwenhywfar-devel >= 4.0.0
BuildRequires: libpcsclite-devel zlib-devel
BuildRequires: rpm-build-compat

Provides:  libchipcard2
Obsoletes: libchipcard2

%description
LibChipCard allows easy access to smart cards. It provides basic
access to memory and processor cards and has special support for
German medical cards, German "Geldkarten" and HBCI (homebanking) cards
(both type 0 and type 1). It accesses the readers via CTAPI or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil and
Reiner-SCT readers.

%package devel
Summary: Header files for LibChipCard
Group: Development/Other
Requires: %name = %version
Provides: libchipcard2-devel
Obsoletes: libchipcard2-devel

%description devel
This package contains libchipcard-config and header files for writing
programs using LibChipCard.

%package tools
Summary: Terminal tools and daemons for LibChipCard
License: GPL
Group: Communications
Requires: %name = %version
Provides: libchipcard2-tools
Obsoletes: libchipcard2-tools


%description tools
This package contains the terminal tools and daemons for LibChipCard.
The most important daemon here is chipcardd which is needed to access
local card readers.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure \
	--disable-static \
	--enable-pcsc \
	--with-pcsc-libs="%_libdir"
#	--with-pid-dir=/var/run \

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/gwenhywfar/plugins/60/ct/*.la

install -d %buildroot%_initrddir
install %SOURCE1 %buildroot%_initrddir/chipcardd

%find_lang %name

%post tools
%post_service chipcardd

%preun tools
%preun_service chipcardd

%files
# COPYING contains only summary, note *GPL texts themselves
%doc AUTHORS COPYING ChangeLog README* TODO
%_libdir/*.so.*
%_sysconfdir/chipcard/
%_libdir/gwenhywfar/plugins/60/ct/*

%files devel
%_libdir/*.so
%_datadir/chipcard/
%_includedir/*
%_aclocaldir/*

%files tools -f %name.lang
%_bindir/*
%_initrddir/chipcardd
%attr(754,root,root) %_initrddir/chipcardd


%changelog
* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt2
- Remove standard library path from RPATH
- Add watch file

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version 5.0.2

* Thu Mar 03 2011 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version 5.0.0

* Mon Apr 05 2010 Andrey Cherepanov <cas@altlinux.org> 4.2.9-alt1
- New version 4.2.9

* Mon Nov 24 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.3-alt1
- new version 4.2.3 (with rpmrb script)

* Tue Apr 22 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)
- update buildreqs

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt0.1
- new version (2.1.3)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt0.1beta
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)
