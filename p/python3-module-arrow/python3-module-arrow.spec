%define modname arrow
%def_disable docs
#24 failed, 1674 passed, 2 xfailed, 14 errors in 20.22s
%def_disable check

Name: python3-module-%modname
Version: 1.2.2
Release: alt1

Summary: Better dates & times for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/arrow/

Vcs: https://github.com/crsmithdev/arrow.git
Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-dateutil python3-module-nose
BuildRequires: python3-module-chai
BuildRequires: python3-module-simplejson
BuildRequires: python3-module-mock python3-module-dateparser >= 0.7.2
%{?_enable_docs:
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx python3-module-sphinx-autodoc-typehints}
%{?_enable_check:BuildRequires: python3-module-tox}

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%prep
%setup -n %modname-%version

sed -i 's/pytest/py.test3/' tox.ini

%build
%python3_build_debug

%install
%python3_install

%if_enabled docs
export PYTHONPATH=%buildroot%python3_sitelibdir
SPHINXBUILD=sphinx-build-3 %make -C docs html
mkdir man
cp -fR docs/_build/html/* man/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
tox.py3 -e py%(echo %__python3_version | tr -d .) --sitepackages -o -v

%files
%python3_sitelibdir/*
%doc *.rst LICENSE
%{?_enable_docs: man/}

%changelog
* Fri Jan 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Oct 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Aug 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1.1
- fixed BR

* Fri Jun 25 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Apr 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Mar 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt2
- NMU: drop unneeded nose-cov buildrequires

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Sat Sep 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

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

