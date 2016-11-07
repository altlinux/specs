%define ver_major 3.22
%define xdg_name org.gnome.Terminal
%define _libexecdir %_prefix/libexec

%def_with nautilus

Name: gnome-terminal
Version: %ver_major.1
Release: alt1

Summary: GNOME Terminal
License: GPLv3+
Group: Terminals
Url: http://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.40
%define gtk_ver 3.12.0
%define vte_ver 0.46.1

Provides: xvt

PreReq: libvte3 >= %vte_ver
Requires: common-licenses
Requires: dconf gnome-icon-theme

BuildRequires: rpm-build-gnome gnome-common intltool yelp-tools desktop-file-utils appdata-tools
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libvte3-devel >= %vte_ver
BuildRequires: libvala-devel vala-tools
BuildRequires: gsettings-desktop-schemas-devel gnome-doc-utils-xslt libgio-devel libSM-devel
BuildRequires: libdconf-devel libuuid-devel
BuildRequires: libpcre2-devel
%{?_with_nautilus:BuildRequires: libnautilus-devel}
# for migration
BuildRequires: libGConf-devel
# %%_datadir/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
Buildrequires: gnome-shell-data

%description
GNOME terminal emulator application.

%package nautilus
Summary: Nautilus extension for the GNOME Terminal
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description nautilus
This package provides integration with the GNOME Terminal for the
Nautilus file manager.

%prep
%setup

# license
%__rm -f COPYING
%__ln_s -f %_licensedir/GPL-3 COPYING

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--disable-dependency-tracking \
	%{?_with_nautilus:--with-nautilus-extension}
%make_build

%install
%makeinstall_std

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%name	40
EOF

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-migration
%_libexecdir/%name-server
%_prefix/lib/systemd/user/%name-server.service
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/gnome-shell/search-providers/%name-search-provider.ini
%_datadir/appdata/%xdg_name.appdata.xml
%_altdir/%name
%doc --no-dereference COPYING
%doc AUTHORS NEWS

%if_with nautilus
%files nautilus
%nautilus_extdir/libterminal-nautilus.so
%_datadir/appdata/%xdg_name.Nautilus.metainfo.xml
%exclude %nautilus_extdir/libterminal-nautilus.la
%endif

%changelog
* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.91-alt1
- 3.17.91

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sat Apr 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.92-alt1
- 3.9.92

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- 3.9.90

* Sun Jul 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Fri Apr 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt1
- 3.8.0.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- new -nautilus subpackage

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1.1-alt1
- 3.4.1.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- provides xvt for use with xinitrc

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Mar 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Jan 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Wed Aug 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3.1-alt1
- 2.26.3.1

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3
- updated BuildRequires.
- some cleanups.

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Fri Feb 22 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.4-alt2
- Resolve bug #14609

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.4-alt1
- 2.18.4

* Thu Nov 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.3-alt1
- 2.18.3

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Wed Sep 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Wed May 23 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- Release 2.18.0

* Sat Oct 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.16.1-alt1
- Release 2.16.1

* Mon Sep 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.16.0-alt1
- Updated to 2.16.0

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.2-alt1
- Release 2.14.2

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.1-alt1
- Release 2.14.1

* Tue Mar 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.13.93-alt1
- Updated to 2.13.93
- Removed Debian-style menus and icons
- Buildreq

* Wed Oct 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Fri Sep 02 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.11.3-alt1
- Updated to 2.11.3
- Removed univga font requirement and forced gconf settings
  [bug #2292, bug #2274, bug #4128]

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Thu Feb 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2.

* Wed Dec 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.3-alt1
- 2.7.3

* Sun Apr 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5
- removed monospace.patch (fixed in upstream).
- requires xfonts-uni-vga (now default font is "VGA9 12")

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Mon May 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1. By ZVT :/.

* Sun Feb 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Sat Dec 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- Build with libzvt again.

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3
- Test build with vte 0.10.7 (:-//)

* Wed Nov 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2
  (mhz) - Mandrake: remove patches 1 (no longer needed), 3 (merged upstream)
	- Added icons (thanks Mandrake)
- Some default keybindings.

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt2
- fix default settings using %%gconf_add macro

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0
- patch3 in mainstream now.

* Sat Sep 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt2
- Applied mdk patches.
- Requires newest libzvt-2.0.1-alt2
- Buildreqs updated.

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Thu Jun 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build for Sisyphus.
