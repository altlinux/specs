%define oname flake8-import-order

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1.git20141029
Summary: Flake8 and pylama plugin that checks the ordering of import statements
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/flake8-import-order/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/public/flake8-import-order.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8 python-module-pylama
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8 python3-module-pylama
%endif

%py_provides flake8_import_order

%description
Flake8 plugin that checks import order in the fashion of the Google
Python Style Guide.

%package -n python3-module-%oname
Summary: Flake8 and pylama plugin that checks the ordering of import statements
Group: Development/Python3
%py3_provides flake8_import_order

%description -n python3-module-%oname
Flake8 plugin that checks import order in the fashion of the Google
Python Style Guide.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20141029
- Initial build for Sisyphus

