Name: elementary
Version: 1.0.1
Release: alt1

Summary: Widget set based on the Enlightenment Foundation Libraries
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

Requires: %name-data = %version-%release
Requires: lib%name = %version-%release

BuildRequires: libecore-devel libeina-devel libeet-devel libedje-devel
BuildRequires: libevas-devel edje embryo_cc libeet-utils libeio-devel
BuildRequires: libethumb-devel libedbus-devel libefreet-devel libemotion-devel
BuildRequires: libSDL-devel doxygen

%description
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for
mobile and embedded devices. This package contains binary helpers and
data.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for mobile and embedded devices.
This package contains shared libraries.

%package data
Summary: noarch data for %name
Group: Graphical desktop/Enlightenment
BuildArch: noarch

%description data
The %name-data package contains architecture independent data files for
Elementary.

%package -n lib%name-devel
Summary: Development files for Elementary
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use Elementary libraries.


%prep
%setup -q

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*

%files data
%_datadir/%name/
%_desktopdir/*.desktop
%_iconsdir/*.png

%files -n lib%name
%_libdir/lib%{name}*.so.*
%_libdir/edje/modules/elm/*/*.so
%_libdir/%name/modules/test_entry/*/*.so
%_libdir/%name/modules/access_output/*/*.so
%_libdir/%name/modules/test_map/*/*.so
%_libdir/%name/modules/datetime_input_ctxpopup/*/*.so
%doc COPYING

%exclude %_libdir/*.la
%exclude %_libdir/edje/modules/elm/*/*.la
%exclude %_libdir/%name/modules/*/*/*.la

%files -n lib%name-devel
%_includedir/%{name}*/
%_libdir/lib%{name}*.so
%_libdir/%{name}_testql.so
%_pkgconfigdir/%{name}*.pc

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0.65643-alt1.1
- Removed bad RPATH

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0.65643-alt1
- 0.8.0.65643

* Sat Oct 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0.52995-alt1
- 0.7.0.52995

* Thu Feb 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0.63-alt1
- 0.6.0.63

* Thu Feb 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1
- Initial
