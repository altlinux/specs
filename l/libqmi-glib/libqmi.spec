%define _name libqmi
%define _libexecdir %prefix/libexec

%def_enable introspection

Name: %_name-glib
Version: 1.32.2
Release: alt1

Summary: QMI modem protocol helper library
License: LGPLv2+
Group: System/Libraries
URL: https://gitlab.freedesktop.org/mobile-broadband/libqmi
Vcs: https://gitlab.freedesktop.org/mobile-broadband/libqmi.git
Source: %name-%version.tar
Patch: %_name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: glib2-devel libgio-devel
BuildRequires: libmbim-glib-devel >= 1.18.0
BuildRequires: libgudev-devel
BuildRequires: libqrtr-glib-devel
BuildRequires: python3
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libqrtr-glib-gir-devel}
BuildRequires: gtk-doc help2man bash-completion

%define _unpackaged_files_terminate_build 1

%description
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

%package utils
Summary: QMI command line utilities
License: GPLv2+
Group: System/Base
Requires: %name = %version-%release

%description utils
QMI command line utilities

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: glib2-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
%summary

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
%summary

%package devel-doc
Summary: This package contains development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: %name-devel = %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup
%patch -p1
touch README ChangeLog

%build
%meson \
	-Dmbim_qmux=true \
	-Dfirmware_update=true \
	-Dudev=true \
	-Dqrtr=true \
%if_enabled introspection
    -Dintrospection=true \
%else
    -Dintrospection=false \
%endif
    -Dgtk_doc=true

%meson_build -v

%install
%meson_install

%check
%meson_test

%files
%doc NEWS README.md AUTHORS
%_libdir/*.so.*
%_libexecdir/qmi-proxy

%files utils
%_bindir/*
%_man1dir/qmi*.1*
%_datadir/bash-completion/completions/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Tue Nov 15 2022 Mikhail Efremov <sem@altlinux.org> 1.32.2-alt1
- Packaged NEWS, README.md and AUTHORS files.
- Updated to 1.32.2.

* Mon Nov 07 2022 Mikhail Efremov <sem@altlinux.org> 1.32.0-alt1
- Use meson build system.
- Dropped obsoleted patch.
- Updated to 1.32.0.

* Tue Jun 28 2022 Mikhail Efremov <sem@altlinux.org> 1.30.8-alt1
- Updated to 1.30.8.

* Wed May 11 2022 Mikhail Efremov <sem@altlinux.org> 1.30.6-alt1
- Updated to 1.30.6.

* Tue Feb 15 2022 Mikhail Efremov <sem@altlinux.org> 1.30.4-alt1
- Updated to 1.30.4.

* Wed Sep 15 2021 Mikhail Efremov <sem@altlinux.org> 1.30.2-alt1
- Use python3 everywhere.
- Do not add --no-as-needed to LDFLAGS.
- Dropped autoconf-archive from BR.
- Updated to 1.30.2.

* Fri Aug 13 2021 Mikhail Efremov <sem@altlinux.org> 1.28.8-alt1
- Updated to 1.28.8.

* Tue Jun 08 2021 Mikhail Efremov <sem@altlinux.org> 1.28.6-alt1
- Disabled gtkdocize in autoreconf.
- Updated to 1.28.6.

* Mon Mar 01 2021 Mikhail Efremov <sem@altlinux.org> 1.28.2-alt1
- Fixed build on armh.
- BR: requre autoconf-archive >= 2021.02.19-alt1.
- Dropped workaround for --no-as-needed.
- Updated to 1.28.2.

* Thu Feb 25 2021 Mikhail Efremov <sem@altlinux.org> 1.28.0-alt1
- Dropped --no-as-needed from LD_FLAGS.
- Fixed configure option.
- Updated Vcs and Url tags.
- Enabled libqrtr-glib support.
- Updated to 1.28.0.

* Fri Jan 22 2021 Mikhail Efremov <sem@altlinux.org> 1.26.8-alt1
- Updated to 1.26.8.

* Fri Oct 16 2020 Mikhail Efremov <sem@altlinux.org> 1.26.6-alt1
- Updated to 1.26.6.

* Tue Sep 22 2020 Mikhail Efremov <sem@altlinux.org> 1.26.4-alt1
- Updated to 1.26.4.

* Mon Jul 27 2020 Mikhail Efremov <sem@altlinux.org> 1.26.0-alt1
- Added autoconf-archive to BR.
- Enabled gobject-introspection support.
- Updated to 1.26.0.

* Tue May 12 2020 Mikhail Efremov <sem@altlinux.org> 1.24.12-alt1
- Updated to 1.24.12.

* Thu May 07 2020 Mikhail Efremov <sem@altlinux.org> 1.24.10-alt1
- Updated to 1.24.10.

* Wed Mar 18 2020 Mikhail Efremov <sem@altlinux.org> 1.24.8-alt1
- Updated to 1.24.8.

* Tue Mar 03 2020 Mikhail Efremov <sem@altlinux.org> 1.24.6-alt1
- Updated to 1.24.6.

* Tue Jan 21 2020 Mikhail Efremov <sem@altlinux.org> 1.24.4-alt1
- Updated to 1.24.4.

* Tue Dec 24 2019 Mikhail Efremov <sem@altlinux.org> 1.24.2-alt1
- Don't use rpm-build-licenses.
- Use RPMTAG_VCS.
- Updated to 1.24.2.

* Fri Sep 20 2019 Mikhail Efremov <sem@altlinux.org> 1.24.0-alt1
- Updated to 1.24.0.

* Thu Sep 12 2019 Mikhail Efremov <sem@altlinux.org> 1.22.6-alt1
- Updated to 1.22.6.

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 1.22.4-alt1
- Updated to 1.22.4.

* Tue Mar 12 2019 Mikhail Efremov <sem@altlinux.org> 1.22.2-alt1
- Updated to 1.22.2.

* Thu Jan 10 2019 Mikhail Efremov <sem@altlinux.org> 1.22.0-alt1
- Updated to 1.22.0.

* Wed Aug 29 2018 Mikhail Efremov <sem@altlinux.org> 1.20.2-alt1
- Use %%e2k macro.
- Updated to 1.20.0.

* Fri Jan 26 2018 Mikhail Efremov <sem@altlinux.org> 1.20.0-alt1
- Move qmi-proxy to %prefix/libexec.
- Updated to 1.20.0.

* Thu Jan 25 2018 Mikhail Efremov <sem@altlinux.org> 1.18.2-alt1
- Fix build on e2k.
- Updated to 1.18.2.

* Wed Apr 12 2017 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt2
- utils: drop useless g_file_test() call.

* Thu Apr 06 2017 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt1
- Fix qmi-firmware-update manpage.
- Updated to 1.18.0.

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 1.16.2-alt1
- Updated to 1.16.2.

* Tue Jul 19 2016 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt1
- Build with mbim-qmux support.
- Updated to 1.16.0.

* Thu Jun 09 2016 Mikhail Efremov <sem@altlinux.org> 1.14.2-alt1
- Updated to 1.14.2.

* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0.

* Mon Feb 29 2016 Mikhail Efremov <sem@altlinux.org> 1.12.8-alt1
- Updated to 1.12.8.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 1.12.6-alt1
- Updated to 1.12.6.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.12.4-alt1
- Updated to 1.12.4.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1.10.6-alt1
- Updated to 1.10.6.

* Fri Oct 24 2014 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt1
- Updated to 1.10.4.

* Mon Jul 14 2014 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Wed Dec 18 2013 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Update description.
- Updated to 1.8.0.

* Fri Sep 06 2013 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Build and package manpage for qmicli.
- Updated to 1.6.0.

* Fri Jun 14 2013 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- devel-doc subpackage: Fix group.
- Package doc subpackage as noarch.
- Updated to 1.2.0.

* Mon Feb 25 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Initial build.

