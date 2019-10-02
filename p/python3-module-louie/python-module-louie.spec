%define _name Louie

Name: python3-module-louie
Version: 2.0
Release: alt1

Summary: Dispatches signals between Python objects in a wide variety of contexts
License: BSD
Group: Development/Python3
Url: http://pylouie.org/

Source: http://cheeseshop.python.org/packages/source/L/Louie/Louie-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the
Python Cookbook.

%prep
%setup -n %_name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/Louie-*.egg-info/
%python3_sitelibdir/louie/

%changelog
* Wed Oct 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- 2.0 with Python3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- adapted for Sisyphus

* Tue Aug 28 2007 Matthias Saou <http://freshrpms.net/> 1.1-2
- Update python-setuptools build requirement to new python-setuptools-devel.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.1-1
- Initial RPM release.

