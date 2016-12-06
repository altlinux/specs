%define ver_major 1.14
%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: libgsf
Version: %ver_major.41
Release: alt1

Summary: GNOME Structured file library
License: %lgpl2plus
Group: System/Libraries
Url: http://www.gnumeric.org/

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.ac
BuildPreReq: intltool gtk-doc >= 1.0
BuildPreReq: libgio-devel >= 2.26.0
BuildPreReq: libxml2-devel >= 2.4.16
BuildRequires: libgdk-pixbuf-devel bzlib-devel zlib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_static:BuildRequires: glibc-devel-static}
# for check
BuildRequires: unzip

%description
GNOME Structured file library

%package devel
Summary: Libraries and include files for gsf
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using gsf.

%package gir
Summary: GObject introspection data for the gsf library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GNOME Structured file library.

%package gir-devel
Summary: GObject introspection devel data for the gsf library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GNOME Structured file library.


%package devel-doc
Summary: Development documentation for gsf
Group: Development/C
BuildArch: noarch
Conflicts: %name-gnome < %version

%description devel-doc
This package contains the documentation for development programs using gsf.

%package devel-static
Summary: Static gsf libraries
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package provides the necessary development libraries to allow you
to build programs staticallly linked against libgsf.

%setup_python_module gsf
%package -n python-module-gsf
Summary: Python bindings for %name
Group: Development/Python
Autoreq: yes
Requires: %name = %version-%release
%add_python_req_skip _gsf

%description -n python-module-gsf
This package contains files that are needed to use libgsf from Python
programs.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q

subst 's/pythondir/pyexecdir/' python/Makefile.am

%build
%autoreconf
%configure \
    --with-gdk-pixbuf \
    --with-bz2 \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_enable_introspection:--enable-introspection=yes} \
    %{subst_enable static}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%check
%make check

%files -f %name.lang
%_bindir/*
%_libdir/%name-1.so.*
%_datadir/thumbnailers/gsf-office.thumbnailer
%_man1dir/*
%doc AUTHORS README TODO NEWS

%files devel
%dir %_includedir/%name-1
%dir %_includedir/%name-1/gsf
%_includedir/%name-1/gsf/*.h
%_libdir/%name-1.so
%_pkgconfigdir/%name-1.pc

%if_enabled introspection
%files gir
%_typelibdir/Gsf-1.typelib

%files gir-devel
%_girdir/Gsf-1.gir
%endif

%if_enabled static
%files devel-static
%_libdir/%name-1.a
%endif

%files devel-doc
%_gtk_docdir/*


%changelog
* Tue Dec 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.41-alt1
- 1.14.41

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.40-alt1
- 1.14.40

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.39-alt1
- 1.14.39

* Sat Jun 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.38-alt1
- 1.14.38

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.37-alt1
- 1.14.37

* Sat Feb 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.36-alt1
- 1.14.36

* Sat Feb 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.14.35-alt1
- 1.14.35

* Wed Jul 29 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.34-alt1
- 1.14.34

* Fri Apr 17 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.33-alt1
- 1.14.33

* Thu Mar 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.32-alt1
- 1.14.32

* Thu Feb 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.31-alt1
- 1.14.31

* Thu Mar 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.14.30-alt1
- 1.14.30

* Sun Jan 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.14.29-alt1
- 1.4.29

* Fri Aug 02 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.28-alt1
- 1.14.28

* Sun Jun 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.27-alt1
- 1.14.27

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.26-alt1
- 1.14.26

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.25-alt1
- 1.14.25

* Fri Sep 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.24-alt1
- 1.14.24

* Fri Apr 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.23-alt2
- 1.14.23 release

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.23-alt1
- 1.14.23 snapshot
- new -gir gir-devel subpackages
- fixed tests

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.22-alt1
- 1.14.22
- no more gnome-vfs/bonobo support (-gnome subpackages)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14.21-alt1.1
- Rebuild with Python-2.7

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.14.21-alt1
- 1.4.21

* Fri Mar 25 2011 Yuri N. Sedunov <aris@altlinux.org> 1.14.20-alt1
- 1.4.20

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.14.19-alt3
- rebuilt for debuginfo

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.14.19-alt2
- updated buildreqs

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1.14.19-alt1
- 1.14.19

* Thu Apr 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.14.18-alt1
- 1.14.18

* Sun Feb 14 2010 Yuri N. Sedunov <aris@altlinux.org> 1.14.17-alt1
- 1.14.17

* Mon Oct 12 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.16-alt1
- 1.14.16

* Mon Jun 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.15-alt1
- new version

* Sun May 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.14-alt1
- 1.14.14

* Thu May 07 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.13-alt1
- 1.14.13

* Sun Apr 26 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.12-alt1
- 1.14.12

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.14.11-alt1
- 1.14.11
- removed obsolete %%post{,un}_ldconfig

* Mon Nov 10 2008 Yuri N. Sedunov <aris@altlinux.org> 1.14.10-alt1
- 1.14.10
- don't rebuild documentation
- don't package documentation twice
- move documentaion to separate package
- move gsf-office-thumbnailer to libgsf-gnome
- install gsf-office-thumbnailer.schemas

* Mon Sep 01 2008 Alexey Rusakov <ktirf@altlinux.org> 1.14.9-alt1
- Version 1.14.9.
- Added intltool to explicit buildreqs.
- Updated the files list of the -devel subpackage (no more gsf-gvfs).

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1.14.8-alt1
- Version 1.14.8.

* Sun Feb 03 2008 Grigory Batalov <bga@altlinux.ru> 1.14.7-alt3.1
- Rebuilt with python-2.5.

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 1.14.7-alt3
- Fixed Python bindings packaging.

* Wed Jan 09 2008 Alexey Rusakov <ktirf@altlinux.org> 1.14.7-alt2
- Python bindings packaged.
- Use more macros.
- Updated the files list.

* Tue Sep 25 2007 Alexey Morsov <swi@altlinux.ru> 1.14.7-alt1
- version 1.14.7

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 1.14.6-alt1
- bug fixes
- some function deprecated/deleted/renamed

* Tue Jul 31 2007 Alexey Morsov <swi@altlinux.ru> 1.14.5-alt1
- fix a doc build error
- many small fixes
- needed for gnumeric 1.7.11

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 1.14.3-alt1
- new version (bug fixes)

* Thu Dec 14 2006 Alexey Morsov <swi@altlinux.ru> 1.14.2-alt1
- NMU: new version

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.1-alt2
- fixed dependencies.

* Fri Aug 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.1-alt1
- new version 1.14.1 (with rpmrb script)

* Sat Jun 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.0-alt2
- fixed the license.

* Tue Mar 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.0-alt1
- new version (1.14.0)
- spec cleanup

* Thu Nov 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.13.3-alt1
- new version

* Tue Oct 11 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.13.2-alt1
- new version
- Removed excess buildreqs.

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.12.3-alt1
- 1.12.3

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon May 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed May 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.8.2-alt3
- do not package .la files.
- do not build devel-static subpackages by default.

* Thu Oct 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.8.2-alt2
- libgsf-gnome{,-devel{,-static}} subpackages.

* Sun Sep 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sat Jun 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Mon May 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sun Feb 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.7.2-alt1
- new version.

* Thu Oct 03 2002 AEN <aen@altlinux.ru> 1.4.0-alt1
- first build for Sisyphus

