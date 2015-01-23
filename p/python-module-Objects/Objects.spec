%define oname Objects

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150123
Summary: Python catalogs of objects providers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Objects/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rmk135/objects.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
%endif

%py_provides objects
%py_requires six

%description
Python catalogs of objects providers.

%package -n python3-module-%oname
Summary: Python catalogs of objects providers
Group: Development/Python3
%py3_provides objects
%py3_requires six

%description -n python3-module-%oname
Python catalogs of objects providers.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150123
- Initial build for Sisyphus

