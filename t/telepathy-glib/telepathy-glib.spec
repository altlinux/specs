%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_enable vala

Name: telepathy-glib
Version: 0.18.1
Release: alt1

Summary: Telepathy framework - GLib connection manager library
License: LGPL
Group: System/Libraries
Url: http://telepathy.freedesktop.org/wiki/TelepathyGLib

Source: http://telepathy.freedesktop.org/releases/telepathy-glib/%name-%version.tar.gz

%define glib_ver 2.30.0
%define dbus_ver 0.90
%define gir_ver 0.10.3
%define vala_ver 0.11.7

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libdbus-glib-devel >= %dbus_ver
BuildRequires: gtk-doc  python-module-PyXML
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver}
%{?_enable_vala:BuildPreReq: vala >= %vala_ver vala-tools >= %vala_ver}

# for check
BuildRequires: /proc dbus dbus-tools-gui

%description
This package contains telepathy-glib, a GLib-based library for Telepathy
components.

%package -n lib%name
Summary: Telepathy framework - GLib connection manager library
Group: System/Libraries

Obsoletes: %name
Provides: %name = %version-%release

%description -n lib%name
This package contains telepathy-glib, a GLib-based library for Telepathy
components.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: lib%name = %version-%release

Obsoletes: %name-devel
Provides: %name-devel = %version-%release

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
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-vala
Summary: Vala language bindings for the %name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings for the %name library

%prep
%setup -q

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{?_enable_vala:--enable-vala-bindings}

%make_build

%install
%make_install DESTDIR=%buildroot install

%check
%make check

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


%changelog
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


