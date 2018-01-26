Name:    appstream
Version: 0.11.8
Release: alt1
Summary: Utilities to generate, maintain and access the AppStream Xapian database 

# lib LGPLv2+, tools GPLv2+
License: GPLv2+ and LGPLv2+
Group:   System/Configuration/Packaging
URL:     http://www.freedesktop.org/wiki/Distributions/AppStream/Software
Source0: appstream-%{version}.tar
# VCS:   https://github.com/ximion/appstream

BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: libprotobuf-lite-devel
BuildRequires: libstemmer-devel
BuildRequires: libxapian-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: protobuf-compiler
BuildRequires: publican
BuildRequires: qt5-base-devel
BuildRequires: xmlto
BuildRequires: gtk-doc

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

%package doc
Summary:  Documenation for development using %{name}
Group:	  Development/Documentation

%description doc
%{summary}.

%prep
%setup

%build
%meson  -Dqt=true \
	-Ddocs=true \
	-Dstemming=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/app-info/{icons,xmls}
mkdir -p %{buildroot}/var/cache/app-info/{icons,xapian,xmls}
touch %{buildroot}/var/cache/app-info/cache.watch

%find_lang appstream

# move metainfo to right/legacy location, at least until our tools can handle it
mkdir -p %{buildroot}%{_datadir}/appdata/
mv %{buildroot}%{_datadir}/metainfo/*.xml \
   %{buildroot}%{_datadir}/appdata/

%check
%meson_test

%files -f appstream.lang
%doc AUTHORS LICENSE.GPLv2 LICENSE.LGPLv2.1 MAINTAINERS NEWS README.md RELEASE
%config(noreplace) %_sysconfdir/appstream.conf
%_bindir/appstreamcli
%_libdir/girepository-1.0/AppStream-1.0.typelib
%_libdir/libappstream.so.*
%dir %_datadir/app-info/
%dir %_datadir/app-info/icons
%dir %_datadir/app-info/xmls
%ghost %_cachedir/app-info/cache.watch
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xapian
%dir %_cachedir/app-info/xmls
%_man1dir/appstreamcli.1.*
%_datadir/gettext/its/metainfo.*
%_datadir/appdata/org.freedesktop.appstream.cli.*.xml

%files devel
%_includedir/appstream/
%_libdir/libappstream.so
%_libdir/pkgconfig/appstream.pc
%_datadir/gir-1.0/AppStream-1.0.gir

%files qt
%_libdir/libAppStreamQt.so.*

%files qt-devel
%_includedir/AppStreamQt/
%_libdir/cmake/AppStreamQt/
%_libdir/libAppStreamQt.so

%files doc
%_defaultdocdir/%name
%_datadir/gtk-doc/html/%name

%changelog
* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.8-alt1
- New version.

* Mon Oct 23 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.7-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.6-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.5-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.4-alt1
- New version
- Use meson and ninja-build for build
- Package development documentation

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.3-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.2-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.1-alt1.gita6f9e55
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version

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
