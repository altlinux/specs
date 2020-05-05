%define rname mint-x-icons

Name: icon-themes-mint-x
Version: 1.5.5
Release: alt1
Summary: Mint-X icon theme
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-x-icons
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar

BuildArch: noarch

%description
A mint/metal theme based on mintified versions of
Clearlooks Revamp, Elementary and Faenza.

%prep
%setup -q -n %rname-%version

%build

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%_datadir/icons/*

%changelog
* Tue May 05 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- initial release

