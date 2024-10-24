Name: xfce4-power-manager
Version: 4.19.3
Release: alt2.g974546ec
Summary: Power management for the Xfce desktop environment
Summary (ru_RU.UTF8): Утилита расширенного управления питанием для Xfce

Group: Graphical desktop/XFce
License: GPLv2+
Url: https://docs.xfce.org/xfce/xfce4-power-manager/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/xfce/xfce4-power-manager.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-xfce4 >= 0.2.0-alt1 xfce4-dev-tools
BuildRequires: libxfce4util >= 4.19.2 libxfconf-devel libxfce4panel-gtk3-devel
BuildRequires: libxfce4ui-gtk3-devel >= 4.18.4
BuildRequires: libX11-devel libXext-devel libXrandr-devel
BuildRequires: libwayland-client-devel wayland-devel wayland-protocols wlr-protocols
BuildRequires: libnotify-devel >= 0.7.8
BuildRequires: libupower-devel
BuildRequires: libpolkit-devel
BuildRequires: gettext

Requires: polkit
Requires: upower

Conflicts: xfce4-screensaver < 0.1.10-alt1

%define _unpackaged_files_terminate_build 1

%description
This software is a power manager for the Xfce desktop, Xfce power
manager manages the power sources on the computer and the devices that
can be controlled to reduce their power consumption (such as LCD
brightness level, monitor sleep). In addition, xfce4-power-manager
provides a set of freedesktop-compliant DBus interfaces to inform other
applications about current power level so that they can adjust their
power consumption, and it provides the inhibit interface which allows
applications to prevent automatic sleep actions via the power manager.

%prep
%setup
%patch -p1
%xfce4_cleanup_version

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-x11 \
	--enable-wayland \
	--enable-polkit \
	--with-backend=linux \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/*
%_sbindir/xfpm-power-backlight-helper
%_sbindir/xfce4-pm-helper
%_libdir/xfce4/panel/plugins/*.so
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/polkit-1/actions/*.policy
%_mandir/man?/*
%_datadir/metainfo/*.xml

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri Jun 07 2024 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt2.g974546ec
- Upstream git snapshot (master branch).

* Mon Jun 03 2024 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt1
- Updated to 4.19.3.

* Thu May 30 2024 Mikhail Efremov <sem@altlinux.org> 4.19.2-alt1
- Updated to 4.19.2.

* Thu Nov 30 2023 Mikhail Efremov <sem@altlinux.org> 4.18.3-alt1
- Dropped %%xfce4_drop_gitvtag macro.
- Required libxfce4ui >= 4.18.4.
- Updated to 4.18.3.

* Tue May 30 2023 Mikhail Efremov <sem@altlinux.org> 4.18.2-alt1
- Updated to 4.18.2.

* Fri Feb 10 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- Updated to 4.18.1.

* Thu Dec 15 2022 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt1
- Updated BR.
- Updated decription.
- Updated to 4.18.0.

* Thu Dec 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.1-alt1
- Updated to 4.17.1.

* Tue Nov 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt1
- Updated to 4.17.0.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- Fixed xkb settings after sleep.
- Updated to 4.16.0.

* Sat Nov 07 2020 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1
- Dropped exo-csource from BR.
- Updated Vcs tag.
- Updated to 1.7.1.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt3
- Added conflict for broken xfce4-screensaver.
- Dropped workaround for xfce4-screensaver.

* Wed Mar 11 2020 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt2
- Workaround for xfce4-screensaver.
- Updated Url.

* Fri Mar 06 2020 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1
- Added Vcs tag.
- Updated to 1.7.0.

* Wed Dec 18 2019 Mikhail Efremov <sem@altlinux.org> 1.6.5-alt2
- Don't use rpm-build-licenses.
- Initialize output variables for g_object_get().

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 1.6.5-alt1
- Updated to 1.6.5.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 1.6.4-alt1
- Updated to 1.6.4.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 1.6.3-alt1
- Updated to 1.6.3.

* Fri May 17 2019 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Tue Aug 14 2018 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Don't requre xfce4-panel.
- Updated url.
- Updated to 1.6.1.

* Mon May 30 2016 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt2
- Enable debug (minimum level).
- Patch from upstream:
  + Look up the schema for light-locker's settings recursively

* Mon Mar 23 2015 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.

* Tue Feb 17 2015 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.
- Drop obsoleted patches.

* Mon Jun 02 2014 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Mar 28 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt7.git20140319
- logind support: treat "challenge" responses as true.
- Port to upower-0.99 D-Bus interface.
- Drop obsoleted patch.
- Fix Xfce name (XFCE -> Xfce).
- Upstream git snapshot (master branch).

* Thu Aug 29 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt6
- Use xfsm-shutdown-helper for suspend/hibernate.

* Fri May 31 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt5
- Fix xrandr brightness control for 64 bit builds.
- Enable xrandr brightness control for eDP displays
     (from xfce4-dev@ by Marcus Overhagen).

* Tue Apr 09 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt4
- Add systemd support for suspend/hibernate (closes: #28763).

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3
- Don't allow systemd to handle suspend/hibernate events.

* Thu Aug 30 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- Don't control disk's spin speed.
- Don't try to use internel documentation.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Tue Apr 10 2012 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1
- Fix crash when all outputs don't support the backlight property.
- Fix crash when xfpm tries to refresh the status icon of a removed
  battery.
- Let the brightness keys work even when numlock is on.
- Drop AC_PROG_LIBTOOL and AC_DISABLE_STATIC for LT_PREREQ and
  LT_INIT.
- Drop obsoleted patches.
- Updated to 1.0.11.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt6
- Rebuild with xfce4-panel-4.9.

* Wed Nov 30 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt5
- Run xfce4-fixkeyboard script after suspend/hibernate.

* Tue May 31 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt4
- Don't attach to the status icon if libnotify >= 0.7
    (patch from upstream).
- Add patch for NM-0.9 support.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt3
- Update Russian translation (by Andrey Cherepanov).
- Add more strings for translation.

* Tue Mar 29 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt2
- Added upower and udisks to requires.

* Tue Feb 22 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Updated to 1.0.10.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- tar.bz2 -> tar.
- Updated to 1.0.3.

* Tue Jan 19 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.8.4.2-alt1
- Version update.

* Fri Oct 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.4-alt1
- Version update.

* Thu Jul 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.1.1-alt1
- Version update.

* Wed May 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.1-alt1
- Update to 0.8.0RC2. Version updated to 0.8.1 for resolve conflicts with 0.8.0beta2

* Fri Apr 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.0beta2-alt1
First build for Sisyphus
