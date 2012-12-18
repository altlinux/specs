%define _name pyatspi
%define ver_major 2.7

Name: python3-module-%_name
Version: %ver_major.2
Release: alt1
Summary: Python bindings for at-spi library

Group: Development/Python
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: %_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pygobject3-devel >= 3.0.1
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

%package samples
Summary: Python bindings for at-spi library
Group: Development/Python
Requires: %name = %version-%release

%description samples
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes the sample programs.

%prep
%setup -n %_name-%version

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot pythondir=%python3_sitelibdir install

%files
%python3_sitelibdir/%_name/
%doc AUTHORS README NEWS

%files samples
%_bindir/magFocusTracker.py

%changelog
* Tue Dec 18 2012 Paul Wolneykien <manowar@altlinux.ru> 2.7.2-alt1
- Switch to Python 3.
- Upstream version 2.7.2.

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

