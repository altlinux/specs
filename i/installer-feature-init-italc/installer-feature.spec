Name: installer-feature-init-italc
Version: 0.1
Release: alt1

Summary: Setup iTALC-master
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setup iTALC-master

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{preinstall.d,postinstall.d}
install -pm755 preinstall.sh %buildroot%hookdir/preinstall.d/90-italc.sh
install -pm755 postinstall.sh %buildroot%hookdir/postinstall.d/90-italc.sh

%files
%hookdir/postinstall.d/*
%hookdir/preinstall.d/*

%changelog
* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


