Name: cpu-x
Version: 3.1.3
Release: alt1
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPLv3+
Group: System/Kernel and hardware
Url: https://github.com/X0rg/CPU-X
Source: %name-%version.tar
Buildrequires(pre): rpm-macros-cmake cmake
Buildrequires: gcc-c++ pkgconfig(gtk+-3.0) pkgconfig(libarchive) pkgconfig(libcurl) pkgconfig(libpci) pkgconfig(libprocps) pkgconfig(libstatgrab) pkgconfig(ncurses) pkgconfig(libcpuid)
Requires: icon-theme-hicolor

%description
CPU-X is a Free software that gathers information on CPU, motherboard and more.
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line. 

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_desktopdir/*
%_datadir/polkit-1/actions/org.pkexec.cpu-x.policy

%changelog
* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- Initial build for Alt Linux Sisyphus.
