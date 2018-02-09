# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt5.1.1.1.1
%define oname repoze.who-friendlyform

%def_with python3

Name:           python-module-%oname
Version:        1.0.8
#Release:        alt5.1.1
Summary:        Collection of repoze.who friendly form plugins
Group:          Development/Python
License:        BSD-derived
URL:            http://pypi.python.org/pypi/repoze.who-friendlyform/
Source:         %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel gif2png
#BuildPreReq: python-module-webob python-module-zope.interface
#BuildPreReq: python-module-repoze.who python-module-paste
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: texlive-latex-recommended
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who zope.interface webob

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-pytz python-module-repoze python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: gif2png python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-repoze.who python3-module-setuptools rpm-build-python3 time

%description
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

%package -n python3-module-%oname
Summary: Collection of repoze.who friendly form plugins
Group: Development/Python3
%py3_requires repoze.who zope.interface webob
%py3_provides repoze.who.plugins.friendlyform

%description -n python3-module-%oname
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

%package docs
Summary: Documentation for repoze.who-friendlyform
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

This package contains documentation for repoze.who-friendlyform.

%package pickles
Summary: Pickles for repoze.who-friendlyform
Group: Development/Python

%description pickles
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

This package contains pickles for repoze.who-friendlyform.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv/ docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD
pushd docs/source/_static
gif2png logo_hi.gif
popd
%make -C docs html

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt PKG-INFO tests.py CONTRIBUTORS
%python_sitelibdir/repoze.who_friendlyform*
%python_sitelibdir/repoze/who/plugins/*
%exclude %python_sitelibdir/*.pth

%files docs
#doc docs/build/latex/*.pdf
%doc docs/build/html

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt PKG-INFO tests.py CONTRIBUTORS
%python3_sitelibdir/repoze.who_friendlyform*
%python3_sitelibdir/repoze/who/plugins/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 1.0.8-alt5.1.1.1.1
- (NMU) Fix Provides of python3 module

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt5.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt5.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt5.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt5
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt4.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt3
- Set as archdep package

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2
- Rebuilt with python-module-sphinx-devel

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus

