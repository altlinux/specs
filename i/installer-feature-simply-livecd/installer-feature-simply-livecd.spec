Name: installer-feature-simply-livecd
Version: 10.5.0
Release: alt1

Summary: LiveCD install hooks for Simply Linux.
License: GPLv2+
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-livecd >= 0.5
Conflicts: installer-common-stage2
Conflicts: livecd-install < 0.7-alt1
Provides: installer-features-simply-livecd
Obsoletes: installer-features-simply-livecd < 0.3

Requires: libshell

# Run installer features while install from LiveCD.
Requires: livecd-installer-features

# For luks installer step. Despite it is installer
# package it seems harmless enough to be used
# on live system.
Requires: installer-distro-simply-linux

# Alterator modules used for livecd-install
# Only require alterator-grub for arches that have grub.
%ifarch  %ix86 x86_64 aarch64 ppc64le
Requires: alterator-grub
%endif
Requires: alterator-vm
Requires: alterator-luks

# Installer fearures for Simply Linux.
# NOTE: installer-feature-bell-off-stage3 uneeded:
# the same changes are made by rootfs image script
# in mkimage-profiles.
# NOTE: installer-feature-online-repo replaced
# by m-p use/live/repo feature.
Requires: installer-feature-lightdm-stage3
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-desktop-suspend-stage2

%description
LiveCD install hooks for Simply Linux.

%prep
%setup

%install
%define init_hookdir %_libexecdir/alterator/hooks/livecd-initinstall.d
%define pre_hookdir %_libexecdir/alterator/hooks/livecd-preinstall.d
%define post_hookdir %_libexecdir/alterator/hooks/livecd-postinstall.d
mkdir -p %buildroot%_datadir/livecd-install/alterator-menu/
mkdir -p %buildroot%init_hookdir
mkdir -p %buildroot%pre_hookdir
mkdir -p %buildroot%post_hookdir
install -pm755 livecd-initinstall.d/* %buildroot%init_hookdir/
install -pm755 livecd-preinstall.d/* %buildroot%pre_hookdir/
install -pm755 livecd-postinstall.d/* %buildroot%post_hookdir/
cp -ar alterator-menu/ %buildroot%_datadir/livecd-install

%files
%init_hookdir/*
%pre_hookdir/*
%post_hookdir/*
%_datadir/livecd-install/

%changelog
* Wed Sep 04 2024 Mikhail Efremov <sem@altlinux.org> 10.5.0-alt1
- Show alterator-logs in the acc.

* Fri Jun 16 2023 Mikhail Efremov <sem@altlinux.org> 10.4.0-alt1
- Drop installer-feature-sudo-enable-by-default-stage3.

* Thu Jun 08 2023 Mikhail Efremov <sem@altlinux.org> 10.3.0-alt1
- livecd-preinstall: Drop 80-setup-user-groups hook.
- Drop installer-feature-desktop-other-fs-stage2.
- Use installer-feature-desktop-suspend-stage2 again (closes: #44474).
- setup-backgrounds: Don't exit if failed to change background.

* Thu Jun 23 2022 Mikhail Efremov <sem@altlinux.org> 10.2.0-alt1
- livecd-preinstall: Add setup-backgrounds hook.

* Mon Apr 11 2022 Mikhail Efremov <sem@altlinux.org> 10.1.0-alt1
- Include user to fuse group.
- Drop installer-feature-online-repo.

* Wed Oct 13 2021 Mikhail Efremov <sem@altlinux.org> 10.0.0-alt1
- Drop 05-vm-profile.sh.

* Thu Feb 25 2021 Mikhail Efremov <sem@altlinux.org> 9.1.0-alt1
- Try to kill light-locker during install.
- Only require alterator-grub for arches that have grub.
- Drop installer-feature-nfs-client-stage3.

* Mon Dec 23 2019 Mikhail Efremov <sem@altlinux.org> 9.0.0-alt1
- Set license as GPLv2+.
- Requre alterator modules used by us.
- Require installer-distro-simply-linux.
- Drop installer-feature-bell-off-stage3.
- Drop installer-feature-symlinks-from-sbin.

* Tue Dec 03 2019 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Drop lightdm hook.
- Kill xfce4-screensaver during install.

* Mon Oct 07 2019 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Require installer-feature-lightdm-stage3.
- cleanup: Arrange installer-features in alphabet order.
- Change lightdm theme to ClassicLooks.

* Mon Jun 19 2017 Mikhail Efremov <sem@altlinux.org> 0.8.11-alt1
- 05-vm-profile.sh from i-d-simply-linux.
- Disable thunar automount during install.

* Thu May 18 2017 Mikhail Efremov <sem@altlinux.org> 0.8.10-alt1
- Disable light-locker during install.

* Fri Mar 31 2017 Mikhail Efremov <sem@altlinux.org> 0.8.9-alt1
- i-f-sudo-enable-by-default moved stage2 -> stage3.
- lightdm: Setup indicators.

* Tue Apr 14 2015 Mikhail Efremov <sem@altlinux.org> 0.8.8-alt1
- Set Xfce4 as default session to start.
- lightdm: Disable language selector.

* Thu Feb 13 2014 Mikhail Efremov <sem@altlinux.org> 0.8.7-alt1
- Disable cups.socket.

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt2
- Drop installer-feature-cpufreq-stage3.

* Mon Jun 10 2013 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt1
- Enable cpufreq-simple.service.

* Fri May 31 2013 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt1
- Add module-expert-list (by cas@).

* Mon May 27 2013 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- Drop 'removable' initinstall hook.
- Add installer-feature-symlinks-from-sbin.

* Thu Apr 18 2013 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Add 'removable' initinstall hook.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- lightdm: Set icon theme SimpleSL.
- Hide alterator-logs in the acc.

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Explicitly enable prefdm.service.
- Disable krb5kdc service.
- Change lightdm theme to Clearlooks-Phenix.
- Added setup-journald postinstall hook.

* Thu Feb 28 2013 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Enable ntpd.service.
- Enable more services.
- Enable nmb and smb services.
- services postinstall hook: Use systemctl.
- Replace gdm-theme with lightdm-theme preinstall hook.

* Thu Feb 14 2013 Mikhail Efremov <sem@altlinux.org> 0.7.7-alt2
- Drop installer-feature-hdd-pm-disable-stage3.

* Thu Jan 10 2013 Mikhail Efremov <sem@altlinux.org> 0.7.7-alt1
- Drop obsoleted installer features.
- Drop disable-whatis hook.

* Fri Dec 23 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt4
- Add disable-whatis hook.
- Drop updatedb.sh.

* Thu Nov 24 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt3
- Use installer-feature-hdd-pm-disable-stage3.

* Thu Nov 03 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt2
- Use installer-feature-cpufreq-stage3.

* Thu Sep 22 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt1
- services: Turn on crond, anacron and dnsmasq.
- Use own setup-resume install hook.
- Use installer-feature-bell-off-stage3.
- gdm: Set SoundOnLogin=false.

* Thu Aug 25 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- setup-user-groups hook: Add vboxusers group.

* Mon Aug 22 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- gdm: Simplify greeter.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Install all hooks.
- Set gdm theme 'simply' again.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Return gdm theme 'simple'.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Change gdm-theme: simple -> simply.
- Rename hook: gdm-simple -> gdm-theme.

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Add vm-profile hook.
- Add setup-user-groups hook.
- Use installer-feature-online-repo instead of own hook.
- Add dependences on installer-features for Simply.

* Wed Jul 20 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Add updatedb hook.
- Kill polkit agent before install.

* Mon Jun 20 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Map hostname to 127.0.0.1.

* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- Drop remove-installer-pkgs hook.

* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Use digital prefix for hooks.
- Add remove-installer-pkgs hook.

* Thu Jun 02 2011 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- livecd-postinstall.d -> livecd-preinstall.d.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Rename package.
- Disable zram-swap.

* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Add online-repo hook.

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

