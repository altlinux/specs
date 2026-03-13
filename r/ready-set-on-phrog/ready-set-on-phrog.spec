%define _libexecdir %_prefix/libexec

Name: ready-set-on-phrog
Version: 0.6.1
Release: alt1

Summary: Configs for start ready-set through phrog
License: GPL-3.0-or-later
Group: Other
URL: https://altlinux.space/alt-gnome/ReadySet
VCS: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar

Requires: phrog
Requires: ready-set >= 0.5.0
Requires: ready-set-plugin-language
Requires: ready-set-plugin-keyboard
Requires: ready-set-plugin-user-passwdqc

BuildArch: noarch

BuildRequires(pre): rpm-macros-systemd

%description
%summary.

%prep
%setup

%install
for i in 50_*; do
	install -pDm0644 $i %buildroot%_sysconfdir/dconf/db/local.d/$i;
done

install -pDm0644 50_org.gnome.desktop.screensaver_lock-enabled \
	%buildroot%_sysconfdir/dconf/db/local.d/50_org.gnome.desktop.screensaver_lock-enabled

install -pDm0644 config \
	%buildroot%_datadir/ready-set/config

install -pDm0644 %name.conf \
	%buildroot%_sysusersdir/%name.conf

install -pDm0755 %name-system-post \
	%buildroot%_datadir/ready-set/post-hooks/system/%name

%files
%_sysconfdir/dconf/db/local.d/50_*
%_datadir/ready-set/config
%_sysusersdir/%name.conf
%_datadir/ready-set/post-hooks/system/%name

%changelog
* Fri Mar 13 2026 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt1
- Use dconf override instead ready-set hooks.

* Wed Mar 11 2026 Vladimir Romanov <rirusha@altlinux.org> 0.6-alt1
- Improved hooks:
  - Added animation disabling;
  - Added ignoring hardware keyboard.

* Tue Feb 24 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5-alt1
- Updated for new ready-set 0.5.0.

* Tue Jan 20 2026 Vladimir Romanov <rirusha@altlinux.org> 0.4-alt1
- Updated for new ready-set 0.3.1.
- Removed pwquality config file, because we use passwdqc.
- Added permission for running ready-set-ruler.

* Fri Jan 16 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3-alt1
- Updated for new ready-set 0.3.0.

* Tue Dec 16 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- Added polkit rule with self-remove in run script.

* Thu Dec 11 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
