%define _unpackaged_files_terminate_build 1
%define oname redis_structures

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt2
Summary: Redis data structures wrapped with Python 3
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/redis_structures/

# https://github.com/jaredlunde/redis_structures.git
Source: %oname-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-redis-py python-module-ujson
BuildRequires: python-module-pip
BuildRequires: python-modules-compiler python-modules-encodings
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-redis-py python3-module-ujson
BuildRequires: python3-module-pip python-tools-2to3
BuildRequires: python3-module-html5lib python3-module-pytest
%endif

%py_provides %oname
%py_requires redis ujson

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
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.a0.git20150318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.a0.git20150318.1
- NMU: Use buildreq for BR.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.a0.git20150318
- Initial build for Sisyphus

