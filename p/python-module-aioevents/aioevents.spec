%define oname aioevents

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt2.git20140222.1
Summary: Events for asyncio (PEP 3156)
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/aioevents/

# https://github.com/astronouth7303/aioevents.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires asyncio

%description
Events for asyncio (PEP 3156).

%package -n python3-module-%oname
Summary: Events for asyncio (PEP 3156)
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Events for asyncio (PEP 3156).

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
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
py.test -vv
%endif
%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%if_with python2
%files
%doc *.md test.py
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md test.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.git20140222.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.git20140222
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140222.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140222
- Initial build for Sisyphus

