%define oname nose-watch

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.1
Summary: A nose plugin that re-runs test suite on filesystem event
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose-watch/

# https://github.com/lukaszb/nose-watch.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-watchdog
BuildRequires: python-module-mock
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-watchdog
BuildRequires: python3-module-mock
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-pytest
%endif

%py_provides nosewatch
%py_requires nose watchdog

%description
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

%if_with python3
%package -n python3-module-%oname
Summary: A nose plugin that re-runs test suite on filesystem event
Group: Development/Python3
%py3_provides nosewatch
%py3_requires nose watchdog

%description -n python3-module-%oname
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
rm -fR build
py.test -vv

%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.dev.git20130219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1.dev.git20130219.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.dev.git20130219
- Initial build for Sisyphus

