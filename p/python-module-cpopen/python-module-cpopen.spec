%define _name cpopen

Name: python-module-%_name
Version: 1.4
Release: alt1

Summary: A C reimplementation of the tricky bits of Python's Popen
Group: Development/Python
License: GPLv2+
Url: http://pypi.python.org/pypi/%_name

Source: http://bronhaim.fedorapeople.org/%_name-%version.tar.gz

BuildRequires: python-devel

%description
Python package for creating sub-process in simpler and safer manner by
using C code.

%prep
%setup -n %_name-%version

%build
%python_build

%install
%__python setup.py install --root %buildroot

%files
%dir %python_sitelibdir/%_name
%python_sitelibdir/%_name/%_name.so
%python_sitelibdir/%_name/__init__.py*
%python_sitelibdir/%_name-%version-py*.egg-info
%doc AUTHORS README PKG-INFO

%changelog
* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- first build for Sisyphus

