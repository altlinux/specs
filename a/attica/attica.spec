Name: attica
Version: 0.3.0
Release: alt1

Summary: Open Collaboration Service providers library
License: GPLv2+
Group: System/Base
Url: http://www.kde.org/

Requires: libqt4-core >= %{get_version libqt4-core}

Source0: http://fr2.rpmfind.net/linux/KDE/stable/attica/%name-%version.tar.bz2
Patch1: attica-0.1.2-alt-pc-version.patch

# Automatically added by buildreq on Mon Jan 18 2010 (-bi)
#BuildRequires: cmake gcc-c++ glib2-devel glibc-devel-static libXfixes-devel libqt3-devel phonon-devel qt4-assistant
BuildRequires(pre): libqt4-devel kde-common-devel
BuildRequires: cmake gcc-c++ glib2-devel glibc-devel phonon-devel libqt4-devel

%description
A library to access Open Collaboration Service providers
Required to access OSC providers in get hot new stuff.

%package -n libattica
Summary: KDE 4 library
Group: System/Libraries
%description -n libattica
KDE 4 library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: libattica = %version-%release
Provides: libattica-devel-%version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -q -n %name-%version
#%patch1 -p1

%build
%Kbuild

%install
%Kinstall

%find_lang %name

%files -n libattica
%_libdir/libattica.so.*

%files devel
%_includedir/attica
%_libdir/libattica.so
%_libdir/pkgconfig/libattica.pc

%changelog
* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt3
- fix build requires

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt2
- fix to build

* Wed Jan 26 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.4-alt2
- rebuilt

* Wed May 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.4-alt0.M51.1
- built for M51

* Wed May 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.4-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt0.M51.1
- built for M51

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- built for ALT

