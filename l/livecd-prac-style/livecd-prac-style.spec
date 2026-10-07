%define WALLPAPER_DESKTOP %_datadir/backgrounds/xfce/xfce-leaves.svg
%define DEFAULT %_datadir/backgrounds/xfce/default-background
%define WALLPAPER_GREETING %_datadir/backgrounds/xfce/xfce-shapes.svg

Name: livecd-prac-style
Version: 1.0
Release: alt6

Summary: Provides configurations for regular-practicum 
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/practicum/practicum-xfce

BuildArch: noarch

Source: %name-%version.tar

Requires: lightdm-gtk-greeter
Requires(pre): xfdesktop
Requires(pre): shared-desktop-icons

%description
This package provides configurations.
1. modified ~/.vimrc
2. ~/.local/bin in $PATH
3. changed default desktop and greeter wallpaper to XFCE
4. don't show unmounted filesystems on desktop
5. allow any user in the 'vmusers' group to connect to system libvirtd

%prep
%setup

%install
install -pD -m644 .vimrc %buildroot%_sysconfdir/skel/.vimrc
install -pD -m755 dotlocal.sh %buildroot%_sysconfdir/profile.d/dotlocal.sh
install -pD -m644 xfce4-desktop.xml \
	%buildroot%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
install -pD -m644 99-allow-libvirt.rules \
	%buildroot%_datadir/polkit-1/rules.d/99-allow-libvirt.rules

%post
if [ $1 -eq 1 ]; then
	rm -f %DEFAULT
	ln -sf %WALLPAPER_DESKTOP %DEFAULT
	cat >> %_sysconfdir/lightdm/lightdm-gtk-greeter.conf << EOF
background=%WALLPAPER_GREETING
EOF
fi

%files
%_sysconfdir/skel/.vimrc
%_sysconfdir/profile.d/dotlocal.sh
%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
%_datadir/polkit-1/rules.d/99-allow-libvirt.rules
%doc README.practicum.md

%changelog
* Mon Aug 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt6
- Allow any user in the 'vmusers' group to connect to system libvirtd.

* Mon Aug 03 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt5
- Add prohibition to show unmounted filesystems on desktop.

* Mon Aug 03 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt4
- Changed default desktop and greeter wallpaper to XFCE.

* Mon Aug 03 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt3
- Add README.

* Mon Aug 03 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add profile.d script for changing PATH.

* Sat Nov 22 2025 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
