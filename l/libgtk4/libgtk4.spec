%def_disable snapshot

%define _name gtk
%define ver_major 4.14
%define api_ver_major 4
%define api_ver %api_ver_major.0
%define binary_ver 4.0.0
%define _libexecdir %_prefix/libexec

%def_enable x11
%def_disable static
%def_enable man
%def_enable introspection
%def_enable gtk_doc
%def_enable colord
# wayland gdk backend
%def_enable wayland
# broadway (HTML5) gdk backend
%def_enable broadway
%def_enable cloudproviders
# 4.8.0: tracker disabled by default
%def_disable tracker
# enabled by default since 4.13.5
%def_enable vulkan
# media backends
# gstreamer enabled by default
%def_enable gstreamer
# droped in 4.13.7
%def_disable ffmpeg

%def_disable sysprof
%def_enable tests
# fatal: posix_spawn: Resource temporarily unavailable on basalt
%def_disable testsuite
# File box-packing.ltr.nodes does not exist
%def_disable install_tests
%def_disable check

Name: lib%_name%api_ver_major
Version: %ver_major.5
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
Source5: gtk4-icon-cache.filetrigger
Patch: gtk+-2.16.5-alt-stop-spam.patch
# backported from main
Patch10: gtk-4.12.3-alt-printdialog-papersize.patch

%define meson_ver 0.63
%define glib_ver 2.76
%define gi_ver 1.76
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
%define graphene_ver 1.10
%define cloudproviders_ver 0.2.5
%define rsvg_ver 2.52.0
%define vulkan_ver 1.3

Requires: gtk4-update-icon-cache = %EVR
Requires: at-spi2-core
Requires: icon-theme-adwaita
Requires: iso-codes
Requires: librsvg >= %rsvg_ver

%{?_enable_colord:Requires: colord}

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson >= %meson_ver gcc-c++ sassc
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
BuildRequires: docbook-utils zlib-devel
BuildRequires: pkgconfig(libdrm)
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
%{?_enable_tracker:BuildRequires: tracker3-devel}
%{?_enable_vulkan:BuildRequires: /usr/bin/glslc vulkan-devel >= %vulkan_ver}
# for examples
BuildRequires: libcanberra-gtk3-devel libharfbuzz-devel python3-module-pygobject3
%{?_enable_sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}
%{?_enable_tests:BuildRequires: librsvg-devel >= %rsvg_ver}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui icon-theme-hicolor gnome-icon-theme-symbolic}
# since 3.94.0 for media backends
%{?_enable_gstreamer:BuildRequires: pkgconfig(gstreamer-player-1.0)}
%{?_enable_ffmpeg:
BuildRequires: libavfilter-devel libavformat-devel libavdevice-devel
BuildRequires: libavcodec-devel libavutil-devel libswscale-devel libswresample-devel}

%description
GTK is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains X11 part of GTK. It is required for GNOME 3 desktop
and programs.

%package devel
Summary: Development files and tools for GTK%api_ver_major applications
Group: Development/C
Requires: %name = %EVR
Requires: gtk-builder-convert

%description devel
This package contains development files for GTK%api_ver_major. Use this to
build programs that use GTK%api_ver_major.

%package -n gtk4-update-icon-cache
Summary: Icon theme caching utility for GTK
Group: System/Libraries
# last release of gtk-update-icon-cache is 3.24.32
Obsoletes: gtk-update-icon-cache < %version
Provides: gtk-update-icon-cache = %EVR

%description -n gtk4-update-icon-cache
gtk-update-icon-cache creates mmap()able cache files for icon themes.
GTK can use the cache files created by gtk-update-icon-cache to avoid
a lot of system call and disk seek overhead when the application starts.

%package -n gtk4-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %EVR

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
Requires: %name = %EVR

%description -n %name-devel-static
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains the static libraries for GTK%api_ver_major.

%package gir
Summary: GObject introspection data for the GTK+ library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the GTK%api_ver_major library

%package gir-devel
Summary: GObject introspection devel data for the GTK%api_ver_major library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the GTK+ library

This package contains development documentation for GAIL.

%package tests
Summary: Tests for the GTK%api_ver_major packages
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GTK+3 packages.


%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -n %_name-%version
%patch -p1

%build
%ifarch %e2k
%add_optflags -mno-sse4.2
%endif

%meson \
    %{?_enable_x11:-Dx11-backend=true} \
    %{?_enable_wayland:-Dwayland-backend=true} \
    %{?_enable_broadway:-Dbroadway-backend=true} \
    %{?_enable_cloudproviders:-Dcloudproviders=enabled} \
    %{?_enable_tracker:-Dtracker=enabled} \
    %{?_enable_introspection:-Dintrospection=enabled} \
    %{?_enable_gtk_doc:-Ddocumentation=true} \
    %{?_enable_man:-Dman-pages=true} \
    %{?_enable_colord:-Dcolord=enabled} \
    %{?_enable_sysprof:-Dsysprof=enabled} \
    %{?_disable_tests:-Dbuild-tests=false} \
    %{?_disable_testsuite:-Dbuild-testsuite=false} \
    %{?_enable_install_tests:-Dinstall-tests=true} \
    %{?_enable_vulkan:-Dvulkan=enabled} \
    %{?_disable_gstreamer:-Dmedia-gstreamer=disabled} \
    %{?_enable_ffmpeg:-Dmedia-ffmpeg=enabled}
%nil
%meson_build

%install
%meson_install
install -d %buildroot{%_sysconfdir/gtk-%api_ver,%_libdir/gtk-%api_ver/%binary_ver/engines}

# posttransfiletrigger for update icons cache
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/gtk4-icon-cache.filetrigger
# backward compatibility symlink
ln -s gtk4-update-icon-cache %buildroot%_bindir/gtk-update-icon-cache

# The license
ln -sf %_licensedir/LGPL-2.0-or-later COPYING

%find_lang --output=gtk40.lang gtk40 gtk40-properties

bzip2 -9kf NEWS

mkdir %buildroot%_libdir/gtk-%api_ver/modules

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version/examples
cp -r examples/* %buildroot/%_docdir/%name-devel-%version/examples/

%check
%__meson_test

%files -f gtk40.lang
%{?_enable_broadway:%_bindir/gtk4-broadwayd}
%_bindir/gtk4-query-settings
%_bindir/gtk4-launch
%_bindir/gtk4-encode-symbolic-svg
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
%endif

%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%_datadir/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml

%doc --no-dereference COPYING
%doc AUTHORS NEWS.bz2 README.md

%files devel
%_bindir/gtk4-builder-tool
%_bindir/gtk4-path-tool
%_bindir/gtk4-rendernode-tool
%_includedir/gtk-%api_ver/
%_libdir/libgtk-%api_ver_major.so
%_pkgconfigdir/gtk%api_ver_major.pc
%_pkgconfigdir/gtk%api_ver_major-x11.pc
%_pkgconfigdir/gtk%api_ver_major-unix-print.pc
%_pkgconfigdir/gtk%api_ver_major-atspi.pc
%_datadir/gtk-%api_ver/gtk%{api_ver_major}builder.rng
%_datadir/gettext/its/gtk%{api_ver_major}builder.its
%_datadir/gettext/its/gtk%{api_ver_major}builder.loc
%_datadir/gtk-%api_ver/valgrind/
%{?_enable_man:%_man1dir/gtk%{api_ver_major}-builder-tool.1*
%_man1dir/gtk4-path-tool.1*
%_man1dir/gtk4-rendernode-tool.1*}

%if_enabled wayland
%_pkgconfigdir/gtk%api_ver_major-wayland.pc
%endif

%if_enabled broadway
%_pkgconfigdir/gtk%api_ver_major-broadway.pc
%endif

%files -n gtk4-update-icon-cache
%_bindir/gtk4-update-icon-cache
# compatibility symlink
%_bindir/gtk-update-icon-cache
%_man1dir/gtk4-update-icon-cache*
%_rpmlibdir/gtk4-icon-cache.filetrigger

%files -n gtk4-demo
%_desktopdir/org.gtk.Demo4.desktop
%_desktopdir/org.gtk.IconBrowser4.desktop
%_desktopdir/org.gtk.gtk4.NodeEditor.desktop
%_desktopdir/org.gtk.WidgetFactory4.desktop
%_desktopdir/org.gtk.PrintEditor4.desktop
%_bindir/gtk4-demo
%_bindir/gtk4-demo-application
%_bindir/gtk4-widget-factory
%_bindir/gtk4-icon-browser
%_bindir/gtk4-node-editor
%_bindir/gtk4-print-editor
%_datadir/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%_iconsdir/hicolor/scalable/apps/org.gtk.Demo4.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.IconBrowser4.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.PrintEditor4*.svg
%_iconsdir/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.IconBrowser4-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg
%_iconsdir/hicolor/*/*/org.gtk.gtk4.NodeEditor*.svg

%_datadir/metainfo/org.gtk.Demo4.appdata.xml
%_datadir/metainfo/org.gtk.IconBrowser4.appdata.xml
%_datadir/metainfo/org.gtk.PrintEditor4.appdata.xml
%_datadir/metainfo/org.gtk.WidgetFactory4.appdata.xml
%_datadir/metainfo/org.gtk.gtk4.NodeEditor.appdata.xml

%if_enabled man
%_man1dir/gtk4-demo.1.*
%_man1dir/gtk4-demo-application.1.*
%_man1dir/gtk4-icon-browser.1.*
%_man1dir/gtk4-widget-factory.1.*
%_man1dir/gtk4-node-editor.1*
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
* Fri Aug 16 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.5-alt1
- 4.14.5

* Fri May 03 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.4-alt1
- 4.14.4

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.3-alt1
- 4.14.3

* Wed Apr 03 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.2-alt1
- 4.14.2

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.1-alt1.1
- E2K: disabled sse-4.2

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.1-alt1
- 4.14.1

* Tue Mar 12 2024 Yuri N. Sedunov <aris@altlinux.org> 4.14.0-alt1
- 4.14.0

* Thu Jan 18 2024 Yuri N. Sedunov <aris@altlinux.org> 4.12.5-alt1
- 4.12.5

* Sat Nov 18 2023 Yuri N. Sedunov <aris@altlinux.org> 4.12.4-alt1
- 4.12.4

* Thu Sep 28 2023 Yuri N. Sedunov <aris@altlinux.org> 4.12.3-alt1
- 4.12.3

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 4.12.2-alt1
- 4.12.2

* Thu Sep 07 2023 Yuri N. Sedunov <aris@altlinux.org> 4.12.1-alt1
- 4.12.1

* Thu Sep 07 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.5-alt1.1
- disabled experimental ffmpeg media backend incompatible with 6.0
  (https://gitlab.gnome.org/GNOME/gtk/-/issues/5581)

* Sat Aug 05 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.5-alt1
- 4.10.5

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.4-alt1
- 4.10.4

* Tue May 02 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.3-alt2
- updated to 4.10.3-10-gd2490c30b1 (fixed ALT #45946)

* Sat Apr 22 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.3-alt1
- 4.10.3

* Tue Mar 14 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.1-alt1
- 4.10.1

* Tue Mar 07 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.0-alt2
- fixed by upstream https://gitlab.gnome.org/GNOME/gtk/-/issues/5644

* Sun Mar 05 2023 Yuri N. Sedunov <aris@altlinux.org> 4.10.0-alt1
- 4.10.0

* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.3-alt1
- 4.8.3

* Mon Oct 24 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.2-alt1
- 4.8.2

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.1-alt1
- 4.8.1

* Tue Sep 06 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.0-alt1
- 4.8.0

* Wed Aug 17 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.7-alt1
- 4.6.7

* Sun Jul 03 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.6-alt1
- 4.6.6

* Tue May 31 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.5-alt1
- 4.6.5

* Fri May 13 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.4-alt1
- 4.6.4

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.3-alt1
- 4.6.3

* Mon Mar 28 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.2-alt2
- new gtk4-update-icon-cache subpackage obsoletes/provides
  gtk-update-icon-cache from libgtk+3

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.2-alt1
- 4.6.2

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

