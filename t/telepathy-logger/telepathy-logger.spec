%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_disable check

%define api_ver 0.2

Name: telepathy-logger
Version: 0.8.2
Release: alt2

Summary: Telepathy client that logs information received by the Telepathy framework
License: LGPLv2.1+
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/

Vcs: https://gitlab.freedesktop.org/telepathy/telepathy-logger.git
Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.bz2
Patch10: telepathy-logger-0.8.2-deb-Add-a-systemd-user-service.patch
Patch11: telepathy-logger-0.8.2-deb-doc-Use-CDATA-section-to-avoid-XML-error-caused-by-e.patch
Patch12: telepathy-logger-0.8.2-deb-sync_tools_with_tp-glib_master.patch
Patch13: telepathy-logger-0.8.2-deb-update_gtkdoc.patch

Requires: lib%name = %version-%release
Requires: libtelepathy-mission-control >= 5.4.0

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: gtk-doc intltool libgio-devel >= 2.28.0
BuildRequires: libdbus-devel libdbus-glib-devel libtelepathy-glib-devel >= 0.24.2
BuildRequires: libxml2-devel libsqlite3-devel
%{?_enable_introspection:BuildRequires: libtelepathy-glib-gir-devel}
%{?_enable_check:BuildRequires: xvfb-run /proc dbus python3-module-twisted-words python3-module-xmpp}

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
%setup
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%autoreconf
%add_optflags %(getconf LFS_CFLAGS)
%configure \
	--disable-schemas-compile \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	PYTHON=%__python3
%make_build

%check
xvfb-run %make -k check VERBOSE=1

%install
%makeinstall_std

%files
%_libexecdir/%name
%_datadir/telepathy/clients/Logger.client
%_datadir/dbus-1/services/*
%config %_datadir/glib-2.0/schemas/*
%_prefix/lib/systemd/user/telepathy-logger.service
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver
%_libdir/lib%name.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif


%changelog
* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt2
- applied debian (0.8.2-4) patchset
- updated BR

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Tue Feb 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Nov 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

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

