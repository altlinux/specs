%define _name gstreamer
%define ver_major 1.24
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_disable doc
%def_disable debug
%def_disable libunwind
%def_disable libdw
%ifarch %e2k
%def_disable ptp_helper
%else
%def_enable ptp_helper
%endif
%def_disable check

Name: %_name%api_ver
Version: %ver_major.8
Release: alt1

Summary: GStreamer streaming media framework runtime
License: LGPLv2+
Group: System/Libraries
Url: http://gstreamer.freedesktop.org

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

Provides: %_name = %EVR

Requires(pre): libcap-utils
Requires: lib%name = %EVR

%define glib_ver 2.64.0
%define meson_ver 1.1

BuildRequires(pre): rpm-macros-meson >= %meson_ver rpm-build-gir rpm-build-python3
BuildRequires: meson flex gcc-c++
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: ghostscript-utils libcheck-devel libxml2-devel
BuildRequires: python-modules sgml-common transfig xml-utils gobject-introspection-devel
BuildRequires: libgsl-devel libgmp-devel
BuildRequires: libcap-devel libcap-utils
BuildRequires: bash-completion
%{?_enable_libunwind:BuildRequires: libunwind-devel}
%{?_enable_libdw:BuildRequires: libdw-devel}
%{?_enable_ptp_helper:BuildRequires: rust-cargo}
%{?_enable_doc:BuildRequires: hotdoc}

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package -n lib%name
Summary: Shared libraries of GStreamer
Group: System/Libraries
Provides: lib%_name = %EVR

%description -n lib%name
This package contains the shared libraries of the GStreamer media framework

%package -n lib%name-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Provides: lib%_name-gir = %EVR
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the GStreamer library

%package devel
Summary: Development files for GStreamer streaming-media framework
Group: Development/C
Provides: %_name-devel = %EVR
Requires: lib%name = %EVR

%description devel
This package contains the libraries and header files necessary to
develop applications and plugins for GStreamer

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Provides: lib%_name-gir-devel = %EVR
Requires: lib%name-gir = %EVR %name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the GStreamer library

%package devel-doc
Summary: Development documentation for GStreamer
Group: Development/C
BuildArch: noarch
Provides: %_name-devel-doc = %EVR

%description devel-doc
This package contains development documentation for GStreamer

%package utils
Summary: GStreamer utilities
Group: System/Libraries
Provides: %_name-utils = %EVR
Requires: lib%name = %EVR

%description utils
This package contains some utilities used to register, analyze, and run
Gstreamer plugins.

%prep
%setup -n %_name-%version

%build
%ifarch %e2k
# till lcc ~1.23
export LIBS=-lcxa
%endif
%meson \
	-Dpackage-name="GStreamer" \
	-Dpackage-origin=%name \
	-Dexamples=disabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_enable_debug:-Dgst_debug=true} \
	%{subst_enable_meson_feature ptp_helper ptp-helper} \
	%{?_enable_ptp_helper:-Dptp-helper-permissions="capabilities"}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver

%check
%__meson_test

%post
setcap cap_sys_nice,cap_net_bind_service,cap_net_admin+ep %_libexecdir/%_name-%api_ver/gst-ptp-helper{,-test} 2>/dev/null ||:

%files -f %_name-%api_ver.lang
%dir %_libexecdir/%_name-%api_ver
%_libexecdir/%_name-%api_ver/gst-plugin-scanner
%{?_enable_ptp_helper:%_libexecdir/%_name-%api_ver/gst-ptp-helper}
#%_libexecdir/%_name-%api_ver/gst-ptp-helper-test
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%doc AUTHORS NEWS README* RELEASE

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/Gst-%api_ver.typelib
%_typelibdir/GstBase-%api_ver.typelib
%_typelibdir/GstCheck-%api_ver.typelib
%_typelibdir/GstController-%api_ver.typelib
%_typelibdir/GstNet-%api_ver.typelib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*
%if_enabled debug
%_datadir/gdb/auto-load/%_libdir/lib%name-%api_ver.so.*-gdb.py
%_datadir/glib-2.0/gdb/glib_gobject_helper.py
%_datadir/glib-2.0/gdb/gst_gdb.py
%endif

%files -n lib%name-gir-devel
%_girdir/Gst-%api_ver.gir
%_girdir/GstBase-%api_ver.gir
%_girdir/GstCheck-%api_ver.gir
%_girdir/GstController-%api_ver.gir
%_girdir/GstNet-%api_ver.gir

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%files utils
%_bindir/gst-inspect-%api_ver
%_bindir/gst-launch-%api_ver
%_bindir/gst-stats-%api_ver
%_bindir/gst-tester-%api_ver
%_bindir/gst-typefind-%api_ver
%_man1dir/*
# bash-completions
%_libexecdir/%_name-%api_ver/gst-completion-helper
%_datadir/bash-completion/completions/gst-inspect-%api_ver
%_datadir/bash-completion/completions/gst-launch-%api_ver
%_datadir/bash-completion/helpers/gst
%_libexecdir/%_name-%api_ver/gst-hotdoc-plugins-scanner
%_libexecdir/%_name-%api_ver/gst-plugins-doc-cache-generator

%changelog
* Thu Sep 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.8-alt1
- 1.24.8

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

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1.1
- fixed "ptp_helper" knob (disabled by default for %%e2k)

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

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1
- 1.18.5

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt2
- BR: +rpm-build-python3

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

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Wed Feb 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt2
- packaged bash-completions

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

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt2
- rebuilt --with-ptp-helper-permissions=capabilities (ALT #33909)

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3
- mike@:
  E2K:
  initial architecture support
  force linking against -lcxa

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

