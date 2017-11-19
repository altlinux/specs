%define ver_major 0.10
%define api_ver 0.10
%define _name goffice

%def_with lasem
%def_enable introspection

Name: libgnomeoffice%api_ver
Version: %ver_major.36
Release: alt1

Summary: Library for writing gnome office programs
Group: Graphical desktop/GNOME
License: GPL
Url: http://www.gnumeric.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.28.0
%define gsf_ver 1.14.40
%define gtk_ver 3.0.0
%define cairo_ver 1.10.0
%define lasem_ver 0.4.1

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgsf-devel >= %gsf_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildRequires: libgs-devel
BuildRequires: libXext-devel libXrender-devel libxml2-devel libxslt-devel librsvg-devel
BuildRequires: intltool gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgsf-gir-devel libgtk+3-gir-devel}
%{?_with_lasem:BuildRequires: liblasem-devel >= %lasem_ver}

%description
GOffice is a library that eases the task of writing gnome office
programs.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libgnomeoffice%api_ver-devel
Provides: libgnomeoffice%api_ver-devel = %version-%release

%description devel
This package contains the header files and libraries needed to write and
compile programs that use %name.

%package devel-doc
Summary: Development documentation for Goffice
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Goffice library.

%package gir
Summary: GObject introspection data for the Goffice library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Goffice library.

%package gir-devel
Summary: GObject introspection devel data for the Goffice library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Goffice library.


%define _libexecdir %_libdir/%name

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--with-config-backend=gsettings \
	%{subst_with lasem} \
	%{?_enable_introspection:--enable-introspection=yes}

%make_build

%install
%makeinstall_std

%find_lang --output=%_name.lang %_name-%version

%check
%make check

%files -f %_name.lang
%_libdir/*.so.*
%dir %_libdir/goffice
%dir %_libdir/goffice/%version
%dir %_libdir/goffice/%version/plugins
%_libdir/goffice/%version/plugins/plot_barcol/
%_libdir/goffice/%version/plugins/plot_distrib/
%_libdir/goffice/%version/plugins/plot_pie/
%_libdir/goffice/%version/plugins/plot_radar/
%_libdir/goffice/%version/plugins/plot_surface/
%_libdir/goffice/%version/plugins/plot_xy/
%_libdir/goffice/%version/plugins/reg_linear/
%_libdir/goffice/%version/plugins/reg_logfit/
%_libdir/goffice/%version/plugins/smoothing/
%_libdir/goffice/%version/plugins/lasem/
%dir %_datadir/goffice
%dir %_datadir/goffice/%version
%_datadir/goffice/%version/mmlitex/
%doc AUTHORS NEWS README

%exclude %_libdir/%_name/%version/plugins/*/*.la

%files devel
%_includedir/libgoffice-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/*

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/

%if_enabled introspection
%files gir
%_typelibdir/GOffice-%api_ver.typelib

%files gir-devel
%_girdir/GOffice-%api_ver.gir
%endif


%changelog
* Sun Nov 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.36-alt1
- 0.10.36

* Fri Jul 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.35-alt1
- 0.10.35

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.34-alt1
- 0.10.34

* Tue Jan 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.33-alt1
- 0.10.33

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.32-alt1
- 0.10.32

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.31-alt1
- 0.10.31

* Sat Jun 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.30-alt1
- 0.10.30

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.29-alt1
- 0.10.29

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.28-alt1
- 0.10.28

* Sat Feb 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.27-alt1
- 0.10.27

* Tue Dec 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.26-alt1
- 0.10.26

* Sat Dec 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.25-alt1
- 0.10.25

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.24-alt1
- 0.10.24

* Wed Jul 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.23-alt1
- 0.10.23

* Fri Apr 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.22-alt1
- 0.10.22

* Thu Mar 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.21-alt1
- 0.10.21

* Thu Feb 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.20-alt1
- 0.10.20

* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.19-alt1
- 0.10.19

* Fri Sep 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.18-alt1
- 0.10.18

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.17-alt1
- 0.10.17

* Mon May 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.16-alt1
- 0.10.16

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.14-alt1
- 0.10.14

* Wed Mar 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.13-alt1
- 0.10.13

* Sun Feb 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.11-alt1
- 0.10.11

* Wed Feb 12 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.10-alt1
- 0.10.10

* Fri Nov 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.9-alt1
- 0.10.9

* Tue Oct 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt1
- 0.10.8

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.7-alt1
- 0.10.7

* Wed Aug 28 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- 0.10.6

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Mon Jul 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Sun Jun 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sat Nov 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.90-alt1
- 0.9.90 (0.10 API)

* Tue Jun 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.17-alt2
- used GSettings as a configuration backend
- updated buildreqs
- obsoletes/provides libgnomeoffice0.8
- new devel-doc subpackage
- fixed find_lang usage

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 0.8.17-alt1
- new version

* Sun Mar 20 2011 Alexey Morsov <swi@altlinux.ru> 0.8.13-alt1
- new version

* Sun Dec 19 2010 Alexey Morsov <swi@altlinux.ru> 0.8.12-alt1
- new version

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 0.8.11-alt1
- new version

* Sat Jul 03 2010 Alexey Morsov <swi@altlinux.ru> 0.8.7-alt1
- new version

* Tue Jun 01 2010 Alexey Morsov <swi@altlinux.ru> 0.8.5-alt1
- new version

* Wed Apr 21 2010 Alexey Morsov <swi@altlinux.ru> 0.8.2-alt1
- new version

* Tue Apr 20 2010 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt2
-  fix build (add intltool)

* Wed Feb 17 2010 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1
- new version

* Sat Dec 19 2009 Alexey Morsov <swi@altlinux.ru> 0.7.17-alt1
- new version

* Tue Nov 03 2009 Alexey Morsov <swi@altlinux.ru> 0.7.15-alt1
- new version

* Sun Aug 30 2009 Alexey Morsov <swi@altlinux.ru> 0.7.9-alt1
- new version
- fix #20655

* Thu Jul 23 2009 Alexey Morsov <swi@altlinux.ru> 0.7.8-alt1
- new version

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.7-alt1
- new version

* Thu Mar 19 2009 Alexey Morsov <swi@altlinux.ru> 0.7.3-alt1
- new version
- remove post/postun (repocop)

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 0.7.2-alt1
- version 0.7.2

* Wed Sep 10 2008 Alexey Morsov <swi@altlinux.org> 0.7.1-alt1
- new version (development)
- fix bug #16482 (remove abi version from devel package name)
- fix bug #16962

* Sat Jul 19 2008 Alexey Morsov <swi@altlinux.ru> 0.7.0-alt1
- new version (development)
  + abi version changed to 0.8
- clean spec
  + remove static

* Fri Jul 18 2008 Alexey Morsov <swi@altlinux.ru> 0.6.4-alt1
- new version
- pursue ChangeLog policy

* Sat Mar 15 2008 Alexey Morsov <swi@altlinux.ru> 0.6.2-alt1
- version 0.6.2

* Tue Jan 01 2008 Alexey Morsov <swi@altlinux.ru> 0.6.1-alt1
- version 0.6.1

* Thu Nov 08 2007 Alexey Morsov <swi@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 0.5.0-alt1
- version 0.5.0
- so-name changed

* Tue Jul 31 2007 Alexey Morsov <swi@altlinux.ru> 0.4.2-alt1
- Avoid crash if libxml2 returns ERROR or NONE when guessing encoding.
- do not leak the mime type
- fixed signedness issue spotted with help of sparse
- needed for gnumeric 1.7.11


* Sat Jun 02 2007 Alexey Morsov <swi@altlinux.ru> 0.4.0-alt1
- new version for Gnumeric 1.7.10
- added new cubic spline support
- new convenience function
- fixes

* Wed Apr 25 2007 Alexey Morsov <swi@altlinux.ru> 0.3.8-alt1
- new version
- clean spec from cvs bounds (port to git)
- add docs for -devel

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 0.3.7-alt1
- new version (bug fixes)
- add libpcre-devel req (patch for pcre)

* Mon Feb 19 2007 Alexey Morsov <swi@altlinux.ru> 0.3.6-alt1
- new version (for gnumeric 1.7.7)

* Mon Dec 25 2006 Alexey Morsov <swi@altlinux.ru> 0.3.5-alt2
- fix spec (bug 10496)

* Tue Dec 19 2006 Alexey Morsov <swi@altlinux.ru> 0.3.5-alt1
- new version (for gnumeric 1.7.6)

* Tue Dec 05 2006 Alexey Morsov <swi@altlinux.ru> 0.3.4-alt1
- build new version (for gnumeric 1.7.5)

* Fri Mar 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.2-alt1.1
- Rebuild with libgsf-1.so.114 .

* Thu Nov 17 2005 Vital Khilko <vk@altlinux.ru> 0.1.2-alt1
- first release

