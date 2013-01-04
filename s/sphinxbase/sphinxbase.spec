Name: sphinxbase
Version: 0.8
Release: alt1

Summary: Base files of CMU Sphinx Recognition System

Group: Sound
License: BSD-style (see COPYING)
Url: http://cmusphinx.sourceforge.net/

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Tue Feb 24 2009
BuildRequires: python-module-setuptools

%description
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.

This package will install the sphinx3 library and some examples.

%package -n lib%name
Summary: %name shared library
Group: Sound

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Headers for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers for building software that uses %name

%prep
%setup

%build
%configure
%make_build

%install
install -d %buildroot%python_sitelibdir
PYTHONPATH=%buildroot%python_sitelibdir %make_install DESTDIR=%buildroot install

%files
%_bindir/sphinx*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Fri Jan 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- 0.8

* Mon Mar 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.1-alt2
- Add libsphinxbase and libsphinxbase-devel subpackages (Closes: #13980)

* Tue Feb 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Sep 08 2008 Denis Klimov <zver@altlinux.ru> 0.3-alt2
- fix directory ownership violation

* Tue Jan 08 2008 Denis Klimov <zver@altlinux.org> 0.3-alt1
- initial build for ALT Linux
