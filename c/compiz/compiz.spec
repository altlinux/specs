%define gnome_plugins compiz-annotate compiz-blur compiz-clone compiz-commands compiz-core compiz-cube compiz-dbus compiz-decoration compiz-fade compiz-fs compiz-gconf compiz-glib compiz-gnomecompat compiz-ini compiz-inotify compiz-minimize compiz-move compiz-obs compiz-place compiz-png compiz-regex compiz-resize compiz-rotate compiz-scale compiz-screenshot compiz-svg compiz-switcher compiz-video compiz-water compiz-wobbly compiz-zoom gwd
%define default_plugins animation,core,dbus,decoration,expo,glib,gnomecompat,imgjpeg,move,place,png,regex,resize,scale,session,svg,switcher,text,wall,wobbly,workarounds

Name: compiz
Version: 0.8.8
Release: alt4
Summary: OpenGL window and compositing manager
License: MIT/X11 GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

Obsoletes: compiz-manager
Provides: compiz-manager = %version-%release
Provides: COMPIZ_CORE_ABIVERSION = 20091102

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): libGConf-devel
BuildRequires: GConf gcc-c++ intltool gnome-control-center-devel libGLU-devel libXcomposite-devel
BuildRequires: libdbus-glib-devel libgnome-desktop-devel libmetacity-devel librsvg-devel
BuildRequires: libwnck-devel libxslt-devel xorg-xextproto-devel kde4libs-devel kde4base-workspace-devel
BuildRequires: kdebase-devel libdbus-qt-devel libtqt-devel

%description
Compiz is an OpenGL compositing manager that use GLX_EXT_texture_from_pixmap
for binding redirected top-level windows to texture objects. It has a flexible
plug-in system and it is designed to run well on most graphics hardware.

%package gnome
Summary: Gnome Window Manager
Group: Graphical desktop/GNOME
Requires: %name = %version-%release %name-gtk = %version-%release simple-ccsm

%description gnome
Compiz Window Manager for Gnome

%package gtk
Summary: Gtk Compiz window decorator
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: compizconfig-backend-gconf >= 0.8.4

%description gtk
Compiz window decorator for Gtk

%package kde4
Summary: KDE4 Compiz window decorator
Group: Graphical desktop/KDE
Requires: %name = %version-%release
Requires: compizconfig-backend-kconfig4 >= 0.8.4 simple-ccsm

%description kde4
Compiz window decorator for KDE4

%package devel
Summary: Development files for Compiz
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for Compiz

%package -n rpm-build-%name
Summary: RPM macros for sawfish-related packages
Group: Development/Other

%description -n rpm-build-%name
RPM macros for sawfish-related packages

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-default-plugins="%default_plugins" \
	--enable-librsvg \
	--enable-gtk \
	--disable-gnome \
	--enable-metacity \
	--disable-gconf \
	--disable-gnome-keybindings \
	--disable-kde \
	--enable-kde4 \
	--disable-static

%make_build

echo "%%compiz_core_abi_version $(sed -ne 's|^#define[[:space:]]*CORE_ABIVERSION[[:space:]]*\(.*\)|\1|p' include/%name-core.h)" > %name-core.rpmmacros

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%_libdir/%name/*.la

# rpm macros
install -pD -m644 %name-core.rpmmacros %buildroot%_rpmmacrosdir/%name-core

%find_lang %name

#post gnome
#gconf2_install %gnome_plugins

#preun gnome
#if [ $1 = 0 ]; then
#gconf2_uninstall %gnome_plugins
#fi

%files -f %name.lang
%doc AUTHORS COPYING COPYING.GPL COPYING.MIT README TODO NEWS
%_bindir/%name
%dir %_libdir/%name
%_libdir/*.so.*
#exclude %_libdir/%name/libgconf.so
%exclude %_libdir/%name/libgnomecompat.so
%exclude %_libdir/%name/libglib.so
%_libdir/%name/lib*.so
%_datadir/%name
%exclude %_datadir/%name/kc*
%exclude %_datadir/%name/gconf.xml
%exclude %_datadir/%name/gnomecompat.xml
%exclude %_datadir/%name/glib.xml

#files gnome
#_sysconfdir/gconf/schemas/*.schemas
#exclude %_sysconfdir/gconf/schemas/*kconfig.schemas
#_libdir/%name/libgconf.so
#_libdir/%name/libgnomecompat.so
#_libdir/%name/libglib.so
#_libdir/window-manager-settings/*.so
#_desktopdir/%name.desktop
#_datadir/%name/gconf.xml
#_datadir/%name/gnomecompat.xml
#_datadir/%name/glib.xml
#_datadir/gnome-control-center/keybindings/*.xml
#_datadir/gnome/wm-properties/%name-wm.desktop

%files gtk
%_bindir/gtk-window-decorator

%files kde4
%_bindir/kde4-window-decorator

%files devel
%_includedir/compiz
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n rpm-build-%name
%_rpmmacrosdir/%name-core

%changelog
* Sun May 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt4
- fix kde4-window-decorator linking
- fix underlinked plugins

* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt3
- restore compiz in Sisyphus
- disable gnome decorator

* Wed Apr 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt2
- updated to compiz-0.8 git.a24c99c

* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Tue Nov 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt3
- updated build dependencies

* Sat Oct 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt2
- compiz-0.8 branch 2010-10-10

* Sun Mar 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt4
- disabled KDE 3

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt3
- supported KDE 4.4

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- fixed some focus issues
- bumb ABI

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Thu Aug 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt15
- fixed lag by a call of options

* Tue Aug 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt14
- compiz-0.8 branch 2009-08-15 (aa65a16d3a0b3e40ab5bc717e5a804991b44793a)

* Fri Aug 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt13
- port of KDE4 window decorator to KDE 4.3

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt12
- merged compiz-0.8 branch

* Wed Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt11
- build kde4 window decorator (closes: #20713)

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt10
- rebuild with libpng12 1.2.37-alt2

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt9
- added replace option for kde/gtk window-decorator
- sets default plugins

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt8
- compiz-gnome: requires simple-ccsm

* Mon May 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt7
- compiz-kde: fixed startcompiz (closes: #20082)

* Fri Apr 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt6
- compiz-kde: autorun kde-window-decorator

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt5
- compiz-gnome: fixed double start if session preservation is included

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt4
- oops... renamed compiz.desktop to compiz-wm.desktop

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt3
- don't renamed %_desktopdir/compiz.desktop

* Sat Apr 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- enabled gnome

* Sun Mar 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- added altlinux logo for cube plugin

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt2
- rebuild for Mesa-7.1

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt5.20080116
- git snapshot 2008-01-16 (256728b9de329bcdbed6d665589082ad8f3bc7e2)

* Tue Nov 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt5
- fix for buffer overflow in strncat

* Tue Nov 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt4
- added %_sysconfdir/X11/wmsession.d/30Compiz to %name-kde

* Wed Nov 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt3
- CVE-2007-3920

* Sat Oct 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt2
- drop compiz-0.5.2-aiglx-defaults.patch: use option "--indirect-rendering"
- rewrite tfp-server-extension patch

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Sep 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt2
- disable GConf
- updated build dependencies

* Fri Aug 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Mon Apr 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Wed Jan 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Wed Dec 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.5-alt1.git20061227
- 0.3.5 2006-12-27 GIT snapshot

* Tue Nov 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt3.git20061101
- added compiz-0.3.3-aiglx-defaults.patch,
	compiz-0.3.3-tfp-server-extension.patch

* Tue Nov 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt2.git20061101
- rename subpackage %name-gnome to %name-gtk
- new subpackage %name-kde, %name-devel

* Mon Nov 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt1.git20061101
- 0.3.3 2006-11-01 GIT snapshot

* Sat Sep 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt1.git20060901
- merged RH patches
- added ALT Linux logo for cube plugin

* Fri Sep 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt0.git20060901
- 0.0.13 git snapshot 2006-09-01

* Thu May 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.10-alt0.cvs20060503
- 0.0.10

* Sun Apr 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.9-alt0.cvs20060420
- CVS snapshot 2006-04-20

* Wed Mar 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.7-alt1
- initial release

