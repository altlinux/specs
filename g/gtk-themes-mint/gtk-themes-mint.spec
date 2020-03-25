%define rname mint-themes

Name: gtk-themes-mint
Version: 1.8.0
Release: alt1
Summary: Mint themes
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-themes.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: icon-themes-mint-x

Source: %rname-%version.tar
Patch: %rname-%version.patch

BuildArch: noarch
BuildRequires: sassc python3

%description
A collection of mint themes

%prep
%setup -q -n %rname-%version
%patch -p1

%build
./generate-themes.py
rm -fr usr/share/themes/Mint-Y*

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%_datadir/themes/*

%changelog
* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- initial release

