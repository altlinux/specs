Name:     ovirt-guest-agent
Version:  1.0.16
Release:  alt3

Summary:  The oVirt Guest Agent
License:  Apache-2.0
Group:    System/Libraries
URL:      http://wiki.ovirt.org/wiki/Category:Ovirt_guest_agent
#VCS:     https://github.com/oVirt/ovirt-guest-agent

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch1:   allowed-dbus-user.patch
Patch2:   alt-udev-dir.patch

BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
BuildRequires: libpam-devel

Requires: python-module-ethtool
Requires: python-module-rpm
Requires: qemu-guest-agent
Requires: udev >= 095

%description
This is the oVirt management agent running inside the guest. The agent
interfaces with the oVirt manager, supplying heart-beat info as well as
run-time data from within the guest itself. The agent also accepts
control commands to be run executed within the OS (like: shutdown and
restart).

%package pam-module
Summary: PAM module for the oVirt Guest Agent
Group:   Security/Networking
Requires: %name = %EVR
Requires: pam

%description pam-module
The oVirt PAM module provides the functionality necessary to use the
oVirt automatic log-in system.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --without-gdm \
           --without-kdm \
           --with-systemdsystemunitdir=%_unitdir \
           --enable-securedir=%_pam_modules_dir \
           --with-pam-prefix=%_sysconfdir
%make_build

%install
%makeinstall_std
rm -f %buildroot%_pam_modules_dir/*.{a,la}

%check
#%%make_build check

%pre
getent group ovirtagent > /dev/null || /usr/sbin/groupadd -r ovirtagent
getent passwd ovirtagent > /dev/null || \
%_sbindir/useradd -M -r -g ovirtagent -c 'ovirt-guest-agent' \
     -d / -s /sbin/nologin ovirtagent 2> /dev/null ||:

%preun
if [ "$1" -eq 0 ]
then
    %preun_service ovirt-guest-agent
    # Send an "uninstalled" notification to vdsm.
    if [ -w /dev/virtio-ports/com.redhat.rhevm.vdsm ]
    then
        # Non blocking uninstalled notification
        echo -e '{"__name__": "uninstalled"}\n' | dd \
            of=/dev/virtio-ports/com.redhat.rhevm.vdsm \
            oflag=nonblock status=noxfer conv=nocreat 1>& /dev/null || :
    fi
    if [ -w /dev/virtio-ports/ovirt-guest-agent.0 ]
    then
        # Non blocking uninstalled notification
        echo -e '{"__name__": "uninstalled"}\n' | dd \
            of=/dev/virtio-ports/ovirt-guest-agent.0 \
            oflag=nonblock status=noxfer conv=nocreat 1>& /dev/null || :
    fi
fi


%post
%post_service ovirt-guest-agent


%files
%doc AUTHORS COPYING NEWS README
%dir %attr (755,ovirtagent,ovirtagent) %_logdir/ovirt-guest-agent
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent

# Hook configuration directories
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent/hooks.d
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent/hooks.d/before_migration
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent/hooks.d/after_migration
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent/hooks.d/before_hibernation
%dir %attr (755,root,root) %_sysconfdir/ovirt-guest-agent/hooks.d/after_hibernation

# Hook installation directories
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/defaults
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/before_migration
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/after_migration
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/before_hibernation
%dir %attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/after_hibernation

%config(noreplace) %_sysconfdir/ovirt-guest-agent.conf

%config %_sysconfdir/pam.d/ovirt-logout
%config %_sysconfdir/pam.d/ovirt-locksession
%config %_sysconfdir/pam.d/ovirt-container-list
%config %_sysconfdir/pam.d/ovirt-shutdown
%config %_sysconfdir/pam.d/ovirt-hibernate
%config %_sysconfdir/pam.d/ovirt-flush-caches
%config %attr (644,root,root) %_udevrulesdir/55-ovirt-guest-agent.rules
%config %_sysconfdir/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf
%config %_sysconfdir/security/console.apps/ovirt-logout
%config %_sysconfdir/security/console.apps/ovirt-locksession
%config %_sysconfdir/security/console.apps/ovirt-container-list
%config %_sysconfdir/security/console.apps/ovirt-shutdown
%config %_sysconfdir/security/console.apps/ovirt-hibernate
%config %_sysconfdir/security/console.apps/ovirt-flush-caches

%attr (755,root,root) %_datadir/ovirt-guest-agent/ovirt-guest-agent.py*

%_datadir/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches
%attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches.consolehelper
%attr (755,root,root) %_datadir/ovirt-guest-agent/scripts/hooks/defaults/flush-caches

%_datadir/ovirt-guest-agent/OVirtAgentLogic.py*
%_datadir/ovirt-guest-agent/VirtIoChannel.py*
%_datadir/ovirt-guest-agent/CredServer.py*
%_datadir/ovirt-guest-agent/GuestAgentLinux2.py*
%_datadir/ovirt-guest-agent/hooks.py*
%_datadir/ovirt-guest-agent/timezone.py*
%_datadir/ovirt-guest-agent/ovirt-osinfo
%_datadir/ovirt-guest-agent/ovirt-logout
%_datadir/ovirt-guest-agent/ovirt-flush-caches

# consolehelper symlinks
%_datadir/ovirt-guest-agent/ovirt-locksession
%_datadir/ovirt-guest-agent/ovirt-shutdown
%_datadir/ovirt-guest-agent/ovirt-hibernate
%_datadir/ovirt-guest-agent/ovirt-container-list

# Symlinks for the default hooks
%config(noreplace) %_datadir/ovirt-guest-agent/scripts/hooks/before_hibernation/55_flush-caches
%config(noreplace) %_datadir/ovirt-guest-agent/scripts/hooks/before_migration/55_flush-caches
%config(noreplace) %_sysconfdir/ovirt-guest-agent/hooks.d/before_hibernation/55_flush-caches
%config(noreplace) %_sysconfdir/ovirt-guest-agent/hooks.d/before_migration/55_flush-caches

%attr (755,root,root) %_datadir/ovirt-guest-agent/LockActiveSession.py*
%attr (755,root,root) %_datadir/ovirt-guest-agent/LogoutActiveUser.py*
%attr (755,root,root) %_datadir/ovirt-guest-agent/hibernate

%attr (644,root,root) %_datadir/ovirt-guest-agent/default.conf
%attr (644,root,root) %_datadir/ovirt-guest-agent/default-logger.conf
%attr (755,root,root) %_datadir/ovirt-guest-agent/diskmapper
%attr (755,root,root) %_datadir/ovirt-guest-agent/container-list

%_unitdir/ovirt-guest-agent.service

%files pam-module
%_pam_modules_dir/pam_ovirt_cred.so

%changelog
* Mon Mar 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt3
- Moved udev rules to %%_udevrulesdir.

* Thu Jul 29 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt2
- Fix dbus service permissions.
- Remove deprecated requirements.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt1
- New version.

* Tue Jan 22 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.15-alt1
- New version.
- Requires python-module-rpm for correct package system detection.
- Add some additional requirements.

* Fri Dec 07 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.14-alt1
- Initial build for Sisyphus.
