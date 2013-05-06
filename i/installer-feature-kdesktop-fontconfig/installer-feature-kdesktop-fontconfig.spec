Name: installer-feature-kdesktop-fontconfig
Version: 0.2
Release: alt1

Summary: Setup fonts default settings
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setup fonts default settings

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
* Mon May 06 2013 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- disable autohint by default

* Wed Mar 16 2011 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial release
