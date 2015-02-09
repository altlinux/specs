Name:    pcmanfm-qt
Version: 0.9.0
Release: alt1

Summary: PCManFM-Qt is the Qt port of the LXDE file manager PCManFM
License: GPLv2+
Group:   File tools

Url:     http://lxqt.org
Source0: %name-%version.tar
Source1: %name.desktop

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: libXdmcp-devel
BuildRequires: libfm-devel >= 1.2.0
BuildRequires: libmenu-cache-devel

Requires: menu-cache

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM.

%package -n libfm-qt
Summary: Shared library for %name
Group: System/Libraries

%description -n libfm-qt
LibFM-Qt is a companion library providing components to build desktop
file managers.

%package -n libfm-qt-devel
Summary: Development headers for libfm-qt
Group: Development/C++

%description -n libfm-qt-devel
LibFM-Qt is a companion library providing components to build desktop
file managers.

This package provides the development files for libfm-qt.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang --with-qt %name
%find_lang --with-qt libfm-qt
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*

%files -n libfm-qt -f libfm-qt.lang
%_libdir/libfm-qt5.so.*

%files -n libfm-qt-devel
%_includedir/libfm-qt
%_libdir/libfm-qt5.so
%_pkgconfigdir/libfm-qt5.pc
%_datadir/libfm-qt/translations/libfm-qt_template.qm

%changelog
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- rebuilt against 0.8.0 release libraries

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Mar 31 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt4.gitf58b1b7
- Increase release number to backport to p7 branch

* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt3.gitf58b1b7
- New snapshot
- Fix requirement on development packages
- Link with libfm2

* Mon Apr 08 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2.gite99916f
- New snapshot

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus
