%def_disable snapshot
%define _name gst-plugins
%define ver_major 1.24
%define api_ver 1.0

%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%ifarch %e2k
# https://gitlab.gnome.org/GNOME/gnome-build-meta/issues/38
# https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/564
%def_disable doc
%else
%def_disable doc
%endif
%def_disable debug
%def_disable libunwind
%def_disable libdw
%def_disable examples
%def_disable check

Name: %_name-base%api_ver
Version: %ver_major.6
Release: alt1

Summary: An essential set of GStreamer plugins
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/

%if_disabled snapshot
Source: http://gstreamer.freedesktop.org/src/%_name-base/%_name-base-%version.tar.xz
%else
Source: %_name-base-%version.tar
%endif

Provides: %_name-base = %EVR

Requires: lib%_name%api_ver = %EVR
Requires: gstreamer%api_ver >= %ver_major
Conflicts: gst-plugins-bad%api_ver < %ver_major

Provides: gstreamer%api_ver(audio-hardware-sink) = %version
Provides: gstreamer%api_ver(audio-hardware-source) = %version

%define opus_ver 0.9.4

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gcc-c++ orc >= 0.4.18 liborc-test-devel
BuildRequires: gstreamer%api_ver-devel >= %version libgstreamer%api_ver-gir-devel
BuildRequires: libgudev-devel libglvnd-devel libdrm-devel libgbm-devel
BuildRequires: libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel wayland-protocols
BuildRequires: libgraphene-devel libjpeg-devel libpng-devel
BuildRequires: libXext-devel libXi-devel libXv-devel libSM-devel libalsa-devel libgtk+3-devel libvisual0.4-devel iso-codes-devel
BuildRequires: libcdparanoia-devel libtheora-devel
BuildRequires: pkgconfig(vorbis)
#BuildRequires: pkgconfig(vorbisidec)
BuildRequires: libopus-devel >= %opus_ver
BuildRequires: gobject-introspection-devel
%{?_enable_libunwind:BuildRequires: libunwind-devel}
%{?_enable_libdw:BuildRequires: libdw-devel}
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}
%{?_enable_check:BuildRequires: /proc gstreamer%api_ver %_bindir/gst-tester-%api_ver}

%description
GStreamer Base Plug-ins is a well-groomed and well-maintained
collection of GStreamer plug-ins and elements, spanning the range of
possible types of elements one would want to write for GStreamer. A
wide range of video and audio decoders, encoders, and filters are
included.

%package -n lib%_name%api_ver
Summary: GStreamer plugin libraries
Group: System/Libraries
Provides: lib%_name = %EVR
# GstGL moved from bad to base in 1.13
# https://bugzilla.altlinux.org/show_bug.cgi?id=35636
Conflicts: gst-plugins-bad%api_ver < 1.13

%description -n lib%_name%api_ver
Helper libraries for GStreamer plugins, containing base classes useful for elements

%package -n lib%_name%api_ver-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Provides: lib%_name-gir = %EVR
Requires: lib%_name%api_ver = %EVR

%description -n lib%_name%api_ver-gir
GObject introspection data for the GStreamer library

%package -n %_name%api_ver-tools
Summary: GStreamer plugin tools
Group: Development/Other
Provides: %_name-tools = %EVR
Requires: %name = %EVR

%description -n %_name%api_ver-tools
This package contains a few test tools from the
GStreamer Base Plugins distribution.

%package -n %_name%api_ver-devel
Summary: Development files for GStreamer plugins
Group: Development/C
Provides: %_name-devel = %EVR
Requires: lib%_name%api_ver = %EVR
Requires: gstreamer%api_ver-devel

%description -n %_name%api_ver-devel
This package contains the libraries, headers and other files necessary
to develop GStreamer plugins.

%package -n %_name%api_ver-devel-doc
Summary: Development documentation for GStreamer Base plugins
Group: Development/Documentation
BuildArch: noarch
Provides: %_name-devel-doc = %EVR

%description -n %_name%api_ver-devel-doc
This package contains development documentation for GStreamer Base Plugins

%package -n %_name%api_ver-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Provides: %_name-gir-devel = %EVR
Requires: lib%_name%api_ver-gir = %EVR
Requires: %_name%api_ver-devel = %EVR

%description -n %_name%api_ver-gir-devel
GObject introspection devel data for the GStreamer library

%prep
%setup -n %_name-base-%version

%build
%meson \
	-Dexamples=disabled \
	-Dgio=enabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_enable_debug:-Dgst_debug=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-base-%api_ver

%check
%__meson_test

%files -f %_name-base-%api_ver.lang
%dir %_gst_libdir
%_gst_libdir/*.so
%_datadir/%_name-base/%api_ver/*.dict

%files -n lib%_name%api_ver
%_libdir/*.so.*
%dir %_gst_libdir

%files -n lib%_name%api_ver-gir
%_typelibdir/GstAllocators-1.0.typelib
%_typelibdir/GstApp-%api_ver.typelib
%_typelibdir/GstAudio-%api_ver.typelib
%_typelibdir/GstGL-%api_ver.typelib
%_typelibdir/GstGLEGL-%api_ver.typelib
%_typelibdir/GstGLWayland-%api_ver.typelib
%_typelibdir/GstGLX11-%api_ver.typelib
%_typelibdir/GstPbutils-%api_ver.typelib
%_typelibdir/GstRtp-%api_ver.typelib
%_typelibdir/GstRtsp-%api_ver.typelib
%_typelibdir/GstSdp-%api_ver.typelib
%_typelibdir/GstTag-%api_ver.typelib
%_typelibdir/GstVideo-%api_ver.typelib

%files -n %_name%api_ver-tools
%_bindir/*-%api_ver
%_man1dir/*

%files -n %_name%api_ver-devel
%_includedir/*
%_libdir/gstreamer-%api_ver/include/gst/gl/gstglconfig.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled doc
%files -n %_name%api_ver-devel-doc
%_gtk_docdir/%_name-base-*/
%endif

%files -n %_name%api_ver-gir-devel
%_girdir/GstAllocators-1.0.gir
%_girdir/GstApp-%api_ver.gir
%_girdir/GstAudio-%api_ver.gir
%_girdir/GstGL-%api_ver.gir
%_girdir/GstGLEGL-%api_ver.gir
%_girdir/GstGLWayland-%api_ver.gir
%_girdir/GstGLX11-%api_ver.gir
%_girdir/GstPbutils-%api_ver.gir
%_girdir/GstRtp-%api_ver.gir
%_girdir/GstRtsp-%api_ver.gir
%_girdir/GstSdp-%api_ver.gir
%_girdir/GstTag-%api_ver.gir
%_girdir/GstVideo-%api_ver.gir


%changelog
* Tue Jul 30 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.6-alt1
- 1.24.6

* Thu Jun 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.5-alt1
- 1.24.5

* Wed May 29 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.4-alt1
- 1.24.4

* Tue Apr 30 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.3-alt1
- 1.24.3

* Wed Apr 10 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.2-alt1
- 1.24.2

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1
- 1.24.1

* Tue Mar 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Wed Feb 14 2024 Yuri N. Sedunov <aris@altlinux.org> 1.22.10-alt1
- 1.22.10

* Thu Jan 25 2024 Yuri N. Sedunov <aris@altlinux.org> 1.22.9-alt1
- 1.22.9

* Mon Dec 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.8-alt1
- 1.22.8

* Mon Nov 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.7-alt1
- 1.22.7

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.6-alt1
- 1.22.6

* Thu Jul 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.5-alt1
- 1.22.5

* Wed Jun 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Fri May 19 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt1
- 1.22.3

* Wed Apr 12 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2

* Sat Mar 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1

* Wed Jan 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Thu Oct 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.4-alt1
- 1.20.4

* Thu Jun 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Tue May 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1.1
- fixed meson options

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1
- 1.18.5

* Thu May 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt2
- updated to 1.18.4-16-g0f86fca8d

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Thu Jan 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Mon Dec 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Wed Dec 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- BR: s/libGL-devel libGLES-devel/libglvnd-devel/

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.1
- mike@: E2K: disabled gtk_doc knob by default due to wayland-related ftbfs

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Tue Apr 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt2
- built lost cdparanoia plugin (ALT #36488)

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Sun Nov 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt3
- libgst-plugins1.0: added conflict to gst-plugins-bad1.0 < 1.13 (ALT #35636)

* Fri Oct 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt2
- updated to 1.14.4-6-g01a3a5b79 (fixed BGO ##796860, 797272)

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Dec 29 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Fri Jul 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

