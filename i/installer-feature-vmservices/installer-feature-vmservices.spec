Name: installer-feature-vmservices
Version: 0.2.0
Release: alt1%ubt

Summary: Setup virtual machine services
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt

%description
Setup services for start/not start in/out of virtual machine.

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
* Wed Apr 11 2018 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1%ubt
- detect Hyper-V

* Wed Apr 11 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.4-alt1%ubt
- force switch services

* Wed Apr 11 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1%ubt
- update services list

* Wed Apr 11 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1%ubt
- fix path to chkconfig

* Tue Apr 10 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1%ubt
- fix setup services

* Tue Apr 10 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1%ubt
- initial build
