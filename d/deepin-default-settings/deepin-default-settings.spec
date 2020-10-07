%define repo default-settings

Name: deepin-default-settings
Version: 2020.09.11
Release: alt1
Summary: deepin-default-settings
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/default-settings
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.xz

BuildArch: noarch

Requires: icon-theme-deepin

%description
deepin-default-settings

%prep
%setup -n %repo-%version
%__subst 's|%_libexecdir/sysctl.d/|%_sysctldir/|' Makefile

%install
%makeinstall_std

mkdir -p %buildroot%_binfmtdir/
mv -f %buildroot/etc/binfmt.d/wine.conf %buildroot%_binfmtdir/wine.conf

%files
%doc CHANGELOG.md LICENSE
%_bindir/dde-first-run
%_sysctldir/deepin.conf
%_sysconfdir/X11/xinit/xinitrc.d/50-systemd-user.sh
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/*.conf
# conflicts with xorg-drv-libinput
%exclude %_sysconfdir/X11/xorg.conf.d/40-libinput.conf
%_binfmtdir/wine.conf
%config(noreplace) %_sysconfdir/fonts/conf.d/*.conf
%config(noreplace) %_sysconfdir/gimp/2.0/fonts.conf
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
# conflicts with altlinux-mime-defaults
%exclude %_desktopdir/mimeapps.list
%dir %_datadir/%name/
%_datadir/%name/fontconfig.json
%_datadir/fontconfig/conf.avail/*.conf
%_datadir/mime/packages/deepin-workaround.xml
%_datadir/mime/wine-ini.xml
%dir %_datadir/music/
%_datadir/music/bensound-sunny.mp3

%changelog
* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 2020.09.11-alt1
- Initial build for ALT Sisyphus.
