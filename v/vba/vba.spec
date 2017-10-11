Name: vba
Version: 2.0.0
Release: alt1

Summary: GBA emulator
License: GPLv2.0
Group: Emulators
Url: https://github.com/visualboyadvance/visualboyadvance

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://github.com/visualboyadvance/visualboyadvance/archive/master.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libarchive-devel
BuildRequires: glib2-devel

%description
A GameBoy Advance emulator,
requires BIOS-file to run GBA ROMs.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_datadir/%name/db
%_datadir/%name/flags
%_datadir/%name/icon
%_datadir/%name/fonts

%changelog
* Wed Oct 11 2017 Alexey Appolonov <alexey@altlinux.org> 2.0.0-alt1
- First ALT Linux release.
