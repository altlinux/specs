%define _name libmbim

Name: %_name-glib
Version: 1.12.4
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
BuildRequires: gtk-doc help2man

%description
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM modem protocol helper library.

%package utils
Summary: MBIM command line utilities
License: %gpl2plus
Group: System/Base
Requires: %name = %version-%release

%description utils
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM command line utilities.

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

# Fix mbimcli name in the man page
sed -i 's;lt\\-mbimcli;mbimcli;' docs/man/mbimcli.1

%install
%makeinstall_std

%check
make check

%files
%_libdir/*.so.*
%_libexecdir/mbim-proxy

%files utils
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*


%changelog
* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 1.12.4-alt1
- Updated to 1.12.4.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- Updated to 1.10.2.

* Tue Aug 05 2014 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Tue Mar 11 2014 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Wed Dec 18 2013 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Wed Jul 03 2013 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Fri Jun 14 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Improve descriptions.
- Updated to 1.2.0.

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Use G_GUINT64_FORMAT for printing speed values.
- Initial build.
