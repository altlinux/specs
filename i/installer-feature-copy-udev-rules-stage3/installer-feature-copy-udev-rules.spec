Name: installer-feature-copy-udev-rules-stage3
Version: 0.7
Release: alt2

Summary: Copy generated udev rules to installed system
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/devel/installer/features
BuildArch: noarch
Requires: installer-common-stage3
Provides: installer-feature-eth-by-mac-stage3 = %version-%release
Obsoletes: installer-feature-eth-by-mac-stage3

Source: %name-%version.tar

%description
This package contains installer stage3 hook to
copy generated udev rules to installed system.

%prep
%setup

%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Jul 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt2
- Race fixed.

* Tue Jul 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- Forced persistent rules creation added.

* Thu Jun 18 2009 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Rewritten to support new udev rules generator.

* Thu Jun 18 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Added iftab2rules support.

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Changed iftab format (closes: #19313).
- Switched to stage3.

* Tue Apr 28 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- fixed return code when there are virtual interfaces 

* Fri Apr 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- rewritten using altarator-hw-functions to avoid binding virtual interfaces 

* Thu May 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- script based on installer-ltsp 0.1.1

