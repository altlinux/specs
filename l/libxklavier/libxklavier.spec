%define ver_major 5.2
%define api_ver 1.0

%def_disable static
%def_enable introspection

Name: libxklavier
Version: %ver_major.1
Release: alt1

Summary: libXklavier library
License: %lgpl2plus
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/LibXklavier
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.in
%define libxml_ver 2.0.0
%define glib_ver 2.16.0

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-build-gnome

# From configure.in
BuildPreReq: gtk-doc libX11-devel libxkbfile-devel
BuildPreReq: libxml2-devel >= %libxml_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: iso-codes-devel libX11-devel
BuildPreReq: xkbcomp libXi-devel >= 1.1.3
%{?_enable_introspection:BuildRequires:gobject-introspection-devel}

%description
This library allows you simplify XKB-related development.

%package devel
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries, include files, etc you can use to develop libxklavier applications.

%package devel-doc
Summary: Development documentation for libxklavier
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation for libxklavier

%package gir
Summary: GObject introspection data for libxklavier
Group: System/Libraries
Requires: %name = %version-%release

%description gir
This package provides GObject introspection data for the libxklavier.

%package gir-devel
Summary: GObject introspection devel data for libxklavier
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
This package provides GObject introspection devel data for libxklavier.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-xkb-support \
	--enable-xmodmap-support \
	--with-xkb-base=%_datadir/X11/xkb \
	--with-xkb-bin-base=%_bindir \
	--with-xmodmap-base=%_datadir/xmodmap

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS CREDITS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-doc
%_gtk_docdir/%name

%files gir
%_typelibdir/Xkl-%api_ver.typelib

%files gir-devel
%_girdir/Xkl-%api_ver.gir

%changelog
* Thu Feb 16 2012 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- 5.2.1
- removed obsolete linking patch
- new introspection subpackages

* Sun Feb 13 2011 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt2
- rebuild for soname set-versions

* Mon Apr 05 2010 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0

* Sun Feb 21 2010 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt2
- applied patch(3) fixed gnome-settings-daemon fail from a NX session
  (closes #23004)

* Wed Jul 08 2009 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0 (soname changed 12.2.0->15.0.0)

* Thu Mar 19 2009 Yuri N. Sedunov <aris@altlinux.org> 3.9-alt1
- 3.9
- updated patches

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 3.8-alt1
- 3.8
- updated linking patch
- updated buildreqs
- removed obsolete *ldconfig in %%post{,un}
- new -devel-doc noarch subpackage

* Sat Sep 06 2008 Alexey Rusakov <ktirf@altlinux.org> 3.7-alt1
- new version (3.7), with crashes on non-UTF8 locales hopefully fixed
- bumped up Glib version buildreq
- minor changes to facilitate building new versions with the same symbols
- dropped --enable-doxygen, it is not applicable anymore

* Fri Jun 06 2008 Alexey Shabalin <shaba@altlinux.ru> 3.6-alt1
- new version (3.6)
- add --with-xkb-bin-base option for configure (#15822)
- move libs from LDFLAGS to LIBADD (patch1)
- add versioning

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 3.5-alt1
- NMU
- new version (3.5)
- change options for configure xmodmap-base: from  %%_datadir/X11/xkb/rules to %%_datadir/xmodmap

* Thu Dec 27 2007 Alexey Rusakov <ktirf@altlinux.org> 3.3-alt2
- Create config.rpath to fix building with new autotools.

* Sat Sep 08 2007 Alexey Rusakov <ktirf@altlinux.org> 3.3-alt1
- new version (3.3)
- use more macros, in particular, use one from rpm-build-licenses
- updated the Source url to make it agnostic wrt SourceForge mirrors.

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 3.2-alt1
- new version 3.2 (with rpmrb script)

* Wed Oct 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Thu Aug 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 3.0-alt1
- new version 3.0 (with rpmrb script)

* Sun Jul 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.91-alt1
- new version 2.91 (with rpmrb script)
- updated dependencies
- spec cleanup
- development documentation has been moved back to gtk-doc directory, as intended.

* Sun Mar 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.2-alt1
- new version 2.2. (with rpmrb script)

* Sat Jan 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.1-alt1
- 2.1, thanks to shrek@ for the spec updates.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1
- 2.0

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.14-alt1
- 1.14.

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.04-alt1
- 1.04

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.02-alt1
- 1.02

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.00-alt1
- 1.00

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.97-alt1
- 0.97

* Thu Dec 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.95-alt2
- do not package .la files.

* Fri Oct 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.95-alt1
- 0.95

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.90-alt2
- rebuild.

* Thu Jul 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.90-alt1
- 0.90

* Thu Jun 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.80-alt1
- 0.80

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.71-alt2
- build current cvs snapshot.

* Sat May 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.71-alt1
- 0.71

* Fri May 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Thu Jan 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- 0.6

* Fri Dec 20 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.5-alt1
- 0.5

* Tue Nov 19 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.4-alt1
- ALTLinux build
