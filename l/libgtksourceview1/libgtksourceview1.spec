%define _name gtksourceview
%define ver_major 1.8
%def_disable static

Name: lib%{_name}1
Version: %ver_major.5
Release: alt8

Summary: GtkSourceView text widget library
License: %lgpl2plus
Group: System/Libraries
Url: http://www.gnome.org

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.bz2
Patch: %_name-1.8.5-fix-build.patch
Patch1: %_name-1.8.5-alt-include.patch

Provides: lib%_name%ver_major = %version-%release
Obsoletes: lib%_name%ver_major < %version-%release
Obsoletes: lib%_name < %version-%release

# From configure.in
%define intltool_ver 0.35
%define gtk_ver 2.8.0
%define gnome_vfs_ver 2.2.0
%define libxml2_ver 2.5.0
%define gnome_print_ver 2.8.0

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gnome-common
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: gnome-vfs-devel >= %gnome_vfs_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libgnomeprint2-devel >= %gnome_print_ver
BuildPreReq: gtk-doc >= 1.0


BuildRequires: perl-XML-Parser zlib-devel

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package provides development documentation for %_name.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version
%patch
%patch1 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-build-tests
	
%make_build

%install
%makeinstall

%find_lang %_name-1.0

%files -f %_name-1.0.lang
%_libdir/*.so.*
%_datadir/%_name-1.0
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc HACKING MAINTAINERS TODO

%files devel-doc
%_gtk_docdir/*

%changelog
* Sat May 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt8
- fixed includes for newest glib

* Wed Jul 06 2011 Dmitry V. Levin <ldv@altlinux.org> 1.8.5-alt7
- Rebuilt for soname set-versions and debuginfo.

* Sat Aug 22 2009 Alexey Rusakov <ktirf@altlinux.org> 1.8.5-alt6
- Removed obsolete post/postun macros

* Thu Nov 06 2008 Alexey Rusakov <ktirf@altlinux.org> 1.8.5-alt5
- specify license more exactly
- fix building with the new toolchain

* Wed Jan 09 2008 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt4
- add Obsoletes: libgtksourceview < 1.8.5-alt4 (#13902)

* Thu Jan 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt3
- building 1.8.5 as a normal version, 2.0 rename as gtksourceview2
- rename package to gtksourceview1

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt2 
- building 1.8.5 as a legacy version, 2.0.1 is about to come.

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 1.8.5-alt1
- new version (1.8.5)
- removed unneeded dependencies of -devel subpackage

* Thu Jan 18 2007 Alexey Rusakov <ktirf@altlinux.org> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Mon Oct 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Tue Sep 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Mon Aug 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.7.2-alt1
- new version (1.7.2)
- renamed source package from gtksourceview to libgtksourceview to streamline binary packages naming.

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.1-alt1
- new version 1.6.1 (with rpmrb script)

* Sun Mar 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Sun Mar 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.7-alt1
- new version 1.6. (with rpmrb script)

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.7-alt1
- new version (1.5.7)

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.5-alt1
- new version

* Mon Jan 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.4-alt1
- new version
- fixed bug #8787.

* Thu Jan 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.3-alt1
- new version

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.5.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.1-alt1
- 1.4.1
- devel-doc subpackage has been introduced.

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.0-alt1
- 1.4.0
- Removed more excess buildreqs.

* Mon Sep 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.3.92-alt1
- 1.3.92
- Removed excess buildreqs.

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.93-alt1
- 1.1.93.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Sep 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Mar 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1.1
- ruby.lang by Vital.

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Dec 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt2
- do not package .la files.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt2
- fixed buildreqs.

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Jul 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Fri Jun 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Sat May 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus.

