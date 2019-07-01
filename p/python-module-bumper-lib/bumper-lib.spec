%define oname bumper-lib

%def_with python3

Name: python-module-%oname
Version: 2.0.4
Release: alt1

Summary: A library to bump / pin your dependency requirements

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bumper-lib/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/b/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools
BuildRequires: python-module-requests python-module-simplejson
BuildRequires: python-module-sphinx-devel

%py_provides bumper

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests python3-module-simplejson
%endif

%description
A library to bump / pin your dependency requirements. This is used by
the bumper and workspace-tools package.

%if_with python3
%package -n python3-module-%oname
Summary: A library to bump / pin your dependency requirements
Group: Development/Python3
%py3_provides bumper

%description -n python3-module-%oname
A library to bump / pin your dependency requirements. This is used by
the bumper and workspace-tools package.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A library to bump / pin your dependency requirements. This is used by
the bumper and workspace-tools package.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
A library to bump / pin your dependency requirements. This is used by
the bumper and workspace-tools package.

This package contains documentation for %oname.

%prep
%setup
subst "s|'setuptools-git'|'setuptools'|" setup.py
# drop unneeded module wheel
subst "s|, 'wheel'||" setup.py

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

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
# AttributeError: module '__main__' has no attribute 'test'
#python3 setup.py test
popd
%endif

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
* Mon Jul 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- build new version
- switch to build from tarball, enable python3 module

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.10-alt1.git20150224.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1.git20150224
- Version 0.2.10

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150216
- Initial build for Sisyphus

