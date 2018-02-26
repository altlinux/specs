Name: installer-feature-kdm4-autologin
Version: 0.0.1
Release: alt1

Summary: KDM4 auto login for user altlinux
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 29 2011 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build.
