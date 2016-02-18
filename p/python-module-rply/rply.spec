%define oname rply

%def_with python3

Name: python-module-%oname
Version: 0.7.3
Release: alt1.git20141226.1
Summary: A pure Python Lex/Yacc that works with RPython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rply/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alex/rply.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires json

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
Welcome to RPLY! A pure python parser generator, that also works with
RPython. It is a more-or-less direct port of David Beazley's awesome
PLY, with a new public API, and RPython support.

%package -n python3-module-%oname
Summary: A pure Python Lex/Yacc that works with RPython
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Welcome to RPLY! A pure python parser generator, that also works with
RPython. It is a more-or-less direct port of David Beazley's awesome
PLY, with a new public API, and RPython support.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Welcome to RPLY! A pure python parser generator, that also works with
RPython. It is a more-or-less direct port of David Beazley's awesome
PLY, with a new public API, and RPython support.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Welcome to RPLY! A pure python parser generator, that also works with
RPython. It is a more-or-less direct port of David Beazley's awesome
PLY, with a new public API, and RPython support.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.git20141226.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20141226
- Initial build for Sisyphus

