# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_enable opencl

Name: cpu-x
Version: 5.0.4
Release: alt2
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/X0rg/CPU-X
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires(pre): rpm-macros-cmake
Buildrequires: gcc-c++ cmake 
BuildRequires: nasm
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.12.0
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glfw3) >= 3.3
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libcpuid) >= 0.4.0
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libproc2)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(ncursesw)
%{?_enable_opencl:BuildRequires: ocl-icd-devel}
Requires: icon-theme-hicolor

ExclusiveArch: %ix86 x86_64

%description
CPU-X is a Free software that gathers information on CPU, motherboard and more.
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line.

%prep
%setup
%patch -p1

%build
%cmake \
%if_enabled opencl
    -DWITH_OPENCL=ON \
%endif
%nil

%cmake_build

%install
%cmake_install
%find_lang %name

# Cleanup unpackage files
rm -r %buildroot%_datadir/fish
rm -r %buildroot%_datadir/zsh
rm -r %buildroot%_datadir/locale/zh_Hant

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_desktopdir/*
%_datadir/polkit-1/actions/*
%_datadir/metainfo/*.appdata.xml
%_datadir/bash-completion/completions/*
%_datadir/glib-2.0/schemas/*
%_prefix/libexec/*

%changelog
* Tue Sep 17 2024 Anton Midyukov <antohami@altlinux.org> 5.0.4-alt2
- Enable OpenCL (thanks L.A. Kostis) (Closes: 51118)

* Wed May 01 2024 Anton Midyukov <antohami@altlinux.org> 5.0.4-alt1
- New version 5.0.4

* Mon Jan 08 2024 Anton Midyukov <antohami@altlinux.org> 5.0.3-alt1
- New version 5.0.3.

* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- New version 5.0.2.

* Mon Oct 23 2023 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- New version 5.0.1 (Closes: 48113).

* Wed Oct 18 2023 Anton Midyukov <antohami@altlinux.org> 4.5.3-alt2
- rebuild with libproc2

* Sun Apr 23 2023 Anton Midyukov <antohami@altlinux.org> 4.5.3-alt1
- New version 4.5.3.

* Sat Jan 14 2023 Anton Midyukov <antohami@altlinux.org> 4.5.2-alt1
- new version 4.5.2

* Fri Oct 28 2022 Anton Midyukov <antohami@altlinux.org> 4.5.1-alt1
- new version 4.5.1
- fix russian translate

* Mon Oct 17 2022 Anton Midyukov <antohami@altlinux.org> 4.5.0-alt1
- new version 4.5.0

* Fri Sep 09 2022 Anton Midyukov <antohami@altlinux.org> 4.4.0-alt1
- new version 4.4.0

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 4.3.1-alt1
- new version 4.3.1

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 4.3.0-alt1
- new version 4.3.0

* Fri Apr 09 2021 Anton Midyukov <antohami@altlinux.org> 4.2.0-alt1
- new version 4.2.0

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- new version 4.0.0

* Wed Apr 17 2019 Anton Midyukov <antohami@altlinux.org> 3.2.4-alt1
- new version 3.2.4
- drop xdg-su support

* Mon Oct 15 2018 Anton Midyukov <antohami@altlinux.org> 3.2.3-alt1
- new version 3.2.3

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Wed Jan 10 2018 Anton Midyukov <antohami@altlinux.org> 3.1.3.1-alt1
- new version 3.1.3.1

* Mon Sep 18 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2
- fix run as root for sysvinit

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- Initial build for Alt Linux Sisyphus.
