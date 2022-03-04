%def_disable snapshot

%define _name gtk
%define ver_major 4.6
%define api_ver_major 4
%define api_ver %api_ver_major.0
%define binary_ver 4.0.0
%define _libexecdir %_prefix/libexec

%def_enable x11
%def_disable static
%def_enable man
%def_enable gtk_doc
%def_enable introspection
%def_enable colord
# wayland gdk backend
%def_enable wayland
# broadway (HTML5) gdk backend
%def_enable broadway
%def_enable cloudproviders
%def_enable tracker3
%def_enable vulkan
# media backends
# gstreamer enabled by default
%def_enable gstreamer
%def_enable ffmpeg

%def_disable sysprof
%def_enable tests
# File box-packing.ltr.nodes does not exist
%def_disable install_tests
%def_disable check

Name: lib%_name%api_ver_major
Version: %ver_major.1
Release: alt1

Summary: The GIMP ToolKit (GTK)
Group: System/Libraries
License: LGPL-2.0-or-later
Url: http://www.gtk.org

%if_enabled snapshot
Vcs: https://gitlab.gnome.org/GNOME/gtk.git
Source: %_name-%version.tar
%else
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%endif
Patch: gtk+-2.16.5-alt-stop-spam.patch

%define glib_ver 2.66.0
%define gi_ver 1.41.0
%define cairo_ver 1.14.0
%define pango_ver 1.50.0
%define atk_ver 2.15.1
%define pixbuf_ver 2.30.0
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.32.1
%define colord_ver 0.1.9
%define cups_ver 1.6
%define wayland_ver 1.17.0
%define wayland_protocols_ver 1.21
%define xkbcommon_ver 0.2.0
%define epoxy_ver 1.4
%define graphene_ver 1.9.1
%define cloudproviders_ver 0.2.5
%define rsvg_ver 2.46.0

Requires: gtk-update-icon-cache
Requires: icon-theme-adwaita
Requires: iso-codes
Requires: librsvg >= %rsvg_ver
# ALT #32028
Requires: gtk+3-themes-incompatible
%{?_enable_colord:Requires: colord}

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson gcc-c++ sassc
BuildRequires: glib2-devel >= %glib_ver libgio-devel
BuildRequires: libcairo-devel >= %cairo_ver
BuildRequires: libcairo-gobject-devel >= %cairo_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libatk-devel >= %atk_ver
BuildRequires: libgdk-pixbuf-devel >= %pixbuf_ver
BuildRequires: libtiff-devel libjpeg-devel
BuildRequires: fontconfig-devel >= %fontconfig_ver
BuildRequires: libcups-devel >= %cups_ver
BuildRequires: libepoxy-devel >= %epoxy_ver
BuildRequires: libgraphene-devel >= %graphene_ver
BuildRequires: iso-codes-devel
BuildRequires: libfribidi-devel
BuildRequires: gtk-update-icon-cache docbook-utils zlib-devel

%if_enabled x11
BuildRequires: libXdamage-devel libX11-devel libXcursor-devel
BuildRequires: libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libXrender-devel libXt-devel
%endif
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: python3-module-docutils}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver libpango-gir-devel libatk-gir-devel >= %atk_ver libgdk-pixbuf-gir-devel libgraphene-gir-devel}
%{?_enable_colord:BuildRequires: libcolord-devel >= %colord_ver}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= %wayland_ver libwayland-cursor-devel libEGL-devel libwayland-egl-devel libxkbcommon-devel >= %xkbcommon_ver wayland-protocols >= %wayland_protocols_ver}
%{?_enable_cloudproviders:BuildRequires: libcloudproviders-devel >= %cloudproviders_ver}
%{?_enable_tracker3:BuildRequires: tracker3-devel}
%{?_enable_vulkan:BuildRequires: vulkan-devel}
# for examples
BuildRequires: libcanberra-gtk3-devel libharfbuzz-devel python3-module-pygobject3
%{?_enable_sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}
%{?_enable_tests:BuildRequires: librsvg-devel >= %rsvg_ver}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui icon-theme-hicolor gnome-icon-theme-symbolic}
# since 3.94.0 for media backends
%{?_enable_gstreamer:BuildRequires: pkgconfig(gstreamer-player-1.0)}
%{?_enable_ffmpeg:
BuildRequires: libavfilter-devel libavformat-devel
BuildRequires: libavcodec-devel libavutil-devel libswscale-devel}

%description
GTK is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains X11 part of GTK. It is required for GNOME 3 desktop
and programs.

%package devel
Summary: Development files and tools for GTK%api_ver_major applications
Group: Development/C
Requires: %name = %version-%release
Requires: gtk-builder-convert

%description devel
This package contains development files for GTK%api_ver_major. Use this to
build programs that use GTK%api_ver_major.

%package -n gtk4-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gtk4-demo
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains a program, along with its source code, that
demonstrates GTK%api_ver_major variety of all its widgets.

%package -n %name-devel-doc
Summary: Development documentation for GTK%api_ver_major
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description -n %name-devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains documentation needed for developing GTK+ applications.

%package -n %name-devel-doc-examples
Summary: Examples for developing applications which will use GTK%api_ver_major
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description -n %name-devel-doc-examples
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains sources for example programs.

%package -n %name-devel-static
Summary: Static libraries for GTK+ (GIMP ToolKit) applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n %name-devel-static
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains the static libraries for GTK%api_ver_major.

%package gir
Summary: GObject introspection data for the GTK+ library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GTK%api_ver_major library

%package gir-devel
Summary: GObject introspection devel data for the GTK%api_ver_major library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GTK+ library

This package contains development documentation for GAIL.

%package tests
Summary: Tests for the GTK%api_ver_major packages
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GTK+3 packages.


%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -n %_name-%version
%patch -p1
sed -i "s|\('rst2man\)|\1.py|" docs/reference/gtk/meson.build

%build
%meson \
    %{?_enable_x11:-Dx11-backend=true} \
    %{?_enable_wayland:-Dwayland-backend=true} \
    %{?_enable_broadway:-Dbroadway-backend=true} \
    %{?_enable_cloudproviders:-Dcloudproviders=enabled} \
    %{?_enable_tracker:-Dtracker=enabled} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_man:-Dman-pages=true} \
    %{?_enable_colord:-Dcolord=enabled} \
    %{?_enable_sysprof:-Dsysprof=enabled} \
    %{?_disable_tests:-Dbuild-tests=false} \
    %{?_enable_install_tests:-Dinstall-tests=true} \
    %{?_disable_vulkan:-Dvulkan=disabled} \
    %{?_disable_gstreamer:-Dmedia-gstreamer=disabled} \
    %{?_enable_ffmpeg:-Dmedia-ffmpeg=enabled}
%nil
%meson_build

%install
%meson_install
install -d %buildroot{%_sysconfdir/gtk-%api_ver,%_libdir/gtk-%api_ver/%binary_ver/engines}

# The license
ln -sf %_licensedir/LGPL-2.0-or-later COPYING

%find_lang --output=gtk40.lang gtk40 gtk40-properties

bzip2 -9kf NEWS

mkdir %buildroot%_libdir/gtk-%api_ver/modules

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version/examples
cp -r examples/* %buildroot/%_docdir/%name-devel-%version/examples/

%check
%meson_test

%files -f gtk40.lang
%{?_enable_broadway:%_bindir/gtk4-broadwayd}
%_bindir/gtk4-query-settings
%_bindir/gtk4-launch
%_bindir/gtk4-encode-symbolic-svg
%_bindir/gtk4-update-icon-cache
%_libdir/libgtk-4.so.*
%dir %_libdir/gtk-%api_ver/modules
%dir %fulllibpath
%dir %fulllibpath/engines
%dir %fulllibpath/printbackends
%dir %fulllibpath/media
%fulllibpath/printbackends/libprintbackend-*.so
%{?_enable_gstreamer:%fulllibpath/media/libmedia-gstreamer.so}
%{?_enable_ffmpeg:%fulllibpath/media/libmedia-ffmpeg.so}
%dir %_datadir/gtk-%api_ver/
%_datadir/gtk-%api_ver/emoji/
%dir %_sysconfdir/gtk-%api_ver
%if_enabled man
%{?_enable_broadway:%_man1dir/gtk4-broadwayd.1.*}
%_man1dir/gtk4-query-settings.1.*
%_man1dir/gtk4-launch.*
%_man1dir/gtk4-encode-symbolic-svg.1.*
%_man1dir/gtk4-update-icon-cache.1.*
%endif

%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml

%doc --no-dereference COPYING
%doc AUTHORS NEWS.bz2 README.md

%files devel
%_bindir/gtk4-builder-tool
%_includedir/gtk-%api_ver/
%_libdir/libgtk-%api_ver_major.so
%_pkgconfigdir/gtk%api_ver_major.pc
%_pkgconfigdir/gtk%api_ver_major-x11.pc
%_pkgconfigdir/gtk%api_ver_major-unix-print.pc
%_datadir/gtk-%api_ver/gtk%{api_ver_major}builder.rng
%_datadir/gettext/its/gtk%{api_ver_major}builder.its
%_datadir/gettext/its/gtk%{api_ver_major}builder.loc
%_datadir/gtk-%api_ver/valgrind/
%{?_enable_man:%_man1dir/gtk%{api_ver_major}-builder-tool.1*}

%if_enabled wayland
%_pkgconfigdir/gtk%api_ver_major-wayland.pc
%endif

%if_enabled broadway
%_pkgconfigdir/gtk%api_ver_major-broadway.pc
%endif

%files -n gtk4-demo
%_desktopdir/org.gtk.Demo4.desktop
%_desktopdir/org.gtk.IconBrowser4.desktop
%_desktopdir/org.gtk.WidgetFactory4.desktop
%_desktopdir/org.gtk.PrintEditor4.desktop
%_bindir/gtk4-demo
%_bindir/gtk4-demo-application
%_bindir/gtk4-widget-factory
%_bindir/gtk4-icon-browser
%_bindir/gtk4-print-editor
%_datadir/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%_iconsdir/hicolor/scalable/apps/org.gtk.Demo4.svg
#%_iconsdir/hicolor/scalable/apps/org.gtk.gtk4.NodeEditor*.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.IconBrowser4.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.PrintEditor4*.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg
#%_iconsdir/hicolor/symbolic/apps/org.gtk.gtk4.NodeEditor-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.IconBrowser4-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg

%_datadir/metainfo/org.gtk.Demo4.appdata.xml
%_datadir/metainfo/org.gtk.IconBrowser4.appdata.xml
%_datadir/metainfo/org.gtk.PrintEditor4.appdata.xml
%_datadir/metainfo/org.gtk.WidgetFactory4.appdata.xml

%if_enabled man
%_man1dir/gtk4-demo.1.*
%_man1dir/gtk4-demo-application.1.*
%_man1dir/gtk4-icon-browser.1.*
%_man1dir/gtk4-widget-factory.1.*
%endif

%if_enabled gtk_doc
%files devel-doc
#%_datadir/gtk-doc/html/*
%_datadir/doc/gdk4/
%_datadir/doc/gdk4-wayland/
%_datadir/doc/gdk4-x11/
%_datadir/doc/gsk4/
%_datadir/doc/gtk4/
%endif

%files devel-doc-examples
%doc %_docdir/%name-devel-%version/examples

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%fulllibpath/*/*.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%if_enabled install_tests
%files tests
%_libexecdir/installed-tests/gtk-%api_ver/
%_datadir/installed-tests/gtk-%api_ver/
%endif


%changelog
* Fri Mar 04 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.1-alt1
- 4.6.1

* Sun Feb 27 2022 Yuri N. Sedunov <aris@altlinux.org> 4.4.2-alt1
- 4.4.2

* Mon Nov 22 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt2
- updated to 4.4.1-14-gb3840c6a0d

* Mon Nov 01 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt1
- 4.4.1

* Mon Nov 01 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1.1
- updated BR for "gtk_doc"

* Mon Aug 23 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Tue May 04 2021 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Thu Apr 08 2021 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 4.1.2-alt1
- 4.1.2-5-g3daad8fe87

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 4.1.1-alt1
- 4.1.1

* Sun Jan 31 2021 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Tue Jan 19 2021 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Sat Jan 09 2021 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Wed Dec 16 2020 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Dec 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.99.5-alt1
- 3.99.5

* Thu Nov 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.99.4-alt1
- 3.99.4

* Thu Sep 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.99.1-alt1
- 3.99.1

* Fri Jul 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.99.0-alt1
- 3.99.0

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.98.4-alt1
- 3.98.4

* Tue Apr 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.98.3-alt1
- 3.98.3

* Wed Apr 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.98.2-alt1
- 3.98.2

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.98.1-alt1
- 3.98.1

* Tue Feb 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.98.0-alt1
- 3.98.0

* Tue May 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.96.0-alt1
- 3.96.0

* Tue Jun 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.94.0-alt1
- 3.94.0

* Wed Dec 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.93.0-alt1
- 3.93.0

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.92.1-alt1
- 3.92.1

* Fri Aug 25 2017 Yuri N. Sedunov <aris@altlinux.org> 3.91.2-alt1
- 3.91.2

* Thu Jun 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.90.0-alt2
- rebuilt for new vulkan release (ALT #33536)

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.90.0-alt1
- 3.90.0

* Tue Jan 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.89.3-alt1
- 3.89.3

* Wed Dec 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.2-alt1.1
- rebuilt with vulkan support

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.2-alt1
- 3.89.2

* Tue Nov 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.1-alt1
- first build for Sisyphus

