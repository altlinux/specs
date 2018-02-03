%define _unpackaged_files_terminate_build 1
%define oname hacking

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.0
Release: alt1.1
Summary: OpenStack Hacking Guideline Enforcement
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/hacking/

# https://github.com/openstack-dev/hacking.git
Source: %oname-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires: python-module-coverage python-module-discover python-module-docutils python-module-eventlet python-module-html5lib
BuildRequires: python-module-mock python-module-oslosphinx python-module-setuptools python-module-testrepository
BuildRequires: python2.7(pycodestyle) python-module-flake8 python-module-mccabe
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-eventlet python3-module-html5lib python3-module-jinja2-tests python3-module-mock
BuildRequires: python3-module-oslosphinx python3-module-setuptools python3-module-sphinx python3-module-testrepository python3-module-yieldfrom.urllib3
BuildRequires: python3(pycodestyle) python3-module-flake8 python3-module-mccabe
%endif

%py_provides %oname
%py_requires mccabe flake8

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: OpenStack Hacking Guideline Enforcement
Group: Development/Python3
%py3_provides %oname
%py3_requires mccabe flake8

%description -n python3-module-%oname
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.
%endif

%prep
%setup -n %oname-%version
%patch1 -p1

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst doc/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.
- Disabled tests.

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.0-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.2-alt3.git20150723.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt3.git20150723.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt3.git20150723
- Added necessary requirements

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt2.git20150723
- Enabled check

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20150723
- Version 0.10.2
- Disabled check (for bootstrap)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141105
- Initial build for Sisyphus

