%define ver_major 2.11
%def_disable static

Name: libgtkhtml
Version: %ver_major.1
Release: alt1

Summary: GTK HTML widget 2
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

Provides: gtkhtml2 = %version-%release

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

%define gnome_vfs_ver 2.6.1.1
%define gail_ver 1.6.6
%define libxml2_ver 2.5.6
%define gtk_ver 2.4.9

BuildPreReq: rpm-build-gnome
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libgail-devel >= %gail_ver
BuildPreReq: gnome-vfs-devel >= %gnome_vfs_ver

BuildRequires: gcc-c++ libbonobo-devel libgnomecanvas-devel zlib-devel

%description
GTK HTML Widget for the GNOME 2 platform.
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed
to be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

%package -n %{name}2
Summary: GTk HTML widget 2
Group: System/Libraries

%description -n %{name}2
GTK HTML Widget for the GNOME 2 platform.
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed
to be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

%package -n %{name}2-devel
Summary: Header and development libraries for libgtkhtml
Group: Development/GNOME and GTK+
Requires: %{name}2 = %version-%release

%description -n %{name}2-devel
GTK HTML Widget for the GNOME 2 platform.
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed
to be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.
This package contains the files necessary to develop applications
with GtkHTML.

%package -n %{name}2-devel-static
Summary: Static libraries for libgtkhtml
Group: Development/GNOME and GTK+
Requires: %{name}2-devel = %version-%release

%description -n %{name}2-devel-static
GTK HTML Widget for the GNOME 2 platform.
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed
to be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains the files necessary to develop statically
linked applications with GtkHTML.

%prep
%setup -q

%build
%configure \
	%{subst_enable static}

# SMP-incompatible build
%make_build

%install
%makeinstall

%files -n libgtkhtml2
%_libdir/*.so.*
%doc AUTHORS ChangeLog README NEWS

%files -n libgtkhtml2-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc docs/IDEAS

%if_enabled static
%files -n libgtkhtml2-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.11.1-alt1
- 2.11.1

* Tue Jul 03 2007 Alexey Rusakov <ktirf@altlinux.org> 2.11.0-alt3
- add Provides: gtkhtml2 to let install some closed-source software.
- removed excess Requires from subpackages

* Fri Sep 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt2
- rebuild with newer libgail

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt1.1
- new version 2.11.0 (with rpmrb script)

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Sun Apr 03 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Jun 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Thu Dec 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Mon Oct 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri May 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Thu May 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Mar 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Mon Dec 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Dec 08 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Jun 19 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- Initial build for AltLinux
- Static libraries moved to devel-static
- Add buildreq
- (inger) fixed build

* Mon Jan 28 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- improved requirements

* Thu Jan 24 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.99.2-4
- added requirements from Chris

* Tue Jan 16 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- created new spec file

