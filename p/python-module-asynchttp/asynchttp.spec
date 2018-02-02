%define oname asynchttp

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20120701.1.1
Summary: A simple httplib2 based asynchronous HTTP library for python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/asynchttp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ross/python-asynchttp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-httplib2 python-module-coverage
BuildPreReq: python-module-mockito python-module-nose
BuildPreReq: python-module-unittest2 python-tools-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-httplib2 python3-module-coverage
BuildPreReq: python3-module-mockito python3-module-nose
BuildPreReq: python3-module-unittest2 python3-tools-pep8
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires httplib2

%description
asynchttp is an almost drop in replacement for httplib2 that provides
asynchronous http request behavior.

asynchttp uses python threading and Queues and provides callback
mechanisms to allow de-serialization and process to happen in the
background (worker threads) as well. You can queue up arbitrary numbers
of requests and a specified maximum number of workers will process each
request in turn.

%package -n python3-module-%oname
Summary: A simple httplib2 based asynchronous HTTP library for python
Group: Development/Python3
%py3_provides %oname
%py3_requires httplib2

%description -n python3-module-%oname
asynchttp is an almost drop in replacement for httplib2 that provides
asynchronous http request behavior.

asynchttp uses python threading and Queues and provides callback
mechanisms to allow de-serialization and process to happen in the
background (worker threads) as well. You can queue up arbitrary numbers
of requests and a specified maximum number of workers will process each
request in turn.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|coverage|coverage3|' ../python3/coverage.sh
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
python test.py
./coverage.sh
%if_with python3
pushd ../python3
python3 setup.py test
python3 test.py
./coverage.sh
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.4-alt1.git20120701.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20120701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120701
- Initial build for Sisyphus

