%define ver_major 2.18
%def_disable static
%def_disable gtk_doc

%define _unpackaged_files_terminate_build 1

Name: libgnomeprintui
Version: %ver_major.6
Release: alt1

Summary: GUI support for libgnomeprint
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

%define libgnomeprint_ver 2.18.7
%define libgnomecanvas_ver 2.10.0

PreReq: libgnomeprint2 >= %libgnomeprint_ver
PreReq: libgnomecanvas >= %libgnomecanvas_ver

BuildPreReq: rpm-build-gnome gnome-common
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libgnomeprint-devel >= %libgnomeprint_ver
BuildPreReq: libgnomecanvas-devel >= %libgnomecanvas_ver
BuildPreReq: gnome-icon-theme
BuildPreReq: libglade-devel
BuildRequires: gcc-c++ gtk-doc

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary: Libraries and headers for libgnomeprintui
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%package devel-doc
Summary: Development documentation for libgnomeprintui
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
The libgnomeprintui package contains GTK+ widgets related to printing.

You can install the libgnomeprintui-devel-doc package if you would like
to develop applications that use the widgets in libgnomeprintui.

%package devel-static
Summary: Static libraries and objects
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
Static libraries and objects for the GNOME Printing User Interface.

%prep
%setup -q

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall

%find_lang %name-2.2

%files -f %name-2.2.lang
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/*.xml
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.18.6-alt1
- 2.18.6

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.18.5-alt1
- 2.18.5

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4
- removed obsolete %post{,un}_ldconfig
- new noarch devel-doc subpackage
- don't rebuild documentation

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.18.2-alt1
- new version (2.18.2)

* Tue Jun 26 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- updated dependencies and files list
- don't allow unpackaged files

* Mon Dec 25 2006 Alexey Rusakov <ktirf@altlinux.org> 2.12.1-alt3
- %%datadir/libgnomeprintui and %%datadir/libgnomeprintui/%%version are
  mentioned in the files list (bug 8549).

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.12.1-alt2.1
- Rebuilt for new pkg-config dependencies.

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Fixed dependencies of the -devel subpackage.

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- 2.12.1

* Mon Sep 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Thu Mar 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Wed Mar 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Sat Sep 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.90-alt1
- 2.7.90

* Thu Sep 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Wed Jun 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Mar 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Feb 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Tue Dec 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2
- do not package .la files.
- do not build devel-static subpackage by default.

* Fri Nov 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Jun 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.3-alt1
- 2.2.1.3

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.2-alt1
- 2.2.1.2

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Mon Dec 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Wed Dec 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Dec 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Thu Dec 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.0-alt2
- rebuild with new pango, gtk+

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.0-alt1
- 1.116.0

* Mon Jun 17 2002 Igor Androsov <blake@altlinux.ru> 1.115.0-alt1
- Initial build for AltLinux
- (aris):
    + SMP-compatible build.
    + ldconfig in post{un}.
    + prereq, buildprereq lists added.
    + other small fixes and cleanups.

* Thu May 16 2002 Igor Androsov <blace@mail.ru> 1.114.0-blk0.1
- New version from CVS

* Sat May 11 2002 Igor Androsov <blace@mail.ru> 1.113.0-blk0.1
- New version from CVS

* Mon Feb 18 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.110.0-1
- new version
- split package
- disabled binary stripping

