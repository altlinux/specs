Name: installer-feature-server-raid-fixup
Version: 0.5.0
Release: alt1

Summary: Tune mdraid sync speeds and write-intent bitmaps
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Tune mdraid sync speeds and write-intent bitmaps
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2 >= 1.8.0

%description stage2
%summary

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/initinstall.d/*
%_datadir/install2/preinstall.d/*
%_datadir/install2/postinstall.d/*

%changelog
* Fri Oct 24 2014 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- updated for current installer (including remount scripts)
  + do not modify mdadm.conf, it's been cared for already

* Thu May 22 2008 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- fix postinstall script (thanks ldv@ for diags/hint)

* Mon Apr 21 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- more strict check (don't do anything if no arrays exist)

* Fri Apr 11 2008 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- move common md slow-down earlier (to initinstall)
  so that basesystem step is less hindered by resync

* Fri Apr 11 2008 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- add postinstall script calling mdadm in attempt to set up
  write intent bitmaps (see also #14877)

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- add raid sync regulatory stuff based on
  installer/initinstall.d/10-disk.sh with major bugfixes:
  will focus on getting root md synced

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- use script from installer (with small but crucial fix)

