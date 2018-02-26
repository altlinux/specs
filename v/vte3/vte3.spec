%define _name vte
%define ver_major 0.32

Name: %{_name}3
Version: %ver_major.2
Release: alt1

%def_enable pty_helper
%def_disable static
%def_enable introspection
%define gtk_api_ver 3.0
%define vte_api_ver 2.90

Summary: Terminal emulator widget for use with GTK+
License: LGPL
Group: Terminals

Requires: lib%name = %version-%release
Requires: gnome-pty-helper

Source: ftp://gnome.org/pub/gnome/sources/%name/%ver_major/%_name-%version.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=663779
# http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
Patch: vte-virtual_modifier_mapping.patch

%define gtk3_ver 3.1.9
%define glib_ver 2.31.13
%define pango_ver 1.22
%define gir_ver 0.10.2

BuildPreReq: rpm-build-python

BuildRequires: libSM-devel libncurses-devel libcairo-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: gtk-doc >= 1.1.0
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libpango-devel >= %pango_ver
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

%description
VTE is a terminal emulator widget for use with GTK+

%package utils
Summary: VTE utilities and test programs
Group: Terminals
Requires: lib%name = %version-%release

%description utils
Utilities, samples and test programs distributed with VTE, a terminal
emulator widget for use with GTK+3.

%package -n lib%name
Summary: Terminal emulator widget library for use with GTK+3
Group: System/Libraries
Requires: gnome-pty-helper

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
%setup -q -n %_name-%version

#%%patch -p1

%build
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
	%{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

%__install -d -m755 %buildroot%pkgdocdir
%__install -p -m644 AUTHORS MAINTAINERS NEWS README %buildroot%pkgdocdir/
%__ln_s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING

%__install -p -m644 doc/utmpwtmp.txt doc/boxes.txt \
    %buildroot%pkgdocdir/
%__install -p -m644 src/iso2022.txt \
    %buildroot%pkgdocdir/
%__install -p -m644 doc/openi18n/*.txt \
    %buildroot%pkgdocdir/

# Remove unpackaged files
find %buildroot -type f -name '*.la' -delete

%find_lang %_name-%vte_api_ver --output=%name.lang

%files
%_bindir/*

%if 0
%files utils
%helperdir/*
%if_enabled pty_helper
%exclude %helperdir/gnome-pty-helper
%endif
%endif

%files -n lib%name -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/MAINTAINERS
%pkgdocdir/NEWS
%pkgdocdir/README
%_libdir/*.so.*
%if_enabled pty_helper
#%dir %helperdir
#%attr(2711,root,utmp) %helperdir/gnome-pty-helper
%exclude %helperdir/gnome-pty-helper
%endif

%files -n lib%name-devel
%pkgdocdir/*.txt
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%_name-%vte_api_ver.pc

%files -n lib%name-devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%changelog
* Wed May 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.2-alt1
- 0.32.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.1-alt1
- 0.32.1

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Wed Nov 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt2
- applied patch proposed in
  http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
  (ALT #26611)

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Mon Aug 29 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Wed Jun 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 2.28.0

* Thu Feb 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.27.90-alt1
- first build for Sisyphus.

