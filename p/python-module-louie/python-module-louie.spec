%define _name Louie

Name: python-module-louie
Version: 1.1
Release: alt1.1.1

Summary: Dispatches signals between Python objects in a wide variety of contexts
License: BSD
Group: Development/Python
Url: http://pylouie.org/
Packager: Yuri N. Sedunov <aris@altlinux.org>

Source: http://cheeseshop.python.org/packages/source/L/Louie/Louie-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python rpm-build-compat
BuildRequires: python-devel python-module-setuptools

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the
Python Cookbook.

%prep
%setup -q -n %_name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/Louie-*.egg-info/
%python_sitelibdir/louie/
%doc doc/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- adopted for Sisyphus

* Tue Aug 28 2007 Matthias Saou <http://freshrpms.net/> 1.1-2
- Update python-setuptools build requirement to new python-setuptools-devel.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.1-1
- Initial RPM release.

