Name: livecd-install
Version: 0.6
Release: alt8

Summary: Permanently install Live system
License: GPLv2
Group: System/Configuration/Other

Source: %name-%version.tar
Source1: %name.pam
Source2: %name.apps

Packager: Andriy Stepanov <stanv@altlinux.ru>

BuildArch: noarch
Requires: alterator-wizardface
Requires: alterator-livecd >= 0.5-alt1
Requires: alterator-vm alterator-grub alterator-users >= 10.2-alt1 alterator-root >= 0.9-alt1
Requires: livecd-evms
Requires: make-initrd-plymouth 
Requires: consolehelper

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary

%prep
%setup -q

%install
%makeinstall
%__install -D -p -m 0644 %{S:1} %buildroot%_sysconfdir/pam.d/%name
%__install -D -p -m 0644 %{S:2} %buildroot%_sysconfdir/security/console.apps/%name
%__install -d -m 0755 %buildroot%_bindir
%__ln_s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
mkdir -p %buildroot%_x11sysconfdir/profile.d
install -m 0755 zdg-user-dirs-install.sh %buildroot%_x11sysconfdir/profile.d/

%files
%config(noreplace) %_sysconfdir/%name
%_bindir/%name
%_sbindir/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name
%_datadir/alterator/steps/*
%_libexecdir/alterator/hooks/livecd-*.d/*
%_desktopdir/*.desktop
%_x11sysconfdir/profile.d/*

%changelog
* Wed Jun 27 2012 Mikhail Efremov <sem@altlinux.org> 0.6-alt8
- preinstall hooks: Add rm-issue.

* Thu Sep 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt7
- remove alterator-wisardf*, not only alterator-wisardface

* Thu Jun 30 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt6
- remove-livecd-pkgs: Remove branding-*-slideshow.

* Tue Jun 28 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt5
- Add License install step.

* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt4
- remove-livecd-pkgs: preinstall -> postinstall stage.
- remove-livecd-pkgs: remove more packages.

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- put livecd-install.desktop only if UID==500

* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt2
- Add postinstall firsttime hook.
- preinstall hooks: Use digital prefix.

* Thu Jun 02 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- livecd-postinstall.d -> livecd-preinstall.d.
- Drop hal.sh hook.

* Mon Apr 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- put install icon on desktop

* Tue Apr 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt3
- plymouth setup added

* Wed Apr 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- turn GdM autologin off

* Tue Apr 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- use grub instead lilo

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- fix application name (closes: #20601)
- improve some livecd-postinstall.d scripts
- don't umount partitions with newly installed system
- move profile specific data from general framework package

* Fri Jun 19 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Adjust date time at running Live, then copy settings.
  Export $ALTERATOR_DESTDIR

* Wed Jun 17 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt8
- Use consolehelper

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt7
- umount bind over bind

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt6
- after installation umount all FS at $target_dir

* Tue Jun 09 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- Correct .desktop file

* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- Add step: ditetime

* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- Add steps: root, users

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- Add dependency to lived-evms

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- Initial build
