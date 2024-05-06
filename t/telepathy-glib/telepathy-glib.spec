%def_disable snapshot
%define _libexecdir %_prefix/libexec

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable check
# not ready for python3 yet
%def_disable installed_tests

Name: telepathy-glib
Version: 0.24.2
Release: alt3

Summary: Telepathy framework - GLib connection manager library
License: LGPL-2.1
Group: System/Libraries
Url: https://telepathy.freedesktop.org/wiki/TelepathyGLib
Patch10: telepathy-glib-0.24.2-up-test-cm.patch

%if_disabled snapshot
Source: https://telepathy.freedesktop.org/releases/telepathy-glib/%name-%version.tar.gz
%else
Vcs: https://github.com/TelepathyIM/telepathy-glib.git
#Vcs: https://anongit.freedesktop.org/git/telepathy/telepathy-glib.git
Source: %name-%version.tar
%endif

%define glib_ver 2.36.0
%define dbus_ver 0.90
%define gir_ver 0.10.3
%define vala_ver 0.16.0

BuildRequires(pre): rpm-build-python3
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libdbus-glib-devel >= %dbus_ver
BuildRequires: gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gir_ver}
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
This package contains telepathy-glib, a GLib-based library for Telepathy
components.

%package -n lib%name
Summary: Telepathy framework - GLib connection manager library
Group: System/Libraries

Obsoletes: %name
Provides: %name = %EVR

%description -n lib%name
This package contains telepathy-glib, a GLib-based library for Telepathy
components.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: lib%name = %EVR

Obsoletes: %name-devel
Provides: %name-devel = %EVR

%description -n lib%name-devel
Development libraries and header files for %name.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
This package contains development documentation for the %name

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-vala
Summary: Vala language bindings for the %name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name = %EVR

%description -n lib%name-vala
This package provides Vala language bindings for the %name library

%package -n lib%name-tests
Summary: Tests for the %name package
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-tests
This package provides tests programs that can be used to verify
the functionality of the installed %name library package.

%prep
%setup
%patch10 -p1
sed -i 's;\(\/bin\/python\)$;\13;' tests/*.py
sed -i 's;\(env python\)$;\13;' examples/client/python/*.py

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{?_enable_vala:--enable-vala-bindings} \
	%{?_enable_installed_tests:--enable-installed-tests} \
	PYTHON=%__python3
%make_build

%install
%makeinstall_std

%check
export TP_TESTS_NO_TIMEOUT=1
%make -k check CHECK_VERBOSE=1

%files -n lib%name
%doc AUTHORS ChangeLog
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%dir %_includedir/telepathy-1.0/telepathy-glib
%_includedir/telepathy-1.0/telepathy-glib/*.h
%dir %_includedir/telepathy-1.0/telepathy-glib/_gen
%_includedir/telepathy-1.0/telepathy-glib/_gen/*.h

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled vala
%files -n lib%name-vala
%_datadir/vala/vapi/telepathy-glib.deps
%_datadir/vala/vapi/telepathy-glib.vapi
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%if_enabled installed_tests
%files -n lib%name-tests
%_bindir/telepathy-example*
%_libexecdir/telepathy-example*
%_libdir/%name-tests/
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.example*
%_datadir/telepathy/managers/example_*
%endif

%changelog
* Sun May 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt3
- fixed test-cm for newer glib (upstream patch)

* Thu Feb 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt2
- updated sources to actual telepathy-glib-0.24.2 tarball

* Wed Jan 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2
- enabled %%check, gtk-doc
- fixed License tag

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt3.2
- disabled %%check

* Mon Apr 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt3.1
- set TP_TESTS_NO_TIMEOUT=1 (ALT #36485)

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt3
- rebuild with glib-2.60.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt2
- fixed tests for glib >= 2.46

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Wed Oct 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.2

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Tue May 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Thu Nov 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.19.9-alt1
- 0.19.9

* Tue May 08 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Fri Mar 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.17.7-alt1
- 0.17.7

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0
- requires /proc for tests

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.9-alt1
- 0.14.9

* Wed Jun 29 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.8-alt1
- 0.14.8

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.7-alt1
- 0.14.7

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.6-alt1
- 0.14.6

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.5-alt1
- 0.14.5

* Sun Apr 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.4-alt1
- 0.14.4

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt2
- rebuild for debuginfo

* Tue Dec 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Mon Dec 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.7-alt1
- 0.10.7

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- 0.10.6

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Wed Apr 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Fri Apr 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Fri Apr 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Sat Jan 23 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0
- %%check section

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Tue Nov 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.35-alt1
- 0.7.35

* Thu Jun 25 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.32-alt1
- 0.7.32

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.29-alt1
- 0.7.29

* Thu Jan 29 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.24-alt1
- new version

* Thu Dec 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.20-alt1
- 0.7.20

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.19-alt1
- new version
- removed obsolete %%post{,un} scripts

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.18-alt1
- 0.7.18
- new devel-doc noarch subpackage

* Fri Jul 04 2008 Igor Zubkov <icesik@altlinux.org> 0.7.11-alt1
- 0.7.10 -> 0.7.11

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 0.7.10-alt1
- 0.7.8 -> 0.7.10

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 0.7.8-alt1
- 0.7.7 -> 0.7.8

* Sun May 04 2008 Igor Zubkov <icesik@altlinux.org> 0.7.7-alt2
- fix for fresh sisyphus_check

* Fri May 02 2008 Igor Zubkov <icesik@altlinux.org> 0.7.7-alt1
- 0.7.6 -> 0.7.7

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 0.7.6-alt1
- 0.7.3 -> 0.7.6
- buildreq

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.7.3-alt1
- 0.7.1 -> 0.7.3

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 0.7.0-alt2
- rename telepathy-glib to libtelepathy-glib
- rename telepathy-glib-devel to libtelepathy-glib-devel

* Tue Dec 04 2007 Igor Zubkov <icesik@altlinux.org> 0.7.0-alt1
- 0.6.1 -> 0.7.0

* Mon Nov 12 2007 Igor Zubkov <icesik@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- 0.5.14 -> 0.6.0

* Thu Sep 06 2007 Igor Zubkov <icesik@altlinux.org> 0.5.14-alt1
- 0.5.13 -> 0.5.14

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 0.5.13-alt2
- add docs
- update Url
- add static library libtelepathy-glib-unstable.a to devel subpackage

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 0.5.13-alt1
- build for Sisyphus


