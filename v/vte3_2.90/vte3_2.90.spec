%define _name vte
%define ver_major 0.36
%define api_ver 2.90

Name: %{_name}3_%api_ver
Version: %ver_major.3
Release: alt1

%def_disable pty_helper
%def_disable static
%def_enable introspection
%def_enable gtk_doc

Summary: Terminal emulator widget for use with GTK+
License: LGPL
Group: Terminals

Requires: lib%name = %version-%release
%if_enabled pty_helper
Requires: gnome-pty-helper
%endif

Source: ftp://gnome.org/pub/gnome/sources/%name/%ver_major/%_name-%version.tar.xz

%define gtk3_ver 3.1.9
%define glib_ver 2.31.13
%define pango_ver 1.22
%define gir_ver 0.10.2

BuildPreReq: rpm-build-python

BuildRequires: gperf
BuildRequires: libSM-devel libncurses-devel libcairo-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: gtk-doc >= 1.1.0
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libpango-devel >= %pango_ver
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

%description
VTE is a terminal emulator widget for use with GTK+

%package -n lib%name
Summary: Terminal emulator widget library for use with GTK+3
Group: System/Libraries
%if_enabled pty_helper
Requires: gnome-pty-helper
%endif

%description -n lib%name
VTE is a terminal emulator widget for use with GTK+3.
This package contains the VTE shared libraries.

%package -n lib%name-devel
Summary: Development files for VTE
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
VTE is a terminal emulator widget for use with GTK+3. This package
contains the files needed for building applications using VTE.

%package -n lib%name-devel-doc
Summary: Development documentation for VTE
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
API documentation for the VTE library.
VTE is a terminal emulator widget for use with GTK+3.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for VTE
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
VTE is a terminal emulator widget for use with GTK+3. This package
contains the libraries needed for building applications statically
linked with VTE.
%endif	# enabled static

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


%define helperdir %_libdir/%_name
%define pkgdocdir %_docdir/%name-%version

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-dependency-tracking \
	--libexecdir=%helperdir \
	--without-glX \
%if_enabled pty_helper
	--enable-gnome-pty-helper \
%else
	--disable-gnome-pty-helper \
%endif
	--enable-shared \
	--disable-schemas-compile \
	%{subst_enable static} \
	%{subst_enable introspection} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS MAINTAINERS NEWS README %buildroot%pkgdocdir/
ln -s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING

install -p -m644 doc/utmpwtmp.txt doc/boxes.txt %buildroot%pkgdocdir/
install -p -m644 src/iso2022.txt %buildroot%pkgdocdir/
install -p -m644 doc/openi18n/*.txt %buildroot%pkgdocdir/

# Remove unpackaged files
find %buildroot -type f -name '*.la' -delete

%find_lang %_name-%api_ver --output=%name.lang

%files
%_bindir/*

%files -n lib%name -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/MAINTAINERS
%pkgdocdir/NEWS
%pkgdocdir/README
%_libdir/*.so.*
%exclude %_sysconfdir/profile.d/vte.sh
%if_enabled pty_helper
%exclude %helperdir/gnome-pty-helper
%endif

%files -n lib%name-devel
%pkgdocdir/*.txt
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc

%files -n lib%name-devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Vte-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Vte-%api_ver.gir
%endif

%changelog
* Sat Sep 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.3-alt1
- first build for Sisyphus

