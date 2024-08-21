%define _name gst-plugins
%define ver_major 1.24
%define api_ver 1.0

%define _gst_datadir %_datadir/gstreamer-%api_ver
%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable jack
%def_enable pulse
%def_enable caca
%def_enable qt5
%ifnarch armh
%def_enable qt6
%endif

%def_disable doc
%def_disable debug
%def_disable examples
%ifarch %ix86 x86_64 aarch64
%def_enable valgrind
%endif
%def_disable check

Name: %_name-good%api_ver
Version: %ver_major.7
Release: alt1

Summary: A set of GStreamer plugins considered good
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/%_name-good/%_name-good-%version.tar.xz

Provides: %_name-good = %EVR
# https://bugzilla.altlinux.org/45382
Conflicts: gst-plugins-ugly%api_ver < 1.22.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ orc nasm liborc-devel
BuildRequires: bzlib-devel gst-plugins%api_ver-devel >= %version
BuildRequires: libSM-devel libXdamage-devel libXext-devel libXfixes-devel
BuildRequires: libXv-devel libavc1394-devel libcairo-devel libdv-devel libflac-devel libiec61883-devel libjpeg-devel
BuildRequires: libshout2-devel libtag-devel libv4l-devel libwavpack-devel
BuildRequires: libsoup-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libpng-devel libcairo-gobject-devel libgudev-devel libspeex-devel zlib-devel libvpx-devel
BuildRequires: libmpg123-devel liblame-devel libtwolame-devel
BuildRequires: libgtk+3-devel
BuildRequires: liborc-test-devel
BuildRequires: pkgconfig(libxml-2.0)
%{?_enable_valgrind:BuildRequires: valgrind-tool-devel}
%{?_enable_jack:BuildRequires: libjack-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_caca:BuildRequires: libcaca-devel}
%{?_enable_qt5:BuildRequires: qt5-base-devel qt5-tools qt5-declarative-devel qt5-x11extras-devel qt5-wayland-devel}
%{?_enable_qt6:BuildRequires: qt6-base-devel qt6-tools-devel qt6-declarative-devel qt6-wayland-devel /usr/bin/qsb-qt6}
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}
%{?_enable_check:BuildRequires: /proc gstreamer%api_ver %_bindir/gst-tester-%api_ver}

%description
GStreamer Good Plug-ins is is a set of plug-ins that the developers consider
to have good quality code, correct functionality, and their preferred license
(LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting
library).

%package qt5
Summary: Qt5 plugin for GStreamer
Group: System/Libraries
Requires: gst-plugins-base%api_ver >= %version

%description qt5
This package contains Qt5 GL plugin for Gstreamer.

%package qt6
Summary: Qt6 plugin for GStreamer
Group: System/Libraries
Requires: gst-plugins-base%api_ver >= %version

%description qt6
This package contains Qt6 Qml plugin for Gstreamer.


%package devel-doc
Summary: Development documentation for GStreamer Good plugins
Group: Development/Documentation
BuildArch: noarch
Provides: %_name-good-devel-doc = %EVR

%description devel-doc
This package contains development documentation for GStreamer Good Plugins

%prep
%setup -n %_name-good-%version

%build
%meson \
	-Dexamples=disabled \
	%{?_disable_check:-Dtests=disabled} \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_enable_debug:-Dgst_debug=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-good-%api_ver

%check
%__meson_test

%files -f %_name-good-%api_ver.lang
%_gst_libdir/*.so
%{?_enable_qt5:%exclude %_gst_libdir/libgstqmlgl.so}
%{?_enable_qt6:%exclude %_gst_libdir/libgstqml6.so}
%_gst_datadir/*
%doc AUTHORS NEWS README* RELEASE

%if_enabled qt5
%files qt5
%_gst_libdir/libgstqmlgl.so
%endif

%if_enabled qt6
%files qt6
%_gst_libdir/libgstqml6.so
%endif


%if_enabled doc
%files devel-doc
%_gtk_docdir/*
%endif

%changelog
* Wed Aug 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.7-alt1
- 1.24.7

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

* Thu Jan 04 2024 Michael Shigorin <mike@altlinux.org> 1.22.8-alt1.1
- fix check knob (looks like current meson default is to enable it)

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
- new qt6 subpackage

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

* Sun Oct 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- enabled twolame mp2 audio encoder plugin 

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.1
- mike@: disable BR: valgrind-tool-devel on non-primary arches (rather missing)

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt2
- new -qt5 subpackage (ALT #36313)

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Tue Feb 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt2
- rebuild against libvpx.so.6

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- rebuild against libvpx.so.5

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

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.12.2-alt2
- BOOTSTRAP: introduce jack, pulse knobs (on by default)

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

* Sat Mar 12 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libvpx.so.3

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

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt2
- 1.0.3

* Tue Nov 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- built lost vp8 plugins

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

