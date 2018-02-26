%define oname repoze.what-xml
Name: python-module-%oname
Version: 1.0rc1
Release: alt3.1
Summary: The repoze.what 1.0 XML plugin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-PasteDeploy
BuildPreReq: python-module-repoze.what.plugins python-module-nose
BuildPreReq: python-module-repoze.who-testutil python-module-coverage
BuildPreReq: python-module-zope.interface

%py_requires repoze.what.plugins repoze.what

%description
This is an adapters plugin for repoze.what.

%package pickles
Summary: Pickles for repoze.what-xml
Group: Development/Python

%description pickles
This is an adapters plugin for repoze.what.

This package contains pickles for repoze.what-xml.

%package docs
Summary: Documentation for repoze.what-xml
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an adapters plugin for repoze.what.

This package contains documentation for repoze.what-xml.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch:$PWD
%python_build

pushd docs
%make pickle
%make html
popd

%install
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch:$PWD
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0rc1-alt3.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0rc1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0rc1-alt2
- Excluded unnecessary tests

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0rc1-alt1
- Initial build for Sisyphus

