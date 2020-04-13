%define rname mint-themes

Name: gtk-themes-mint
Version: 1.8.0
Release: alt2
Summary: Mint themes
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-themes.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: icon-themes-mint-x

Source: %rname-%version.tar
Patch: %rname-%version.patch

BuildArch: noarch
BuildRequires: python3
# sassc

%description
A collection of mint themes

%prep
%setup -q -n %rname-%version
%patch -p1

%build
./generate-themes.py

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%_datadir/themes/*

%changelog
* Mon Apr 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt2
- do not generate Mint-Y* themes

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- initial release

