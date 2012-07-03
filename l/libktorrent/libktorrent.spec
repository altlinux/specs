
%define sonum 4
%define libname libktorrent%sonum

Name: libktorrent
Version: 1.2.1
Release: alt1

Group: System/Libraries
Summary: BitTorrent library for KDE
Url: http://ktorrent.org/
License: GPLv2

# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source: http://www.libssh.org/files/%name-%version.tar.gz

# Automatically added by buildreq on Wed Mar 16 2011 (-bi)
#BuildRequires: boost-devel-headers doxygen gcc-c++ glib2-devel graphviz kde4libs-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgcrypt-devel libgmp-devel libqca2-devel libqt3-devel libxkbfile-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: boost-devel doxygen gcc-c++ glib2-devel graphviz kde4libs-devel
BuildRequires: libgcrypt-devel libgmp-devel libqca2-devel zlib-devel

%description
Library that allow using BitTorrent with KDE programs

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Libraries
Conflicts: libktorrent1
Conflicts: libktorrent3 <= 1.1.0-alt2
%description common
Common %name files

%package -n %libname
Summary: KTorrent library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libname
KTorrent library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %libname = %version-%release
Requires: libgcrypt-devel libqca2-devel
%description devel
This package contains the development files for %name.


%prep
%setup -q

%build
%K4cmake
%K4make

%install
%K4install
%K4find_lang --with-kde %name

%files common -f %name.lang

%files -n %libname
%_libdir/lib*.so.%sonum
%_libdir/lib*.so.%sonum.*

%files devel
%_K4apps/cmake/modules/*.cmake
%_K4includedir/%name
%_K4link/lib*.so

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- release 1.2.0

* Thu Feb 02 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.1
- 1.2rc1

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt0.M60P.1
- built for M60P

* Mon Dec 19 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt1
- new version

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.2-alt0.M60P.1
- built for M60P

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.2-alt1
- new version

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt4
- fix build requires

* Thu Mar 17 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt3
- separate common files

* Thu Mar 17 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- obsolete libktorrent1

* Wed Mar 16 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt2
- fix to build

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt0.M51.1
- built for M51

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt0.M51.1
- built for M51

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M51.1
- built for M51

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial specfile
