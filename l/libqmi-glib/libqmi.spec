%define _name libqmi

Name: %_name-glib
Version: 1.2.0
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
BuildRequires: python-modules-json
BuildRequires: gtk-doc

%description
QMI modem protocol helper library

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
	--with-docs \
	--with-tests
%make_build

%install
%makeinstall_std

%check
make check

%files
%_libdir/*.so.*

%files utils
%_bindir/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*


%changelog
* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- devel-doc subpackage: Fix group.
- Package doc subpackage as noarch.
- Updated to 1.2.0.

* Mon Feb 25 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Initial build.

