%define ver_major 0.11
%define api_ver 1

%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: libsecret
Version: %ver_major
Release: alt1

Summary: A client library for the Secret Service DBus API
Group: System/Libraries
License: LGPLv2
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.0

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgcrypt-devel gtk-doc intltool xsltproc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
# for check
BuildRequires: /proc dbus-tools-gui python-module-dbus  python-module-pygobject

%description
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides development documentations for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for %name.


%prep
%setup

%build
%autoreconf
%configure --disable-static \
%{?_enable_gtk_doc:--enable-gtk-doc} \
%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang %name

%check
# required X11
#%%make check

%files -f %name.lang
%_bindir/secret-tool
%_libdir/%name-%api_ver.so.*
%_man1dir/secret-tool.1.*
%doc AUTHORS README NEWS

%files devel
%_includedir/%name-%api_ver
%_libdir/%name-%api_ver.so
%_libdir/pkgconfig/%name-%api_ver.pc
%_libdir/pkgconfig/%name-unstable.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/Secret-%api_ver.typelib
%_typelibdir/SecretUnstable-0.typelib

%files gir-devel
%_girdir/Secret-%api_ver.gir
%_girdir/SecretUnstable-0.gir
%endif


%changelog
* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

