%define rname mint-themes

Name: gtk-themes-mint
Version: 2.1.8
Release: alt1
Summary: Mint themes
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-themes.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: icon-themes-mint-x icon-themes-mint-y

Source: %rname-%version.tar

BuildArch: noarch
BuildRequires: python3-module-libsass

%description
A collection of mint themes

%prep
%setup -q -n %rname-%version

%build
./generate-themes.py
for i in X Y; do cp metacity-theme-2.xml usr/share/themes/Mint-$i/metacity-1/; done

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%_datadir/themes/*

%changelog
* Thu Oct 10 2024 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.8.8-alt1
- 1.8.8

* Wed Sep 09 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Tue May 05 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Apr 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt3
- remove Mint-Y* themes

* Mon Apr 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt2
- do not generate Mint-Y* themes

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- initial release

