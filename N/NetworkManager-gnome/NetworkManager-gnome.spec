%define nm_version 0.9.4.0
#define git_date .git20120315
%define git_date %nil
%define gtkver 3

Name: NetworkManager-gnome
Version: 0.9.4.1
Release: alt3%git_date
License: %gpl2plus
Group: Graphical desktop/GNOME
Summary: GNOME applications for use with NetworkManager
Url: http://www.gnome.org/projects/NetworkManager/
# Upstream: git://git.gnome.org/network-manager-applet
Source: nm-applet-%version.tar
Patch: nm-applet-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: libdbus-devel libdbus-glib libGConf-devel libgtk+%gtkver-devel intltool libtool libpolkit1-devel

BuildRequires: libGConf-devel libgnome-keyring-devel libwireless-devel
BuildRequires: libnotify-devel
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgnome-bluetooth-devel
BuildRequires: iso-codes-devel

Requires: NetworkManager >= %nm_version
Requires: libnm-gtk = %version-%release
Requires: gnome-keyring gcr
Requires: dbus-tools-gui
Requires: mobile-broadband-provider-info
Requires: polkit-gnome

%description
This package contains GNOME utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%package -n libnm-gtk
License: %gpl2plus
Group: Graphical desktop/GNOME
Summary: Private libraries for NetworkManager GUI support

%description -n libnm-gtk
This package contains private libraries to be used only by nm-applet and
the GNOME Control Center.

%package -n libnm-gtk-devel
License: %gpl2plus
Group: Development/GNOME and GTK+
Summary: Private header files for NetworkManager GUI support
Requires: libnm-gtk = %version-%release
Requires: NetworkManager-glib-devel >= %nm_version
Requires: libgtk+%gtkver-devel

%description -n libnm-gtk-devel
This package contains private header and pkg-config files to be used
only by nm-applet and the GNOME control center.

%prep
%setup -n nm-applet-%version
%patch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
    --with-gtkver=%gtkver \
    --enable-more-warnings=no

%make_build

%install
%makeinstall_std
%find_lang nm-applet

# For VPN plugins
mkdir -p %buildroot/%_datadir/gnome-vpn-properties

%check
make check

%post
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
echo "WARNING: nm-applet requires running messagebus service." >&2
fi

%files -f nm-applet.lang
%_bindir/*
%_datadir/nm-applet
%_iconsdir/hicolor/*/apps/*
%_sysconfdir/xdg/autostart/nm-applet.desktop
%_sysconfdir/gconf/schemas/nm-applet.schemas
%_datadir/applications/*.desktop
%dir %_datadir/gnome-vpn-properties
%_libdir/gnome-bluetooth/plugins/*.so

%exclude %_libdir/gnome-bluetooth/plugins/*.la

%files -n libnm-gtk
%_libdir/*.so.*
%_datadir/libnm-gtk/

%files -n libnm-gtk-devel
%_includedir/libnm-gtk/
%_libdir/*.so
%_pkgconfigdir/libnm-gtk.pc

%changelog
* Fri Apr 27 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt3
- Updated translations from upstream git.
- Add gcr to requires.

* Tue Apr 10 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt2
- Fix %%_datadir/libnm-gtk packaging.

* Mon Apr 02 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt1
- Updated from upstream git (e4e5146f1e).
- 0.9.4.1.

* Thu Mar 15 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.995-alt1.git20120315
- upstream git snapshot (master branch)

* Wed Feb 29 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.990-alt2.git20120228
- Temporary don't treat warrnings as errors.

* Tue Feb 28 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.990-alt1.git20120228
- upstream git snapshot (master branch)

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1
- 0.9.1.95 (0.9.2-rc1).

* Wed Sep 21 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt2.git20110920
- Fix typo in requires.

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt1.git20110920
- Add iso-codes to BR.
- upstream git snapshot (master branch)

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Don't package empty files.
- 0.9.0 release.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.9997-alt1.git20110607
- upstream git snapshot (master branch)

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Build with GTK+3.
- Rename src.rpm package.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- Build with libnotify-0.7.
- Own %%_datadir/gnome-vpn-properties.
- Enable tests.
- upstream git snapshot (master branch)

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.997-alt1.git20110323
- Changed libexecdir to %%_libexecdir/NetworkManager.
- Don't create auto wired connection.
- Drop Packager from spec.
- upstream git snapshot (master branch)

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Fix source tarball and general patch packaging.

* Sun Nov 07 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Oct 19 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt3.git20100914
- rebuild with libgnome-bluetooth.so.8

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100914
- upstream git snapshot (master branch)

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100722
- spec cleanup
- upstream git snapshot
    (almost corresponds with 0.8.1 release, but builded from master branch).

* Wed Jun 30 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100628
- drop nm-applet.desktop.

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100628
- upstream git snapshot (master branch)

* Thu May 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt2.git20100525
- build gnome-bluetooth plugin

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- upstream git snapshot
- Updated Russian translation (by Andrey Cherepanov).

* Thu Apr 29 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt1
- 0.7.998 (0.8-rc2)

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.997-alt1.git20091209
- upstream git snapshot

* Fri Nov 27 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- add polkit-gnome require (closes #22371).

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091124
- upstream git snapshot

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091026
- 0.7.996 (upstream git snapshot).

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1.997-alt1
- 0.7.1.997 (0.7.2-rc3)

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091005
- Russian translation by Andrey Cherepanov.
- new upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)

* Tue Jul 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20090728
- new upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)

* Thu Jul 16 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20090716
- upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)
- removed libmbca support.

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt1
- 0.7.0.100 (0.7.1-rc4)

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Thu Feb 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.98-alt1
- 0.7.0.98 (0.7.1-rc2)
- pack source as tar instead tar.gz

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)

* Thu Jan 22 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt9
- applied Ubuntu patch for libmbca support.

* Fri Dec 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt8
- enable 'Available for all users' checkbutton

* Thu Dec 11 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7
- fix 'no icon' bug again 

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt6
- Release NetworkManager 0.7

* Tue Dec 02 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt5.svn.r1043
- create auto wired connection if needed

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn.r1043
- BuildRequires fixed

* Mon Nov 24 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn.r1043
- new svn snapshot
- nm-applet-no-icon-fix.patch removed (obsolete)

* Fri Nov 21 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn.r986
- update_menus removed (obsolete)
- Requires fixed
- disable 'Available for all users' checkbutton (it does not work yet)

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r986
- Requires and BuildRequires updated

* Tue Oct 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r986
- new svn ref

* Fri Oct 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.4
- fix 'no icon' bug  

* Thu Sep 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.3
- autostarting in KDE 

* Mon Sep 08 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.svn.r838.M41.2
- don't call gtk-update-icon-cache in %%post{,un}

* Fri Sep 05 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.1
- port to M41 

* Wed Aug 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r838
- new svn snapshot
- spec updated

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080722
- new svn snapshot (797)
- .desktop file is added (applet can start from the menu now)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080527
- new svn snapshot (730)
- spec post/postun sections fixed

* Tue Apr 29 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080428
- new svn snapshot (705)
- spec cleanup

* Tue Apr 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080419
- initial build
