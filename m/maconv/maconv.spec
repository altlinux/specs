Name:           maconv
Version:        1.0
Release:        alt2
Summary:       Convert old Macintosh formats, including MacBinary, Stuffit archives and HFS disk
Source:         %name-%version.tar
Patch:          maconv-gcc13.patch
Patch1:         GCC15-fix.patch
URL:            https://github.com/ParksProjets/Maconv/
Group:          Archiving/Compression
License:        GPLv3

# Automatically added by buildreq on Fri Jan 12 2024
# optimized out: bash5 cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libp11-kit libsasl2-3 libstdc++-devel python3-base sh5
BuildRequires: cmake gcc-c++

%description
Maconv is a Linux software that can convert all kinds of old Macintosh
formats, including MacBinary, Stuffit archives and HFS disk files.

%prep
%setup
%patch -p1
%patch1 -p1
sed -i "s@{CMAKE_INSTALL_PREFIX}/man@{CMAKE_INSTALL_PREFIX}/share/man@" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md docs
%_bindir/*
%_man1dir/*

%changelog
* Wed Jun 17 2026 Fr. Br. George <george@altlinux.org> 1.0-alt2
- Fix GCC15 build

* Fri Jan 12 2024 Fr. Br. George <george@altlinux.org> 1.0-alt1
- Initial build for ALT
