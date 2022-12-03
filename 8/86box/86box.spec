Name: 86box
Version: 3.11
Release: alt1
Summary: 86Box is a low level x86 emulator that runs older operating systems and software designed for IBM PC systems
Group: Emulators
License: GPLv3
Url: https://86box.net/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildPreReq: rpm-macros-cmake qt5-declarative-devel libslirp-devel
BuildRequires: gcc-c++
BuildRequires: cmake libpng-devel zlib-devel libopenal-devel librtmidi-devel libpcre-devel qt5-tools-devel
BuildRequires: fontconfig-devel git-core libxcb libSDL2_ttf-devel libXi-devel libalsa-devel python-modules-compiler python-modules-encodings python-modules-logging python-modules-xml qt5-base-devel

ExcludeArch: aarch64 armh ppc64le

%description
86Box is a low level x86 emulator that runs older operating systems
and software designed for IBM PC systems and compatibles from 1981
through fairly recent system designs based on the PCI bus.

Important note.
For correct work you need BIOS files: https://github.com/86Box/roms/
Download release with the release number of emulator, and unzip in
~/.local/share/86Box/

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install
install -D -m0755 ./%_arch-alt-linux/src/86Box %buildroot%_bindir/%name

%files
%doc README.md COPYING
%_bindir/%name

%changelog
* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.11-alt1
- update to new version

* Fri Aug 5 2022 Artyom Bystrov <arbars@altlinux.org> 3.7-alt1
 - update to new version

* Mon Jul 26 2022 Artyom Bystrov <arbars@altlinux.org> 3.6-alt1
 - initial release
