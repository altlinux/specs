%def_disable snapshot

%define ver_major 2.6
%define sover 9
%def_disable docs

%ifnarch %valgrind_arches
%def_disable tests
%def_disable check
%else
%def_disable tests
%def_enable check
%endif

Name: libwacom
Version: %ver_major.0
Release: alt1

Summary: A Wacom tablets library
Group: System/Libraries
License: MIT
Url: https://github.com/linuxwacom/libwacom

%if_disabled snapshot
Source: %url/releases/download/%name-%version/%name-%version.tar.xz
%else
Vcs: https://github.com/linuxwacom/libwacom.git
Source: %name-%version.tar
%endif

Requires: %name-data = %version-%release
Requires: python3-module-pyudev python3-module-libevdev

BuildRequires(pre): rpm-macros-meson rpm-macros-valgrind rpm-build-python3
BuildRequires: /proc meson glib2-devel libgudev-devel libxml2-devel
%{?_enable_docs:BuildRequires: doxygen graphviz}
%{?_enable_tests:
BuildRequires: python3-module-pytest
BuildRequires: udev libudev-devel python3-module-pyudev
BuildRequires: libevdev-devel python3-module-libevdev
BuildRequires: valgrind}

%description
%name is a library to identify Wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package data
Summary: Tablets data for %name
Group: System/Libraries
BuildArch: noarch

%description data
%name is a library to identify wacom tablets and their model-specific
features.

This package contains tablets/stylus data for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%prep
%setup
%{?_enable_tests:sed -i 's/pytest-3/py.test-3/' meson.build}

%build
%meson \
    -Dudev-dir='/lib/udev' \
    %{?_disable_docs:-Ddocumentation=disabled} \
    %{?_disable_tests:-Dtests=disabled} \
    %{?optflags_lto:-Db_lto=true}
%nil
%meson_build

%install
%meson_install
# since 1.9 libwacom can read tablet and stylus files from /etc/libwacom
mkdir -p %buildroot%_sysconfdir/%name

%check
%__meson_test

%files
%dir %_sysconfdir/%name
%_bindir/%name-list-local-devices
%_bindir/%name-list-devices
%_bindir/%name-update-db
%_bindir/%name-show-stylus
%_libdir/*.so.%{sover}*
%_udevrulesdir/65-libwacom.rules
%_man1dir/libwacom-list-local-devices.1*
%_man1dir/libwacom-list-devices.1*
%doc NEWS README* COPYING

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files data
%dir %_datadir/%name
%_datadir/%name/*.tablet
%_datadir/%name/*.stylus
%_datadir/%name/layouts/
%_udevhwdbdir/65-%name.hwdb

#%files devel-doc
#%_datadir/gtk-doc/html/*

%changelog
* Tue Jan 24 2023 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Oct 18 2022 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt2
- explicitly required python3{libev,pyu}dev for libwacom-show-stylus

* Fri Oct 14 2022 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Thu Jul 28 2022 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Tue Apr 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1.1
- spec: fixed typo

* Fri Apr 01 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0 (soname bumped)

* Mon Jan 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Wed Sep 01 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1.1
- rebuild with -Db_lto=true

* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt2
- BR: +rpm-build-python3

* Wed Apr 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Fri Jan 29 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Sat Dec 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1.1
- fixed BR with disabled %%check

* Thu Dec 17 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7

* Tue Nov 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Mon Aug 31 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Tue Jun 30 2020 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Jun 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3
- built with Meson instead of Autotools
- introduced "docs" knob
- fixed License tag

* Mon Dec 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Tue Aug 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.33-alt1
- 0.33

* Mon Nov 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.32-alt1
- 0.32

* Sat Aug 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.31-alt1
- 0.31

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30-alt1
- 0.30 (new %%url)

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29-alt1
- 0.29

* Sat Feb 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1
- 0.28

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27-alt1
- 0.27

* Sun Aug 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25

* Sun Feb 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Sun Jan 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Sun Jul 24 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- 0.19

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Sun Nov 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Sat Jul 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Wed Jan 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Wed Feb 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Tue Jan 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

