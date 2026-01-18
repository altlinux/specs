%define _libexecdir %_prefix/libexec

Name: ready-set-on-phrog
Version: 0.3
Release: alt1

Summary: Configs for start ready-set through phrog
License: GPL-3.0-or-later
Group: Other
URL: https://altlinux.space/alt-gnome/ReadySet
VCS: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar

Requires: phrog
Requires: ready-set-plugin-language
Requires: ready-set-plugin-keyboard
Requires: ready-set-plugin-user-passwdqc

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -pDm0755 ready-set-first-run \
	%buildroot%_libexecdir/ready-set-first-run
install -pDm0644 50_mobi.phosh.phrog_first-run \
	%buildroot%_sysconfdir/dconf/db/local.d/50_mobi.phosh.phrog_first-run
install -pDm0644 50_org.gnome.desktop.screensaver_lock-enabled \
	%buildroot%_sysconfdir/dconf/db/local.d/50_org.gnome.desktop.screensaver_lock-enabled
install -pDm0644 50_%name.conf \
	%buildroot%_sysconfdir/security/pwquality.conf.d/50_%name.conf
install -pDm0644 50_%name.rules \
	%buildroot%_datadir/polkit-1/rules.d/50_%name.rules

%files
%_libexecdir/ready-set-first-run
%_sysconfdir/dconf/db/local.d/50_mobi.phosh.phrog_first-run
%_sysconfdir/dconf/db/local.d/50_org.gnome.desktop.screensaver_lock-enabled
%_sysconfdir/security/pwquality.conf.d/50_%name.conf
%_datadir/polkit-1/rules.d/50_%name.rules

%changelog
* Fri Jan 16 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3-alt1
- Updated for new ready-set 0.3.0.

* Tue Dec 16 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- Added polkit rule with self-remove in run script.

* Thu Dec 11 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
