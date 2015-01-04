%define oname Trololio

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20150102
Summary: Trollius and asyncio compatibility library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Trololio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ThinkChaos/Trololio.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio
%endif

%py_provides trololio
%py_requires trollius

%description
Trololio provides a compatibility layer for Trollius and asyncio (aka
Tulip). It addresses the differences listed in Trollius and Tulip:

* Allows the use of Trollius' syntax with asyncio.
* Provides missing objects and aliases for the others.
* Synchronizes debug environnement variables.

%package -n python3-module-%oname
Summary: Trollius and asyncio compatibility library
Group: Development/Python3
%py3_provides trololio
%py3_requires asyncio

%description -n python3-module-%oname
Trololio provides a compatibility layer for Trollius and asyncio (aka
Tulip). It addresses the differences listed in Trollius and Tulip:

* Allows the use of Trollius' syntax with asyncio.
* Provides missing objects and aliases for the others.
* Synchronizes debug environnement variables.

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

%check
python setup.py test
python test.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 test.py
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20150102
- Initial build for Sisyphus

