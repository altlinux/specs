%define mname yify
%define oname asyncio-%mname

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20141222
Summary: Damned fast YIFY parser using Asyncio
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio-yify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidyen1124/Asyncio-YIFY.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-lxml
BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-lxml
BuildPreReq: python3-module-asyncio
%endif

%py_provides %mname
Conflicts: python-module-%mname > %EVR
Conflicts: python-module-%mname < %EVR
Provides: python-module-%mname = %EVR

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
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141222
- Initial build for Sisyphus

