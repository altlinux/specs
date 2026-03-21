%define _name pyatspi
%define ver_major 2.58

%def_enable tests
%def_enable check

Name: python3-module-%_name
Version: %ver_major.2
Release: alt1

Summary: Python bindings for at-spi library
Group: Development/Python3
License: LGPL-2.0-only
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Vcs: https://gitlab.gnome.org/GNOME/pyatspi2.git

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildArch: noarch

%define pygobject_ver 3.9.90

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson python3-module-pygobject3-devel >= %pygobject_ver
%{?_enable_tests:BuildRequires: python3(dbus) pkgconfig(atk)
BuildRequires: pkgconfig(atspi-2) pkgconfig(atk-bridge-2.0) libxml2-devel}
%{?_enable_check:BuildRequires: xvfb-run /proc dbus at-spi2-core typelib(Atspi) = 2.0}

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a Python 3 client library for at-spi.

%prep
%setup -n %_name-%version

%build
%meson \
    %{subst_enable_meson_bool tests enable_tests}
%nil
%meson_build

%install
%meson_install

%check
xvfb-run %__meson_test

%files
%python3_sitelibdir/%_name/
%doc AUTHORS README* NEWS


%changelog
* Sat Mar 21 2026 Yuri N. Sedunov <aris@altlinux.org> 2.58.2-alt1
- 2.58.2

* Sun Jan 18 2026 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt1
- 2.58.1
- enabled %%check

* Wed Sep 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.58.0-alt1
- 2.58.0

* Sat Jan 06 2024 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Thu Dec 09 2021 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Sun Mar 14 2021 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 2.20.0-alt2
- NMU removed incorrect LD_PRELOADS from noarch package

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.18.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

