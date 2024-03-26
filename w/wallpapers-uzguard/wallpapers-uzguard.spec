Name: wallpapers-uzguard
Version: 1.0.0
Release: alt2

Summary: Wallpapers for Uzguard
License: Distributable
Group: Graphics

Source: wallpapers.tar

BuildArch: noarch

%description
%summary

%prep
%setup -n wallpapers

%install
mkdir -p %buildroot%_datadir/wallpapers
mkdir -p %buildroot%_datadir/backgrounds
cp -a * %buildroot%_datadir/wallpapers
for i in *;do ln -s ../wallpapers/$i %buildroot%_datadir/backgrounds/$i;done

%files
%_datadir/wallpapers/*
%_datadir/backgrounds/*

%changelog
* Wed Mar 13 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- Make symlinks to /usr/share/backgrounds.

* Wed Mar 13 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus.
