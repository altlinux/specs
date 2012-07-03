%define ver_major 3.4
%def_enable libnotify

Name: zenity
Version: %ver_major.0
Release: alt1

Summary: The GNOME port of dialog(1)
License: LGPLv2+
Group: Graphical desktop/GNOME

URL: http://ftp.gnome.org/pub/gnome/sources/%name/
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: scrollkeeper

# from configure.in
%define intltool_ver 0.40.0
%define gtk_ver 3.0.0

BuildPreReq: gnome-common docbook-dtds gnome-doc-utils
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: glib2-devel
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: perl-XML-Parser xsltproc
%{?_enable_libnotify:BuildPreReq: libnotify-devel >= 0.7.0}

%description
Zenity is a tool that allows you to display Gtk+ dialog boxes from
the command line and through shell scripts.  It is similar to gdialog,
but is intended to be saner.  It comes from the same family as dialog,
Xdialog, and cdialog, but it surpasses those projects by having
a cooler name.

%prep
%setup -q

%build
%configure --disable-scrollkeeper \
	%{subst_enable libnotify}

%make_build

%install
%makeinstall

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS NEWS README THANKS TODO
%_bindir/%name
%_bindir/gdialog
%_datadir/%name
%_man1dir/*

%changelog
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
