%define ver_major 3.26
%def_enable libnotify
%def_enable webkitgtk

Name: zenity
Version: %ver_major.0
Release: alt1

Summary: The GNOME port of dialog(1)
License: LGPLv2+
Group: Graphical desktop/GNOME
URL: https://wiki.gnome.org/Projects/Zenity

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%define gtk_ver 3.0.0

BuildPreReq: gnome-common yelp-tools
BuildPreReq: glib2-devel
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: perl-XML-Parser xsltproc
%{?_enable_libnotify:BuildPreReq: libnotify-devel >= 0.7.0}
%{?_enable_webkitgtk:BuildRequires: libwebkit2gtk-devel}

%description
Zenity is a tool that allows you to display Gtk+ dialog boxes from
the command line and through shell scripts.  It is similar to gdialog,
but is intended to be saner.  It comes from the same family as dialog,
Xdialog, and cdialog, but it surpasses those projects by having
a cooler name.

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable libnotify} \
	%{subst_enable webkitgtk}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gdialog
%_datadir/%name
%_man1dir/*
%doc AUTHORS NEWS README THANKS TODO

%changelog
* Tue Nov 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Oct 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1.1-alt1
- 3.18.1.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Jun 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Thu May 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Sat Apr 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sat Mar 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.90-alt1
- 2.91.90

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated buildreqs

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed obsolete %%post{,un} scripts
- updated buildreqs

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version 2.22.1

* Sun Apr 06 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version 2.22.0

* Wed Jan 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)

* Thu Dec 21 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Fri Oct 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)
- updated dependencies
- use --disable-scrollkeeper instead of a workaround.

* Sun May 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Tue Jan 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version

* Sat Jan 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt2
- updated dependencies.
- minor spec improvements.

* Sat Jan 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version

* Mon Nov 14 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Mon Oct 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Wed Oct 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sun Sep 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sun May 08 2005 Alexey Tourbin <at@altlinux.ru> 2.10.0-alt1
- 2.8.1 -> 2.10.0

* Tue Oct 12 2004 Alexey Tourbin <at@altlinux.ru> 2.8.1-alt1
- 2.7.0 -> 2.8.1

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 2.7.0-alt1
- initial revision
