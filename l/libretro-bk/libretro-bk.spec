Name: libretro-bk
Version: git.cf70ce5
Release: alt1

Summary: BK computer series emulatior libretro core
License: GPL-2.0-only
Group: Emulators

Url: https://github.com/libretro/bk-emulator
Source: %name-%version-%release.tar

BuildRequires: build-essential
BuildRequires: gcc-c++
BuildRequires: make libSDL-devel

%description
This software is a Linux/SDL emulator for Soviet (russian) Electronica BK series.
%summary

This package is for RetroArch/Libretro front-end.

%prep
%setup -n %name-%version-%release

%build
%make_build -f Makefile.libretro

%install
mkdir -p %buildroot%_libexecdir/libretro
install -Dp -m0644 ./bk_libretro.so %buildroot%_libexecdir/libretro

%files
%_libexecdir/libretro/bk_libretro.so

%changelog
* Tue Apr  2 2024 Artyom Bystrov <arbars@altlinux.org> git.cf70ce5-alt1
- Initial package.
