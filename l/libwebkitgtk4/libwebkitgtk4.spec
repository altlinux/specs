%set_verify_elf_method textrel=relaxed
%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%define api_ver 4.0
%define gtk_ver 3.0

%define oname webkit
%define _name webkitgtk

%def_disable gtkdoc

Name: libwebkitgtk4
Version: 2.6.5
Release: alt1

Summary: Web browser engine
Group: System/Libraries
License: %bsd %lgpl2plus

Url: http://www.webkitgtk.org/

Source: %url/releases/%_name-%version.tar.xz

BuildPreReq: rpm-build-licenses

BuildRequires: gcc-c++ cmake libicu-devel bison perl-Switch zlib-devel
BuildRequires: chrpath
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel libwebp-devel
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.4.0
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant-devel >= 0.22
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer1.0-devel >= 1.0.3 gst-plugins1.0-devel >= 1.0.3
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.40.0
BuildRequires: libsecret-devel
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel libharfbuzz-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: python-modules-json
BuildRequires: ruby ruby-stdlibs
BuildRequires: libGL-devel libXcomposite-devel libXdamage-devel
BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libsoup-gir-devel
BuildRequires: geoclue2-devel
BuildRequires: libenchant-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: libgtk+2-devel libpixman-devel libexpat-devel

BuildRequires: libXdmcp-devel libxshmfence-devel libXxf86vm-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
# for battery status
BuildRequires: libupower-devel

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n libwebkit2gtk
Summary: WebKit2 is a new API layer for WebKit
Group: System/Libraries
Provides: %name = %version-%release
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libwebkit2gtk
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.

%package -n libwebkit2gtk-devel
Summary: Development files for WebKit GTK+ port
Group: Development/GNOME and GTK+
Provides: %name-devel = %version-%release
Requires: libwebkit2gtk = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release

%description -n libwebkit2gtk-devel
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package -n libwebkit2gtk-devel-doc
Summary: Development documentation for WebKit2GTK
Group: Development/Documentation
BuildArch: noarch
Conflicts: libwebkit2gtk < %version-%release

%description -n libwebkit2gtk-devel-doc
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This package provides development documentation for WebKit2GTK.

%package -n libjavascriptcoregtk4
Summary: GTK+3 version of the JavaScriptCore engine
Group: System/Libraries

%description -n libjavascriptcoregtk4
This package provides GTK+3 version of the JavaScriptCore engine from
WebKit package.

%package -n libjavascriptcoregtk4-devel
Summary: Development files for JavaScriptCore library
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libjavascriptcoregtk4-devel
This package provides development files for GTK+3 version of the
JavaScriptCore engine.

%package -n jsc4
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk4 = %version-%release
Conflicts: jsc

%description -n jsc4
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n libwebkit2gtk-gir
Summary: GObject introspection data for the Webkit2GTK library
Group: System/Libraries
Requires: libwebkit2gtk = %version-%release
Requires: libjavascriptcoregtk4 = %version-%release
Requires: libjavascriptcoregtk4-gir  = %version-%release

%description -n libwebkit2gtk-gir
GObject introspection data for the Webkit2GTK library

%package -n libwebkit2gtk-gir-devel
Summary: GObject introspection devel data for the Webkit2GTK library
Group: Development/Other
BuildArch: noarch
Requires: libwebkit2gtk-gir = %version-%release
Requires: libjavascriptcoregtk4-gir = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release
Requires: libjavascriptcoregtk4-gir-devel = %version-%release

%description -n libwebkit2gtk-gir-devel
GObject introspection devel data for the Webkit2GTK library

%package -n libjavascriptcoregtk4-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libjavascriptcoregtk4-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk4-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libjavascriptcoregtk4-gir = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release

%description -n libjavascriptcoregtk4-gir-devel
GObject introspection devel data for the JavaScriptCore library

%prep
%setup -n %_name-%version
# Remove bundled libraries
rm -rf Source/ThirdParty/leveldb/
rm -rf Source/ThirdParty/gtest/
rm -rf Source/ThirdParty/qunit/

%build
# Decrease debuginfo verbosity and use linker flags to reduce memory consumption
%define optflags_debug -g1
%add_optflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads

%cmake \
-DPORT=GTK \
%{?_enable_gtkdoc:-DENABLE_GTKDOC:BOOL=ON} \
-DCMAKE_BUILD_TYPE=Release \
-DENABLE_TOUCH_ICON_LOADING:BOOL=ON \
-DENABLE_TOUCH_SLIDER:BOOL=ON
#-DENABLE_BATTERY_STATUS:BOOL=ON \
#-DENABLE_DEVICE_ORIENTATION:BOOL=ON \
#-DENABLE_ORIENTATION_EVENTS:BOOL=ON

%cmake_build

%install
%cmakeinstall_std

%find_lang WebKit2GTK-%api_ver

%files -n libwebkit2gtk -f WebKit2GTK-%api_ver.lang
%_libdir/libwebkit2gtk-%api_ver.so.*
%dir %_libexecdir/webkit2gtk-%api_ver
%_libexecdir/webkit2gtk-%api_ver/WebKitNetworkProcess
%_libexecdir/webkit2gtk-%api_ver/WebKitPluginProcess
%_libexecdir/webkit2gtk-%api_ver/WebKitPluginProcess2
%_libexecdir/webkit2gtk-%api_ver/WebKitWebProcess
%dir %_libdir/webkit2gtk-%api_ver
%dir %_libdir/webkit2gtk-%api_ver/injected-bundle
%_libdir/webkit2gtk-%api_ver/injected-bundle/libwebkit2gtkinjectedbundle.so
%doc NEWS

%files -n libwebkit2gtk-devel
%_libdir/libwebkit2gtk-%api_ver.so
%dir %_includedir/webkitgtk-%api_ver
%_includedir/webkitgtk-%api_ver/webkit2
%_includedir/webkitgtk-%api_ver/webkitdom
%_pkgconfigdir/webkit2gtk-%api_ver.pc
%_pkgconfigdir/webkit2gtk-web-extension-%api_ver.pc

%if_enabled gtkdoc
%files -n libwebkit2gtk-devel-doc
%_gtk_docdir/*
%endif

%files -n libjavascriptcoregtk4
%_libdir/libjavascriptcoregtk-%api_ver.so.*

%files -n libjavascriptcoregtk4-devel
%_includedir/webkitgtk-%api_ver/JavaScriptCore
%_libdir/libjavascriptcoregtk-%api_ver.so
%_pkgconfigdir/javascriptcoregtk-%api_ver.pc

%files -n jsc4
%_bindir/jsc*

%files -n libwebkit2gtk-gir
%_typelibdir/WebKit2-%api_ver.typelib
%_typelibdir/WebKit2WebExtension-%api_ver.typelib

%files -n libwebkit2gtk-gir-devel
%_girdir/WebKit2-%api_ver.gir
%_girdir/WebKit2WebExtension-%api_ver.gir

%files -n libjavascriptcoregtk4-gir
%_typelibdir/JavaScriptCore-%api_ver.typelib

%files -n libjavascriptcoregtk4-gir-devel
%_girdir/JavaScriptCore-%api_ver.gir


%changelog
* Thu Jan 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.6.5-alt1
- 2.6.5

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt2
- enabled touch (slider/icon loading) support

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- 2.6.4

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Wed Oct 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Oct 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt2
- libwebkitgtk4* subpackages renamed to libwebkit2gtk*

* Thu Sep 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 2.5.90-alt1
- 2.5.90

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- first build for Sisyphus

