%def_disable static
%def_disable gtk_doc
%def_enable introspection
%define api_ver 0.2

Name: telepathy-logger
Version: 0.2.13
Release: alt1

Summary: Telepathy client that logs information received by the Telepathy framework
License: LGPLv2.1+
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.bz2

Requires: lib%name = %version-%release
Requires: libtelepathy-mission-control >= 5.4.0

BuildRequires: gtk-doc intltool libgio-devel >= 2.28.0
BuildRequires: libdbus-devel libdbus-glib-devel libtelepathy-glib-devel >= 0.15.6
BuildRequires: libxml2-devel
BuildRequires: libsqlite3-devel python-module-twisted-words python-module-xmpp
%{?_enable_introspection:BuildRequires: libtelepathy-glib-gir-devel}

# some tests require x11
# for check
#BuildRequires: /proc dbus

%description
tp-logger is a headless observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

%package -n lib%name
Summary: Telepathy framework - tp-logger library
Group: System/Libraries

%description -n lib%name
tp-logger is a headless observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

This package contains telepathy-logger shared library.

%package -n lib%name-devel
Summary: Development libraries and header files for %name library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development libraries and header files for %name.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
This package contains development documentation for %name library.

%package -n lib%name-gir
Summary: GObject introspection data for %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for %name library.


%prep
%setup -q

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags dbus-glib-1`"
%configure \
	--disable-schemas-compile \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

# SMP-incompatible build
%make

%check
# x11 session required
#%%make check

%install
%make_install DESTDIR=%buildroot install

%files
%_libexecdir/%name
%_datadir/telepathy/clients/Logger.client
%_datadir/dbus-1/services/*
%config %_datadir/glib-2.0/schemas/*
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver
%_libdir/lib%name.so
%_libdir/pkgconfig/%name-%api_ver.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.13-alt1
- 0.2.13

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt2
- used %%autoreconf to fix RPATH problem

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- 0.2.12

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Sun Dec 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Fri Jul 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Wed Mar 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

