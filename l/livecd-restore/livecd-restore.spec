Name: livecd-restore
Version: 0.2
Release: alt1

Summary: restore system from backups
License: GPLv2
Group: System/Configuration/Other

Source: %name-%version.tar

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch
Requires: alterator-wizardface alterator-wizardface-usermode
Requires: alterator-vm alterator-bacula alterator-grub alterator-livecd
Requires: livecd-evms

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary

%prep
%setup -q

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/%name
%_bindir/%name
%_desktopdir/*.desktop

%changelog
* Fri Apr 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- use grub instead lilo

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- Add dependency to livecd-evms

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
