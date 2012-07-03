%define _name gnome-desktop
%define ver_major 3.4
%define api_ver 3.0
%define gnome_distributor "%vendor"
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"
%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: %{_name}3
Version: %ver_major.2
Release: alt1

Summary: Library with common API for various GNOME 3 modules
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
Source1: gnome-about.png

Obsoletes: %_name
Provides: %_name = %version-%release

Requires: lib%name = %version-%release
Requires: icon-theme-hicolor
# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.0.1
BuildPreReq: glib2-devel >= 2.28.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: gnome-doc-utils librarian-devel
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.0.0
BuildRequires: libSM-devel libXrandr-devel libXext-devel
BuildRequires: hwdatabase >= 0.3.31-alt1
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software. The

GNOME Desktop provides the core libraries for the gnome desktop.

%package -n lib%name
Summary: GNOME desktop core libraries
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n lib%name
Gnome 3 desktop libraries.

%package -n lib%name-devel
Summary: GNOME 3 desktop development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
License: %lgpl2plus, %fdl

%description -n lib%name-devel
Gnome 3 desktop libraries and header files for creating GNOME applications.

%package -n lib%name-devel-doc
Summary: GNOME 3 desktop development documentation
Group: Development/Documentation
Conflicts: lib%name-devel < %version
License: %lgpl2plus, %fdl
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for Gnome 3 desktop library.

%if_enabled static
%package -n lib%name-devel-static
Summary: GNOME 3 desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
License: %lgpl2plus

%description -n lib%name-devel-static
Gnome 3 desktop static libraries for creating GNOME applications.
%endif

%package -n lib%name-gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %_name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %_name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %_name library


%prep
%setup -q -n %_name-%version
[ ! -d m4 ] && mkdir m4

%build
gnome-doc-prepare -f
%autoreconf
%configure \
    %{subst_enable static} \
    --disable-scrollkeeper \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --with-gnome-distributor=%gnome_distributor \
    --with-pnp-ids-path=%_datadir/misc

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%_name.lang %_name-%api_ver fdl gpl lgpl

%files

%files -n lib%name -f %_name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_datadir/gnome/gnome-version.xml
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif


%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Oct 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=660482

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt2
- add empty package gnome-desktop3 with Provides/Obsoletes gnome-desktop
- update find_lang

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- requires hwdatabase with pnp.ids, not pci.ids (shaba@)

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Dec 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.3-alt1
- first build for Sisyphus

