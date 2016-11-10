%define _name libqmi

Name: %_name-glib
Version: 1.16.2
Release: alt1

Summary: QMI modem protocol helper library
License: %lgpl2plus
Group: System/Libraries
URL: http://cgit.freedesktop.org/libqmi
# git://anongit.freedesktop.org/libqmi
Source: %name-%version.tar

Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: glib2-devel libgio-devel
BuildRequires: libmbim-glib-devel
BuildRequires: python-modules-json
BuildRequires: gtk-doc help2man

%define _unpackaged_files_terminate_build 1

%description
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

%package utils
Summary: QMI command line utilities
License: %gpl2plus
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
%autoreconf
%configure \
	--disable-static \
	--enable-mbim-qmux \
	--enable-gtk-doc
%make_build

# Fix qmicli name in the man page
sed -i 's;lt\\-qmicli;qmicli;' docs/man/qmicli.1

%install
%makeinstall_std

%check
make check

%files
%_libdir/*.so.*
%_libexecdir/qmi-proxy

%files utils
%_bindir/*
%_man1dir/qmicli.1*
%_man1dir/qmi-network.1*
%_datadir/bash-completion/completions/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*


%changelog
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

