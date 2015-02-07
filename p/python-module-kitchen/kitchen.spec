%define oname kitchen

%def_with python3

Name: python-module-%oname
Version: 1.2.1
Release: alt1.git20141202
Summary: Cornucopia of useful code
License: LGPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/kitchen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fedora-infra/kitchen.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sphinx-devel python3-module-nose
%endif

%py_provides %oname

%description
Kitchen contains a cornucopia of useful code.

%package -n python3-module-%oname
Summary: Cornucopia of useful code
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Kitchen contains a cornucopia of useful code.

%package -n python3-module-%oname-docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%oname-docs
Kitchen contains a cornucopia of useful code.

This package contains documentation for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Kitchen contains a cornucopia of useful code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Kitchen contains a cornucopia of useful code.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx %{oname}2
ln -s ../objects.inv %{oname}2/docs/

%if_with python3
%prepare_sphinx %{oname}3
ln -s ../objects.inv %{oname}3/docs/
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

pushd %{oname}2/docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd
%if_with python3
pushd %{oname}3/docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc %{oname}2/docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*

%files -n python3-module-%oname-docs
%doc %{oname}3/docs/_build/html/*
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141202
- Initial build for Sisyphus

