%define rname mint-x-icons

Name: icon-themes-mint-x
Version: 1.7.2
Release: alt1
Summary: Mint-X icon theme
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-x-icons
Vcs: https://github.com/linuxmint/mint-x-icons.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar

BuildArch: noarch

%description
A mint/metal theme based on mintified versions of
Clearlooks Revamp, Elementary and Faenza.

%package -n folder-color-switcher-mint-x
Summary: Mint-X style for Folder Color Switcher
Group: Graphical desktop/Other
Requires: %name = %EVR
%description -n folder-color-switcher-mint-x
This package contains the style for Folder Color Switcher.

%prep
%setup -q -n %rname-%version

%build

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%_datadir/icons/*

%files -n folder-color-switcher-mint-x
%_datadir/folder-color-switcher/colors.d/Mint-X.json

%changelog
* Wed May 21 2025 Alexander Kovalev <alexvk@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue May 05 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- initial release
