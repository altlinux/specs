%define _altdata_dir %_datadir/alterator

Name: alterator-preinstall
Version: 0.6
Release: alt5

Summary: Alterator preinstall hooks runner module
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Source:%name-%version.tar

Requires: alterator >= 4.17-alt1
Requires: alterator-l10n >= 2.1-alt4
Conflicts: alterator-lookout < 1.6-alt6

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
