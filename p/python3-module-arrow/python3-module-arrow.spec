%define modname arrow
%def_enable check

Name: python3-module-%modname
Version: 0.15.8
Release: alt1

Summary: Better dates & times for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/arrow/

# https://github.com/crsmithdev/arrow.git
Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-dateutil python3-module-nose
BuildPreReq: python3-module-nose-cov python3-module-chai
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-simplejson
BuildRequires: python3-module-mock python3-module-dateparser >= 0.7.2
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%prep
%setup -n %modname-%version

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
SPHINXBUILD=sphinx-build-3 %make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%check
python3 setup.py test

%files
%python3_sitelibdir/*
%doc *.rst LICENSE man/

%changelog
* Sun Jul 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.8-alt1
- 0.15.8

* Mon Jun 22 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.7-alt1
- 0.15.7

* Mon May 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.6-alt1
- 0.15.6 (python3 only)

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.15.5-alt1
- 0.15.5

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.15.4-alt1
- 0.15.4
- disabled python2 build

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.7-alt1
- 0.14.7

* Fri Aug 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.6-alt1
- 0.14.6

* Wed Aug 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.5-alt1
- 0.14.5
- made python2 build optional

* Mon Mar 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1.git20140812.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt1.git20140812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20140812
- Initial build for Sisyphus

