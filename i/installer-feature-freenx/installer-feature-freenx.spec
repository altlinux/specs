Name: installer-feature-freenx
Version: 0.2
Release: alt2

Summary: FreeNX Server setup
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: FreeNX Server setup
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2

%description stage2
%summary

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Sun Feb 22 2009 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- built for Sisyphus

* Sun Jan 11 2009 Michael Shigorin <mike@altlinux.org> 0.2-alt1.M40.1
- start/chkconfig sshd, too (so this version actually works)

* Tue Jan 06 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt0.M40.1
- built for M40

* Tue Jan 06 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

