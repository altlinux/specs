%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name xkbcommon

%def_enable x11
%def_enable xkbregistry
%def_enable docs
%def_enable check

Name: lib%_name
Version: 1.5.0
Release: alt1

Summary: X.Org X11 XKB parsing library
Group: System/Libraries
License: MIT
Url: https://www.xkbcommon.org

%if_disabled snapshot
Source: %url/download/%name-%version.tar.xz
#Source: https://github.com/xkbcommon/libxkbcommon/archive/%_name-%version.tar.gz
%else
Vcs: https://github.com/xkbcommon/libxkbcommon.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.51 bison flex
BuildRequires: xkeyboard-config-devel >= 2.29
# since 7.0 for wayland utilities
BuildRequires: wayland-devel >= 1.14 libwayland-client-devel wayland-protocols >= 1.10
%{?_enable_x11:BuildRequires: pkgconfig(xcb) pkgconfig(xcb-xkb) >= 1.10}
%{?_enable_xkbregistry:BuildRequires: libxml2-devel}
%{?_enable_docs:BuildRequires: doxygen}
%{?_enable_check:BuildRequires: python3-module-pytest %{?_enable_x11:xvfb-run}}

%description
%name is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary: X.Org X11 XKB parsing development package
Group: Development/C
Requires: %name = %EVR

%description devel
X.Org X11 XKB parsing development package

%package x11
Summary: X.Org X11 XKB keymap creation library
Group: System/Libraries
Requires: %name = %EVR

%description x11
%name-x11 is the X.Org library for creating keymaps by querying the X
server.

%package x11-devel
Summary: X.Org X11 XKB keymap creation library
Group: System/Libraries
Requires: %name-x11 = %EVR
Requires: %name-devel = %EVR

%description x11-devel
X.Org X11 XKB keymap creation library development package

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%package tools
Summary: Tools from %name package
Group: Development/Tools
Requires: %name = %EVR
Requires: %name-x11 = %EVR

%description tools
This package provides xkbcli -- tool to interact with XKB keymaps.

%prep
%setup

%build
%meson \
	-Ddefault_library=shared \
	%{?_disable_x11:-Denable-x11=false} \
	%{?_disable_xkbregistry:-Denable-xkbregistry=false} \
	%{?_disable_docs:-Denable-docs=false}
%nil
%meson_build

%install
%meson_install

%check
%{?_enable_x11:xvfb-run} %__meson_test

%files
%doc LICENSE NEWS README*
%_libdir/%name.so.*
%{?_enable_xkbregistry:%_libdir/libxkbregistry.so.*}

%files devel
%_libdir/%name.so
%dir %_includedir/%_name/
%_includedir/%_name/%_name.h
%_includedir/%_name/%_name-compat.h
%_includedir/%_name/%_name-compose.h
%_includedir/%_name/%_name-keysyms.h
%_includedir/%_name/%_name-names.h
%_pkgconfigdir/%_name.pc
%{?_enable_xkbregistry:%_libdir/libxkbregistry.so
%_includedir/%_name/xkbregistry.h
%_pkgconfigdir/xkbregistry.pc}

%{?_enable_docs:
%files devel-doc
%_datadir/doc/%name/}

%if_enabled x11
%files x11
%_libdir/%name-x11.so.*

%files x11-devel
%_libdir/%name-x11.so
%_includedir/%_name/%_name-x11.h
%_pkgconfigdir/%_name-x11.pc
%endif

%files tools
%_bindir/xkbcli
%dir %_libexecdir/%_name
%_libexecdir/%_name/xkbcli-*
%_man1dir/xkbcli*


%changelog
* Tue Jan 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sun May 22 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Sep 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- updated to 1.1.0-7-g21c864c
- new devel-doc subpackage

* Tue Nov 24 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- updated to 1.0.0-5-g534e54f
- new -tools subpackage
- updated BR

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

