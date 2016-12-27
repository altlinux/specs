%def_disable snapshot

%define _name gtk+
%define ver_major 3.89
%define api_ver 4.0
%define binary_ver 4.0.0
%define _libexecdir %_prefix/libexec

%def_enable xkb
%def_disable static
%def_disable gtk_doc
%def_enable man
%def_enable introspection
%def_enable colord
# wayland gdk backend
%def_enable wayland
# broadway (HTML5) gdk backend
%def_enable broadway
%def_enable cloudprint
%def_enable vulkan
%def_enable installed_tests

Name: libgtk+4
Version: %ver_major.2
Release: alt1.1

Summary: The GIMP ToolKit (GTK+)
Group: System/Libraries
License: %lgpl2plus
Url: http://www.gtk.org

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%endif
Patch: gtk+-2.16.5-alt-stop-spam.patch

%define glib_ver 2.50.2
%define gi_ver 1.41.0
%define cairo_ver 1.14.0
%define pango_ver 1.38.0
%define atk_ver 2.15.1
%define atspi_ver 2.8.1
%define pixbuf_ver 2.30.0
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.20
%define colord_ver 0.1.9
%define cups_ver 1.6
%define wayland_ver 1.10.0
%define wayland_protocols_ver 1.7
%define epoxy_ver 1.0
%define graphene_ver 1.5.1

Provides: libgtk3-engine-adwaita = %version-%release
Obsoletes: libgtk3-engine-adwaita < 3.13.0

Requires: gtk-update-icon-cache
Requires: icon-theme-adwaita
# ALT #32028
Requires: gtk+3-themes-incompatible
%{?_enable_colord:Requires: colord}

BuildPreReq: rpm-build-licenses rpm-build-gnome autoconf-archive
BuildPreReq: glib2-devel >= %glib_ver libgio-devel
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libcairo-gobject-devel >= %cairo_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libatk-devel >= %atk_ver
BuildPreReq: at-spi2-atk-devel >= %atspi_ver
BuildPreReq: libgdk-pixbuf-devel >= %pixbuf_ver
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
BuildPreReq: libcups-devel >= %cups_ver
BuildPreReq: libepoxy-devel >= %epoxy_ver
BuildPreReq: libgraphene-devel >= %graphene_ver
BuildRequires: gtk-update-icon-cache docbook-utils zlib-devel

BuildRequires: libXdamage-devel libXcomposite-devel libX11-devel libXcursor-devel
BuildRequires: libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libXrender-devel libXt-devel

%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver libpango-gir-devel libatk-gir-devel >= %atk_ver libgdk-pixbuf-gir-devel libgraphene-gir-devel}
%{?_enable_colord:BuildRequires: libcolord-devel >= %colord_ver}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= %wayland_ver libwayland-cursor-devel libEGL-devel libwayland-egl-devel libxkbcommon-devel wayland-protocols >= %wayland_protocols_ver}
%{?_enable_cloudprint:BuildRequires: librest-devel libjson-glib-devel}
%{?_enable_vulkan:BuildRequires: vulkan-devel}
# for examples
BuildRequires: libcanberra-gtk3-devel libharfbuzz-devel
# for check
BuildRequires: /proc dbus-tools-gui icon-theme-hicolor gnome-icon-theme-symbolic

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains X11 part of GTK+. It is required for GNOME 3 desktop
and programs.

%package devel
Summary: Development files and tools for GTK+ applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: gtk-builder-convert

%description devel
This package contains development files for GTK+, X11 version. Use this to
build programs that use GTK+.

%package -n gtk4-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gtk4-demo
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains a program, along with its source code, that
demonstrates GTK+ variety of all its widgets.

%package -n %name-devel-doc
Summary: Development documentation for GTK+
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description -n %name-devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains documentation needed for developing GTK+ applications.

%package -n %name-devel-doc-examples
Summary: Examples for developing applications which will use GTK+
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
This package contains the static libraries for GTK+.

%package gir
Summary: GObject introspection data for the GTK+ library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GTK+ library

%package gir-devel
Summary: GObject introspection devel data for the GTK+ library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GTK+ library

This package contains development documentation for GAIL.

%package tests
Summary: Tests for the GTK+3 packages
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GTK+3 packages.


%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -n %_name-%version
%patch -p1

%{?_enable_snapshot:touch README INSTALL}

%build
%{?_disable_static:export lt_cv_prog_cc_static_works=no}
%{?_enable_static:export lt_cv_prog_cc_static_works=yes}
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable man} \
    --enable-x11-backend \
    %{subst_enable xkb} \
    --disable-schemas-compile \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_enable_snapshot:--enable-gtk-doc} \
    %{subst_enable colord} \
    %{?_enable_wayland:--enable-wayland-backend} \
    %{?_enable_broadway:--enable-broadway-backend} \
    %{?_enable_installed_tests:--enable-installed-tests} \
    %{subst_enable cloudprint} \
    %{subst_enable vulkan}

%make_build

%install
%makeinstall_std
install -d %buildroot{%_sysconfdir/gtk-%api_ver,%_libdir/gtk-%api_ver/%binary_ver/engines}

touch %buildroot%_libdir/gtk-%api_ver/%binary_ver/immodules.cache

# posttransfiletrigger to update immodules cache
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%fulllibpath/immodules
grep -qs '^'\$dir'' && %_bindir/gtk4-query-immodules --update-cache ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger

# The license
ln -sf %_licensedir/LGPL-2 COPYING

%find_lang --output=gtk40.lang gtk40 gtk40-properties

bzip2 -9kf NEWS

mkdir %buildroot%_libdir/gtk-%api_ver/modules

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version/examples
cp examples/*.c examples/Makefile* %buildroot/%_docdir/%name-devel-%version/examples/

%check

%files -f gtk40.lang
%{?_enable_broadway:%_bindir/gtk4-broadwayd}
%_bindir/gtk4-query-immodules
%_bindir/gtk4-query-settings
%_bindir/gtk4-launch
%_bindir/gtk4-encode-symbolic-svg
%_bindir/gtk4-update-icon-cache
%_libdir/libgtk-4.so.*
%dir %_libdir/gtk-%api_ver/modules
%dir %fulllibpath
%dir %fulllibpath/engines
%dir %fulllibpath/immodules
%fulllibpath/immodules/im-am-et.so
%fulllibpath/immodules/im-cedilla.so
%fulllibpath/immodules/im-cyrillic-translit.so
%fulllibpath/immodules/im-inuktitut.so
%fulllibpath/immodules/im-ipa.so
%fulllibpath/immodules/im-thai.so
%fulllibpath/immodules/im-ti-er.so
%fulllibpath/immodules/im-ti-et.so
%fulllibpath/immodules/im-viqr.so
%fulllibpath/immodules/im-multipress.so
%fulllibpath/immodules/im-xim.so
%{?_enable_broadway:%fulllibpath/immodules/im-broadway.so}
%dir %fulllibpath/printbackends
%fulllibpath/printbackends/libprintbackend-*.so
%dir %_datadir/themes/*/gtk-%{api_ver}*
%_datadir/themes/*/gtk-%{api_ver}/*.css
%dir %_sysconfdir/gtk-%api_ver
%config(noreplace) %_sysconfdir/gtk-%api_ver/im-multipress.conf
%ghost %_libdir/gtk-%api_ver/%binary_ver/immodules.cache
%{?_enable_broadway:%_man1dir/gtk4-broadwayd.1.*}
%_man1dir/gtk4-query-immodules*
%_man1dir/gtk4-query-settings.1.*
%_man1dir/gtk4-launch.*
%_man1dir/gtk4-encode-symbolic-svg.1.*
%_man1dir/gtk4-update-icon-cache.1.*
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger
%doc --no-dereference COPYING
%doc AUTHORS NEWS.bz2 README

%files devel
%_bindir/gtk4-builder-tool
%_includedir/gtk-%api_ver/
%_libdir/libgtk-4.so
%_pkgconfigdir/gtk+-%api_ver.pc
%_pkgconfigdir/gtk+-x11-%api_ver.pc
%_pkgconfigdir/gtk+-unix-print-%api_ver.pc
%_pkgconfigdir/gail-%api_ver.pc
%dir %_datadir/gtk-%api_ver
%_datadir/gtk-%api_ver/gtkbuilder.rng
#%_datadir/aclocal/gtk-%api_ver.m4
%_datadir/gettext/its/gtkbuilder.its
%_datadir/gettext/its/gtkbuilder.loc
%_man1dir/gtk4-builder-tool.1*

%if_enabled wayland
%_pkgconfigdir/gtk+-wayland-%api_ver.pc
%endif

%if_enabled broadway
%_pkgconfigdir/gtk+-broadway-%api_ver.pc
%endif

%files -n gtk4-demo
%_desktopdir/gtk4-demo.desktop
%_desktopdir/gtk4-widget-factory.desktop
%_desktopdir/gtk4-icon-browser.desktop
%_bindir/gtk4-demo
%_bindir/gtk4-demo-application
%_bindir/gtk4-widget-factory
%_bindir/gtk4-icon-browser
%_datadir/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%_iconsdir/hicolor/*x*/apps/gtk4-demo*.png
%_iconsdir/hicolor/*x*/apps/gtk4-widget*.png
%_man1dir/gtk4-demo.1.*
%_man1dir/gtk4-widget-factory.1.*
%_man1dir/gtk4-icon-browser.1.*
%_man1dir/gtk4-demo-application.1.*
%config %_datadir/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml

%files devel-doc
%_datadir/gtk-doc/html/*

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

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/gtk+/
%_datadir/installed-tests/gtk+/
%endif

%exclude %fulllibpath/*/*.la

%changelog
* Wed Dec 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.2-alt1.1
- rebuilt with vulkan support

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.2-alt1
- 3.89.2

* Tue Nov 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.89.1-alt1
- first build for Sisyphus

