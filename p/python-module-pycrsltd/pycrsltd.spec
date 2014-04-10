Name: python-module-pycrsltd
Version: 0.1
Release: alt1
Summary: Interface to CRS Ltd hardware (Bits++, ColorCal etc...).
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pycrsltd
Source: pycrsltd-%version.tar.gz
Buildarch: noarch

%setup_python_module pycrsltd

%description
PyCRSltd  is the central library for the python interface to CRS Ltd
hardware (Bits++, ColorCal etc...).

The library is very much under construction and should not be used yet
except by enthusiasts.

It is being written mostly by Jon Peirce, with support from CRS Ltd. If
you would like to contribute please get in touch!

%prep
%setup -n pycrsltd-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt
%python_sitelibdir/*pycrsltd*

%changelog
* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build from scratch

