%define _libexecdir %_prefix/libexec
%define ver_major 2.0
%define api_ver 3.0
%define gnome_distributor "%vendor"
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"
%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: cinnamon-desktop
Version: %ver_major.4
Release: alt1

Summary: Library with common API for various Cinnamon modules
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-desktop
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

Requires: lib%name = %version-%release
Requires: icon-theme-hicolor
# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: glib2-devel >= 2.35.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: yelp-tools itstool
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel libXrandr-devel libXext-devel xkeyboard-config-devel libxkbfile-devel
BuildRequires: hwdatabase >= 0.3.31-alt1
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel}

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience. The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell. The emphasis is
put on making users feel at home and providing them with an easy to use and
comfortable desktop experience. The Cinnamon Desktop provides the core libraries
for the Cinnamon desktop.

%package -n lib%name
Summary: Cinnamon desktop core libraries
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n lib%name
Cinnamon desktop libraries.

%package -n lib%name-devel
Summary: Cinnamon desktop development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
License: %lgpl2plus, %fdl

%description -n lib%name-devel
Cinnamon desktop libraries and header files for creating GNOME applications.

%if_enabled static
%package -n lib%name-devel-static
Summary: Cinnamon desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
License: %lgpl2plus

%description -n lib%name-devel-static
Cinnamon desktop static libraries for creating Cinnamon applications.
%endif

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


%prep
%setup -q -n %name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --with-gnome-distributor=%gnome_distributor \
    --with-pnp-ids-path=%_datadir/misc/pnp.ids

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name fdl gpl lgpl

%files

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%_datadir/glib-2.0/schemas/org.cinnamon.*.xml
%doc AUTHORS README

%files -n lib%name-devel
%_libexecdir/cinnamon-rr-debug
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

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
* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt3
- rebuild for GNOME-3.10

* Mon Sep 16 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- git20130905

* Tue Aug 27 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- Initial build
