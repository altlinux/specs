%def_enable snapshot

%define _name folks
%define ver_major 0.11
%define api_ver 0.6
%def_disable static
%def_enable introspection
%def_enable vala
%def_disable libsocialweb
%def_disable tracker
%def_enable bluez
%def_enable zeitgeist

Name: lib%_name
Version: %ver_major.4
Release: alt3

Summary: GObject contact aggregation library
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Folks

%if_disabled snapshot
Source: http://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.40.0
%define tp_glib_ver 0.19.9
%define vala_ver 0.22.1
%define eds_ver 3.13.90
%define tracker_ver 0.15.2
%define gee_ver 0.8.4
%define zeitgeist_ver 0.9.15

BuildRequires: gnome-common intltool libgio-devel >= %glib_ver libdbus-glib-devel
BuildRequires: libtelepathy-glib-devel >= %tp_glib_ver libgee0.8-devel >= %gee_ver
BuildRequires: evolution-data-server-devel >= %eds_ver
BuildRequires: vala-tools valadoc
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel >= %zeitgeist_ver}
%{?_enable_tracker:BuildRequires: tracker-devel >= %tracker_ver}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee0.8-gir-devel libtelepathy-glib-gir-devel evolution-data-server-gir-devel libgee0.8-gir-devel %{?_enable_tracker:libtracker-gir-devel}}
%{?_enable_vala:BuildRequires:  libvala-devel >= %vala_ver vala >= %vala_ver vala-tools >= %vala_ver libtelepathy-glib-vala evolution-data-server-vala}
%{?_enable_libsocialweb:BuildRequires: libsocialweb-devel libsocialweb-gir-devel %{?_enable_vala:libsocialweb-vala}}

# for tools
BuildRequires: libreadline-devel libncurses-devel libxml2-devel
# for check
BuildRequires: dbus-tools-gui

%description
%name is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release
Provides: typelib(Folks) = %ver_major

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library

%package vala
Summary: vala language bindings for %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides vala language bindings for %_name library

%package tests
Summary: Tests for the Folks
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the Folks library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable vala} \
	%{subst_enable zeitgeist} \
	%{?_enable_eds:--enable-eds-backend} \
	%{?_enable_tracker:--enable-tracker-backend} \
	%{?_enable_libsocialweb:--enable-libsocialweb-backend=yes} \
	%{?_enable_bluez:--enable-bluez-backend=yes} \
	%{?_enable_installed_tests:--enable-installed-tests} \
	--disable-fatal-warnings

%make_build V=1

%install
%makeinstall_std

%check
#%%make check

%find_lang %_name

%files -f %_name.lang
%_libdir/*.so.*
%_libdir/%_name/
%_datadir/GConf/gsettings/%_name.convert
%_datadir/glib-2.0/schemas/org.freedesktop.%_name.gschema.xml
%doc AUTHORS README

%files devel
%_bindir/%_name-import
%{?_enable_vala:%_bindir/%_name-inspect}
%_includedir/%_name
%_libdir/*.so
%_libdir/pkgconfig/%{_name}*.pc

%if_enabled introspection
%files gir
%_typelibdir/FolksDummy-%api_ver.typelib
%_typelibdir/Folks-%api_ver.typelib
%_typelibdir/FolksEds-%api_ver.typelib
%_typelibdir/FolksTelepathy-%api_ver.typelib
%{?_enable_tracker:%_typelibdir/FolksTracker-%api_ver.typelib}

%files gir-devel
%_girdir/FolksDummy-%api_ver.gir
%_girdir/Folks-%api_ver.gir
%_girdir/FolksEds-%api_ver.gir
%_girdir/FolksTelepathy-%api_ver.gir
%{?_enable_tracker:%_girdir/FolksTracker-%api_ver.gir}
%endif

%if_enabled vala
%files vala
%_vapidir/%_name.deps
%_vapidir/%_name-dummy.deps
%_vapidir/%_name-dummy.vapi
%_vapidir/%_name-eds.deps
%_vapidir/%_name-eds.vapi
%{?_enable_libsocialweb:%_vapidir/%_name-libsocialweb.deps}
%{?_enable_libsocialweb:%_vapidir/%name-libsocialweb.vapi}
%_vapidir/%_name-telepathy.deps
%_vapidir/%_name-telepathy.vapi
%{?_enable_tracker:%_vapidir/%_name-tracker.deps}
%{?_enable_tracker:%_vapidir/%_name-tracker.vapi}
%_vapidir/%_name.vapi
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Tue Feb 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt3
- updated to 0.11.4-24-g84b78da

* Wed Aug 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt2
- rebuilt for GNOME-2.6 without tracker support

* Mon Jul 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt1
- 0.11.4

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt2
- rebuilt with new eds-3.23 libraries

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2 release

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt0.1
- 0.11.2_46e5abf5

* Sat Aug 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt2
- rebuilt with eds/cheese-3.17 libraries

* Tue May 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Fri Feb 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Tue Jan 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Sun Oct 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- rebuilt with zeitgeist support

* Fri Sep 12 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt2
- rebuilt for GNOME-3.12 (temporarily disabled tracker backend)

* Wed Nov 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Tue Aug 27 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Sat Feb 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Oct 05 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Sep 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.4.1-alt1
- 0.7.4.1

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.9-alt1
- 0.6.9
- enabled tracker backend

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.8-alt1
- 0.6.8

* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt2
- used %autoreconf to fix RPATH problem

* Wed Dec 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Fri Nov 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.4.1-alt2
- tracker backend enabled

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.4.1-alt1
- 0.6.4.1

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.3.2-alt1
- 0.6.3.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Feb 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Tue Sep 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt1
- first build for Sisyphus

