%define oname rednose

%def_with python3

Name: python-module-%oname
Version: 0.4.3
Release: alt1
Summary: Coloured output for nosetests
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rednose/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-termstyle
BuildPreReq: python-module-colorama
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-termstyle
BuildPreReq: python3-module-colorama
%endif

%py_provides %oname
%py_requires nose termstyle colorama

%description
rednose is a nosetests plugin for adding colour (and readability) to
nosetest console results.

%package -n python3-module-%oname
Summary: Coloured output for nosetests
Group: Development/Python3
%py3_provides %oname
%py3_requires nose termstyle colorama

%description -n python3-module-%oname
rednose is a nosetests plugin for adding colour (and readability) to
nosetest console results.

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

