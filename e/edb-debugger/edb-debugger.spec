%define _unpackaged_files_terminate_build 1

Name: edb-debugger
Version: 1.5.0
Release: alt1

Summary: Cross platform x86/x86-64 debugger
License: GPL-2.0
Group: Development/Debuggers
Url: https://github.com/eteran/edb-debugger

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(capstone)
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(libgvc)

ExclusiveArch: %ix86 x86_64

%description
edb is a graphical cross platform x86/x86-64 debugger.
It was inspired by Ollydbg, but aims to function on x86
and x86-64.

%prep
%setup -a1
%patch -p1

%build
%cmake \
       -Wno-dev
%cmake_build

%install
%cmake_install

install -Dm 644 src/res/images/edb.svg %buildroot%_iconsdir/hicolor/scalable/apps/edb.svg
install -Dm 644 edb.appdata.xml %buildroot%_datadir/metainfo/edb.appdata.xml

%files
%doc README.md
%_bindir/edb
%dir %_libdir/edb
%_libdir/edb/*.so
%_desktopdir/edb.desktop
%_pixmapsdir/edb.png
%_iconsdir/hicolor/scalable/apps/edb.svg
%_man1dir/edb.1.*
%_datadir/metainfo/edb.appdata.xml

%changelog
* Sun Jul 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
