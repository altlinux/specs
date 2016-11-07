%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name gnome-desktop
%define ver_major 3.22
%define api_ver 3.0
%define gnome_distributor "%vendor"
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"
%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable installed_tests
%def_enable udev

Name: %{_name}3
Version: %ver_major.2
Release: alt1

Summary: Library with common API for various GNOME 3 modules
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Obsoletes: %_name
Provides: %_name = %version-%release

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: intltool >= 0.40.6
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: libgio-devel >= 2.44.0
BuildPreReq: yelp-tools itstool
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91
BuildRequires: iso-codes-devel
BuildRequires: xkeyboard-config-devel
BuildRequires: libudev-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel}

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
Requires: icon-theme-hicolor
Requires: udev-hwdb

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

%package tests
Summary: Tests for the Gnome 3 desktop library
Group: Development/Other
Requires: lib%name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the Gnome 3 desktop library.


%prep
%setup -n %_name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --with-gnome-distributor=%gnome_distributor \
    %{?_enable_installed_tests:--enable-installed-tests} \
    %{subst_enable udev}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%_name.lang %_name-%api_ver fdl gpl lgpl

%files

%files -n lib%name -f %_name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_libexecdir/gnome-rr-debug
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

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- updated to 3.14_2b563b26 (fixed BGO #740289)

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt2
- fixed reqs

* Fri Nov 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sun Jun 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt2
- fixed pnp.ids path

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt1
- 3.8.0.1

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.1-alt1
- 3.6.0.1

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

