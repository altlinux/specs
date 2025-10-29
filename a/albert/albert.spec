%def_with check
%define abiver 33

Name:    albert
Version: %abiver.0.1
Release: alt1

Summary: A fast and flexible keyboard launcher
License: BSD-3-Clause
Group:   Graphical desktop/Other
Url:     https://albertlauncher.github.io
Vcs:     https://github.com/albertlauncher/albert

Source0: %name-%version.tar
Source1: %name-%version-i18n.tar
Source2: %name-%version-lib-QHotkey.tar
Source3: %name-%version-lib-QNotification.tar
Source4: %name-%version-plugins-applications.tar
Source5: %name-%version-plugins-application.tar
Source6: %name-%version-plugins-bluetooth.tar
Source7: %name-%version-plugins-caffeine.tar
Source8: %name-%version-plugins-calculator-qalculate.tar
Source9: %name-%version-plugins-chromium.tar
Source10: %name-%version-plugins-clipboard.tar
Source11: %name-%version-plugins-contacts.tar
Source12: %name-%version-plugins-datetime.tar
Source13: %name-%version-plugins-debug.tar
Source14: %name-%version-plugins-dictionary.tar
Source15: %name-%version-plugins-docs.tar
Source16: %name-%version-plugins-files.tar
Source17: %name-%version-plugins-github.tar
Source18: %name-%version-plugins-hash.tar
Source19: %name-%version-plugins-mediaremote.tar
Source20: %name-%version-plugins-menubar.tar
Source21: %name-%version-plugins-obsidian.tar
Source22: %name-%version-plugins-path.tar
Source23: %name-%version-plugins-python.tar
Source24: %name-%version-plugins-snippets.tar
Source25: %name-%version-plugins-spotify.tar
Source26: %name-%version-plugins-ssh.tar
Source27: %name-%version-plugins-system.tar
Source28: %name-%version-plugins-timer.tar
Source29: %name-%version-plugins-timezones.tar
Source30: %name-%version-plugins-urlhandler.tar
Source31: %name-%version-plugins-vpn.tar
Source32: %name-%version-plugins-websearch.tar
Source33: %name-%version-plugins-widgetsboxmodel-qss.tar
Source34: %name-%version-plugins-widgetsboxmodel.tar
# Link application against existent pybind from repo
# Upstream requires submodule
Patch0: albert-0.26.10-alt-build-without-pybind-src.patch

BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: gcc-c++

BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libxml++-2.6)
BuildRequires: pkgconfig(pybind11)
BuildRequires: pkgconfig(Qt6Scxml)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(python3)
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-mysql
BuildRequires: qt6-sql-odbc
BuildRequires: qt6-sql-postgresql
BuildRequires: libqtkeychain-qt6-devel
%if_with check
BuildRequires: doctest-devel
%endif

Requires: libqt6-statemachineqml
Requires: libqt6-svg
Requires: qt6-5compat
Requires: libarchive13
Requires: lib%name%abiver = %EVR

%description
Albert is a plugin based, desktop agnostic C++/Qt keyboard launcher that helps
you to accomplish your workflows in a breeze.

%package -n lib%name-devel
Summary: Albert launcher development files
License: BSD-3-Clause
Group:   Development/KDE and QT
Requires: lib%name%abiver = %EVR

%description -n lib%name-devel
Development files for building applications under Albert launcher

%package -n lib%name%abiver
Summary: Albert launcher shared library
License: BSD-3-Clause
Group:   System/Libraries
Obsoletes: lib%name < %EVR

%description -n lib%name%abiver
Shared libraries for running Albert launcher application

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34
%patch0 -p2

%build
%cmake \
    -DBUILD_APPLICATIONS_XDG=ON \
    %if_with check
    -DBUILD_TESTS=ON
    %endif
%cmake_build

%install
%cmake_install

%check
%_cmake__builddir/bin/%{name}_test

%files
%doc *.md
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%name.desktop
%dir %_iconsdir/hicolor/scalable/
%dir %_iconsdir/hicolor/scalable/apps/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/%name-tray.svg

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_libdir/cmake/Albert/

%files -n lib%name%abiver
%_libdir/lib%name.so.%abiver.*

%changelog
* Tue Oct 28 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 33.0.1-alt1
- New version.

* Fri Sep 26 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.32.1-alt1
- New version.
- Added huge amount of new submodules.

* Tue May 20 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.27.8-alt1
- New version.

* Tue Apr 01 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.27.5-alt1
- New version.

* Fri Feb 28 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.27.1-alt1
- New version.

* Wed Dec 25 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.26.10-alt1
- New version.

* Thu Aug 01 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.24.3-alt1
- New version

* Fri Mar 29 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.23.0-alt1
- Initial build for Sisyphus (Closes: #47237)
