%define nameL com.github.luisbocanegra.minimize2tray

Name: plasma-addon-kwin-minimize2tray
Version: 20250430
Release: alt2

Summary: Hide windows to the system tray, similar to KDocker but in the form of a KWin Script that works on Wayland
License: GPL-3.0-only
Group: Graphical desktop/KDE

Url: https://github.com/luisbocanegra/kwin-minimize2tray
Vcs: https://github.com/luisbocanegra/kwin-minimize2tray

Source: %name-%version.tar

# https://github.com/luisbocanegra/kwin-minimize2tray/issues/13
Patch: main-20250430-pr-fix.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ pkgconfig(Qt6Qml)
BuildRequires: kf6-kpackage-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kservice-devel kf6-kstatusnotifieritem-devel

%description
%summary

%prep
%setup

%patch -p0

%build
%K6cmake
%K6make

%install
%K6install

%files
%doc *.md LICENSE
%_datadir/metainfo/%nameL.appdata.xml
%_datadir/kwin/scripts/%nameL
%_libdir/qt6/qml/com/github/luisbocanegra/*

%changelog
* Wed May 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250430-alt2
- added upstream patch for fix:
    + skip splash, utility and transient windows from auto hide
    + hide parent of transient windows when manually hiding

* Thu May 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250430-alt1
- Update upstream git.e8560f34:
    + change default shortcut to Meta+Alt+PgDown

* Mon Apr 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250413-alt1
- Initial build for ALT Linux.
