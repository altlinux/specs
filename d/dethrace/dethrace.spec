Name: dethrace
Version: 0.6.0
Release: alt1
Summary: Source port of the vehicular combat video game Carmageddon
### dethrace is GPL-3.0+, but uses glad (MIT license) and miniaudio (MIT)
License: GPL-3.0-or-later
Group: Games/Arcade
Url: https://twitter.com/dethrace_labs
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/dethrace-labs/dethrace/archive/refs/tags/v%version.tar.gz#/%name-%version.tar.gz
Source2: dethrace.sh
#Thanks to OpenSUSE team!s
Patch: 0001-build-dynamically-link-libsmacker.patch
BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ 
BuildRequires: libsmacker-devel
BuildRequires: pkg-config
BuildRequires: libSDL2-devel
#https://github.com/Dav1dde/glad
Provides: bundled(glad)
#https://miniaud.io/
Provides: bundled(miniaudio)

%description
A source port of the vehicular combat video game Carmageddon.

NOTE: To play Carmageddon with dethrace you need the original game files!
https://github.com/dethrace-labs/dethrace#game-content

%prep
%setup
# unbundle libsmacker
%patch0 -p1
rm -r lib/libsmacker/

%build
echo %version > VERSION
mkdir %_cmake__builddir && cd %_cmake__builddir
cmake .. && cd ..
# for some reason it segfaults with the distro CFLAGS
#%%cmake
%cmake_build

%install
install -Dm0755 ./%_cmake__builddir/dethrace %buildroot%_libexecdir/dethrace-bin
install -Dm0755 %SOURCE2 %buildroot%_bindir/dethrace

%files
%doc LICENSE
%doc NOTES.md README.md
%_bindir/dethrace
%_libexecdir/dethrace-bin

%changelog
* Tue May 30 2023 Artyom Bystrov <arbars@altlinux.org> 0.6.0-alt1
- initial build for ALT Sisyphus

