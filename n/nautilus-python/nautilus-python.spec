%def_disable snapshot
%define ver_major 4.0
%define beta %nil

%def_enable docs

Name: nautilus-python
Version: %ver_major
Release: alt1.1%beta

Summary: Python bindings for Nautilus
Group: Development/Python3
License: GPLv2+
Url: https://www.gnome.org/

Provides: python-module-nautilus = %version-%release
Obsoletes: python-module-nautilus

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define ext_api_ver 4
%define nautilus_extdir %_libdir/nautilus/extensions-%ext_api_ver
%define _pkgconfigdir %_datadir/pkgconfig

%add_python3_path %nautilus_extdir

%define nautilus_ver 43
%define pygobject_ver 3.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libnautilus-extension-%ext_api_ver) >= %nautilus_ver libnautilus-gir-devel
BuildRequires: python3-devel python3-module-pygobject3-devel >= %pygobject_ver
%{?_enable_docs:BuildRequires: gtk-doc}

%description
This package provides Python bindings for the Nautilus extension library.

%package devel
Summary: Development files for %name
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR
Provides: python-module-nautilus-devel = %EVR
Obsoletes: python-module-nautilus-devel

%description devel
Development files for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Python3
BuildArch: noarch
Conflicts: %name-devel < %version
Provides: python-module-nautilus-devel-doc = %EVR
Obsoletes: python-module-nautilus-devel-doc

%description devel-doc
Development documentation for %name.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_docs:-Ddocs=enabled}
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_datadir/nautilus-python/extensions/__pycache__

%files
%nautilus_extdir/lib%name.so
%dir %_datadir/nautilus-python/extensions
%dir %_datadir/nautilus-python/extensions/__pycache__

%files devel
%_pkgconfigdir/%name.pc
%doc README* AUTHORS NEWS* examples

%if_enabled docs
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%exclude %_docdir/%name

%changelog
* Fri Aug 04 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1.1
- packaged /usr/share/nautilus-python/extensions/__pycache__ (ALT# 47116)

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Mon Feb 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt2
- Fixed build with gcc10.

* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- updated to NAUTILUS_PYTHON_1_2_2-11-g13d40c1
- switched to python3

* Mon Jan 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- fixed %%add_python_lib_path

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- build with pygobject3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.1
- Rebuild with Python-2.7

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- build for nautilus-3
- only dir /usr/share/nautilus-python/extensions for arch-independent extensions

* Mon Jun 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Mon Jul 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt2
- rename python-module-nautilus to nautilus-python
- cleanup spec
- fix path for nautilus-python extentions

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- new version
- new devel-doc noarch subpackage

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Jan 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus
