%define ver_major 4.4
%define origname gtkhtml
%def_disable static
%def_disable gtk_doc
%define api_ver 4.0

Name: gtkhtml4
Version: %ver_major.3
Release: alt1

Summary: GtkHTML is a HTML rendering/editing library
License: LGPLv2
Group: Graphical desktop/GNOME
Url: http://projects.gnome.org/evolution/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%origname/%ver_major/%origname-%version.tar.xz

# from configure.in
%define gtk3_ver 3.0.5
%define gnome_icon_ver 2.91.0
%define libsoup_ver 2.33.92
%define enchant_ver 1.1.17
%define cairo_ver 1.10.0

BuildPreReq: gnome-common

BuildPreReq: intltool >= 0.36.3
BuildPreReq: libgtk+3-devel >= %gtk3_ver
BuildPreReq: gnome-icon-theme >= %gnome_icon_ver
BuildPreReq: libsoup-devel >= %libsoup_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libenchant-devel >= %enchant_ver
BuildRequires: libgio-devel libgail3-devel iso-codes-devel
BuildRequires: gsettings-desktop-schemas-devel

%description
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

GtkHTML was originally based on KDE's KHTMLW widget, but is now
developed independently of it. The most important difference between
KHTMLW and GtkHTML, besides being GTK-based, is that GtkHTML is also an
editor. Thanks to the Bonobo editor component that comes with the
library, it's extremely simple to add HTML editing to an existing
application.

%package -n lib%name
Summary: Libraries for GtkHTML
Group: System/Libraries

%description -n lib%name
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains libraries used by GtkHTML.

%package -n lib%name-devel
Provides: lib%name-devel
Summary: Development libraries, header files and utilities for GtkHTML
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains the files necessary to develop applications with GtkHTML.

%package -n lib%name-devel-static
Provides: lib%name-devel-static
Summary: Static libraries for GtkHTML
Group: Development/GNOME and GTK+

%description -n lib%name-devel-static
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains the files necessary to develop applications
statically linked with GtkHTML.

%prep
%setup -q -n %origname-%version

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --program-suffix=-%api_ver

%make_build

%check
%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang %origname-%api_ver

%files -n lib%name -f %origname-%api_ver.lang
%_libdir/*.so.*
%_datadir/%origname-%api_ver
%doc AUTHORS ChangeLog NEWS README TODO

%files -n lib%name-devel
%_bindir/gtkhtml-editor-test-%api_ver
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/%origname/*.a
%endif

%changelog
* Mon Jun 18 2012 Yuri N. Sedunov <aris@altlinux.org> 4.4.3-alt1
- 4.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 4.4.2-alt1
- 4.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt1
- 4.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 4.2.3-alt1
- 4.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 4.2.2-alt1
- 4.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 4.1.92-alt1
- 4.1.92

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 4.1.91-alt1
- 4.1.91

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 4.1.90-alt1
- 4.1.90

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Fri Feb 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.91.6-alt1
- first build for Sisyphus

