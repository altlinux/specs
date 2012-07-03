%define ver_major 3.4

Name: gnome-terminal
Version: %ver_major.1.1
Release: alt1

Summary: GNOME Terminal
License: GPLv3+
Group: Terminals
Url: http://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define intltool_ver 0.40.0
%define GConf_ver 2.32.02
%define scrollkeeper_ver 0.3.14
%define glib_ver 2.28.0
%define gtk_ver 3.0.1
%define vte_ver 0.32.1
%define gnome_doc_utils_ver 0.3.5

Provides: xvt

PreReq: libvte3 >= %vte_ver
Requires(post,preun): GConf >= %GConf_ver
Requires: scrollkeeper >= %scrollkeeper_ver
Requires: common-licenses

BuildPreReq: gnome-common
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gnome-doc-utils >= %gnome_doc_utils_ver
BuildPreReq: GConf >= %GConf_ver libGConf-devel >= %GConf_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libvte3-devel >= %vte_ver

BuildRequires: gsettings-desktop-schemas-devel gnome-doc-utils-xslt libgio-devel libSM-devel

%description
GNOME terminal emulator application.

%prep
%setup -q

# license
%__rm -f COPYING
%__ln_s -f %_licensedir/GPL-3 COPYING

%build
%autoreconf
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-dependency-tracking

#	--disable-schemas-compile \

%make_build

%install
%make_install install DESTDIR=%buildroot

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%name	40
EOF

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name
#%config %_datadir/glib-2.0/schemas/*
%config %_sysconfdir/gconf/*/*
%_altdir/%name
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README

%changelog
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
