%define _name libmbim

Name: %_name-glib
Version: 1.0.0
Release: alt1

Summary: MBIM modem protocol helper library
License: %lgpl2plus
Group: System/Libraries
URL: http://cgit.freedesktop.org/libmbim/libmbim/
# git://anongit.freedesktop.org/libmbim/libmbim
Source: %name-%version.tar

Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: glib2-devel libgio-devel libgudev-devel
BuildRequires: python-modules-json
BuildRequires: gtk-doc

%description
MBIM modem protocol helper library

%package utils
Summary: MBIM command line utilities
License: %gpl2plus
Group: System/Base
Requires: %name = %version-%release

%description utils
MBIM command line utilities

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
	--enable-gtk-doc \
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
* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Use G_GUINT64_FORMAT for printing speed values.
- Initial build.
