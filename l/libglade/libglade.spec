%define _oldname libglade2
%define ver_major 2.6
%def_disable static
%def_disable python
%def_disable gtk_doc

Name: libglade
Version: %ver_major.4
Release: alt5

Summary: libglade library
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Provides: %_oldname = %version
Obsoletes: %_oldname < %version

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

%define gtk_ver 2.5.0
%define glib_ver 2.10.0
%define atk_ver 1.9.0
%define libxml2_ver 2.6.17
%define pkgconfig_ver 0.15-alt3.2
%define python_ver 2.0

%define xmlcatalog %_sysconfdir/xml/catalog
PreReq: %xmlcatalog

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libatk-devel >= %atk_ver
BuildPreReq: python >= %python_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: pkgconfig >= %pkgconfig_ver

%if_enabled python
BuildPreReq: PyXML python-modules-xml
%endif

%if_enabled gtk_doc
BuildPreReq: gtk-doc 
%endif

BuildRequires: docbook-dtds docbook-style-xsl python-devel xml-utils xsltproc zlib-devel

%description
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

The interfaces can also be edited with GLADE.

%package devel
Summary: Libraries, includes, etc to develop libglade applications
Group: Development/GNOME and GTK+
Provides: %_oldname-devel = %version
Obsoletes: %_oldname-devel < %version
Requires: %name = %version-%release

%description devel
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

Libraries, include files, etc you can use to develop libglade applications.

%if_enabled python
%package devel-converter
Summary: Python script to convert old glade files.
Group: Development/GNOME and GTK+
Provides: %_oldname-devel-python = %version %name-devel-python = %version
Obsoletes: %_oldname-devel-python < %version %name-devel-python < %version
Requires: %name-devel = %version-%release

%description devel-converter
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

This package provides libglade-convert script to convert old glade files.
%endif

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
BuildArch: noarch
Provides: %_oldname-devel-doc = %version
Obsoletes: %_oldname-devel-doc < %version
Conflicts: %name < %version

%description devel-doc
Glade library allows to load user interfaces in programs, which are
stored externally. This allows alteration of the interface without
recompilation of the program.

This package contains development documentation for %name

%if_enabled static
%package devel-static
Summary: Libraries, includes, etc to develop libglade applications
Group: Development/GNOME and GTK+
Requires: libgtk+2-devel libxml2-devel %name-devel = %version-%release

%description devel-static
Libraries, include files, etc you can use to develop libglade applications.
%endif

%prep
%setup

# fix LTVERSION (2.4.1 was 0:5:0)
%__subst 's,0:4:0,0:6:0,' glade/Makefile*

# disable dependency on libxml2-devel
%__subst '/^Requires:/s/ libxml-2.0//' libglade-*.pc.in

%build
%if_disabled python
export ac_cv_path_PYTHON=/bin/false
%endif
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall

# The directory for libglade extenstions.
%__mkdir_p %buildroot%_libdir/%name/2.0

# Development documentation.
%__mkdir_p %buildroot%_docdir/%name-devel-%version
%__cp test-libglade.c examples/*.glade %buildroot%_docdir/%name-devel-%version/

%post
%_bindir/xmlcatalog --noout --add "system" \
    "http://glade.gnome.org/glade-2.0.dtd" \
    %_datadir/xml/%name/glade-2.0.dtd %xmlcatalog ||:

%postun
%_bindir/xmlcatalog --noout --del \
    "%_datadir/xml/%name/glade-2.0.dtd" %xmlcatalog ||:

%files
%_libdir/%name-2.0.so.*
%dir %_libdir/%name
%dir %_libdir/%name/2.0
%dir %_datadir/xml/%name
%_datadir/xml/%name/glade-2.0.dtd
%doc AUTHORS NEWS README

%files devel
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*

%if_enabled python
%files devel-converter
%_bindir/libglade-convert
%endif

%files devel-doc
%_docdir/%name-devel-%version
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Fri Mar 18 2011 Alexey Tourbin <at@altlinux.ru> 2.6.4-alt5
- libglade-2.0.pc: disabled dependency on libxml2-devel

* Wed Mar 16 2011 Alexey Tourbin <at@altlinux.ru> 2.6.4-alt4
- libglade-devel: removed dependencies on libatk-devel libxml2-devel

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt3
- rebuilt for debuginfo

* Mon Oct 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt2
- rebuild

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- 2.6.4

* Mon Aug 18 2008 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- new version
- updated buildreqs
- don't rebuild documentation

* Sat Sep 22 2007 Igor Zubkov <icesik@altlinux.org> 2.6.2-alt1
- 2.6.1 -> 2.6.2

* Wed Jul 04 2007 Igor Zubkov <icesik@altlinux.org> 2.6.1-alt1
- 2.6.0 -> 2.6.1

* Mon Sep 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.0-alt4
- replaced python-dev with python-devel, as told by ALT Python policy.
- devel-python subpackage is now called devel-converter; doesn't build by default, anyway.

* Wed Aug 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.0-alt3
- fixed bug #6454

* Mon Jul 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.0-alt2
- removed '2' from the names of the packages
- removed excess dependencies
- spec cleanup

* Sun Jul 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Fri Mar 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1.1
- put rarely usable libglade-convert to separate devel-python
  subpackage and while python environment is broken do not build it.

* Fri Feb 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0.
- documentation moved to devel-doc subpackage.

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Jun 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1.1
- only devel subpackage requires python for libglade-convert

* Mon May 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt4
- do not package .la files.
- devel-static subpackage is optional.

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt3
- fixed buildreqs.
- added missing prereqs on xml-common (close #1524).

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt2
- rebuild with new pango, gtk+
- post/postun scripts fixed.

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1
- some fixes.

* Fri Jun 07 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- New version

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 1.99.12-alt1.1
- Moved *.la from static to devel package
- Minor fixes spec.

* Thu May 23 2002 Igor Androsov <blake@altlinux.ru> 1.99.12-alt1
- New source from CVS
- Initial build for AltLinux

* Mon May 13 2002 Igor Andrsov <blace@mail.ru> 1.99.12-blk0.1
- Syncing with CVS
- Minor chages spec

* Wed May 08 2002 Igor Andrsov <blace@mail.ru> 1.99.11-blk0.1
- New soruces from CVS
- Chages for AltLinux
- Moved static libs to devel-static

* Sun Nov  1 1998 James Henstridge <james@daa.com.au>

- Updated the dependencies of the devel package, so users must have gtk+-devel.

* Sun Oct 25 1998 James Henstridge <james@daa.com.au>

- Initial release 0.0.1
