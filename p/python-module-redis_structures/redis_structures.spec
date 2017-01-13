%define _unpackaged_files_terminate_build 1
%define oname redis_structures

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1
Summary: Redis data structures wrapped with Python 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/redis_structures/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jaredlunde/redis_structures.git
Source0: https://pypi.python.org/packages/14/ac/6b0b0a4a317683ed79ebdd089a294ee689415bf24457ec801bfb45a0fac1/%{oname}-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-redis-py python-module-ujson
#BuildPreReq: python-module-pip
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-redis-py python3-module-ujson
#BuildPreReq: python3-module-pip python-tools-2to3
%endif

%py_provides %oname
%py_requires redis ujson

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-logging python3 python3-base python3-module-OpenSSL python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-idna python3-module-lxml python3-module-ntlm python3-module-pluggy python3-module-py python3-module-pyasn1 python3-module-pycparser python3-module-setuptools python3-module-six xz
BuildRequires: python-modules-compiler python-modules-encodings python-tools-2to3 python3-module-html5lib python3-module-pip python3-module-pytest python3-module-redis-py python3-module-ujson rpm-build-python3 time

%description
Pythonic data structures backed by Redis.

%if_with python3
%package -n python3-module-%oname
Summary: Redis data structures wrapped with Python 3
Group: Development/Python3
%py3_provides %oname
%py3_requires redis ujson

%description -n python3-module-%oname
Pythonic data structures backed by Redis.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
2to3 -w -n %oname/__init__.py
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test -vv $(find %oname -name '*.py')
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv $(find %oname -name '*.py')
popd
%endif

%if_with python2
%files
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.a0.git20150318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.a0.git20150318.1
- NMU: Use buildreq for BR.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.a0.git20150318
- Initial build for Sisyphus

