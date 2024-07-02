Name: libretro-vitaquake2
Version: 20240629
Release: alt1
Summary: Quake II Vita port for RetroArch
License: GPL-2.0-only
Group: Emulators

Url: https://github.com/libretro/tyrquake
Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libGL-devel

%description

PS Vita homebrew coder Rinnegatamante's port of Quake II for the
PlayStation Vita to libretro API; for use with RetroArch as a game
core.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
mkdir -p %buildroot%_libexecdir/libretro
install -Dp -m0644 ./vitaquake2_libretro.so %buildroot%_libexecdir/libretro

%files
%_libexecdir/libretro/vitaquake2_libretro.so

%changelog
* Tue Jul  2 2024 Artyom Bystrov <arbars@altlinux.org> 20240629-alt1
- Initial package
