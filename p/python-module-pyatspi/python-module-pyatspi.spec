%define _name pyatspi
%define ver_major 2.4

Name: python-module-%_name
Version: %ver_major.0
Release: alt1
Summary: Python bindings for at-spi library

Group: Development/Python
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/sources/%name/%ver_major/%_name-%version.tar.xz

BuildArch: noarch

BuildRequires: python-module-pygobject3-devel >= 3.1.0
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

%prep
%setup -n %_name-%version

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%python_sitelibdir/%_name/
%doc AUTHORS README NEWS

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

