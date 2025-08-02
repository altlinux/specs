%define _unpackaged_files_terminate_build 1

Name: rgbds
Version: 0.9.4
Release: alt1
Summary: Rednex Game Boy Development System - An assembly toolchain for the Nintendo Game Boy and Game Boy Color 
License:  MIT
Group: Games/Other
Url: https://github.com/gbdev/rgbds

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  bison
BuildRequires:  pkgconfig(libpng)

%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker
package for the Game Boy and Game Boy Color.

%prep
%setup
%patch -p1
sed -i 's|/usr/local|%prefix|g' Makefile

%build
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Sat Aug 02 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.4-alt1
- 0.9.3 -> 0.9.4

* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.3-alt1
- Update based on upstream version.

* Thu Jul 25 2024 Pavel Shilov <zerospirit@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
