%define oname repoze.who.plugins.sa

%def_with python3

Name:           python-module-%oname
Version:        1.0.1
Release:        alt2
Summary:        The repoze.who SQLAlchemy plugin
Group:          Development/Python
License:        BSD-derived
URL:            http://pypi.python.org/pypi/repoze.who.plugins.sa/
Source:         %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-repoze.who python-module-SQLAlchemy
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-elixir python-module-pysqlite2
#BuildPreReq: texlive-latex-recommended gif2png
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.who SQLAlchemy

%description
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

%package -n python3-module-%oname
Summary: The repoze.who SQLAlchemy plugin
Group: Development/Python3
%py3_requires repoze.who SQLAlchemy

%description -n python3-module-%oname
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.sa
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires repoze.who coverage nose SQLAlchemy elixir

%description -n python3-module-%oname-tests
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

This package contains tests for repoze.who.plugins.sa.

%package tests
Summary: Tests for repoze.who.plugins.sa
Group: Development/Python
Requires: %name = %version-%release
%py_requires repoze.who coverage nose SQLAlchemy elixir

%description tests
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

This package contains tests for repoze.who.plugins.sa.

%package docs
Summary: Documentation for repoze.who.plugins.sa
Group: Development/Documentation
BuildArch: noarch

%description docs
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

This package contains documentation for repoze.who.plugins.sa.

%package pickles
Summary: Pickles for repoze.who.plugins.sa
Group: Development/Python
%add_python_req_skip tg yourproject

%description pickles
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

This package contains pickles for repoze.who.plugins.sa.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

#prepare_sphinx docs

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

#export PYTHONPATH=$PWD
#pushd docs/source/_static
#gif2png logo_hi.gif
#popd
#make -C docs latex

%install
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

#install -d %buildroot%python_sitelibdir/%oname
#cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt PKG-INFO
%python_sitelibdir/%{oname}*
%exclude %python_sitelibdir/*.pth
#exclude %python_sitelibdir/%oname/pickle
%python_sitelibdir/repoze/who/plugins/*

#files tests
#doc tests

#files docs
#doc docs/build/latex/*.pdf
#doc docs/build/html

#files pickles
#python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt PKG-INFO
%python3_sitelibdir/%{oname}*
%exclude %python3_sitelibdir/*.pth
%python3_sitelibdir/repoze/who/plugins/*
%endif

%changelog
* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt4.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Set as archdep package

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Version 1.0

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.rc2.1
- Rebuilt with python-module-sphinx-devel

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.rc2
- Initial build for Sisyphus

