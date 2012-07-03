%define ver_major 3.4
%define api_ver 0.0
%def_disable static
%def_enable introspection

Name: libcryptui
Version: %ver_major.1
Release: alt1
Summary: Library for OpenPGP prompts

Group: System/Libraries
License: GPLv3
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Obsoletes: seahorse-agent
Provides:  seahorse-agent = %version-%release
Obsoletes: libseahorse
Provides: libseahorse = %version-%release

# From configure.in
%define gtk_ver 3.0.0
%define intltool_ver 0.40.0
%define soup_ver 2.33.1
%define gir_ver 0.10.1

BuildRequires: rpm-build-gnome gtk-doc
BuildRequires: libgio-devel libgtk+3-devel >= %gtk_ver libdbus-glib-devel
BuildRequires: gnupg2-gpg libgpgme-devel >= 1.0.0 libgnome-keyring-devel libSM-devel
BuildRequires: libGConf-devel libnotify-devel >= 0.7.3 intltool >= %intltool_ver xsltproc
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

%description
%name is a library used for prompting for PGP keys.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libseahorse-devel
Provides: libseahorse-devel = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Obsoletes: libseahorse-devel-doc
Provides: libseahorse-devel-doc = %version-%release
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Obsoletes: libseahorse-gir
Provides: libseahorse-gir = %version-%release
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Obsoletes: libseahorse-gir-devel
Provides: libseahorse-gir-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%prep
%setup -q

%build
%configure \
    %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --output=%name.lang cryptui

%files -f %name.lang
%_bindir/seahorse-daemon
%_libdir/*.so.*
%_datadir/cryptui/
%_datadir/dbus-1/services/org.gnome.seahorse.service
%_datadir/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml
%_datadir/GConf/gsettings/org.gnome.seahorse.recipients.convert
%_datadir/pixmaps/cryptui/
%_man1dir/seahorse-daemon.1*
%doc AUTHORS NEWS README

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/CryptUI-%api_ver.typelib

%files gir-devel
%_girdir/CryptUI-%api_ver.gir
%endif

%changelog
* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Mar 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sat Sep 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- first build for Sisyphus


