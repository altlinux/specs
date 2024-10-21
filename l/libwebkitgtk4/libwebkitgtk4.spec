%set_verify_elf_method textrel=relaxed
%define optflags_lto %nil

%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%def_enable soup2
%if_enabled soup2
%define api_ver 4.0
%def_disable webdriver
%def_disable gtk4
%else
%define api_ver 4.1
%def_disable webdriver
%def_disable gtk4
%endif

%define pkglibexecdir %_libexecdir/webkit2gtk-%api_ver
%define ver_major 2.46
%define oname webkit
%define _name webkitgtk
%define bwrap_bin %_bindir/bwrap

%def_enable ninja
%def_disable gtkdoc
%def_enable gold
%def_enable x11
%def_enable wayland
%def_enable systemd
%def_disable soup2
%def_enable libavif
%def_enable speech_synthesis
# we have no libjxl for armh
%ifarch armh
%def_disable jpegxl
%else
%def_enable jpegxl
%endif
%def_enable sysprof

# since 2.19.x in some build environments
# while build webki2gtk-dep typelibs this error appears
# FATAL: Could not allocate gigacage memory with maxAlignment = ..
# To avoid it set GIGACAGE_ENABLED=0
%def_enable gigacage

%def_enable bubblewrap_sandbox

Name: libwebkitgtk4
Version: %ver_major.2
Release: alt1

Summary: Web browser engine
Group: System/Libraries
License: LGPL-2.0
Url: https://www.webkitgtk.org/

Source: %url/releases/%_name-%version.tar.xz
Source1: webkit2gtk.env
Patch2000: webkitgtk-2.34.3-alt-e2k.patch

%define bwrap_ver 0.3.1
%define soup_ver 2.62
%define gtk_ver 3.24
%define gst_ver 1.20

%define soup_api_ver 3.0
%define soup3_ver 2.99.9

BuildRequires(pre): rpm-macros-cmake rpm-build-gir rpm-build-python3
BuildRequires: /proc gcc-c++ cmake unifdef
%{?_enable_ninja:BuildRequires: ninja-build}
BuildRequires: ccache libicu-devel >= 5.6.1 bison
BuildRequires: perl-Switch perl-JSON-PP perl-bignum
BuildRequires: zlib-devel
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel libwebp-devel liblcms2-devel
BuildRequires: libopenjpeg2.0-devel openjpeg-tools2.0
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.4.0 libepoxy-devel
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant2-devel >= 2.2.3
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver gst-plugins-bad1.0-devel
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gi-docgen
%if_enabled soup2
BuildRequires: libsoup-devel >= %soup_ver libsoup-gir-devel
%else
BuildRequires: libsoup%soup_api_ver-devel >= %soup3_ver libsoup%soup_api_ver-gir-devel
%endif
BuildRequires: libsecret-devel
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel libharfbuzz-devel libwoff2-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: ruby ruby-stdlibs
BuildRequires: libdrm-devel libgbm-devel
BuildRequires: libGL-devel libGLES-devel
BuildRequires: libXcomposite-devel libXdamage-devel
BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel 
BuildRequires: geoclue2-devel libgeoclue2-devel
BuildRequires: libenchant-devel libhyphen-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: libpixman-devel libexpat-devel
BuildRequires: libXdmcp-devel libxshmfence-devel libXxf86vm-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libxkbcommon-devel
%{?_enable_wayland:BuildRequires: libwayland-server-devel libwayland-cursor-devel libwayland-egl-devel wayland-protocols}
BuildRequires: libgnutls-devel libnettle-devel
BuildRequires: libtasn1-devel libp11-kit-devel libgcrypt-devel
# for battery status
BuildRequires: libupower-devel
# since 2.25.x
#BuildRequires: libwpe-devel libwpebackend-fdo-devel >= 1.8.0
# since 2.31.x
BuildRequires: libmanette-devel
%{?_enable_bubblewrap_sandbox:BuildRequires: bubblewrap >= %bwrap_ver xdg-dbus-proxy libseccomp-devel}
# since 2.29.x 
%{?_enable_systemd:BuildRequires: pkgconfig(systemd)}
# since 2.34.0
%{?_enable_libavif:BuildRequires: libavif-devel}
%{?_enable_speech_synthesis:BuildRequires: flite-devel >= 2.2}
# since 2.39.x
%{?_enable_jpegxl:BuildRequires: libjxl-devel}
# since 2.43.x
BuildRequires: libbacktrace-devel
# since 2.45.x
%{?_enable_sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n libwebkit2gtk
Summary: WebKit2 is a new API layer for WebKit
Group: System/Libraries
Provides: %name = %EVR
#https://bugzilla.altlinux.org/39394
Provides: webkitgtk4 = %EVR
Requires: libjavascriptcoregtk4 = %EVR
Requires: gst-plugins-base1.0 >= %gst_ver gst-plugins-good1.0 gst-plugins-bad1.0 gst-libav
Requires: hyphen-en hyphen-ru
%{?_enable_bubblewrap_sandbox:Requires: bubblewrap >= %bwrap_ver xdg-dbus-proxy}

%description -n libwebkit2gtk
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.

%package -n %_name-minibrowser
Summary: Simple WebKit browser
Group: Networking/WWW
Requires: libwebkit2gtk = %EVR

%description -n %_name-minibrowser
This package provides simple browser from webkitgtk project.

%package -n libwebkit2gtk-devel
Summary: Development files for WebKit GTK+ port
Group: Development/C++
Provides: %name-devel = %EVR
Requires: libwebkit2gtk = %EVR
Requires: libjavascriptcoregtk4-devel = %EVR

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
Group: Development/C++
Requires: libjavascriptcoregtk4 = %EVR

%description -n libjavascriptcoregtk4-devel
This package provides development files for GTK+3 version of the
JavaScriptCore engine.

%package -n jsc4
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk4 = %EVR

%description -n jsc4
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n libwebkit2gtk-gir
Summary: GObject introspection data for the Webkit2GTK library
Group: System/Libraries
Requires: libwebkit2gtk = %EVR
Requires: libjavascriptcoregtk4 = %EVR
Requires: libjavascriptcoregtk4-gir  = %EVR

%description -n libwebkit2gtk-gir
GObject introspection data for the Webkit2GTK library

%package -n libwebkit2gtk-gir-devel
Summary: GObject introspection devel data for the Webkit2GTK library
Group: Development/Other
BuildArch: noarch
Requires: libwebkit2gtk-gir = %EVR
Requires: libwebkit2gtk-devel = %EVR
Requires: libjavascriptcoregtk4-gir = %EVR
Requires: libjavascriptcoregtk4-devel = %EVR
Requires: libjavascriptcoregtk4-gir-devel = %EVR

%description -n libwebkit2gtk-gir-devel
GObject introspection devel data for the Webkit2GTK library

%package -n libjavascriptcoregtk4-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk4 = %EVR

%description -n libjavascriptcoregtk4-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk4-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: Development/Other
BuildArch: noarch
Requires: libjavascriptcoregtk4-gir = %EVR
Requires: libjavascriptcoregtk4-devel = %EVR

%description -n libjavascriptcoregtk4-gir-devel
GObject introspection devel data for the JavaScriptCore library

%prep
%setup -n %_name-%version
%ifarch %e2k
%patch2000 -p2 -b .e2k
%endif

# Remove bundled libraries
rm -rf Source/ThirdParty/gtest/
rm -rf Source/ThirdParty/qunit/

subst 's|Q\(unused-arguments\)|W\1|' Source/cmake/WebKitCompilerFlags.cmake

# fix flite.h include
[ ! -d %_includedir/flite ] && sed -i 's|<flite/flite.h>|<flite.h>|' Source/WebCore/platform/gstreamer/GUniquePtrFlite.h

%build
%ifarch %e2k
# because of this error on linking:
# "relocation truncated to fit: R_E2K_32_ABS"
%define optflags_debug -g0
%else
# Decrease debuginfo verbosity and use linker flags to reduce memory consumption
%define optflags_debug -g1
%endif
%add_optflags -Wl,--no-keep-memory
%{?_disable_gold: %add_optflags -Wl,--reduce-memory-overheads}
%add_optflags %(getconf LFS_CFLAGS) -Wno-error=return-type
%ifarch %e2k
# EDG frontend mistakenly sees it everywhere
# after each "if constexpr {} else {}" constuct
%add_optflags -Wno-return-type
%endif
%ifarch x86_64
%if_disabled gigacage
export GIGACAGE_ENABLED=0
%endif
%endif
export PYTHON=%__python3
%cmake \
%{?_enable_ninja:-GNinja} \
-DPORT=GTK \
%{?_disable_gtk4:-DUSE_GTK4=OFF} \
-DPYTHON_EXECUTABLE=%__python3 \
-DCMAKE_BUILD_TYPE=Release \
-DENABLE_MINIBROWSER=ON \
%{?_disable_gtkdoc:-DENABLE_DOCUMENTATION:BOOL=OFF} \
%{?_enable_x11:-DENABLE_X11_TARGET:BOOL=ON} \
%{?_enable_wayland:-DENABLE_WAYLAND_TARGET:BOOL=ON} \
%{?_enable_libavif:-DUSE_AVIF:BOOL=ON} \
%{?_enable_speech_synthesis:-DENABLE_SPEECH_SYNTHESIS=ON} \
%{?_disable_jpegxl:-DUSE_JPEGXL=OFF} \
%{?_disable_gold:-DUSE_LD_GOLD:BOOL=OFF} \
%if_disabled bubblewrap_sandbox
-DENABLE_BUBBLEWRAP_SANDBOX=OFF \
%else
-DBWRAP_EXECUTABLE=%bwrap_bin \
%endif
%ifarch %arm
-DENABLE_GLES2=ON \
%endif
%ifarch armh
-DENABLE_JIT=OFF \
-DENABLE_C_LOOP=ON \
-DENABLE_SAMPLING_PROFILER=OFF \
-DUSE_SYSTEM_MALLOC=ON \
%endif
-DUSER_AGENT_BRANDING:STRING="ALTLinux" \
%{?_disable_systemd:-DUSE_SYSTEMD:BOOL=OFF} \
%{?_enable_soup2:-DUSE_SOUP2=ON} \
%{?_disable_webdriver:-DENABLE_WEBDRIVER=OFF} \
%{?_disable_sysprof:-DUSE_SYSTEM_SYSPROF_CAPTURE=NO}
%nil
%ifarch aarch64 x86_64
[ %__nprocs -lt 128 ] || export NPROCS=128
%endif
%cmake_build

%install
%cmake_install
%if_disabled gigacage
install -pD -m755 %SOURCE1 %buildroot%_rpmmacrosdir/webki2gtk.env
%endif

%find_lang WebKitGTK-%api_ver

%files -n libwebkit2gtk -f WebKitGTK-%api_ver.lang
%{?!_disable_webdriver:%_bindir/WebKitWebDriver}
%_libdir/libwebkit2gtk-%api_ver.so.*
%dir %pkglibexecdir
%pkglibexecdir/WebKitNetworkProcess
%pkglibexecdir/WebKitWebProcess
%dir %_libdir/webkit2gtk-%api_ver
%dir %_libdir/webkit2gtk-%api_ver/injected-bundle
%_libdir/webkit2gtk-%api_ver/injected-bundle/libwebkit2gtkinjectedbundle.so
%doc NEWS

%files -n %_name-minibrowser
%pkglibexecdir/MiniBrowser

%files -n libwebkit2gtk-devel
%_libdir/libwebkit2gtk-%api_ver.so
%dir %_includedir/webkitgtk-%api_ver
%_includedir/webkitgtk-%api_ver/webkit
%_includedir/webkitgtk-%api_ver/webkit2
%_includedir/webkitgtk-%api_ver/webkitdom
%_pkgconfigdir/webkit2gtk-%api_ver.pc
%_pkgconfigdir/webkit2gtk-web-extension-%api_ver.pc
%{?_disable_gigacage:%_rpmmacrosdir/webki2gtk.env}

%if_enabled gtkdoc
%files -n libwebkit2gtk-devel-doc
%_gtk_docdir/*
%endif

%files -n libjavascriptcoregtk4
%_libdir/libjavascriptcoregtk-%api_ver.so.*

%files -n libjavascriptcoregtk4-devel
%_includedir/webkitgtk-%api_ver/jsc/
%_includedir/webkitgtk-%api_ver/JavaScriptCore/
%_libdir/libjavascriptcoregtk-%api_ver.so
%_pkgconfigdir/javascriptcoregtk-%api_ver.pc

%files -n jsc4
%pkglibexecdir/jsc*

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
* Mon Oct 21 2024 Yuri N. Sedunov <aris@altlinux.org> 2.46.2-alt1
- 2.46.2

* Mon Sep 30 2024 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Tue Sep 17 2024 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Mon Sep 09 2024 Yuri N. Sedunov <aris@altlinux.org> 2.44.4-alt1
- 2.44.4

* Tue Aug 13 2024 Yuri N. Sedunov <aris@altlinux.org> 2.44.3-alt1
- 2.44.3

* Thu May 16 2024 Yuri N. Sedunov <aris@altlinux.org> 2.44.2-alt1
- 2.44.2

* Tue Apr 09 2024 Yuri N. Sedunov <aris@altlinux.org> 2.44.1-alt1
- 2.44.1

* Mon Mar 18 2024 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0

* Tue Feb 06 2024 Yuri N. Sedunov <aris@altlinux.org> 2.42.5-alt1
- 2.42.5

* Fri Dec 15 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.4-alt1
- 2.42.4

* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.3-alt1
- 2.42.3 (fixed CVE-2023-42916, CVE-2023-42917)

* Sat Nov 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1
- 2.42.2

* Wed Sep 27 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1

* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Wed Aug 02 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.5-alt1
- 2.40.5

* Fri Jul 21 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.4-alt1
- 2.40.4

* Thu Jun 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.3-alt1
- 2.40.3

* Mon May 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Wed Feb 15 2023 Yuri N. Sedunov <aris@altlinux.org> 2.38.5-alt1
- 2.38.5

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 2.38.4-alt1
- 2.38.4

* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 2.38.3-alt1
- 2.38.3

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Fri Oct 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 2.37.91-alt1
- 2.37.91

* Thu Aug 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.7-alt1
- 2.36.7

* Sun Aug 07 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.6-alt1
- 2.36.6

* Fri Jul 29 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.5-alt1
- 2.36.5

* Tue Jul 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.4-alt1
- 2.36.4

* Sun May 29 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt1
- 2.36.3

* Wed May 18 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt1
- 2.36.2

* Fri Apr 22 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 2.34.6-alt1
- 2.34.6

* Fri Jan 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.34.4-alt1
- 2.34.4

* Wed Jan 19 2022 Michael Shigorin <mike@altlinux.org> 2.34.3-alt2
- updated e2k patch (ilyakurdyukov@)

* Mon Dec 20 2021 Yuri N. Sedunov <aris@altlinux.org> 2.34.3-alt1
- 2.34.3 (fixed CVE-2021-30809, CVE-2021-30818, CVE-2021-30823,
  CVE-2021-30836, CVE-2021-30884, CVE-2021-30887, CVE-2021-30888,
  CVE-2021-30889, CVE-2021-30890, CVE-2021-30897)
- enabled libavif support

* Thu Nov 25 2021 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1
- enabled LTO again

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.4-alt2
- Source/cmake/WebKitCompilerFlags.cmake, spec: no force SSE for %%ix86
- decreased nprocs limit for x86_64

* Fri Sep 17 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.4-alt1
- 2.32.4

* Fri Sep 10 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt2.1
- ilyakurdyukov@: improved %%e2k patch

* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt2
- fixed build for %%e2k by ilyakurdyukov@

* Sat Aug 28 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1.1
- disabled LTO and ld.gold
- try to decrease nprocs limit for aarch64 to avoid cc crash

* Fri Jul 23 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Fri Jul 09 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon May 31 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1.1
- adapted to new cmake macros

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Fri Mar 26 2021 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt1
- 2.30.6

* Thu Feb 11 2021 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Tue Dec 15 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Nov 17 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1.1
- rebuilt with ninja instead make

* Fri Oct 23 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Sep 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Jul 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4
- %%arm: enabled GLES
- armh: disabled JIT

* Thu Jul 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Fri Apr 24 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Apr 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1
- used python3 for build

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Fri Feb 14 2020 Yuri N. Sedunov <aris@altlinux.org> 2.26.4-alt1
- 2.26.4

* Wed Jan 22 2020 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Wed Nov 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri Oct 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- rebuild against icu-65.1 libraries

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Aug 28 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Tue Jul 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2 (fixed CVE-2019-8595, CVE-2019-8607, CVE-2019-8615)

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1 (fixed CVE-2019-6251)

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Fri Mar 01 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22.7-alt1
- 2.22.7

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22.6-alt1
- 2.22.6

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- 2.22.5

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.4-alt1
- 2.22.4

* Tue Oct 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Sat Sep 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt1
- 2.22.2

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1.1
- rebuilt with atk-2.30.0

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Mon Aug 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.5-alt1
- 2.20.5

* Mon Aug 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.4-alt2
- 2.20.4 (fixed CVE-2018-4261, CVE-2018-4262, CVE-2018-4263,
  CVE-2018-4264, CVE-2018-4265, CVE-2018-4266, CVE-2018-4267,
  CVE-2018-4270, CVE-2018-4272, CVE-2018-4273, CVE-2018-4278,
  CVE-2018-4284)

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt2
- rebuilt against libicu*.so.62

* Mon Jun 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3 (fixed  CVE-2018-4190, CVE-2018-4199, CVE-2018-4218,
  CVE-2018-4222, CVE-2018-4232, CVE-2018-4233, CVE-2018-4246,
  CVE-2018-11646)

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2 (fixed CVE-2018-4200)

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.6-alt1
- 2.18.6 (fixed CVE-2018-4088, CVE-2017-13885, CVE-2017-7165,
  CVE-2017-13884, CVE-2017-7160, CVE-2017-7153, CVE-2017-7153,
  CVE-2017-7161, CVE-2018-4096)

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.5-alt1
- 2.18.5 (fixed CVE-2017-5753, CVE-2017-5715)

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt2
- rebuilt against libicu*.so.60

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4 (fixed CVE-2017-13866, CVE-2017-13870, CVE-2017-7156, CVE-2017-13856)

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3 (fixed CVE-2017-13798, CVE-2017-13788, CVE-2017-13803)

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.1-alt1
- 2.18.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.6-alt1
- 2.16.6 (fixed CVE-2017-7039, CVE-2017-7018, CVE-2017-7030,
  CVE-2017-7037, CVE-2017-7034, CVE-2017-7055, CVE-2017-7056,
  CVE-2017-7064, CVE-2017-7061, CVE-2017-7048, CVE-2017-7046)

* Fri Jun 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt1
- 2.16.5

* Thu Jun 22 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.4-alt1
- 2.16.4 (fixed CVE-2017-2538)

* Sat May 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.3-alt1
- 2.16.3 (fixed CVE-2017-2496, CVE-2017-2539, CVE-2017-2510)

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.2-alt1
- 2.16.2

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.1-alt1
- 2.16.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.5-alt1
- 2.14.5

* Fri Feb 10 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt1
- 2.14.4 (fixed CVE-2017-2365, CVE-2017-2366, CVE-2017-2373, CVE-2017-2363,
  CVE-2017-2362, CVE-2017-2350, CVE-2017-2350, CVE-2017-2354, CVE-2017-2355,
  CVE-2017-2356, CVE-2017-2371, CVE-2017-2364, CVE-2017-2369)

* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.3-alt1
- 2.14.3 (fixed CVE-2016-7656, CVE-2016-7635, CVE-2016-7654, CVE-2016-7639,
  CVE-2016-7645, CVE-2016-7652, CVE-2016-7641, CVE-2016-7632, CVE-2016-7599,
  CVE-2016-7592, CVE-2016-7589, CVE-2016-7623, CVE-2016-7586)

* Thu Nov 03 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.2-alt1
- 2.14.2
- MiniBrowser moved to separate subpackage

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Mon Sep 05 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.5-alt1
- 2.12.5

* Wed Aug 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.4-alt1
- 2.12.4 (fixed CVE-2016-4622, CVE-2016-4624, CVE-2016-4591, CVE-2016-4590)

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.3-alt1
- 2.12.3 (fixed VE-2016-1857, CVE-2016-1856)

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Thu Mar 17 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.9-alt1
- 2.10.9

* Fri Mar 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.8-alt1
- 2.10.8 (CVE-2016-1726)

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.7-alt2
- rebuild against libicu*.so.56

* Sun Jan 31 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.7-alt1
- 2.10.7

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt1
- 2.10.5 (CVE-2015-7096, CVE-2015-7098)

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.4-alt1
- 2.10.4

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.3-alt1
- 2.10.3

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Fri Aug 07 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.5-alt1
- 2.8.5

* Wed Jul 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.4-alt1
- 2.8.4

* Sun Jun 07 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt3
- fixed BWO #145385

* Tue May 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt2
- fixed build with gcc-5 (fc patch)

* Fri May 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Sun Apr 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt2
- packaged MiniBrowser in -devel subpackage

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Tue Mar 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

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

