%define _unpackaged_files_terminate_build 1

%def_with check

Name: lomiri-notifications
Version: 1.3.3
Release: alt1

Summary: Lomiri Notifications
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-notifications

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(lomiri-shell-notifications)
BuildRequires: pkgconfig(lomiri-shell-api)

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: pkgconfig(libqtdbustest-1)
%endif

%description
Lomiri's implementation of a Free Desktop Notification server. It also
provides some additional features as needed on alternative platforms,
such as mobile.

Since the shell is implemented in QML, this functionality is implemented
as a QML plugin. Notification status is provided as a
QAbstractListModel, making integration simple. The exact form of the API
is defined by the shell, Lomiri notifications only implements it.

Lomiri notifications does not and will not provide a C/C++ API for
sending or receiving notifications. It is QML only.

%prep
%setup
%patch -p1

%build
%cmake \
       -DENABLE_UBUNTU_COMPAT=ON \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING README.txt
%dir %_libdir/lomiri/qml/Lomiri/Notifications
%_libdir/lomiri/qml/Lomiri/Notifications/libnotifyclientplugin.so
%_libdir/lomiri/qml/Lomiri/Notifications/libnotifyplugin.so
%_libdir/lomiri/qml/Lomiri/Notifications/qmldir

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.3-alt1
- New version 1.3.3.

* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.2-alt2
- Follow changes in lomiri-api 0.3.2-alt2 package.

* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.2-alt1
- New version 1.3.2.

* Sun Feb 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt2
- Fixed FTBFS.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
