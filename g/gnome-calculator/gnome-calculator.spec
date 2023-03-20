%def_disable snapshot
%define ver_major 44
%define beta %nil
%define api_ver 2
# GTK interface library
%define gci_api_ver 1
%define xdg_name org.gnome.Calculator
%define _libexecdir %_prefix/libexec

%def_enable check

Name: gnome-calculator
Version: %ver_major.0
Release: alt1%beta

Summary: GTK+3 based desktop calculator
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://wiki.gnome.org/Apps/Calculator

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

Obsoletes: gcalctool <= 6.6.2
Provides: gcalctool = 6.6.2
Requires: libgcalc = %EVR
Requires: libgci = %EVR

%define glib_ver 2.40
%define gtk4_ver 4.5.0
%define adwaita_ver 1.2
%define gee_ver 0.20.0
%define soup_api_ver 3.0
%define soup_ver 3.0
%define gtksource_ver 5.3.0

BuildRequires(pre): rpm-macros-meson rpm-build-licenses rpm-build-gnome
BuildRequires(pre): rpm-build-gir rpm-build-vala
BuildRequires: meson vala-tools valadoc
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgee0.8-devel >= %gee_ver libxml2-devel
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: libmpfr-devel libgtksourceview5-devel >= %gtksource_ver
BuildRequires: pkgconfig(libsoup-%soup_api_ver) >= %soup_ver libmpc-devel
BuildRequires: gobject-introspection-devel libgtk4-gir-devel libgee0.8-gir-devel
BuildRequires: gir(Soup) = %soup_api_ver

%description
This package provides gcalctool, the calculator application that was
previously in the OpenWindows Deskset of the Solaris 8 operating system.

It incorporates a multiple precision arithmetic packages based on the work
of Professor Richard Brent.

A single graphics driver for GTK included with this package.


%package -n libgcalc
Summary: GNOME Calculator Library
Group: System/Libraries

%description -n libgcalc
This package contains shared GNOME Calculator library.

%package -n libgcalc-devel
Summary: Development files for libgcalc
Group: Development/C
Requires: libgcalc = %EVR

%description -n libgcalc-devel
This package development files for GNOME Calculator library.

%package -n libgcalc-gir
Summary: GObject introspection data for the GNOME Calculator library.
Group: System/Libraries
Requires: libgcalc = %EVR

%description -n libgcalc-gir
GObject introspection data for the GNOME Calculator library.

%package -n libgcalc-gir-devel
Summary: GObject introspection devel data for the GNOME Calculator library.
Group: Development/Other
BuildArch: noarch
Requires: libgcalc-devel = %EVR
Requires: libgcalc-gir = %EVR

%description -n libgcalc-gir-devel
GObject introspection devel data for the GNOME Calculator library.

%package -n libgcalc-devel-doc
Summary: Development documentation for the GNOME Calculator library
Group: Development/Documentation
Conflicts: libgcalc < %EVR
BuildArch: noarch

%description -n libgcalc-devel-doc
This package provides Development documentation for the GNOME Calculator library.

%package -n libgci
Summary: GNOME Calculator GTK Interface Library
Group: System/Libraries
Requires: libgcalc = %EVR

%description -n libgci
This package contains shared GNOME Calculator GTK interface library.

%package -n libgci-devel
Summary: Development files for libgci
Group: Development/C
Requires: libgci = %EVR

%description -n libgci-devel
This package development files for GNOME Calculator GTK interface library.

%package -n libgci-gir
Summary: GObject introspection data for the GNOME Calculator GTK interface library
Group: System/Libraries
Requires: libgci = %EVR

%description -n libgci-gir
GObject introspection data for the GNOME Calculator GTK interface library.

%package -n libgci-gir-devel
Summary: GObject introspection devel data for the GNOME Calculator GTK interface library.
Group: Development/Other
BuildArch: noarch
Requires: libgci-devel = %EVR
Requires: libgci-gir = %EVR

%description -n libgci-gir-devel
GObject introspection devel data for the GNOME Calculator GTK interface library.

%package -n libgci-devel-doc
Summary: Development documentation for the GNOME Calculator GTK interface library
Group: Development/Documentation
Conflicts: libgci < %EVR
BuildArch: noarch

%description -n libgci-devel-doc
This package provides Development documentation for the GNOME Calculator
GTK interface library.


%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-search-provider
%_datadir/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_desktopdir/%xdg_name.desktop
%_man1dir/%name.1.*
%_man1dir/gcalccmd.1.*
%config %_datadir/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README*

%files -n libgcalc
%_libdir/libgcalc-%api_ver.so.*

%files -n libgcalc-devel
%_includedir/gcalc-%api_ver/gcalc/
%_libdir/libgcalc-%api_ver.so
%_pkgconfigdir/gcalc-%api_ver.pc
%_vapidir/gcalc-%api_ver.deps
%_vapidir/gcalc-%api_ver.vapi

%files -n libgcalc-gir
%_typelibdir/GCalc-%api_ver.typelib

%files -n libgcalc-gir-devel
%_girdir/GCalc-%api_ver.gir

%files -n libgcalc-devel-doc
%_datadir/devhelp/books/GCalc-%api_ver/

%files -n libgci
%_libdir/libgci-%gci_api_ver.so.*

%files -n libgci-devel
%_includedir/gci-%api_ver
%_libdir/libgci-%gci_api_ver.so
%_pkgconfigdir/gci-%gci_api_ver.pc
%_vapidir/gci-%gci_api_ver.deps
%_vapidir/gci-%gci_api_ver.vapi

%files -n libgci-gir
%_typelibdir/GCi-%gci_api_ver.typelib

%files -n libgci-gir-devel
%_girdir/GCi-%gci_api_ver.gir

%files -n libgci-devel-doc
%_datadir/devhelp/books/GCi-%gci_api_ver/

%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0.1-alt1
- 43.0.1

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0 (ported to GTK4)

* Mon Dec 06 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2
- enabled %%check

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0
- new libgci subpackages

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0
- new libgcalc* subpackages

* Wed Jun 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- rebuilt against libmpfr.so.6 (ALT #34582)

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt2
- use git snapshot with some *.ui that were missed in tarball

* Mon Aug 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Thu Apr 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Feb 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- gcalctool -> gnome-calculator

