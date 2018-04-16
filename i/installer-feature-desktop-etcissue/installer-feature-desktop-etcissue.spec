Name: installer-feature-desktop-etcissue
Version: 0.1.0
Release: alt1%ubt

Summary: Setup /etc/issue
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt

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
* Mon Apr 16 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1%ubt
- initial build
