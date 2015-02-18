%define oname phonon

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150212
Summary: Provides easy, fault tolerant, distributed references with redis as a backend
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/phonon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/buzzfeed/phonon.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-redis-py python-module-pytz
BuildPreReq: python-module-mock python-module-dateutil
BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-redis-py python3-module-pytz
BuildPreReq: python3-module-mock python3-module-dateutil
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires redis pytz json logging dateutil

%description
The main goals of the Phonon project are

1. Provide a high-level abstraction for easy coordination in Python
2. Fault tolerance for network partitions, single, and multi- node
   failures
3. Failover for unreachable hosts
4. High availability and linear scaling

%package -n python3-module-%oname
Summary: Provides easy, fault tolerant, distributed references with redis as a backend
Group: Development/Python3
%py3_provides %oname
%py3_requires redis pytz json logging dateutil

%description -n python3-module-%oname
The main goals of the Phonon project are

1. Provide a high-level abstraction for easy coordination in Python
2. Fault tolerance for network partitions, single, and multi- node
   failures
3. Failover for unreachable hosts
4. High availability and linear scaling

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
exit 1

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150212
- Initial build for Sisyphus

