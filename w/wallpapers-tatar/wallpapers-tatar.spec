Name: wallpapers-tatar
Version: 1.0.0
Release: alt1

Summary: Wallpapers for tatar localization
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
* Fri Oct 04 2024 Kirill Izmestev <felixz@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus.
