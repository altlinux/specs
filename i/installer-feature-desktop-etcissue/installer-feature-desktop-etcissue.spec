Name: installer-feature-desktop-etcissue
Version: 0.1.1
Release: alt2

Summary: Setup /etc/issue
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar


%description
Setup /etc/issue and /etc/issue.net .

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot/%hookdir
install -pm755 *.sh %buildroot/%hookdir/

%files
%hookdir/*

%changelog
* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt2
- dont use ubt macro

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- fix check /etc/issue presence

* Mon Apr 16 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
