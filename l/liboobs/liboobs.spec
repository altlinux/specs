Name: liboobs
Version: 2.30.1
Release: alt1

Summary: GObject based interface to system-tools-backends - shared library
License: GPL
Group: System/Libraries
Url: http://ftp.gnome.org/pub/gnome/sources/liboobs
Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: rpm-build-gnome gnome-common

BuildRequires: libdbus-devel libdbus-glib-devel libhal-devel system-tools-backends-devel gtk-doc

%description
Liboobs is a lightweight library that provides a GObject based interface
to system-tools-backends. It's completely abstracted of the
communication and authentication details, making it easy for
applications to integrate with the system details.
This package contains the shared library.

%package devel
Summary: GObject based interface to system-tools-backends - development files
Group: Development/C
PreReq: %name = %version-%release

%description devel
Liboobs is a lightweight library that provides a GObject based interface
to system-tools-backends. It's completely abstracted of the
communication and authentication details, making it easy for
applications to integrate with the system details.
This package contain development files.

%package docs
Summary: GObject based interface to system-tools-backends - documentation
Group: Development/Documentation
PreReq: %name = %version-%release

%description docs
Liboobs is a lightweight library that provides a GObject based interface
to system-tools-backends. It's completely abstracted of the
communication and authentication details, making it easy for
applications to integrate with the system details.
This package contain documentation files.

%prep
%setup -q

%build
%autoreconf
%configure --disable-static --enable-gtk-doc
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-1.so.*

%files devel
%_includedir/%name-1.0
%_libdir/pkgconfig/%name-1.pc
%_libdir/%name-1.so
%doc AUTHORS ChangeLog NEWS COPYING README

%files docs
%_datadir/gtk-doc/html/%name

%changelog
* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 2.30.1-alt1
- New version 2.30.1

* Sat Apr 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.30.0-alt1
- New version 2.30.0

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 2.29.92-alt1
- New version 2.29.92

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 2.29.91-alt1
- New version 2.29.91

* Sun Jan 24 2010 Vladimir Lettiev <crux@altlinux.ru> 2.29.2.1-alt1
- New version 2.29.2.1

* Mon Dec 28 2009 Vladimir Lettiev <crux@altlinux.ru> 2.29.1-alt1
- new version

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 2.22.2-alt1
- new version

* Wed Sep 17 2008 Vladimir Lettiev <crux@altlinux.ru> 2.22.0-alt1
- Initial build for Sisyphus

