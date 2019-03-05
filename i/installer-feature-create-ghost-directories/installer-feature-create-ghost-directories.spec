Name: installer-feature-create-ghost-directories
Version: 0.1
Release: alt1
Summary: Installer feature for fixing ALT bug 35350
License: GPLv2
Group: System/Configuration/Other
Url: https://www.altlinux.org/Installer/beans
BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,postinstall}.d
install -pm755 04-* %buildroot%hookdir/initinstall.d/
install -pm755 99-* %buildroot%hookdir/postinstall.d/

%files
%hookdir/initinstall.d/*
%hookdir/postinstall.d/*

%changelog
* Tue Mar 05 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build

