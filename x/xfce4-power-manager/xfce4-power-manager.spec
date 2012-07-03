Name: xfce4-power-manager
Version: 1.2.0
Release: alt1
Summary: Power management for the Xfce desktop environment
Summary (ru_RU.UTF8): Утилита расширенного управления питанием для Xfce

Group: Graphical desktop/XFce
License: %gpl2plus
Url: http://goodies.xfce.org/projects/applications/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfce4-power-manager
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfconf-devel libxfce4panel-devel libxfce4ui-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libnotify-devel >= 0.4.1
BuildRequires: libglade-devel > 2.0.0
BuildRequires: gettext intltool desktop-file-utils
# For exo-csource (needed in maintainer mode)
BuildPreReq: libexo-devel

Requires: xfce4-panel
Requires: polkit
Requires: upower udisks

%description
xfce4-power-manager is a tool for the Xfce desktop environment for
managing profiles of policies which affect power consumption, such as
the display brightness level, display sleep times, or CPU frequency
scaling.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-polkit \
	--enable-dpms \
	--enable-network-manager \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/*
%_sbindir/xfpm-power-backlight-helper
%_libdir/xfce4/panel-plugins/xfce4-*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/polkit-1/actions/*.policy
%_mandir/man?/*
%doc %_datadir/xfce4/doc/C/images/*.png
%doc %_datadir/xfce4/doc/C/%name.html

%changelog
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
