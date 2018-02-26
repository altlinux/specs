# Ahtung!
#%%set_verify_elf_method unresolved=relaxed

%define ver_major 3.4
%define _libexecdir %_prefix/libexec
%def_enable gtk_doc
%define api_ver 1.0

Name: gnome-online-accounts
Version: %ver_major.2
Release: alt1

Summary: Provide online accounts information
Group: Graphical desktop/GNOME
License: LGPLv2+
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-3.2.0-alt-link.patch

Requires: lib%name = %version-%release

%define glib_ver 2.29.5
%define oauth_ver 0.9.5
%define rest_ver 0.7.12

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: liboauth-devel >= %oauth_ver
BuildPreReq: librest-devel >= %rest_ver
BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libgtk+3-devel libwebkitgtk3-devel libjson-glib-devel
BuildRequires: libgnome-keyring-devel libnotify-devel libsoup-gnome-devel
BuildRequires: gobject-introspection-devel

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n lib%name
Summary: %name shared libraries
Group: System/Libraries

%description -n lib%name
This package contains shared %name libraries.

%package -n lib%name-devel
Summary: Development files for %name libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use %name libraries.

%package -n lib%name-gir
Summary: GObject introspection data for the %name libraries
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name libraries

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name libraries
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name libraries

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name libraries.

%prep
%setup -q
%patch

%build
%autoreconf
%configure --disable-static \
	--enable-facebook \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libexecdir/goa-daemon
%_datadir/dbus-1/services/org.gnome.OnlineAccounts.service
%_datadir/icons/hicolor/*/*/*.png
%_man8dir/goa-daemon.*
%doc NEWS

%files -n lib%name
%_libdir/libgoa-%api_ver.so.*
%_libdir/libgoa-backend-%api_ver.so.*

%files -n lib%name-devel
%_includedir/goa-%api_ver/
%_libdir/libgoa-%api_ver.so
%_libdir/libgoa-backend-%api_ver.so
%_libdir/pkgconfig/goa-%api_ver.pc
%_libdir/pkgconfig/goa-backend-%api_ver.pc

%files -n lib%name-gir
%_libdir/girepository-%api_ver/Goa-%api_ver.typelib

%files -n lib%name-gir-devel
%_datadir/gir-%api_ver/Goa-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/goa/

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- first build for Sisyphus

