%define oname pymlconf

%def_with python3

Name: python-module-%oname
Version: 0.3.11
Release: alt1.git20140603
Summary: Python high level configuration library
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pymlconf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pylover/pymlconf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml
%endif

%py_provides %oname

%description
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python high level configuration library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.11-alt1.git20140603
- Initial build for Sisyphus

