%define oname bumper-lib

Name: python3-module-%oname
Version: 2.0.4
Release: alt2

Summary: A library to bump / pin your dependency requirements

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/bumper-lib/

# Source-url: https://pypi.io/packages/source/b/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%py3_provides bumper

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-requests python3-module-simplejson
BuildRequires: python3-module-sphinx

%description
A library to bump / pin your dependency requirements. This is used by
the bumper and workspace-tools package.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD/src
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
# AttributeError: module '__main__' has no attribute 'test'
#python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.4-alt2
- Drop python2 support

* Mon Jul 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- build new version
- switch to build from tarball, enable python3 module

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.10-alt1.git20150224.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1.git20150224
- Version 0.2.10

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150216
- Initial build for Sisyphus

