%define _name elementary
%define ver_major 1.8
Name: %_name%ver_major
Version: %ver_major.3
Release: alt1

Summary: Widget set based on the Enlightenment Foundation Libraries
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%_name-%version.tar.bz2

BuildRequires: efl-libs-devel >= 1.8.3
BuildRequires: /proc dbus-tools-gui doxygen /usr/bin/convert

%description
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for
mobile and embedded devices. This package contains binary helpers and
data.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
Requires: %name-data = %version-%release
Conflicts: lib%_name < %version
#Obsoletes: lib%_name < %ver_major
Provides: lib%_name = %version-%release

%description -n lib%name
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for mobile and embedded devices.
This package contains shared libraries.

%package data
Summary: noarch data for %name
Group: Graphical desktop/Enlightenment
BuildArch: noarch
Obsoletes: %_name-data < %ver_major
Provides: %_name-data = %version-%release

%description data
The %name-data package contains architecture independent data files for
Elementary.

%package -n lib%name-devel
Summary: Development files for Elementary
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: lib%_name-devel < %ver_major
Provides: lib%_name-devel = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use Elementary libraries.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static
%make_build
%make doc

%install
%makeinstall_std

%find_lang %_name

%files -n lib%name
%_bindir/elementary_config
%_bindir/elementary_quicklaunch
%_bindir/elementary_run
%_libdir/lib%{_name}*.so.*
%_libdir/edje/modules/elm/*/*.so
%_libdir/%_name/modules/test_entry/*/*.so
%_libdir/%_name/modules/access_output/*/*.so
%_libdir/%_name/modules/test_map/*/*.so
%_libdir/%_name/modules/datetime_input_ctxpopup/*/*.so
%_libdir/%_name/modules/prefs/*/*.edj
%_libdir/%_name/modules/prefs/*/*.so
%doc README COPYING

%exclude %_libdir/edje/modules/elm/*/*.la
%exclude %_libdir/%_name/modules/*/*/*.la

%files -n lib%name-devel
%_bindir/elementary_codegen
%_bindir/elementary_test
%_bindir/elm_prefs_cc
%_includedir/%{_name}*/
%_libdir/lib%{_name}*.so
%_libdir/cmake/Elementary/
%_pkgconfigdir/%{_name}*.pc

%files data -f %_name.lang
%_datadir/%_name/
%_desktopdir/*.desktop
%_iconsdir/*.png

%changelog
* Fri Jan 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Sat Dec 21 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1
- obsoletes/provides elementary < 1.8

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon Nov 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.9-alt2
- rebuilt to remove poppler36 dependency

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.9-alt1
- 1.7.9

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.8-alt1
- 1.7.8

* Wed May 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.7-alt1
- 1.7.7

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.6-alt1
- 1.7.6

* Sat Jan 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Sat Dec 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

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
