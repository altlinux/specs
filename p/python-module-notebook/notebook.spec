%define oname notebook

%def_with python3
#def_disable check
%def_with doc

Name: python-module-%oname
Version: 5.2.2
Release: alt2

Summary: Jupyter Interactive Notebook
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/notebook/
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildArch: noarch

BuildRequires: python-module-pathlib
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-zmq python-module-jinja2
BuildRequires: python-module-tornado python-module-ipython_genutils-tests
BuildRequires: python-module-traitlets-tests python-module-jupyter_core
BuildRequires: python-module-jupyter_client python-module-nbformat
BuildRequires: python-module-nbconvert python-module-ipykernel
BuildRequires: python-module-mock python-module-terminado
BuildRequires: python-module-nose python-module-requests
BuildRequires: python-module-coverage
%{?!_without_check:%{?!_disable_check:BuildRequires: python2.7(pandocfilters) python2.7(nose_warnings_filters)}}
%if_with doc
BuildRequires: pandoc
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-zmq python3-module-jinja2
BuildRequires: python3-module-tornado python3-module-ipython_genutils-tests
BuildRequires: python3-module-traitlets-tests python3-module-jupyter_core
BuildRequires: python3-module-jupyter_client python3-module-nbformat
BuildRequires: python3-module-nbconvert python3-module-ipykernel
BuildRequires: python3-module-mock python3-module-terminado
BuildRequires: python3-module-nose python3-module-requests
BuildRequires: python3-module-coverage
%{?!_without_check:%{?!_disable_check:BuildRequires: python3(pandocfilters) python3(nose_warnings_filters)}}
%if_with doc
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3(nbsphinx) python3-module-sphinx_rtd_theme
%endif
%endif

%py_provides %oname
%py_requires zmq jinja2 tornado ipython_genutils traitlets jupyter_core
%py_requires jupyter_client nbformat nbconvert ipykernel

%description
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter Interactive Notebook
Group: Development/Python3
%py3_provides %oname
%py3_requires zmq jinja2 tornado ipython_genutils traitlets jupyter_core
%py3_requires jupyter_client nbformat nbconvert ipykernel

%description -n python3-module-%oname
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains tests for %oname.

%package -n python3-module-%oname-pickles
Summary: Pickles for %oname
Group: Development/Python3

%description -n python3-module-%oname-pickles
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains pickles for %oname.

%package -n python3-module-%oname-docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%oname-docs
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%if_with doc
%prepare_sphinx3 docs
ln -s ../objects.inv ../python3/docs/source/
%endif
%endif

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

%if_with doc
export PYTHONPATH=$PWD
%make -C docs pickle SPHINXBUILD=py3_sphinx-build
%make -C docs html SPHINXBUILD=py3_sphinx-build
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
nosetests -vv --with-coverage --cover-package=%oname %oname

%if_with python3
pushd ../python3
nosetests3 -vv --with-coverage --cover-package=%oname %oname
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests
%if_with doc
%exclude %python3_sitelibdir/*/pickle
%endif

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests

%if_with doc
%files -n python3-module-%oname-pickles
%python3_sitelibdir/*/pickle

%files -n python3-module-%oname-docs
%doc ../python3/docs/build/html/*
%endif
%endif

%changelog
* Mon Jan 08 2018 Michael Shigorin <mike@altlinux.org> 5.2.2-alt2
- Avoid BR: pandoc when --without doc (e2k: no ghc so far)
- Move %%check BRs under corresponding knob as well
- Spec tags prettified a bit

* Wed Nov 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.2-alt1
- Updated to upstream version 5.2.2.

* Fri Jun 02 2017 Michael Shigorin <mike@altlinux.org> 4.0.4-alt3.1
- BOOTSTRAP: fixed build --without doc
  + renamed the docs knob for consistency

* Mon Mar 27 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.4-alt3
- (NMU) Fixed build

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Enabled check
- Added documentation

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus

