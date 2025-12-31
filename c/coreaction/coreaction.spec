%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global __find_debuginfo_files %nil

%define _libdir %_prefix/lib

Name: coreaction
Version: 5.0.0
Release: alt1

Summary: Side bar for showing widgets for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/coreaction

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6SvgWidgets)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)

# TODO - find the exact root of the problems shown below
#            error: file /usr/lib64/libQt6Core.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Core.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6Gui.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Gui.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6Network.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Network.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6SvgWidgets.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6SvgWidgets.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6Widgets.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Widgets.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libc.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libc.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libgcc_s.so.1()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libgcc_s.so.1()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libstdc++.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libstdc++.so.6()(64bit) is not yet set-versioned
#        and then remove the below HACK-y line
AutoReq: nolib

# TODO - find the exact root of the problem like
#            phdr[5]: unknown object file note type 1951465473 with owner name 'qt-project!' at offset 144
#            section [19] '.note.qt.metadata': unknown object file note type 1951465473 with owner name 'qt-project!' at offset 80
#            verify-elf: WARNING: ./usr/lib/coreapps/plugins/libcalendar.so: eu-elflint failed
#        and then remove the below HACK-y line
%set_verify_elf_method none

Requires: libqt6-core
Requires: libqt6-gui
Requires: libqt6-network
Requires: libqt6-svgwidgets
Requires: libqt6-widgets

Requires: hicolor-icon-theme
Requires: coretoppings
Requires: coregarage

%description
%summary.

%prep
%setup
%patch -p1
sed -i "s|Utility;|Utility;Clock;|" app/cc.cubocore.CoreAction.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coreaction.png LICENSE README.md
%_bindir/coreaction
%_libdir/coreapps/plugins/libbattery.so
%_libdir/coreapps/plugins/libcalculator.so
%_libdir/coreapps/plugins/libcalendar.so
%_libdir/coreapps/plugins/libnetwork.so
%_libdir/coreapps/plugins/libnotes.so
%_libdir/coreapps/plugins/libsearch.so
%_libdir/coreapps/plugins/libsystem.so
%_libdir/coreapps/plugins/libweather.so
%_desktopdir/cc.cubocore.CoreAction.desktop
%_datadir/coreapps/resource/country.txt
%_datadir/coreapps/resource/international.txt
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreAction.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
