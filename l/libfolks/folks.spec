%def_disable snapshot

%define _name folks
%define ver_major 0.15
%define api_ver 0.7

%def_disable libsocialweb
# tracker support removed since 1.15.1
%def_disable tracker
%def_enable eds
%def_enable bluez
%def_enable zeitgeist
%def_disable check

Name: lib%_name
Version: %ver_major.6
Release: alt1

Summary: GObject contact aggregation library
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Folks

%if_disabled snapshot
Source: http://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.58.0
%define tp_glib_ver 0.19.9
%define vala_ver 0.22.1
%define eds_ver 3.38
%define tracker_ver 0.15.2
%define gee_ver 0.8.4
%define zeitgeist_ver 0.9.15

BuildRequires(pre): rpm-macros-meson rpm-build-vala rpm-build-gir
BuildRequires: meson vala-tools >= %vala_ver valadoc
BuildRequires: libgio-devel >= %glib_ver libdbus-glib-devel
BuildRequires: libtelepathy-glib-devel >= %tp_glib_ver libtelepathy-glib-vala libgee0.8-devel >= %gee_ver
BuildRequires: gobject-introspection-devel libgee0.8-gir-devel libtelepathy-glib-gir-devel libgee0.8-gir-devel
BuildRequires: python3-module-dbusmock
%{?_enable_eds:BuildRequires: evolution-data-server-devel >= %eds_ver evolution-data-server-gir-devel evolution-data-server-vala}
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel >= %zeitgeist_ver}
%{?_enable_tracker:BuildRequires: tracker-devel >= %tracker_ver libtracker-gir-devel}
%{?_enable_libsocialweb:BuildRequires: libsocialweb-devel libsocialweb-gir-devel libsocialweb-vala}
# for tools
BuildRequires: libreadline-devel libncurses-devel libxml2-devel
%{?_enable_check:BuildRequires: dbus-tools-gui}

%description
%name is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %_name library

%package vala
Summary: vala language bindings for %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description vala
This package provides vala language bindings for %_name library

%package tests
Summary: Tests for the Folks
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the Folks library.


%prep
%setup -n %_name-%version

%build
%meson \
	%{?_enable_zeitgeist:-Dzeitgeist=true} \
	%{?_disable_eds:-Deds_backend=false} \
	%{?_enable_tracker:-Dtracker_backend=true} \
	%{?_enable_libsocialweb:-Dlibsocialweb_backend=true} \
	%{?_disable_bluez:-Dbluez_backend=false} \
	%{?_enable_installed_tests:-Dinstalled_tests=true}

%meson_build

%install
%meson_install
%find_lang %_name

%check
%meson_test

%files -f %_name.lang
%_libdir/*.so.*
%_libdir/%_name/
%_datadir/glib-2.0/schemas/org.freedesktop.%_name.gschema.xml
%_datadir/GConf/gsettings/%_name.convert
%doc AUTHORS README*

%files devel
%_bindir/%_name-import
%_bindir/%_name-inspect
%_includedir/%_name
%_libdir/*.so
%_pkgconfigdir/%{_name}*.pc

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

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Thu Mar 09 2023 Yuri N. Sedunov <aris@altlinux.org> 0.15.6-alt1
- 0.15.6

* Tue Aug 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.15.5-alt2
- updated to 0.15.5-7-g74886b1d
- built against e-d-s-3.45.* libraries

* Wed Mar 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.15.5-alt1
- 0.15.5

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.15.4-alt1
- updated to 0.15.4-2-gc44d8e32

* Fri Sep 03 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.3-alt1
- 0.15.3

* Mon Feb 15 2021 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Wed Nov 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1.2
- removed unnecessary "Provides" from -gir subpackage.

* Sat Aug 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1.1
- rebuilt against libedataserver-1.2.so.25 (e-d-s-3.37.*)

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Feb 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1 (ported to Meson build system)

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt5
- updated to 0.11.4-55-gc8c3b4c9
- built against new eds-3.31.x libraries

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt4
- updated to 0.11.4-43-gd73a03d2

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

