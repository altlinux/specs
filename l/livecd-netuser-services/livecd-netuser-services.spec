%define theme test

Name: livecd-netuser-services
Version: 1.0
Release: alt6

Summary: Changing standard lightdm greeter and desktop wallpapers
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD
Requires: livecd-cmdline-mount

BuildArch: noarch

Source: %name-%version.tar

%description
This package provides services for net users.
livecd-nfs-link to link mounted net filesystem to home dir.
livecd-net-backup to save selected home files into net filesystem.
livecd-nftable-rules to fetch, check and apply nftable rules provided
by /proc/cmdline. If rules filename contains "strict" - change wallpaper.

%prep
%setup

%install
install -pD -m644 livecd-nfs-link.service \
	%buildroot%_user_unitdir/livecd-nfs-link.service
install -pD -m644 livecd-net-backup.service \
	%buildroot%_user_unitdir/livecd-net-backup.service
install -pD -m644 livecd-nftable-rules.service \
	%buildroot%systemd_unitdir/livecd-nftable-rules.service
install -pD -m755 livecd-net-backup %buildroot%_bindir/livecd-net-backup
install -pD -m755 livecd-nftable-rules %buildroot%_bindir/livecd-nftable-rules
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar graphics/* %buildroot/%_datadir/design/%theme

%post
echo "*;*;%%netusers;Al0000-2400;vmusers,vboxusers" >> /etc/security/group.conf

%files
%_user_unitdir/livecd-nfs-link.service
%_user_unitdir/livecd-net-backup.service
%_bindir/livecd-net-backup
%_bindir/livecd-nftable-rules
%systemd_unitdir/livecd-nftable-rules.service
%_datadir/design
%doc README.practicum.md

%preun
%systemd_user_preun livecd-nfs-link
%systemd_user_preun livecd-net-backup
%systemd_preun livecd-nftable-rules

%changelog
* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt6
- Add netuser users to vmusers and vboxusers groups.

* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt5
- Add README.

* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt4
- Add special wallpaper as warning for strict nftable rules.

* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt3
- Add service to fetch, check and apply nftable rules provided by /proc/cmdline.

* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add service to link files from nfs to user's home.

* Thu Oct 22 2025 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
