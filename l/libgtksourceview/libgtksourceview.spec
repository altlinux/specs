%define _name gtksourceview
%define ver_major 2.10
%def_disable static
%def_disable gtk_doc
%def_disable introspection

Name: lib%{_name}
Version: %ver_major.5
Release: alt2.1

Summary: GtkSourceView text widget library
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.bz2
Source1: %name-%ver_major.map
Patch: %name-2.9.4-alt-symver.patch

Provides: %{name}2 = %version-%release
Obsoletes: %{name}2 < %version-%release

# From configure.ac
%define intltool_ver 0.35
%define gtk_ver 2.12.0
%define libxml2_ver 2.5.0

BuildPreReq: rpm-build-gnome

# From configure.ac
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gnome-common
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libGConf-devel
BuildPreReq: gtk-doc >= 1.0

BuildRequires: gcc-c++ perl-XML-Parser zlib-devel libgio-devel cvs
BuildRequires: gobject-introspection-devel
%{?_enable_introspection:BuildRequires: libgtk+2-gir-devel}

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: %{name}2-devel = %version-%release
Obsoletes: %{name}2-devel < %version-%release


%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package provides development documentation for %_name.

%package gir
Summary: GObject introspection data for the GtkSourceView library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GtkSourceView library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GtkSourceView library


%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q -n %_name-%version
install -p -m644 %SOURCE1 gtksourceview/libgtksourceview.map
%patch

#rm -f gtksourceview/GtkSource-2.0.gir

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

#%check
#%%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang %_name-2.0

%files -f %_name-2.0.lang
%_libdir/*.so.*
%_datadir/%_name-2.0
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc HACKING MAINTAINERS

%files devel-doc
%_gtk_docdir/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.10.5-alt2.1
- Rebuild with Python-2.7

* Sat Nov 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt2
- rebuild for update dependencies

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt1
- 2.10.5

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.4-alt1
- 2.10.4
- introspection support temporarily disabled

* Fri May 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt2
- new gir{,-devel} subpackages
- updated version script

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2
- prepared for introspection

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Wed Mar 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.9.9-alt1
- 2.9.9

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- 2.9.4
- updated symbol version patch and script

* Sat Dec 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Fri Dec 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.9.3-alt1
- 2.9.3
- updated symbol version patch and script

* Tue Sep 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.7.5-alt1
- 2.7.5

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.7.4-alt1
- 2.7.4

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3
- updated version script

* Sat May 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Jan 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- 2.5.3

* Sun Jan 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2
- removed obsolete %%post{,un}_ldconfig

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt2
- add versioning

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0
- rename package from %{name}2 to %name
- build devel-doc as noarch

* Tue Jun 24 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- new version (2.2.2)
- disable build tests
- add --enable-deprecations for configure(remove gnome-vfs-devel from BuildRequires)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- new version (2.2.1)

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- new version (2.2.0)

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 2.0.2-alt3.1
- Rebuilt with python-2.5.

* Wed Jan 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt3
- add Provides:libgtksourceview-devel and Obsoletes:libgtksourceview-devel (#13903)

* Thu Jan 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt2
- rename package to gtksourceview2

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- new version (2.0.2)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- new version (2.0.1)
- add Packager

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

