%def_enable snapshot

%define _name harfbuzz
%define ver_major 6.0
%def_with graphite2
%def_with icu
%def_with gobject
%def_enable introspection
%def_enable docs
%def_disable experimental_api

%ifnarch armh
%def_enable check
%endif

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: HarfBuzz is an OpenType text shaping engine
Group: System/Libraries
License: MIT
Url: http://harfbuzz.org/

%if_disabled snapshot
Source: https://github.com/%_name/%_name/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/harfbuzz/harfbuzz.git
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson gcc-c++ glib2-devel libfreetype-devel libcairo-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_with_graphite2:BuildRequires: libgraphite2-devel}
%{?_with_icu:BuildRequires: libicu-devel}
%{?_enable_docs:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: python3-test fonttools}

%description
HarfBuzz is an implementation of the OpenType Layout engine.
This package provides shared HarfBuzz library.

%package icu
Summary: Shared HarfBuzz library with ICU support.
Group: System/Libraries
Requires: %name = %version-%release

%description icu
HarfBuzz is an implementation of the OpenType Layout engine.
This package provides shared HarfBuzz library with ICU support.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
%{?_with_icu:Requires: %name-icu = %version-%release}
%{?_with_gobject:Requires: %name-gobject = %version-%release}

%description devel
The %name-devel package contains files for developing applications that
use HarfBuzz library.

%package gobject
Summary: GObject bindings for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gobject
This package contains functionality to make HarfBuzz library
integrate well with the GObject object system used by GNOME.

%package devel-doc
Summary: Development documentation for Pango
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
HarfBuzz is an implementation of the OpenType Layout engine.
This package contains development documentation for HarfBuzz.

%package utils
Summary: Utilities from HarfBuzz project
Group: Development/Tools
Requires: %name = %version-%release

%description utils
The %name-utils package provides utilities from %name package.

%package gir
Summary: GObject introspection data for the HarfBuzz library
Group: System/Libraries
Requires: %name-gobject = %version-%release

%description gir
GObject introspection data for the HarfBuzz library

%package gir-devel
Summary: GObject introspection devel data for the HarfBuzz library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the HarfBuzz library

%prep
%setup -n %_name-%version

%build
%meson \
	-Dglib=enabled \
	-Dfreetype=enabled \
	-Dcairo=enabled \
	%{?_with_icu:-Dicu=enabled} \
	%{?_with_graphite2:-Dgraphite2=enabled} \
        %{?_enable_gobject:-Dgobject=enabled} \
        %{?_enable_introspection:-Dintrospection=enabled} \
	%{?_disable_docs:-Ddocs=disabled} \
	%{?_enable_experimental_api:-Dexperimental_api=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test -t 4

%files
%_libdir/%name.so.*
%_libdir/%name-subset.so.*

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_libdir/%name-subset.so
%if_with icu
%_libdir/%name-icu.so
%endif
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/%_name-icu.pc
%_pkgconfigdir/%_name-subset.pc
%_libdir/cmake/%_name/
%doc NEWS AUTHORS COPYING README
%if_with gobject
%_libdir/%name-gobject.so
%_pkgconfigdir/%_name-gobject.pc
%endif

%if_enabled docs
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_with icu
%files icu
%_libdir/%name-icu.so.*
%endif

%files utils
%_bindir/hb-view
%_bindir/hb-ot-shape-closure
%_bindir/hb-shape
%_bindir/hb-subset

%if_with gobject
%files gobject
%_libdir/%name-gobject.so.*
%endif

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif

%changelog
* Mon Dec 19 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- updated to 6.0.0-15-gc292e577f

* Sun Oct 23 2022 Yuri N. Sedunov <aris@altlinux.org> 5.3.1-alt1
- updated to 5.3.1-8-g83769b9cb

* Mon Sep 26 2022 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0

* Sun Jul 24 2022 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Wed Jun 29 2022 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt1
- updated to 4.4.1-2-g22835dea2
- introduced experimental API knob (disabled by default)

* Thu Jun 23 2022 Yuri N. Sedunov <aris@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Fri Apr 08 2022 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Mar 12 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sun Dec 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Nov 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Wed Sep 22 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Sep 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- 2.9.1 (ported to Meson build system)

* Fri Jul 09 2021 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Wed May 05 2021 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Wed Mar 24 2021 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Sun Dec 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.7.4-alt1
- 2.7.4

* Tue Sep 01 2020 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2
- updated BR for %%check

* Thu Jun 25 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6.8-alt1
- updated to 2.6.8-5-g20d1fa367

* Wed Jun 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6.7-alt1
- 2.6.7 (updated to Unicode-13.0.0)

* Wed Apr 15 2020 Alexey Shabalin <shaba@altlinux.org> 2.6.4-alt3
- build with gobject
- enable introspection

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt2
- build tools, tests switched to python3

* Thu Oct 31 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- 2.6.4

* Tue Oct 29 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Tue Oct 01 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Fri Aug 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Wed Aug 14 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Thu Jun 27 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- 2.5.3

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt1
- 2.5.2

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- 2.5.1

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt2
- mike@: drop e2k specifics, just build with lcc 1.23

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Fri Nov 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sat Oct 20 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- updated to 2.0.1-3-gf70f9941

* Mon Sep 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Aug 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.8-alt1
- 1.8.8

* Thu Aug 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt2
- rebuilt against libicu*.so.62

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Mar 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7.6-alt1
- 1.7.6

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt2
- rebuilt against libicu*.so.60

* Thu Dec 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Fri Dec 08 2017 Michael Shigorin <mike@altlinux.org> 1.7.2-alt2
- introduced icu knob (on by default)
- E2K: link against libcxa explicitly

* Mon Dec 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Nov 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Mon Nov 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Oct 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Oct 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Sep 05 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Aug 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Fri Aug 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.8-alt1
- 1.4.8

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt1
- 1.4.7

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Sat Mar 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Sun Feb 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Tue Jan 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Tue Dec 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4

* Wed Oct 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue Sep 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Thu Sep 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Thu Jul 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.7-alt1
- 1.2.7

* Sat Apr 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Tue Apr 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu Feb 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Feb 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Feb 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Feb 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3
- build against libicuuc.so.56

* Wed Dec 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Fri Oct 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Oct 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Aug 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Aug 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.41-alt1
- 0.9.41

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.40-alt1
- 0.9.40

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.39-alt1
- 0.9.39

* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.38-alt1
- 0.9.38

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.37-alt1
- 0.9.37

* Fri Nov 28 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.36-alt1
- 0.9.36

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.35-alt1
- 0.9.35

* Sat Aug 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.33-alt1
- 0.9.33

* Fri Jul 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.32-alt1
- 0.9.32

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.29-alt1
- 0.9.29

* Fri Apr 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.27-alt1
- 0.9.27
- used current automake

* Fri Jan 31 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.26-alt1
- 0.9.26

* Fri Nov 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.24-alt1
- 0.9.24
- enabled graphite2 support
- use automake_1.11

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.22-alt1
- 0.9.22

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.21-alt1
- 0.9.21
- new -devel-doc subpackage
- prepared -gir, gir-devel subpackages

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.18-alt1
- 0.9.18
- new lib%%name-icu{,-devel} subpackages

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.16-alt1
- 0.9.16

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.14-alt1
- 0.9.14

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.13-alt1
- 0.9.13

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12

* Thu Jan 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.11-alt1
- 0.9.11

* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- first build for Sisyphus

