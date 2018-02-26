Name: installer-feature-create-user
Version: 0.1
Release: alt1

Summary: Create user and setup autologin
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Create user and setup autologin

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Sun Mar 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


