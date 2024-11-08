Name:    x-cursor-themes-breezex
Version: 2.0.1
Release: alt1

Summary: BreezeX cursors theme for linux desktops
License: GPL-3.0-only
Group:   Graphics
Url:     https://github.com/ful1e5/BreezeX_Cursor

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%build

%install
mkdir -p %buildroot%_iconsdir
cp -vr themes/BreezeX-Black %buildroot%_iconsdir
cp -vr themes/BreezeX-Dark %buildroot%_iconsdir
cp -vr themes/BreezeX-Light %buildroot%_iconsdir

%files
%doc LICENSE README.md
%_iconsdir/*

%changelog
* Thu Nov 07 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.0.1-alt1
- initial build

