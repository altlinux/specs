%define oname ColanderAlchemy

%def_with python3

Name: python-module-%oname
Version: 0.3.4
Release: alt1.dev1.git20150720.1.1.1
Summary: Autogenerate Colander schemas based on SQLAlchemy models
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ColanderAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stefanofontanelli/ColanderAlchemy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-colander python-module-SQLAlchemy
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-colander python3-module-SQLAlchemy
%endif

%py_provides colanderalchemy
%py_requires colander sqlalchemy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-cssselect python-module-genshi python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-translationstring python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-iso8601 python3-module-pytest python3-module-setuptools python3-module-translationstring
BuildRequires: python-module-alabaster python-module-colander python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-SQLAlchemy python3-module-colander python3-module-setuptools rpm-build-python3 time

%description
ColanderAlchemy helps you to auto-generate Colander schemas that are
based on SQLAlchemy mapped classes.

Such Colander schemas can be used with libraries like Deform and helps
remove the need for duplication of schema definitions.

%package -n python3-module-%oname
Summary: Autogenerate Colander schemas based on SQLAlchemy models
Group: Development/Python3
%py3_provides colanderalchemy
%py3_requires colander sqlalchemy

%description -n python3-module-%oname
ColanderAlchemy helps you to auto-generate Colander schemas that are
based on SQLAlchemy mapped classes.

Such Colander schemas can be used with libraries like Deform and helps
remove the need for duplication of schema definitions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ColanderAlchemy helps you to auto-generate Colander schemas that are
based on SQLAlchemy mapped classes.

Such Colander schemas can be used with libraries like Deform and helps
remove the need for duplication of schema definitions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ColanderAlchemy helps you to auto-generate Colander schemas that are
based on SQLAlchemy mapped classes.

Such Colander schemas can be used with libraries like Deform and helps
remove the need for duplication of schema definitions.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1.dev1.git20150720.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.dev1.git20150720.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1.dev1.git20150720.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.dev1.git20150720
- Version 0.3.4.dev1

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.dev1.git20150423
- Version 0.3.3.dev1

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev1.git20150115
- Initial build for Sisyphus

