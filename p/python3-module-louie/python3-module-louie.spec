%define modname Louie
%define pypi_name louie

%def_enable check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Dispatches signals between Python objects in a wide variety of contexts
License: BSD
Group: Development/Python3
Url: https://pylouie.org/

Source: https://cheeseshop.python.org/packages/source/L/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest)}

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the
Python Cookbook.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3 %pypi_name/test

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%modname-%version.dist-info/
#%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sat Jul 22 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

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

