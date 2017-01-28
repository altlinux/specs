Name:    appstream
Version: 0.10.6
Release: alt1
Summary: Utilities to generate, maintain and access the AppStream Xapian database 

# lib LGPLv2+, tools GPLv2+
License: GPLv2+ and LGPLv2+
Group:   System/Configuration/Packaging
URL:     http://www.freedesktop.org/wiki/Distributions/AppStream/Software
Source0: appstream-%{version}.tar
# VCS:   https://github.com/ximion/appstream

Patch:   appstream-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires: libxml2-devel
BuildRequires: qt5-base-devel
BuildRequires: libyaml-devel
BuildRequires: libxapian-devel
BuildRequires: xmlto
BuildRequires: ctest
BuildRequires: libprotobuf-lite-devel
BuildRequires: protobuf-compiler

#Requires: appstream-data

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary:  Development files for %{name}
Group:	  Development/C
Requires: %name = %version-%release

%description devel
%{summary}.

%package qt
Summary: Qt bindings for %{name}
Group:	  System/Libraries
Requires: %name = %version-%release

%description qt
%{summary}.

%package qt-devel
Summary:  Development files for %{name}-qt bindings
Group:	  Development/KDE and QT
Requires: %name-qt = %version-%release

%description qt-devel
%{summary}.

%prep
%setup
%patch -p1

%build
%cmake \
  -DQT:BOOL=ON -DAPPSTREAM_QT_VERSION:STRING="5"\
  -DTESTS:BOOL=ON \
  -DVAPI:BOOL=OFF
%cmake_build


%install
%makeinstall_std -C BUILD

mkdir -p %{buildroot}%{_datadir}/app-info/{icons,xmls}
mkdir -p %{buildroot}/var/cache/app-info/{icons,xapian,xmls}
touch %{buildroot}/var/cache/app-info/cache.watch

%find_lang appstream

%check
#LDFLAGS=-Lsrc make test -C BUILD ARGS="--output-on-failure --timeout 300"

%files -f appstream.lang
%doc AUTHORS LICENSE.GPLv2 LICENSE.LGPLv2.1
%config(noreplace) %_sysconfdir/appstream.conf
%_bindir/appstreamcli
%_libdir/girepository-1.0/AppStream-1.0.typelib
%_libdir/libappstream.so.*
%dir %_datadir/app-info/
%dir %_datadir/app-info/icons
%dir %_datadir/app-info/xmls
%_datadir/app-info/categories.xml
%ghost %_cachedir/app-info/cache.watch
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xapian
%dir %_cachedir/app-info/xmls
%_man1dir/appstreamcli.1.*

%files devel
%_includedir/AppStream/
%_libdir/libappstream.so
%_libdir/pkgconfig/appstream.pc
%_datadir/gir-1.0/AppStream-1.0.gir

%files qt
%_libdir/libAppstreamQt.so.*

%files qt-devel
%_includedir/AppstreamQt/
%_libdir/cmake/AppstreamQt/
%_libdir/libAppstreamQt.so

%changelog
* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.6-alt1
- new version 0.10.6

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.4-alt1
- new version 0.10.4

* Mon Nov 07 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1
- new version 0.10.3

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version 0.10.1

* Tue Aug 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version

* Mon May 16 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version

* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version

* Mon Sep 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- New version

* Tue Jun 30 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1
- New version
- appstream-qt contains libraries only for Qt5

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt2
- Rebuild with new version of xapian-core

* Sat Feb 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version

* Sun Jan 25 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Mon Dec 15 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Tue Oct 28 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Import from Fedora
- Disable tests
