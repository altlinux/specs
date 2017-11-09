%define oname nbconvert

%def_with python3
%def_without docs

Name: python-module-%oname
Version: 5.3.1
Release: alt1
Summary: Converting Jupyter Notebooks
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nbconvert

# https://github.com/jupyter/nbconvert.git
Source: %name-%version.tar
# It may be necessary to update this file when package is updated
# https://cdn.jupyter.org/notebook/4.3.0/style/style.min.css
Source1: 4.3.0-style.min.css

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: pandoc time python-module-alabaster python-module-html5lib python-module-ipython_genutils-tests
BuildRequires: python-module-notebook python-module-objects.inv python-module-pytest python-module-traitlets-tests
BuildRequires: python-module-pathlib2 python2.7(entrypoints) python2.7(pandocfilters) python2.7(bleach)
%if_with docs
BuildRequires: python2.7(sphinx_rtd_theme) python2.7(nbsphinx)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-ipython_genutils-tests python3-module-jinja2-tests python3-module-notebook python3-module-traitlets-tests
BuildRequires: python3-module-pathlib2 python3(entrypoints) python3(pandocfilters) python3(bleach)
%endif

%py_provides %oname
%py_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py_requires tornado jupyter_client

%description
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Converting Jupyter Notebooks
Group: Development/Python3
%py3_provides %oname
%py3_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py3_requires tornado jupyter_client

%description -n python3-module-%oname
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.
%endif

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains documentation for %oname.
%endif

%prep
%setup

# This is intentionally set up to fail if version of required file changes.
# In case of such fail it's required to obtain new version of file.
cp %SOURCE1 nbconvert/resources/
resource_version=$(grep '^notebook_css_version' setup.py | awk '{print $3}' | xargs echo)
mv nbconvert/resources/${resource_version}-style.min.css nbconvert/resources/style.min.css

%if_with python3
cp -fR . ../python3
%endif

%if_with docs
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
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
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%if_with docs
export PYTHONPATH=$PWD
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export LC_ALL=en_US.UTF-8
PYTHONPATH=$(pwd) py.test -vv
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3 -vv
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/*/pickle
%endif
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt1
- Updated to upstream version 5.3.1.
- Disabled building docs.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt3
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Enabled check

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

