Name:     settings-s
Version:  0.3
Release:  alt1

Summary:  settings for custom distro
License:  GPLv2
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/settings-s.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
Requires:  checker

%description
These are settings for custom distro.

%package -n integ
Summary: integrity checker settings
Group: System/Configuration/Other

%description -n integ
Integrity check setup only

%prep
%setup

%install
mkdir -p %buildroot%_datadir/install2/postinstall.d
mkdir -p %buildroot/sbin
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot/%_sysconfdir/firsttime.d
mkdir -p %buildroot/lib/systemd/system-preset

install -Dm 0755 65-integalert.sh %buildroot/%_sysconfdir/firsttime.d/
install -Dm 0644 65-integrity.preset %buildroot/lib/systemd/system-preset/
install -Dm 0755 65-settings.sh  %buildroot%_datadir/install2/postinstall.d/
install -Dm 0644 integalert.service %buildroot%_unitdir/
install -Dm 0700 integalert %buildroot/sbin/


%post -n integ
if [ $1 -ge 2 ]; then
    if systemctl -q is-enabled integalert.service; then
        systemctl daemon-reload
        systemctl -q preset integalert.service
    fi
fi

%files
%_datadir/install2/postinstall.d/65-settings.sh

%files -n integ
%_sysconfdir/firsttime.d/65-integalert.sh
%_unitdir/integalert.service
/lib/systemd/system-preset/65-integrity.preset
/sbin/integalert


%changelog
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
