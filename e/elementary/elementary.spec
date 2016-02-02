%define _unpackaged_files_terminate_build 1
%define ver_major 1.17
%define beta %nil

Name: elementary
Version: %ver_major.0
Release: alt1

Summary: Widget set based on the Enlightenment Foundation Libraries
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org

Source: http://download.enlightenment.org/rel/libs/%name/%name-%version%beta.tar.xz
# ef4c303
#Source: %name-%version.tar

BuildRequires: efl-libs-devel >= %ver_major.0
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
Obsoletes: lib%{name}1.8
Provides:  lib%{name}1.8 = %version-%release

%description -n lib%name
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for mobile and embedded devices.
This package contains shared libraries.

%package data
Summary: noarch data for %name
Group: Graphical desktop/Enlightenment
BuildArch: noarch
Obsoletes: %{name}1.8-data
Provides:  %{name}1.8-data = %version-%release

%description data
The %name-data package contains architecture independent data files for
Elementary.

%package -n lib%name-devel
Summary: Development files for Elementary
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: lib%{name}1.8-devel
Provides:  lib%{name}1.8-devel = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use Elementary libraries.

%prep
%setup -n %name-%version%beta

%build
%autoreconf
%configure --disable-static
%make_build
%make doc

%install
%makeinstall_std

%find_lang %name

%files -n lib%name
%_bindir/elementary_config
%_bindir/elementary_quicklaunch
%_bindir/elementary_run
%_libdir/lib%{name}*.so.*
%_libdir/edje/modules/elm/*/*.so
%_libdir/%name/modules/test_entry/*/*.so
%_libdir/%name/modules/access_output/*/*.so
%_libdir/%name/modules/test_map/*/*.so
%_libdir/%name/modules/datetime_input_ctxpopup/*/*.so
%_libdir/%name/modules/prefs/*/*.edj
%_libdir/%name/modules/prefs/*/*.so
%doc README COPYING

%exclude %_libdir/edje/modules/elm/*/*.la
%exclude %_libdir/%name/modules/*/*/*.la

%files -n lib%name-devel
%_bindir/elementary_codegen
%_bindir/elementary_test
%_bindir/elm_prefs_cc
%_includedir/%{name}*/
%_libdir/lib%{name}*.so
%_libdir/cmake/Elementary/
%_pkgconfigdir/%{name}*.pc
%_datadir/eolian/include/*

%files data -f %name.lang
%_datadir/%name/
%_desktopdir/*.desktop
%_iconsdir/*.png

%changelog
* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Dec 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0 release

* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt0.1
- 1.16.0-beta3

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0 release

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt0.2
- 1.15.0 beta2

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0 release

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt0.1
- 1.14.0_ef4c303

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2_d0a22099

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.5-alt1
- 1.11.5

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.4-alt1
- 1.11.4

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Jul 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

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
