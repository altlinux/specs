%def_disable snapshot
%def_enable x11
%def_enable check

Name: libxkbcommon
Version: 0.10.0
Release: alt1

Summary: X.Org X11 XKB parsing library
Group: System/Libraries
License: MIT
Url: http://www.xkbcommon.org

%if_disabled snapshot
Source: %url/download/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): meson
BuildRequires: bison flex
BuildRequires: xkeyboard-config-devel
%{?_enable_x11:BuildRequires: pkgconfig(xcb) pkgconfig(xcb-xkb) >= 1.10}
BuildRequires: doxygen
# since 7.0 for wayland utilities
BuildRequires: wayland-devel >= 1.14 libwayland-client-devel wayland-protocols >= 1.10

%description
%name is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary: X.Org X11 XKB parsing development package
Group: Development/C
Requires: %name = %version-%release

%description devel
X.Org X11 XKB parsing development package

%package x11
Summary: X.Org X11 XKB keymap creation library
Group: System/Libraries
Requires: %name = %version-%release

%description x11
%name-x11 is the X.Org library for creating keymaps by querying the X
server.

%package x11-devel
Summary: X.Org X11 XKB keymap creation library
Group: System/Libraries
Requires: %name-x11 = %version-%release
Requires: %name-devel = %version-%release

%description x11-devel
X.Org X11 XKB keymap creation library development package

%prep
%setup

%build
%meson \
	-Ddefault_library=shared \
	%{?_disable_x11:-Ddisable-x11}
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%doc LICENSE NEWS README*
%_libdir/libxkbcommon.so.*

%files devel
%_libdir/libxkbcommon.so
%dir %_includedir/xkbcommon/
%_includedir/xkbcommon/xkbcommon.h
%_includedir/xkbcommon/xkbcommon-compat.h
%_includedir/xkbcommon/xkbcommon-compose.h
%_includedir/xkbcommon/xkbcommon-keysyms.h
%_includedir/xkbcommon/xkbcommon-names.h
%_pkgconfigdir/xkbcommon.pc
%doc %_datadir/doc/%name/

%if_enabled x11
%files x11
%_libdir/libxkbcommon-x11.so.*

%files x11-devel
%_libdir/libxkbcommon-x11.so
%_includedir/xkbcommon/xkbcommon-x11.h
%_pkgconfigdir/xkbcommon-x11.pc
%endif

%changelog
* Mon Jan 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Oct 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Feb 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt1
- updated to 0.8.4-1-g9badb4e

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Mon Aug 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Tue Jan 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_1
- update to new release by fcimport

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- update to new release by fcimport

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_2
- fixed build

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_1
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_8.20120917
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_7.20120306
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_6.20120306
- update to new version

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_4.20111109
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_3.20111109
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_3.20111109
- initial import by fcimport

