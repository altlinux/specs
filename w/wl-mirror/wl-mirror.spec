%define _unpackaged_files_terminate_build 1

Name: wl-mirror
Version: 0.18.3
Release: alt1

Summary: Simple Wayland output mirror client
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/Ferdi265/wl-mirror

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdecor-0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wlr-protocols)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(egl)

%description
Output-mirroring tool for wlroots-based Wayland desktops.
wl-mirror is a tool to add output mirroring to sway and other
wlroots-based Wayland compositors. wl-mirror requires the export-dmabuf
or screencopy protocols to work.

%prep
%setup

%build
%cmake \
       -D INSTALL_EXAMPLE_SCRIPTS=ON \
       -D INSTALL_DOCUMENTATION=ON \
       -D WITH_GBM=ON \
       -D WITH_LIBDECOR=ON
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/wl-mirror
%_bindir/wl-present
%_man1dir/wl-mirror.*
%_man1dir/wl-present.*

%changelog
* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.18.3-alt1
- New version 0.18.3.

* Sat May 10 2025 Nikolay Strelkov <snk@altlinux.org> 0.18.2-alt1
- Initial build for Sisyphus
