%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name gnome-desktop
%define ver_major 43
%define beta %nil
%define api_ver 3.0
%define api_ver4 4.0
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"

%def_enable gtk4
%def_enable legacy_library
%def_enable gtk_doc
%def_enable introspection
%def_enable installed_tests
%def_enable udev
%def_disable check
# seccomp isn't currently supported on all the Linux architectures
%def_enable libseccomp

Name: %{_name}3
Version: %ver_major.2
Release: alt1%beta

Summary: Library with common API for various GNOME 3 modules
License: GPL-2.0 and LGPL-2.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version.tar
%endif
# add e2k to list of libseccomp incompatible cpus
Patch: gnome-desktop-40.3-alt-e2k.patch

Obsoletes: %_name
Provides: %_name = %version-%release

%define glib_ver 2.54.0
%define gdk_pixbuf_ver 2.36.5
%define gtk3_ver 3.3.6
%define gtk4_ver 4.4.0
%define gsds_ver 3.28.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgdk-pixbuf-devel >= %gdk_pixbuf_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: iso-codes-devel
BuildRequires: xkeyboard-config-devel libxkbcommon-devel
BuildRequires: libXrandr-devel >= 1.3 libXext-devel >= 1.1
BuildRequires: libudev-devel pkgconfig(systemd)
%{?_enable_legacy_library:BuildRequires: libgtk+3-devel >= %gtk3_ver}
%{?_enable_gtk4:BuildRequires: libgtk4-devel >= %gtk4_ver}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_libseccomp:BuildRequires: libseccomp-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel %{?_enable_legacy_library:libgtk+3-gir-devel}
BuildRequires: %{?_enable_gtk4:libgtk4-gir-devel} gsettings-desktop-schemas-gir-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software. The

GNOME Desktop provides the core libraries for the gnome desktop.

%package -n lib%name
Summary: GNOME desktop core libraries
Group: Graphical desktop/GNOME
License: LGPL-2.0
Requires: icon-theme-hicolor
Requires: udev-hwdb
Requires: bubblewrap
Requires: pciids usbids

%description -n lib%name
Gnome 3 desktop libraries.

%package -n lib%name-devel
Summary: GNOME 3 desktop development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
License: LGPL-2.0 and FDL-1.1

%description -n lib%name-devel
Gnome 3 desktop libraries and header files for creating GNOME applications.

%package -n lib%name-devel-doc
Summary: GNOME 3 desktop development documentation
Group: Development/Documentation
Conflicts: lib%name-devel < %version
License: LGPL-2.0 and FDL-1.1
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for Gnome 3 desktop library.

%if_enabled static
%package -n lib%name-devel-static
Summary: GNOME 3 desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
License: LGPL-2.0

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
%setup -n %_name-%version%beta
%ifarch %e2k
%patch -p1 -b .e2k
%endif

%build
%meson \
    %{?_disable_legacy_library:-Dlegacy_library=false} \
    %{?_disable_gtk4:-Dgtk4=false} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_installed_tests:-Dinstalled_tests=true} \
    %{?_enable_udev:-Dudev=enabled}
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%_name.lang %_name-%api_ver gpl lgpl fdl

%check
%__meson_test

%files

%files -n lib%name -f %_name.lang
%{?_enable_legacy_library:%_libdir/lib%_name-3.so.*}
%{?_enable_gtk4:
%_libdir/lib%_name-4.so.*
%_libdir/libgnome-bg-4.so.*
%_libdir/libgnome-rr-4.so.*}
%doc AUTHORS NEWS README*

%files -n lib%name-devel
%{?_enable_legacy_library:
%_libexecdir/%_name-debug/
%_includedir/%_name-%api_ver
%_libdir/lib%_name-3.so
%_pkgconfigdir/%_name-%api_ver.pc}
%{?_enable_gtk4:
%_includedir/%_name-4.0
%_libdir/libgnome-bg-4.so
%_libdir/lib%_name-4.so
%_libdir/libgnome-rr-4.so
#%_datadir/gnome/gnome-version.xml
%_pkgconfigdir/gnome-bg-4.pc
%_pkgconfigdir/%_name-4.pc
%_pkgconfigdir/gnome-rr-4.pc}

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files -n lib%name-gir
%{?_enable_legacy_library:%_typelibdir/GnomeDesktop-%api_ver.typelib}
%{?_enable_gtk4:
%_typelibdir/GnomeBG-4.0.typelib
%_typelibdir/GnomeDesktop-4.0.typelib
%_typelibdir/GnomeRR-4.0.typelib}

%files -n lib%name-gir-devel
%{?_enable_legacy_library:%_girdir/GnomeDesktop-%api_ver.gir}
%{?_enable_gtk4:
%_girdir/GnomeBG-4.0.gir
%_girdir/GnomeDesktop-4.0.gir
%_girdir/GnomeRR-4.0.gir}
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Wed Feb 15 2023 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Sat Jan 21 2023 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt1
- 43

* Mon Aug 08 2022 Yuri N. Sedunov <aris@altlinux.org> 42.4-alt1
- 42.4

* Fri Jul 15 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Thu Jun 02 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Mar 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Wed Nov 03 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Wed Nov 03 2021 Yuri N. Sedunov <aris@altlinux.org> 40.5-alt1
- 40.5

* Sun Sep 12 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4
- E2K: updated seccomp-related patch (mike@)

* Thu Jul 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Wed Jun 09 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Feb 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Wed Nov 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Wed Jul 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Mon Jun 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3.1-alt1
- 3.36.3.1

* Wed Apr 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Wed Apr 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt2
- mike@: updated e2k patch
- improved "gtk_doc" knob

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Wed Mar 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Wed Jan 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Tue Dec 03 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1.2-alt2
- introduced libceccomp knob
- added e2k to list of libseccomp incompatible cpus

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1.2-alt1
- 3.32.1.2 (fixed CVE-2019-1146)

* Tue Apr 23 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1.1-alt1
- 3.32.1.1 (fixed CVE-2019-11459)

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Feb 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2.1-alt1
- 3.30.2.1

* Sat Oct 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Wed Apr 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- lib%%name requires bubblewrap

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sat Sep 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- updated to 3.26.0-1-g22b89aa (fixed BGO #787072)

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Sep 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Sun Apr 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

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

