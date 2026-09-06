%define oname OpenFodder

Name: openfodder
Version: 2.0.0
Release: alt2
Summary: An open source version of the Cannon Fodder engine, for modern operating systems
Group: Games/Strategy
License: GPLv3
Url: http://openfodder.com/

Source: %name-%version.tar
patch0: 0001-Change-data-path.patch
BuildPreReq: rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libSDL3_mixer-devel
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

%patch0 -p1

%build

%cmake
%cmake_build

%install

mkdir -p %buildroot%_datadir/%oname
install -D -m0755 ./%_arch-alt-linux/openfodder %buildroot%_bindir/%name
cp -r Run/* %buildroot%_datadir/%oname/
install -D -m0755 FreeDesktop/openfodder.desktop %buildroot%_desktopdir/%name.desktop
install -D -m0755 FreeDesktop/openfodder.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%doc README.md COPYING
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png

%files data
%_datadir/%oname

%changelog
* Sun Sep  6 2026 Artyom Bystrov <arbars@altlinux.org> 2.0.0-alt2
- Add patch for changing path to game data

* Mon Mar 30 2026 Artyom Bystrov <arbars@altlinux.org> 2.0.0-alt1
- update to new version
- remove start script

* Thu Jan 25 2024 Artyom Bystrov <arbars@altlinux.org> 1.8.0-alt1
- update to new version

* Thu May 25 2023 Artyom Bystrov <arbars@altlinux.org> 1.7.0-alt1
- update to new version

* Tue Feb 18 2020 Artyom Bystrov <arbars@altlinux.org> 1.6.0-alt1
 - initial release
