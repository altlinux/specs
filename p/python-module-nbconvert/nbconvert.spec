%define oname nbconvert

%def_without doc
%def_with bootstrap
%def_with check

Name: python-module-%oname
Version: 5.3.1
Release: alt7

Summary: Converting Jupyter Notebooks
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/nbconvert
# https://github.com/jupyter/nbconvert.git
Source: %name-%version.tar
# It may be necessary to update this file when package is updated
# https://cdn.jupyter.org/notebook/4.3.0/style/style.min.css
Source1: 4.3.0-style.min.css

BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: time
%if_with bootstrap
BuildRequires: python-module-ipython_genutils-tests python-module-notebook
%endif
BuildRequires: python-module-objects.inv python-module-pytest python-module-traitlets-tests
BuildRequires: python-module-pathlib2 python2.7(entrypoints) python2.7(bleach)
%if_with doc
BuildRequires: pandoc python-module-alabaster python-module-html5lib
BuildRequires: python2.7(sphinx_rtd_theme) python2.7(nbsphinx) python2.7(pandocfilters)
BuildRequires: texlive texlive-dist
%endif

# FIXME: with/enabled test/check to be strict
%if_with check
BuildRequires: python2.7(pandocfilters)
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

%prep
%setup

# This is intentionally set up to fail if version of required file changes.
# In case of such failure it's required to obtain a new version of file.
cp %SOURCE1 nbconvert/resources/
resource_version=$(grep '^notebook_css_version' setup.py | awk '{print $3}' | xargs echo)
mv nbconvert/resources/${resource_version}-style.min.css nbconvert/resources/style.min.css

%if_with doc
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
%endif

%build
%python_build_debug

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py2
done

%if_with doc
export PYTHONPATH=$PWD
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if_with bootstrap
%check
export LC_ALL=en_US.UTF-8
PYTHONPATH=$(pwd) py.test -vv
%endif

%files
%doc *.md
%_bindir/*
%python_sitelibdir/*
%if_with doc
%exclude %python_sitelibdir/*/pickle
%endif
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with doc
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*
%endif

%changelog
* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt7
- Resolved conflict with python3-module-nbconvert by renaming binaries.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt6
- Rebuilt without python-3 support.

* Sun May 05 2019 Michael Shigorin <mike@altlinux.org> 5.3.1-alt5
- fixed doc knob (renamed from docs for consistency)
- minor spec cleanup

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.1-alt4
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.1-alt3
- off build requires for nmu

* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt2
- Updated build dependencies.

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

