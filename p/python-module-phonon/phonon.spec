%define _unpackaged_files_terminate_build 1
%define oname phonon

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0
Release: alt1
Summary: Provides easy, fault tolerant, distributed references with redis as a backend
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/phonon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/buzzfeed/phonon.git
Source0: https://pypi.python.org/packages/62/ae/8034ef638c285f35bc994b582a51455ee1f96da484f3ebb4e890f7cbfcaf/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-redis-py python-module-pytz
#BuildPreReq: python-module-mock python-module-dateutil
#BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-redis-py python3-module-pytz
#BuildPreReq: python3-module-mock python3-module-dateutil
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires redis pytz json logging dateutil

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-pbr python-module-pytest python-module-pytz python-module-unittest2 python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-pytz python3-module-unittest2 rpm-build-python3 time

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
%setup -q -n %{oname}-%{version}

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150212.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150212.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150212
- Initial build for Sisyphus

