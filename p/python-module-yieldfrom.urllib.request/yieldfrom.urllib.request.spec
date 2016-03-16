%define mname yieldfrom.urllib
%define oname %mname.request

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20141019.1.1
Summary: Asyncio port of urllib.request 
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.urllib.request/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromUrllib2.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python2
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires asyncio yieldfrom.http.client

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-pytest python3-module-setuptools-tests rpm-build-python3

%description
asyncio version of urllib.request (urllib2).

%package -n python3-module-%oname
Summary: Asyncio port of urllib.request
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires asyncio yieldfrom.http.client

%description -n python3-module-%oname
asyncio version of urllib.request (urllib2).

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires yieldfrom

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname
%py3_requires yieldfrom

%description -n python3-module-%mname
Core files of %mname.

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

%ifarch x86_64
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
%python_sitelibdir/yieldfrom/urllib/*
%python_sitelibdir/*.egg.info
%exclude %python_sitelibdir/yieldfrom/urllib/__init__.py*
%endif

%files -n python-module-%mname
%dir %python_sitelibdir/yieldfrom/urllib
%python_sitelibdir/yieldfrom/urllib/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/yieldfrom/urllib/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/yieldfrom/urllib/__init__.*
#exclude %python3_sitelibdir/yieldfrom/urllib/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/yieldfrom/urllib
%dir %python3_sitelibdir/yieldfrom/urllib/__pycache__
%python3_sitelibdir/yieldfrom/urllib/__init__.*
#python3_sitelibdir/yieldfrom/urllib/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20141019.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20141019.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141019
- Initial build for Sisyphus

