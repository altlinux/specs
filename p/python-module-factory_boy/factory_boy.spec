%define oname factory_boy

%def_with python3

Name: python-module-%oname
Version: 2.4.1
Release: alt1.git20140903
Summary: A test fixtures replacement for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/factory_boy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rbarrois/factory_boy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides factory

%description
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

%package -n python3-module-%oname
Summary: A test fixtures replacement for Python
Group: Development/Python3
%py3_provides factory

%description -n python3-module-%oname
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140903
- Initial build for Sisyphus

