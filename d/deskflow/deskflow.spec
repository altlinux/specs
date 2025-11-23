%define _unpackaged_files_terminate_build 1

Name: deskflow
Version: 1.25.0
Release: alt1

Summary: Share a single keyboard and mouse between multiple computers
License: GPL-2.0
Group: Accessibility
Url: https://github.com/deskflow/deskflow

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libei-1.0)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(libportal)
BuildRequires: help2man
BuildRequires: libtomlplusplus-devel
BuildRequires: cli11-devel
BuildRequires: libgtest-devel
BuildRequires: qt6-tools-devel

%description
Deskflow is a free and open source keyboard and mouse sharing app. Use
the keyboard, mouse, or trackpad of one computer to control nearby
computers, and work seamlessly between them. It's like a software KVM
(but without the video). TLS encryption is enabled by default. Wayland
is supported. Clipboard sharing is supported.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_DOCS=OFF \
       -DSKIP_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%files -f %{name}.lang
%doc README.md LICENSE SECURITY.md
%_bindir/%name
%_bindir/%{name}-core
%_man1dir/%name.*
%_man1dir/%{name}-core.*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/*%{name}.*.xml
%exclude %_datadir/licenses/deskflow

%changelog
* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.25.0-alt1
- New version 1.25.0.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.24.0-alt1
- New version 1.24.0.

* Thu Jul 31 2025 Nikolay Strelkov <snk@altlinux.org> 1.23.0-alt1
- New version 1.23.0.

* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.22.0-alt1
- New version 1.22.0.

* Sat May 24 2025 Nikolay Strelkov <snk@altlinux.org> 1.21.2-alt1
- Initial build for Sisyphus
