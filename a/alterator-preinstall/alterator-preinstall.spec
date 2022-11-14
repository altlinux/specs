%define _altdata_dir %_datadir/alterator

Name: alterator-preinstall
Version: 0.8.0
Release: alt1

Summary: Alterator preinstall hooks runner module
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

Requires: alterator >= 4.17-alt1
Requires: alterator-l10n >= 2.1-alt4
Requires: installer-scripts-remount-stage2 >= 0.5.21-alt1
Conflicts: alterator-lookout < 1.6-alt6
Conflicts: installer-common-stage2 < 1.8.4-alt1

BuildPreReq: alterator >= 4.7-alt6

%description
This is an alterator preinstall hooks runner module.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Mon Nov 14 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- copy preinstall scripts from $destdir in order to:
  + execute scripts strictly by numbering
  + do not execute duplicate scripts from $destdir

* Fri Aug 19 2022 Anton Midyukov <antohami@altlinux.org> 0.7.5-alt1
- backend3/preinstall: redirect output of running preinstall scripts
  to /tmp/preinstall.log

* Fri Jun 04 2021 Anton Midyukov <antohami@altlinux.org> 0.7.4-alt1
- backend3/preinstall: running alterator in chroot before mounting socket

* Fri Jun 04 2021 Anton Midyukov <antohami@altlinux.org> 0.7.3-alt1
- backend3/preinstall: not mount /run to /destination/run

* Tue Feb 04 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- Do not turn off host alteratord during preinstall in autoinstall mode (ALT #29783)

* Fri Dec 21 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt2
- require installer-scripts-remount-stage2 for remount script
  (moved from installer-common-stage2)
- added an Url:

* Tue Dec 11 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- notify for remount failure

* Tue Dec 11 2012 Michael Shigorin <mike@altlinux.org> 0.7-alt1
- employ install2-remount-functions to avoid stray processes
  blocking $destdir remounting

* Wed May 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt5
- direct start alteratord even if it seems that systemd is here

* Tue May 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt4
- change alerator socket dir according alterator 4.22

* Tue May 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- /run directory binding added

* Tue May 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- alterator socket dir binding removed

* Tue May 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- change alerator socket dir according alterator 4.21

* Thu Dec 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- use alterator-wait utility to avoid race between daemon switching

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- replace alteratord service instead of chroot operation

* Wed Oct 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- backend: alterator_api_version = 1

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Fixed summary&description.
- Added timestamping.

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
