%define _altdata_dir %_datadir/alterator

Name: alterator-setup
Version: 0.3.15
Release: alt1

Summary: Perform initial setup of an OEM installation (warning!)
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: alterator >= 4.10-alt6
BuildRequires: rpm-macros-alterator

Requires: libshell
Requires: alterator-l10n >= 2.5-alt1
Requires: alterator-browser-qt >= 2.17.0
Requires: alterator-lookout => 2.4-alt1
Requires: alterator-wizardface
Requires: alterator-notes
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-root
Requires: alterator-users

Requires(post): chkconfig
Requires(preun): chkconfig

Conflicts: alterator-livecd
Conflicts: installer-common-stage2

Obsoletes: alterator-setup-x11vnc < %EVR

%description
%summary

WARNING: you really don't want to install this package
into an already configured system as it may spoil the
next boot!  Given that its sole purpose is the _initial_
configuration of a new system (like setting root password)
nobody should need that on an up-and-running host.

%package -n installer-feature-%name-stage2
Summary: Perform initial setup of an OEM installation (warning!)
Group: System/Configuration/Other

%description -n installer-feature-%name-stage2
Perform initial setup of an OEM installation.
This postinstall script for installer.

%package -n installer-feature-%name-x11vnc-stage2
Summary: Perform initial setup of an OEM installation through VNC (warning!)
Group: System/Configuration/Other

%description -n installer-feature-%name-x11vnc-stage2
Perform initial setup of an OEM installation through VNC.
This postinstall script for installer.

%prep
%setup

%install
%makeinstall

cat >> %buildroot%_sysconfdir/alterator-setup/config << EOF
# erase %name and related packages
REMOVE_SELF=1
#ALTERATOR_SETUP_VNC=1
EOF

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/steps
%_initdir/setup
%_sbindir/%name
%_sbindir/%name-prep
%_alterator_datadir/steps/*
%_alterator_datadir/ui/*
%_alterator_libdir/hooks/*/*
%_alterator_backend3dir/*
%_datadir/alterator-setup/
/lib/systemd/system/setup.service
/lib/systemd/system/setup.target

%files -n installer-feature-%name-stage2
%_datadir/install2/postinstall.d/80-alterator-setup

%files -n installer-feature-%name-x11vnc-stage2
%_datadir/install2/postinstall.d/81-alterator-setup-vnc

# package is removed in postinstall hook, but
# 'systemd stop' stops whole setup.service with hook.
%preun
if [ -x /sbin/sd_booted ]; then
/sbin/sd_booted || %preun_service setup
fi

%changelog
* Thu Feb 16 2023 Anton Midyukov <antohami@altlinux.org> 0.3.15-alt1
- setup.service: wait for network-online.target to complete

* Mon Nov 29 2021 Anton Midyukov <antohami@altlinux.org> 0.3.14-alt1
- 93-enable-vnc-server-pkgs.sh: do not require systemctl (Closes: 41457)
- installer-feature-%name-stage2, installer-feature-%name-x11vnc-stage2:
  do not require install2-init-functions

* Fri Nov 19 2021 Anton Midyukov <antohami@altlinux.org> 0.3.13-alt1
- alterator-setup: Enable VNC if ALTERATOR_SETUP_VNC is set in config
- alterator-setup: Generate a password for VNC, run VNC from setup.service
- Add alterator-setup-prep to prepare alterator-setup to work via VNC
- Obsoletes alterator-setup-x11vnc

* Fri Oct 15 2021 Anton Midyukov <antohami@altlinux.org> 0.3.12-alt1
- save screenshots of alterator-setup into /root/.install-log/screenshots

* Wed Aug 18 2021 Anton Midyukov <antohami@altlinux.org> 0.3.11-alt1
- postinstall.d: do not copy setup.target or setup-vnc.target, if not
  available (Closes: 40770)

* Mon Aug 16 2021 Anton Midyukov <antohami@altlinux.org> 0.3.10-alt1
- Not enable setup.target as default.target (Closes: 39546)
- Add installer-feature-alterator-setup,
  installer-feature-alterator-setup-vnc 

* Mon Feb 22 2021 Anton Midyukov <antohami@altlinux.org> 0.3.9-alt1
- Fix conflict with package preinstall (ALT bug 39715)

* Wed Nov 11 2020 Anton Midyukov <antohami@altlinux.org> 0.3.8-alt1
- Added preinstall step, needed rootfs-installer-features

* Sat Nov 07 2020 Anton Midyukov <antohami@altlinux.org> 0.3.7-alt1
- Added requires on alteratord.service into systemd units (Closes: 39076)
- Added packages install step from installer-common-stage2
- Added net-eth step from installer-common-stage2

* Thu Oct 15 2020 Anton Midyukov <antohami@altlinux.org> 0.3.6-alt1
- setup-postinstall.d: Run '/sbin/integalert fix', if it exist before reboot
- setup-postinstall.d: Add 94-bootloder-update

* Tue Apr 03 2020 Nikita Ermakov <arei@altlinux.org> 0.3.5-alt1
- Add VNC support.

* Fri Feb 14 2020 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- postinstall: Run indexhtml-update.

* Fri Dec 27 2019 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt6
- setup.service: restart always (e.g. restart when X falls)

* Thu Dec 12 2019 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt5
- add conflicts with alterator-livecd, installer-common-stage2

* Fri Dec 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt4
- remove rootfs-installer-features on cleanup, if present


* Fri Dec 28 2018 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt3
- setup.service: relax dependency on plymouth-start.service

* Tue Sep 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt2
- closes: #35276

* Tue Sep 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt1.0.mips2
- Deleted now unnecessary reboot commands

* Tue Aug 21 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt1.0.mips1
- Added forcible reboot to work around the incompatibility problem with
- systemd 238

* Tue Apr 03 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.3-alt1
- made service file more correct.

* Mon Apr 02 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.2-alt1
- fixed service file to make it work with modern systemd.

* Mon Apr 28 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.1-alt1
- preun: do not use preun_service on systemd.

* Mon Apr 21 2014 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- sysvinit support

* Wed Mar 26 2014 Michael Shigorin <mike@altlinux.org> 0.2.1-alt2
- added a warning to description

* Thu Mar 06 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt1
- Remove more packages during cleanup.

* Tue Jul 16 2013 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- made self destruction optional (sysconfig knob)
- minor spec cleanup

* Fri Jul 12 2013 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- added license step

* Thu Jun 20 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release, thanks sem@

