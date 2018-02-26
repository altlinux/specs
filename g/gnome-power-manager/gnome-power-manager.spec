%define ver_major 3.4
%def_enable xevents

Name: gnome-power-manager
Version: %ver_major.0
Release: alt1

Summary: GNOME Power management tools
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/projects/gnome-power-manager/

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: common-licenses gnome-session gnome-filesystem
Requires: upower >= 0.9.7

BuildPreReq: rpm-build-gnome >= 0.5
BuildPreReq: rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-doc-utils >= 0.3.2
BuildPreReq: glib2-devel >= 2.31.10
BuildPreReq: libgtk+3-devel >= 2.91.3
BuildPreReq: libupower-devel >= 0.9.1
# for docbook2man
BuildPreReq: docbook-utils
BuildPreReq: gnome-common

%description
GNOME Power Manager comes in three parts:

- gnome-settings-daemon plugin: the manager daemon itself
- gnome-control-center panel:   the control panel program, for configuration
- gnome-power-statistics:       the statistics graphing program


%prep
%setup -q

# Fix icons location
%__subst 's/pkgdatadir/datadir/' data/icons/*/{apps,status}/Makefile.am

%build
%autoreconf
%configure \
    --enable-tests \
    --disable-schemas-compile

%make_build

%check
#%make check

%install
%make_install DESTDIR=%buildroot install

# The license
ln -sf %_licensedir/GPL-2 COPYING

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/gnome-power-statistics
%_desktopdir/gnome-power-statistics.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%config %_datadir/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%_man1dir/*.1.gz
%doc --no-dereference COPYING
%doc README NEWS AUTHORS


%changelog
* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt3
- replaced obsolete {build,}reqs

* Wed Oct 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- drop hal dependence again

* Wed Oct 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.1-alt2
- drop hal dependences

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.2-alt1
- 2.29.2
- obsolete patches removed

* Mon Feb 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt2
- applied upstream patch for show the device name even when using UPower
  in gpm-statistics.

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- fixed icons location

* Mon Dec 07 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2
- don't show help url when sleep failed, actual page doesn't exist (ALT #22421)
- show Suspend and Hibernate in the menu by default

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.4-alt1
- 2.26.4

* Mon Jul 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3 release
- libdevkit-power-devel added to buildreqs

* Sat May 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt3
- build current git

* Tue May 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- build current git
- potentially fixed (ALT#19953)

* Wed Apr 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Apr 07 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- move to DeviceKit

* Fri Jan 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- don't run {update,clean}_scrollkeeper in post{,un}

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Oct 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- New version (2.22.1).

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- New version (2.22.0).
- disable Policykit support

* Sun Dec 16 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.2-alt1
- New version (2.20.2).

* Wed Nov 14 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- New version (2.20.1).
- The fix for XEvents has been applied upstream.

* Sat Nov 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt3
- Added a fix for the problem with XEvents, turned using them back on.

* Mon Nov 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt2
- Switched off compiling with Xevents, because of GNOME Bug #413360.

* Sun Oct 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt1
- New version (2.20.0).
- Updated dependencies, in particular fixing the build failure due to
  absent libgnome-keyring.
- Enabled unit tests.
- Updated files list.
- Added a subst to fix incorrect status and actions icons location.
- Invoke autoreconf before configure to make the mentioned subst work.

* Tue Aug 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version
- updated the license tag
- use more macros
- updated buildreqs
- added --enable-keyring configure switch to lock GNOME keyring on suspend
  and hibernate
- also added --enable-xevents and --enable-applets switches

* Wed Jan 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)
- added --with-dpms-ext to configure flags

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)
- updated dependencies
- minor cleanup

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- Initial Sisyphus package.

