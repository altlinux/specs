%define mname yieldfrom
%define oname %mname.http.client

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt2.git20150311.1
Summary: asyncio version of http.client
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.http.client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromHttplib.git
Source: %name-%version.tar

%if_with python2
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
Requires: python-module-%mname.http = %EVR
%py_requires asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-setuptools rpm-build-python3

%description
Asyncio conversion of http.client.

The classes are named the same as in http.client.

%package -n python3-module-%oname
Summary: asyncio version of http.client
Group: Development/Python3
Requires: python3-module-%mname.http = %EVR
%python3_req_hier

%description -n python3-module-%oname
Asyncio conversion of http.client.

The classes are named the same as in http.client.

%package -n python-module-%mname.http
Summary: Core files of %mname.http
Group: Development/Python
%py_provides %mname.http
%py_requires %mname

%description -n python-module-%mname.http
Core files of %mname.http.

%package -n python3-module-%mname.http
Summary: Core files of %mname.http
Group: Development/Python3
%py3_requires %mname

%description -n python3-module-%mname.http
Core files of %mname.http.

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

%if "%_libdir" != "%_libexecdir"
mv %buildroot%_libexecdir %buildroot%_libdir
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
%doc *.md
%python_sitelibdir/%mname/http/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/http/__init__.py*

%files -n python-module-%mname.http
%dir %python_sitelibdir/%mname/http
%python_sitelibdir/%mname/http/__init__.py*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/http/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/http/__init__.*
#exclude %python3_sitelibdir/%mname/http/__pycache__/__init__.*

%files -n python3-module-%mname.http
%dir %python3_sitelibdir/%mname/http
%dir %python3_sitelibdir/%mname/http/__pycache__
%python3_sitelibdir/%mname/http/__init__.*
#python3_sitelibdir/%mname/http/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt2.git20150311.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Apr 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt2.git20150311
- (.spec) re-write in a non-x86_64-centric manner.
- (.spec) %%py3_{provides,requires} should be auto-generated fine.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150311.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150311.1
- NMU: Use buildreq for BR.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150311
- Version 0.1.2

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141018
- Initial build for Sisyphus

