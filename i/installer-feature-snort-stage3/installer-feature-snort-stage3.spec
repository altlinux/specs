Name: installer-feature-snort-stage3
Version: 0.3
Release: alt1

Summary: Installer stage3 snort hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Mikhail Efremov <sem@altlinux.org>
BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-snort >= 0.1.0

%description
This package contains installer stage3 hook for
alterator-snort module.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Dec 22 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Create hook for alterator-net-eth.

* Tue Nov 03 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt3
- fix file path.

* Mon Nov 02 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2
- fix 'unbound variable' error.

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- enable snort only for bridges if they exists.
- fix exit status.

* Tue Oct 20 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

