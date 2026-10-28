Name: snapshot-cleaner-background
Version: 0.1.1
Release: alt1
Summary: Cleanup old on-demand Timeshift btrfs snapshots
License: MIT
Group: Archiving/Backup
Source0: %name-%version.tar
BuildArch: noarch

Requires: bash
Requires: coreutils
Requires: systemd

%description
btrfs-snapshot-clean runs Timeshift snapshot cleanup from a systemd timer. It only
selects on-demand snapshots with the O tag and uses configurable minimum
snapshot count and age limits. The timer is enabled on initial installation.

%prep
%setup -q

%build

%install
install -D -m 0755 bin/btrfs-snapshot-clean %buildroot%_sbindir/btrfs-snapshot-clean
install -D -m 0644 config/btrfs-snapshot-clean.conf %buildroot%_sysconfdir/sysconfig/btrfs-snapshot-clean.conf
install -D -m 0644 systemd/btrfs-snapshot-clean.service %buildroot%_unitdir/btrfs-snapshot-clean.service
install -D -m 0644 systemd/btrfs-snapshot-clean.timer %buildroot%_unitdir/btrfs-snapshot-clean.timer

%check
bash tests/test_cleanup.sh

%post
if [ "$1" -eq 1 ]; then
    systemctl enable --now btrfs-snapshot-clean.timer >/dev/null 2>&1 || :
fi

%preun
if [ "$1" -eq 0 ]; then
    systemctl disable --now btrfs-snapshot-clean.timer >/dev/null 2>&1 || :
fi

%postun
systemctl daemon-reload >/dev/null 2>&1 || :

%files
%_sbindir/btrfs-snapshot-clean
%config(noreplace) %_sysconfdir/sysconfig/btrfs-snapshot-clean.conf
%_unitdir/btrfs-snapshot-clean.service
%_unitdir/btrfs-snapshot-clean.timer

%changelog
* Tue Oct 27 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.1.1-alt1
- clean up snapshots created only by packagekit

* Mon Oct 19 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.1.0-alt1
- initial build
