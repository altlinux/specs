%define oname aiouv

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt2.git20150213.1
Summary: A PEP-3156 compatible event loop
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/aiouv/

# https://github.com/saghul/aiouv.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pyuv
%endif

%py_provides %oname
%py_requires asyncio pyuv

%description
libuv based event loop for asyncio.

%package -n python3-module-%oname
Summary: A PEP-3156 compatible event loop
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio pyuv

%description -n python3-module-%oname
libuv based event loop for asyncio.

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
python setup.py test
%endif

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt2.git20150213.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1-alt2.git20150213
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20150213.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20150213.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150213
- Initial build for Sisyphus

