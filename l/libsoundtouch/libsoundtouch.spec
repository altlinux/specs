%define oname soundtouch
Name: libsoundtouch
Version: 1.3.1
Release: alt2.qa1

Summary: SoundTouch audio processing library

Group: Sound
License: LGPL
Url: http://www.surina.net/soundtouch/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.surina.net/%oname/%{oname}-%version.tar.bz2
Patch: %name-as-needed.patch
Patch1: %name-%version-gcc43.patch

# manually removed: glibc-devel-static gnustep-base libobjc-lf2 libqt4-core sope-appserver
# Automatically added by buildreq on Mon Feb 06 2006
BuildRequires: gcc-c++ libstdc++-devel

BuildRequires: rpm-build-compat >= 0.3

%description
SoundTouch is an open-source audio processing library that allows changing
the sound tempo, pitch and playback rate parameters independently from
each other, i.e.:
 - Sound tempo can be increased or decreased while maintaining the original pitch
 - Sound pitch can be increased or decreased while maintaining the original tempo 
 - Change playback rate that affects both tempo and pi

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries/include files for development with %name.

%prep
%setup -q -n %oname-%version
%patch
%patch1 -p1

#%__subst "s|.*#define ALLOW_OPTIMIZATIONS.*||g" include/STTypes.h

%build
touch NEWS README AUTHORS ChangeLog
%__autoreconf
#chmod u+x configure
%configure --enable-shared --disable-static

%make_build

%install
%make_install install DESTDIR=%buildroot
#install -D -m644 libSoundTouch.pc %buildroot%_pkgconfigdir/libSoundTouch.pc
rm -rf %buildroot/usr/doc

%files
%doc README.html
%_bindir/*
%_libdir/lib*.so.*

%files devel
%_includedir/%oname/
%_libdir/lib*.so
%_aclocaldir/*
%_pkgconfigdir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- fix build with gcc 4.3

* Thu Dec 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- correct version (download 1.3.1 from surina.net)
- use native soundtouch-1.0.pc (fix bug #10366, thanks eostapets@)

* Tue Jun 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.3
- add libSoundTouch.pc (fix bug #9677). Thanks, Debian.

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.2
- fixes for as-needed

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1
- initial build for ALT Linux Sisyphus
- build without asm optimization
