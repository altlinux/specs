%define oname repoze.what-pylons

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.git20110412
Summary: The repoze.what v1 plugin for Pylons/TG2 integration
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-pylons
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-pylons.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel python-module-decorator
BuildPreReq: python-module-pylons python-module-repoze.what.plugins
BuildPreReq: python-module-tempita python-module-webtest
BuildPreReq: python-module-weberror python-module-webob
BuildPreReq: python-module-mako python-module-nose
BuildPreReq: python-module-FormEncode python-module-PasteScript
BuildPreReq: python-module-PasteDeploy python-module-beaker
BuildPreReq: python-module-webhelpers python-module-routes
BuildPreReq: python-module-repoze.who-testutil python-module-markupsafe
BuildPreReq: python-module-zope.interface python-module-TurboGears2
BuildPreReq: python-module-coverage python-module-babel
BuildPreReq: python-module-WebFlash
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.what.plugins repoze.what pylons decorator repoze.who

%description
This is an extras plugin for repoze.what which provides optional and
handy utilities for Pylons applications using this authorization
framework.

Some of the features of the plugin include:

* The utilities are ready to use: There's nothing additional to be
  configured before using.
* 100%% documented. Each component is documented along with code samples.
* The test suite has a coverage of 100%% and it will never decrease -- if
  it ever does, report it as a bug!
* TurboGears 2 is officially supported as well.

%package -n python3-module-%oname
Summary: The repoze.what v1 plugin for Pylons/TG2 integration
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what pylons decorator repoze.who

%description -n python3-module-%oname
This is an extras plugin for repoze.what which provides optional and
handy utilities for Pylons applications using this authorization
framework.

Some of the features of the plugin include:

* The utilities are ready to use: There's nothing additional to be
  configured before using.
* 100%% documented. Each component is documented along with code samples.
* The test suite has a coverage of 100%% and it will never decrease -- if
  it ever does, report it as a bug!
* TurboGears 2 is officially supported as well.

%package pickles
Summary: Pickles for repoze.what-pylons
Group: Development/Python

%description pickles
This is an extras plugin for repoze.what which provides optional and
handy utilities for Pylons applications using this authorization
framework.

This package contains pickles for repoze.what-pylons.

%package docs
Summary: Documentation for repoze.what-pylons
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an extras plugin for repoze.what which provides optional and
handy utilities for Pylons applications using this authorization
framework.

This package contains documentation for repoze.what-pylons.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD
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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
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

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20110412
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.git20110412.2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412.2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412.1
- Excludes unnecessary tests

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412
- Initial build for Sisyphus

