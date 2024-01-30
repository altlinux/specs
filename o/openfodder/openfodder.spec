Name: openfodder
Version: 1.8.0
Release: alt1
Summary: An open source version of the Cannon Fodder engine, for modern operating systems
Group: Games/Strategy
License: GPLv3
Url: http://openfodder.com/

Source: %name-%version.tar
Source2: openfodder.sh
BuildPreReq: rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libSDL2_mixer-devel
BuildRequires: git
ExcludeArch: armh
%description
An open source version of the Cannon Fodder engine, for modern operating systems

%package data
Group: Games/Strategy
Summary: Game demo data for OpenFodder
Requires: %name = %version

%description data
%summary

%prep
%setup -n %name-%version

%build

%cmake
%cmake_build

%install

mkdir -p %buildroot%_datadir/%name
install -D -m0755 ./%_arch-alt-linux/openfodder %buildroot%_libexecdir/%name/%name
install -D -m0755 %SOURCE2 %buildroot%_bindir/%name
cp -r Run/* %buildroot%_datadir/%name/
install -D -m0755 FreeDesktop/openfodder.desktop %buildroot%_desktopdir/%name.desktop
install -D -m0755 FreeDesktop/openfodder.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%doc README.md COPYING
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png

%files data
%_datadir/%name

%changelog
* Thu Jan 25 2024 Artyom Bystrov <arbars@altlinux.org> 1.8.0-alt1
- update to new version

* Thu May 25 2023 Artyom Bystrov <arbars@altlinux.org> 1.7.0-alt1
- update to new version

* Tue Feb 18 2020 Artyom Bystrov <arbars@altlinux.org> 1.6.0-alt1
 - initial release
