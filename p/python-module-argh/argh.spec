%define oname argh

%def_with python3

Name: python-module-%oname
Version: 0.26.1
Release: alt1.git20141030
Summary: An unobtrusive argparse wrapper with natural syntax
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/argh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/neithere/argh.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-pytest-cov python-module-pytest-xdist
BuildPreReq: python-module-tox python-module-argparse
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-mock
BuildPreReq: python3-module-pytest-cov python3-module-pytest-xdist
BuildPreReq: python3-module-tox python3-module-argparse
%endif

%py_provides %oname

%description
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

http://argh.rtfd.org

%package -n python3-module-%oname
Summary: An unobtrusive argparse wrapper with natural syntax
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

http://argh.rtfd.org

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
./coverage.sh
%if_with python3
pushd ../python3
sed -i 's|py.test|py.test-%_python3_version|' coverage.sh \
	test/test_integration.py
./coverage.sh
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26.1-alt1.git20141030
- Initial build for Sisyphus

