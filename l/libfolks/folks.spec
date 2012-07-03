# Ahtung! While g-ir-generate fails on Folks-0.6.typelib
#%%add_findreq_skiplist %_typelibdir/*

%define _name folks
%define ver_major 0.7
%def_disable static
%def_enable introspection
%def_enable vala
%def_enable libsocialweb
%def_enable tracker

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GObject contact aggregation library
Group: System/Libraries
License: LGPLv2+
Url: http://telepathy.freedesktop.org/wiki/Folks

Source: http://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
# git archive --format=tar --prefix=folks-0.6.0/ --output=folks-0.6.0.tar HEAD
#Source: %_name-%version.tar

%define glib_ver 2.24.0
%define tp_glib_ver 0.15.5
%define vala_ver 0.15.1
%define eds_ver 3.1.5
%define gconf_ver 2.31
%define tracker_ver 0.12
%define gee_ver 0.6

BuildRequires: intltool libgio-devel >= %glib_ver libdbus-glib-devel
BuildRequires: libtelepathy-glib-devel >= %tp_glib_ver libgee-devel >= %gee_ver
BuildRequires: evolution-data-server-devel >= %eds_ver libGConf-devel >= %gconf_ver
%{?_enable_tracker:BuildRequires: tracker-devel >= %tracker_ver}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee-gir-devel libtelepathy-glib-gir-devel evolution-data-server-gir-devel}
%{?_enable_vala:BuildRequires: vala >= %vala_ver vala-tools >= %vala_ver libtelepathy-glib-vala evolution-data-server-vala}
%{?_enable_libsocialweb:BuildRequires: libsocialweb-devel libsocialweb-gir-devel %{?_enable_vala:libsocialweb-vala}}
BuildRequires: chrpath

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

%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable vala} \
	%{?_enable_eds:--enable-eds-backend} \
	%{?_enable_tracker:--enable-tracker-backend} \
	%{?_enable_libsocialweb:--enable-libsocialweb-backend=yes}

%make_build

%check
#%make check

%install
%make DESTDIR=%buildroot install

chrpath --delete %buildroot/%_bindir/%_name-{inspect,import}
chrpath --delete %buildroot/%_libdir/%name-*.so.*
chrpath --delete %buildroot/%_libdir/%_name/*/backends/*/*.so

%find_lang %_name

%files -f %_name.lang
%_libdir/*.so.*
%_libdir/%_name/
%doc AUTHORS README

%files devel
%_bindir/folks-import
%{?_enable_vala:%_bindir/folks-inspect}
%_includedir/%_name
%_libdir/*.so
%_libdir/pkgconfig/%{_name}*.pc

%if_enabled introspection
%files gir
%_typelibdir/Folks-0.6.typelib

%files gir-devel
%_girdir/Folks-0.6.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi
%endif

%changelog
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

