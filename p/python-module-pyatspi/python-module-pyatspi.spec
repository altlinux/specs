%define _name pyatspi
%define ver_major 2.20

Name: python-module-%_name
Version: %ver_major.3
Release: alt1

Summary: Python bindings for at-spi library
Group: Development/Python
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildArch: noarch

BuildRequires: python-devel python-module-pygobject3-devel >= 3.9.90
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel >= 3.9.90
BuildRequires: libX11-devel libICE-devel libSM-devel

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a python client library for at-spi.

%package -n python3-module-%_name
Summary: Python3 bindings for at-spi
Group: Development/Python3

%description -n python3-module-%_name
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package provides Python3 bindings for at-spi library.

%prep
%setup -n %_name-%version
%setup -D -c -n %_name-%version
mv %_name-%version py3build

%build
export PYTHON=%__python
%configure --with-python=python2
%make_build

pushd py3build
export PYTHON=python3
%autoreconf
%configure --with-python=python3
%make_build
popd

%install
%makeinstall_std

pushd py3build
%makeinstall_std
popd

%files
#%_bindir/magFocusTracker.py
%python_sitelibdir/%_name/
%doc AUTHORS README NEWS

%files -n python3-module-%_name
%python3_sitelibdir/%_name/
%doc AUTHORS README NEWS

%changelog
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

