%define repo default-settings

Name: deepin-default-settings
Version: 2022.10.19
Release: alt1
Summary: deepin-default-settings
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/default-settings
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.xz

BuildArch: noarch

BuildRequires: rpm-build-python3
#Requires: icon-theme-deepin

%description
deepin-default-settings

%prep
%setup -n %repo-%version
subst 's|%_libexecdir/sysctl.d/|%_sysctldir/|' Makefile
subst 's|/usr/bin/env python3|%__python3|' dde-first-run

%install
%makeinstall_std

mkdir -p %buildroot%_binfmtdir/
mv -f %buildroot/etc/binfmt.d/wine.conf %buildroot%_binfmtdir/wine.conf
cp -r skel %buildroot/%_sysconfdir/
# conflicts with xorg-drv-libinput
rm -f %buildroot%_sysconfdir/X11/xorg.conf.d/40-libinput.conf
# conflicts with altlinux-mime-defaults
rm -f %buildroot%_desktopdir/mimeapps.list

%files
%doc CHANGELOG.md LICENSE
%_bindir/dde-first-run
%_prefix/libexec/dde-first-run
%_sysctldir/deepin.conf
%_sysconfdir/X11/xinit/xinitrc.d/50-systemd-user.sh
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/*.conf
%_binfmtdir/wine.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/*.conf
%_sysconfdir/lscolor-256color
%config(noreplace) %_sysconfdir/modprobe.d/*.conf
%_sysconfdir/skel/.config/Trolltech.conf
%_sysconfdir/skel/.config/user-dirs.dirs
%_sysconfdir/skel/.config/SogouPY/sogouEnv.ini
%_sysconfdir/skel/.config/autostart/dde-first-run.desktop
%_sysconfdir/skel/.config/deepin/qt-theme.ini
%_sysconfdir/skel/.icons/default/index.theme
%_sysconfdir/skel/Music/bensound-sunny.mp3
%_sysconfdir/sudoers.d/01_always_set_sudoers_home
%_udevrulesdir/99-deepin.rules
%dir %_desktopdir/deepin/
%_desktopdir/deepin/dde-mimetype.list
%dir %_datadir/%name/
%_datadir/%name/fontconfig.json
%_datadir/fontconfig/conf.avail/*.conf
%_datadir/mime/packages/deepin-workaround.xml
%_datadir/mime/wine-ini.xml
%dir %_datadir/music/
%_datadir/music/bensound-sunny.mp3

%changelog
* Wed Mar 22 2023 Leontiy Volodin <lvol@altlinux.org> 2022.10.19-alt1
- New version (2022.10.19).

* Thu Sep 09 2021 Leontiy Volodin <lvol@altlinux.org> 2020.12.18-alt1
- New version (2020.12.18).
- Fixed default folders in $$HOME.

* Thu May 06 2021 Leontiy Volodin <lvol@altlinux.org> 2020.10.21-alt2
- Added rpm-build-python3 into BR.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 2020.10.21-alt1
- New version (2020.10.21) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 2020.09.11-alt1
- Initial build for ALT Sisyphus.
