%define oname nbformat

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt1.1
Summary: The Jupyter Notebook format
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nbformat
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ipython_genutils python-module-traitlets
#BuildPreReq: python-module-jsonschema python-module-jupyter_core
#BuildPreReq: python-module-nose python-modules-sqlite3
#BuildPreReq: python-module-numpydoc python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ipython_genutils python3-module-traitlets
#BuildPreReq: python3-module-jsonschema python3-module-jupyter_core
#BuildPreReq: python3-module-nose python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires ipython_genutils traitlets jsonschema jupyter_core sqlite3

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-decorator python-module-docutils python-module-functools32 python-module-genshi python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-traitlets python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-decorator python3-module-ipython_genutils python3-module-setuptools python3-module-traitlets xz
BuildRequires: python-module-alabaster python-module-html5lib python-module-jsonschema python-module-jupyter_core python-module-nose python-module-numpydoc python-module-objects.inv python-module-pytest python-modules-sqlite3 python3-module-jsonschema python3-module-jupyter_core python3-module-nose python3-module-pytest python3-modules-sqlite3 rpm-build-python3 time

%description
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: The Jupyter Notebook format
Group: Development/Python3
%py3_provides %oname
%py3_requires ipython_genutils traitlets jsonschema jupyter_core sqlite3

%description -n python3-module-%oname
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains pickles for %oname.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
nosetests -vv
%if_with python3
pushd ../python3
nosetests3 -vv
popd
%endif

%files
%doc *.md docs/_build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

