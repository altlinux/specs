Name: installer-feature-cleanup-libs-stage3
Version: 0.3
Release: alt1

Summary: Purge the libraries that became unneeded
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define hookdir %_datadir/install2/postinstall.d

%description
%summary
(usually due to deinstallation of packages requiring those
during post-installation cleanup)

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 99-cleanup-libs.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- hardwired skiplist (libre{cad,office} and libvirt)

* Wed Feb 25 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- up to three rounds

* Wed Feb 25 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
