%define oname pyrelic

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt2.git20150520
Summary: Python API Wrapper for NewRelic API
License: MIT / GPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pyrelic

# https://github.com/andrewgross/pyrelic.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-requests
BuildRequires: python-module-sure
BuildRequires: python-module-nose python-module-coverage
BuildRequires: python-module-httpretty
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-requests
BuildRequires: python3-module-sure
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-httpretty
BuildRequires: python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-unittest2
%endif

%py_provides %oname
%py_requires six requests

%description
A New Relic client library written in Python.

%if_with python3
%package -n python3-module-%oname
Summary: Python API Wrapper for NewRelic API
Group: Development/Python3
%py3_provides %oname
%py3_requires six requests

%description -n python3-module-%oname
A New Relic client library written in Python.
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
python setup.py test -v
#make run_test suite=unit
%make run_test suite=fixtures
%if_with python3
pushd ../python3
python3 setup.py test -v
#make run_test suite=unit NOSETESTS=nosetests3
%make run_test suite=fixtures NOSETESTS=nosetests3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt2.git20150520
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20150520.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20150520.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150520
- Initial build for Sisyphus

