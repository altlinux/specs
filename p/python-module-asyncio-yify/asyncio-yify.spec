%define mname yify
%define oname asyncio-%mname

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20141222.1.1
Summary: Damned fast YIFY parser using Asyncio
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio-yify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidyen1124/Asyncio-YIFY.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-aiohttp python-module-lxml
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-aiohttp python3-module-lxml
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %mname
Conflicts: python-module-%mname > %EVR
Conflicts: python-module-%mname < %EVR
Provides: python-module-%mname = %EVR

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-gunicorn python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-html5lib python3-module-pytest rpm-build-python3

%description
Damned fast YIFY parser using Asyncio.

%package -n python3-module-%oname
Summary: Damned fast YIFY parser using Asyncio
Group: Development/Python3
%py3_provides %mname
Conflicts: python3-module-%mname > %EVR
Conflicts: python3-module-%mname < %EVR
Provides: python3-module-%mname = %EVR

%description -n python3-module-%oname
Damned fast YIFY parser using Asyncio.

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

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20141222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20141222.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141222
- Initial build for Sisyphus

