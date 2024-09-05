%define _unpackaged_files_terminate_build 1
%define pname integalert

# Using ifarch instead of ExclusiveArch tag in order to make
# the other packages available on non-PVE arches.
%ifarch x86_64 aarch64
%def_with pve
%else
%def_without pve
%endif


Name:     %pname-source
Version:  0.4.14
Release:  alt1

Summary:  Osec-based integrity checking script and settings
License:  GPLv2
Group:    Monitoring
Url:      http://git.altlinux.org/people/manowar/packages/integalert.git

Packager: Paul Wolneykien <manowar@altlinux.org>
Source:   %name-%version.tar

%description
Osec-based integrity checking script and settings.

%package -n %pname
Summary:  Osec-based integrity checking script and settings
Group:    Monitoring
BuildArch: noarch

Requires: systemd
Requires: osec-cronjob >= 1.3.1-alt2

Obsoletes: integ < 0.4.2-alt2

%description -n %pname
Osec-based integrity checking script and settings.
Includes the 'integalert.service' that is configured to run
before 'sysinit.target' on every boot.

Activates the special 'integ-check-failed.target' on failure.

%package -n installer-feature-integalert-stage2
Summary: Run integrity check after install (installer files)
Group: System/Configuration/Other
BuildArch: noarch

%description -n installer-feature-integalert-stage2
Run integrity check after install (installer files).

%package -n installer-feature-integalert-stage3
Summary: Run integrity check after install (chroot files)
Group: System/Configuration/Other
Requires: integalert = %version-%release
BuildArch: noarch

%description -n installer-feature-integalert-stage3
Run integrity check after install (chroot files).

%package -n %pname-vm-check
Summary: Run VM integrity check before PVE and/or Libvirtd start and then every 5 mins
Group: Monitoring
BuildArch: noarch

%description -n %pname-vm-check
Includes a service that is configured to run 'integalert vm' and
'integalert container' before 'pvedaemon.service' and
'libvirtd.service', and every 5 mins after that (using a timer).

Activates the special 'vm-check-failed.target' on failure.

%package -n %pname-trigger-pve
Summary: Lock down PVE cluster VMs on integrity failure
Group: Monitoring
# For 'qm block' command:
Requires: pve-qemu-server >= 7.4.3-alt3

%description -n %pname-trigger-pve
Lock down PVE cluster VMs on integalert_vm.service failure.

%prep
%setup

%build
%make_build

%install
%makeinstall_std sbindir=%_sbindir sysconfdir=%_sysconfdir datadir=%_datadir unitdir=%_unitdir presetdir=%_presetdir WITH_PVE=%{with pve} logrotatedir=%_logrotatedir mandir=%_mandir man8dir=%_man8dir

# For ghost:
mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/integalert

%post -n %pname
# On package update (don't check the $1 value due to package
# rename):
if systemctl -q is-enabled integalert.service; then
    systemctl daemon-reload
    systemctl -q preset integalert.service
fi

# On first installation, try to migrate from existing
# configuration not maintained by RPM:
if [ $1 -eq 1 ]; then
    for d in integalert integalert_vm integalert_container; do
	for f in pipe.conf; do
	    if [ -e "%_sysconfdir/osec/$d/$f.rpmnew" ]; then
		if [ -e "%_sysconfdir/osec/$d/$f.rpmold" ]; then
		    mv -vf "%_sysconfdir/osec/$d/$f.rpmold" \
		       "$(mktemp %_sysconfdir/osec/$d/$f.rpmold.XXX)"
		fi

		mv -vf "%_sysconfdir/osec/$d/$f" \
		   "%_sysconfdir/osec/$d/$f.rpmold"
		mv -vf "%_sysconfdir/osec/$d/$f.rpmnew" \
		   "%_sysconfdir/osec/$d/$f"

		echo "Warning! %_sysconfdir/osec/$d/$f.rpmnew was automatically re-installed as %_sysconfdir/osec/$d/$f. Existing file has been saved as %_sysconfdir/osec/$d/$f.rpmold." >&2
	    fi
	done

	if [ -d %_sysconfdir/osec/${d}_fix ]; then
	    ls %_sysconfdir/osec/${d}_fix | while read f; do
		if [ -e "%_sysconfdir/osec/$d/$f.fix.rpmold" ]; then
		    mv -vf "%_sysconfdir/osec/$d/$f.fix.rpmold" \
		       "$(mktemp %_sysconfdir/osec/$d/$f.fix.rpmold.XXX)"
		fi

		mv -vf "%_sysconfdir/osec/${d}_fix/$f" \
		   "%_sysconfdir/osec/${d}/$f.fix.rpmold"
	    done

	    rmdir -v %_sysconfdir/osec/${d}_fix

	    echo "Warning! Files in %_sysconfdir/osec/${d}_fix were automatically saved as *.fix.rpmold files in %_sysconfdir/osec/$d." >&2
	fi
    done
fi

%files -n installer-feature-integalert-stage2
%_datadir/install2/postinstall.d/90-integrity-init.sh

%files -n installer-feature-integalert-stage3

%files -n %pname
%_unitdir/integalert.service
%_unitdir/integ-check-failed.target
%_presetdir/*
%_sbindir/integalert
%dir %_sysconfdir/osec/integalert*
%config(noreplace) %_sysconfdir/osec/integalert*/*.conf
%_sysconfdir/osec/integalert*/sender
%dir %_sysconfdir/osec/integalert*/trigger.d
%config(noreplace) %_logrotatedir/integalert*.conf
%ghost %_sysconfdir/sysconfig/integalert
%_man8dir/*.8.*

%files -n %pname-vm-check
%_unitdir/integalert_vm.service
%_unitdir/vm-check-failed.target
%_unitdir/integalert_vm.timer

%if_with pve
%files -n %pname-trigger-pve
%_sysconfdir/osec/integalert_vm/trigger.d/*-pve-*
%endif

%changelog
* Thu Sep 05 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.14-alt1
- Place integalert into /usr/sbin/.
- Install integalert with 0755 (world executable).
- Source /etc/sysconfig/integalert in pipe.conf and sender.conf files.

* Thu Sep 05 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.13-alt1
- Make /etc/sysconfig/integalert optional (do not install the
  default version).

* Thu Jul 04 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.12-alt1
- Support virtual directory mode (files.list).
- Install and package the default /etc/sysconfig/integalert.
- Fixed quotation in the default configuration files.
- FIX: Use separated databases for different profiles!

* Fri Jun 28 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.11-alt1
- Added integalert(8) manual page.
- Search for additional profiles by /etc/osec/integalert_*/dirs.conf.
- Add --help and --version.
- Added copyleft information.

* Mon Jun 03 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.10-alt1
- Add new sender.conf to define logging properties.
- Generate and install logrotate configuration (100 weekly).
- Add profile name to log tag.
- Write last log to /var/log/integalert/lastlog and continuous log
  to /var/log/integalert/integalert.log
- Install and package the special failing targets.

* Thu Mar 28 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.9-alt1
- Use 'qm block' command in PVE triggers.

* Tue Mar 12 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.8-alt1
- Check and lock only the nodes in /etc/pve/qemu-server.
- Don't exit a trigger if some nodes failed to stop.
- Be tolerant to spaces in osec report.
- Install the triggers in overwrite mode.
- Added lrm_status.tmp.* to exclude list.
- Fixed errors in VM triggers.

* Mon Feb 19 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.7-alt1
- Update and fix the package and service descriptions.
- Added /etc/pve/nodes/*/lrm_status files to exclude list.
- Fixed 30-pve-lock-nodes (VM_NODE_DIR, thx Varaksa Artem).
- Fixed PVE triggers: Process only *.conf files related to
  qemu-server.
- Fix: Don't try to use the non-existent 'qm lock' command.
- Fixed typo: OVFM (thx  Varaksa Artem).

* Wed Feb 14 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.6-alt1
- Make integalert_vm.service and timer depend on pvedaemon.service
  and libvirtd.service.

* Mon Feb 12 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.5-alt1
- Fix: Make sysinit.target weakly depend on integalert service
  by default.

* Thu Feb 08 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.4-alt1
- Update: On service failure isolate 'integ-check-failed.target'.

* Fri Jan 26 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt5
- Cosmetic improvement in the sender script.
- Fixed possible errors in the packaged default configuration
  files (there was a race condition).

* Wed Jan 24 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt4
- Added migration %%post script which makes backup copies of old
  integalert profiles.
- Generate and package the default configuration files for the
  default ('main'), 'vm' and 'container' profiles.
- Added 'configure' action which writes down the configuration
  files for the specified integalert profile.
- Run 'integalert container' from integalert_vm.service.

* Wed Jan 17 2024 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt3
- Fix: Use %%ifarch instead of ExclusiveArch tag in order to make
  the other packages available on non-PVE arches.

* Tue Dec 26 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt2
- Make *-trigger-pve package exclusive arch: x86_64 aarch64.

* Tue Dec 19 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt1
- Check that the selected osec profile exists before running osec.
- Add two more packages for VM checking and locking (PVE).
- Added 3 VM lock down scripts for PVE.
- Run triggers in /etc/osec/*/trigger.d after a failed
  check.
- Added VM check service and timer.
- Clarify the unit's description.
- Isolate the emergency.target on failure, set to required by
  sysinit.target.
- Don't directly write to TTY: rely on StandardError=tty.
- Use /etc/osec/*/sender script to write down the report and
  to send a summary message to the system log.
- Allow to explicitly specify the 'check' mode ('integalert check').
- Use the same /etc/osec/*/ config both for 'check' and 'fix' modes.
- Write logs to /var/log/integalert* and /var/log/integalert*_logs.

* Fri Nov 03 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt4
- Rename installer packages to installer-feature-integalert-*.

* Thu Nov 02 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt3
- Obsolete integ < 0.4.2-alt2.

* Wed Nov 01 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt2
- Remove 65-settings.sh and the corresponding package.
- Rename package to "integalert".
- Don't require 'checker' package.
- Add dirs.conf for "vm" and "container" profiles.

* Tue Apr 25 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- Provide the default dirs.conf for 'integalert' profile as a part of
  the 'integ' package.
- Output a warning and exit if dirs.conf is empty.
- Support for 'container' and 'vm' profiles.

* Fri Oct 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.4.1-alt1
- Set integalert service state from its preset after system
  installation.

* Thu Oct 01 2020 Paul Wolneykien <manowar@altlinux.org> 0.4-alt1
- Setup OSEC for full journal output after integrity database
  initialization after install.
- Update: Make integ inself require osec-controls.
- Moved postinstall.d/90-integrity-init.sh to the new stage2 package.
- Use "IMMUTABLE_DATABASE" configuration option for read-only osec runs.
  This requires osec-cronjob >= 1.3.1-alt2.
- Don't modify the main pipe.conf file after 'integ' package
  installation.
- Always create /var/log/lastosec_logs.
- Don't display a warning in "fix" mode.
- Run osec using 'integalert' and 'integalert_fix' sub-configs.
- Initialize OSEC after install, don't initialize it at first boot.
- Setup osec.cron for read-only use and full journal output after
  install.

* Mon Sep 07 2020 Denis Medvedev <nbr@altlinux.org> 0.3-alt3
- added missing requires, set control of osec to journal
(essential).

* Mon Sep 07 2020 Denis Medvedev <nbr@altlinux.org> 0.3-alt2
- revert direct execution of osec from integalert,
lastosec data is needed too.

* Sat Sep 05 2020 Alexey Shabalin <shaba@altlinux.org> 0.3-alt1
- update systemd unit
- not requires plymouth
- improve failure output
- direct execute osec for check integrity in integalert

* Mon Oct 28 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt5
- reenable service (to switch from required to wanted from sysinit)
only when it is an upgrade, not on initial install.

* Fri Oct 11 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt4
- force systemd reconfigure dependencies, fix archiving of osec messages

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt3
- force plymouth quit on integrity error

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt2
- integalert wanted, not required for sysinit by default

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt1
- fix integalert behavour, see nagwad package for modified osec.pipe. Also
disabled interruption of boot by default

* Mon Oct 07 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt4
- Fixed wrong separator in  Conflicts line. Also fixed permissions on a unit.

* Wed Sep 25 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt3
- latest update to sisyphus

* Thu Aug 22 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.18
- fixed dependencies for integalert service, avoiding loops.

* Wed Mar 20 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.17
- do not start service, it is needed only on boot.

* Mon Mar 18 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.16
- fixes on integ integalert service

* Wed Mar 28 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.15
- grub is modified adding option in some other place. Removed
addition of duplicated entry

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.14
- fixed delimiters

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.13
- removed perl parts of settings

* Thu Mar 22 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.12
- fixed place of postinstall.d

* Wed Mar 21 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.11
- moved to postinstall.d, added features from branding

* Thu Mar 01 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.10
- separated to two packets: general settings and integrity service
Removed rhosts from skel: it harms selinux settings.

* Thu Jan 18 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.9
- integrity check strictly before user login now

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.8
- added "Before" to  unit to make it start before DM

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.7
- changed wanted to required in unit

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.6
- added alerting on integrity checks on boot

* Wed Dec 13 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.5
- added fixed rhosts, added dependency to custom settings checker

* Mon Dec 11 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.3
- Updated settings

* Fri Dec 01 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.2
- fixed permissions

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.1
- backport to c8

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt1
Initial release
