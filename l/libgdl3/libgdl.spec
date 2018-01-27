%define major 3.26
%define _unpackaged_files_terminate_build 1

Name: libgdl3
Version: %major.0
Release: alt1

Summary: Gnome docking library (GDL)

License: %gpl2plus
Group: System/Libraries
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %name-%version.tar
#Patch: %name-%version-%release.patch

Provides: gdl = %version

BuildRequires(pre): rpm-build-licenses rpm-build-gnome
# From configure.in
BuildPreReq: gnome-common
BuildPreReq: libgtk+3-devel >= 3.0.0
BuildPreReq: libxml2-devel >= 2.2.8
BuildPreReq: intltool >= 0.40.0
BuildPreReq: gettext-tools
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel
BuildRequires: gcc-c++

%description
GDL contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta.  Currently GDL include:

  o A symbol browser bonobo component (symbol-browser-control).
  o A docking widget (gdl).
  o A utility library that also contains the stubs and skels for
    the symbol browser and text editor components (gdl, idl).

%package gir
Summary: GObject introspection data for the gdl library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the WebkitGTK library

%package gir-devel
Summary: GObject introspection devel data for the gdl library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the gdl library

%package devel
Summary: Gnome Devtool Libraries
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
GDL contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta.

This package contains headers and other development files needed
to develop/compile applications that need GNOME development tools.

%package devel-doc
Summary: Development documentation for gdl
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for gdl.


%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup
#%patch -p1

%build
%autoreconf
%configure --enable-gtk-doc --disable-static
%make_build

%install
%makeinstall_std

%find_lang gdl-3

%check
%make check

%files -f gdl-3.lang
%doc README
%_libdir/lib*.so.*

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files devel
%doc AUTHORS ChangeLog MAINTAINERS NEWS
%dir %_includedir/libgdl-3.0
%dir %_includedir/libgdl-3.0/gdl
%_includedir/libgdl-3.0/gdl/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_gtk_docdir/*

%changelog
* Sat Jan 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Sep 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Wed Mar 26 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.91-alt1
- 3.9.91

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Mon Oct 01 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 3.5.5-alt1
- 3.5.5

* Fri May 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Sun Mar 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Thu May 26 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Wed Apr 20 2011 Alexey Shabalin <shaba@altlinux.ru> 2.31.2-alt1
- 2.31.2

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.30.0-alt1.qa1
- rebuild using girar-nmu to require/provide setversion.
  by request of mithraen@

* Wed Apr 28 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt1
- 2.30.0
- packaged gtk-doc files as noarch subpackage
- add gir and gir-devel subpackages
- updated buildreqs

* Tue Dec 15 2009 Alexey Rusakov <ktirf@altlinux.org> 2.28.2-alt1
- New version (2.28.2), rebased to 2.28 branch.
- Updated and cleaned up buildreqs.

* Fri Sep 11 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2
- Moved 'make check' to %%check section (supported by the latest ALT rpm
  build), so one can disable checks by building with --disable-check.

* Mon May 25 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt1
- New version (2.26.2).
- Moved to git.
- Replaced autoreconf with ./autogen.sh to fix building with automake_1.11.
- Added an explicit --enable-gtk-doc to configure flags (it is off by
  default now).

* Fri Apr 10 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.0-alt1
- New version (2.26.0).
- Added 'make check' invocation after the build

* Thu Dec 25 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.0-alt2
- Removed no more needed ldconfig calls in rpm scriplets.

* Thu Nov 06 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.0-alt1
- New version (2.24.0).

* Sun Jul 06 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.11-alt1
- New version (0.7.11).

* Mon Feb 11 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.9-alt1
- New version (0.7.9).

* Tue Jan 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.8-alt1
- New version (0.7.8).
- Use rpm-build-licenses, rpm-build-gnome and %%autoreconf.

* Wed Aug 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.7-alt1
- new version 0.7.7 (with rpmrb script)

* Mon Jun 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.6-alt1
- new version (0.7.6)
- libgdl-gnome linkage fixed in upstream, no more patch needed.

* Sun May 06 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.4-alt1
- new version (0.7.4)
- updated dependencies

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.3-alt2
- fixed the linking patch (gdl-icons.h got accidentally left out in the cold).
- added _unpackaged_files_terminate_build macro.

* Sat Mar 31 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.3-alt1
- new version (0.7.3)
- spec cleanup

* Mon Feb 12 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.2-alt1
- new version (0.7.2)

* Thu Jan 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)
- added a patch to fix linking of libgdl-gnome

* Tue May 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.6.1-alt1
- new version (0.6.1)

* Tue Mar 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt2
- NMU: cleanup spec, add Url, add URL to Source, use major version
- update buildreq, use make_build
- remove COPYING (pure GPL) from doc
- add Packager tag
- rename spec to libgdl

* Thu Jun 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.6.0-alt1
- New upstream version.

* Mon May 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.5.0-alt1
- New upstream version.
- Switched from CVS to tarball sources.

* Sun Feb 20 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1.1.cvs20040220
- version from cvs

* Fri Feb 18 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- First build for ALTLinux

