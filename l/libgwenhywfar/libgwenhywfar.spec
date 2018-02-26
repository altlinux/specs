%define origname gwenhywfar

Name:     libgwenhywfar
Version:  4.3.1
Release:  alt1

Summary:  A multi-platform helper library for other libraries
Group:    System/Libraries
License:  LGPLv2+
URL:      http://www2.aquamaniac.de/sites/download/packages.php

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %origname-%version.tar.bz2
Source1:  %name.watch
Patch1:   %name-pthread.patch

BuildRequires: gcc-c++ glibc-devel graphviz libcom_err-devel 
BuildRequires: libgnutls-devel libssl-devel tzdata
BuildRequires: libqt4-devel libgtk+2-devel
BuildRequires: zlib-devel libgcrypt-devel ncurses-devel
BuildRequires: ca-certificates

Requires: ca-certificates

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
www.libchipcard.de and OpenHBCI-TNG (The Next Generation)
www.openhbci.de.

Check http://www.freesource.info/wiki/Altlinux/Policy/TLS
for ALT Linux TLS/SSL policy

%package  gtk2
Summary:  Gwenhywfar support for GTK+
Group:    System/Libraries
Requires: %name = %version-%release

%description gtk2
Gwenhywfar support for GTK+

%package  qt4
Summary:  Gwenhywfar support for Qt4
Group:    System/Libraries
Requires: %name = %version-%release

%description qt4
Gwenhywfar support for Qt4

%package  devel
Summary:  Gwenhywfar development kit
Group:    Development/C
Requires: %name = %version-%release
Requires: %name-gtk2 = %version-%release
Requires: %name-qt4  = %version-%release

%description devel
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -q -n %origname-%version
%patch1 -p2

%build
%autoreconf
%configure \
	--disable-static \
	--with-openssl-libs=%_libdir \
	--with-guis="qt4 gtk2" \
	--with-qt4-libs="%_libdir" 

%make_build

%install
%makeinstall_std
%find_lang %origname

# Use system-wide ca-certificates
rm -f %buildroot%_datadir/gwenhywfar/ca-bundle.crt
ln -s %_datadir/ca-certificates/ca-bundle.crt %buildroot%_datadir/gwenhywfar/ca-bundle.crt

%files -f %origname.lang
%doc AUTHORS README ChangeLog TODO NEWS
%_bindir/gct-tool
%_bindir/gsa
%_libdir/*.so.*
%exclude %_libdir/libgwengui-gtk2.so.*
%exclude %_libdir/libgwengui-qt4.so.*
%_libdir/%origname/
%_datadir/gwenhywfar/ca-bundle.crt
%_datadir/gwenhywfar/dialogs/*.dlg

%files gtk2
%_libdir/libgwengui-gtk2.so.*

%files qt4
%_libdir/libgwengui-qt4.so.*

%files devel
%_bindir/%origname-config
%_bindir/xmlmerge
%_bindir/mklistdoc
%_bindir/typemaker
%_bindir/typemaker2
%_libdir/*.so
%_includedir/gwenhywfar4/
%_pkgconfigdir/*
%_datadir/%origname/typemaker2/*
%_datadir/aclocal/gwenhywfar.m4

%changelog
* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version 4.3.1
- Add watch file

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version 4.2.1
- Use system-wide ca-certificates (closes: #10901)

* Thu Mar 03 2011 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version 4.0.7
- Exclude qt4 and gtk+ libraries in separate packages

* Mon Oct 04 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt2
- rebuild with new openssl

* Fri Apr 02 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt1
- new version 3.11.3

* Wed Apr 15 2009 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version 3.8.0 (with rpmrb script)

* Mon Nov 24 2008 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2 (with rpmrb script)

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- cleanup spec, move gct-tool to original dir
- fix bug #10901 (use ca-bundle.crt from datadir/ca-certificates/)

* Tue Apr 22 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)
- update buildreqs

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4
- do not pack /etc/gwen-public-ca.crt
- update buildreq, fix x86_64 build (use --with-openssl-libs (thanks at@))

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt0.1
- new version 2.4.0
- update buildreq

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt0.1
- new version

* Mon Dec 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.19.2-alt0.1
- new version

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 1.16.0-alt1
- new version

* Wed Aug 10 2005 Igor Muratov <migor@altlinux.org> 1.14.0-alt1
- new version

* Sun Mar 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- first build for ALT Linux Sisyphus

