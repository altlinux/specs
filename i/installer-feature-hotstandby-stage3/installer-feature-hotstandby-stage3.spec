Name: installer-feature-hotstandby-stage3
Version: 0.1
Release: alt2

Summary: Installer stage3 alterator-hotstandby hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Mikhail Efremov <sem@altlinux.org>
BuildArch: noarch
Requires: alterator-hotstandby
Source: %name-%version.tar

%description
This package contains installer stage3 hook for
alterator-hotstandby module.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Sep 30 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt2
- rename 95-hotstandby.sh to 96-hotstandby.sh.

* Fri Sep 18 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

