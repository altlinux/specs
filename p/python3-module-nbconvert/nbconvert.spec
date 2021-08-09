%define _unpackaged_files_terminate_build 1

%define oname nbconvert

%def_without doc
%def_without bootstrap
%def_with check

Name: python3-module-%oname
Version: 6.1.0
Release: alt1

Summary: Converting Jupyter Notebooks

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/nbconvert

BuildArch: noarch

# https://github.com/jupyter/nbconvert.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-tests.patch

# It may be necessary to update these files when package is updated
# URLs are taken from setup.py
Source1: lab-3.0.7-index.css
Source2: lab-3.0.7-theme-light.css
Source3: lab-3.0.7-theme-dark.css
Source4: classic-5.4.0-style.css

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-jinja2 python3-module-traitlets-tests
%if_with doc
BuildRequires: python3-module-html5lib python3(pandocfilters)
BuildRequires: python3(sphinx_rtd_theme) python3(nbsphinx) python3(pandocfilters)
BuildRequires: texlive texlive-dist
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif
%if_without bootstrap
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
BuildRequires: python3-module-ipython_genutils-tests python3-module-notebook
%endif
BuildRequires: python3-module-pathlib2 python3(entrypoints) python3(bleach)

# FIXME: with/enabled test/check to be strict
%if_with check
BuildRequires: python3(pandocfilters)
BuildRequires: python3(defusedxml)
BuildRequires: python3(jupyterlab_pygments)
BuildRequires: python3(nbclient)
BuildRequires: python3(nest_asyncio)
%endif

%py3_provides %oname

# from setup.py
%py3_use mistune >= 0.8.1
%py3_use mistune < 2
%py3_use jinja2 >= 2.4
# TODO: py3_use pygments >= 2.4.1
%py3_use Pygments >= 2.4.1
%py3_use jupyterlab_pygments
%py3_use traitlets >= 5.0
%py3_use jupyter_core
%py3_use nbformat >= 4.4
%py3_use entrypoints >= 0.2.2
%py3_use bleach
%py3_use pandocfilters >= 1.4.1
%py3_use testpath
%py3_use defusedxml
%py3_use nbclient >= 0.5.0
%py3_use nbclient < 0.6.0

%description
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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
%patch1 -p1

# This is intentionally set up to fail if version of required file changes.
# In case of such failure it's required to obtain a new version of file.
jupyterlab_css_version=$(grep '^jupyterlab_css_version' setup.py | head -n 1 | awk '{print $3}' | xargs echo)
jupyterlab_theme_light_version=$(grep '^jupyterlab_theme_light_version' setup.py | head -n 1 | awk '{print $3}' | xargs echo)
jupyterlab_theme_dark_version=$(grep '^jupyterlab_theme_dark_version' setup.py | head -n 1 | awk '{print $3}' | xargs echo)
notebook_css_version=$(grep '^notebook_css_version' setup.py | head -n 1 | awk '{print $3}' | xargs echo)

cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .

mkdir -p share/jupyter/nbconvert/templates/lab/static
mkdir -p share/jupyter/nbconvert/templates/classic/static

mv lab-${jupyterlab_css_version}-index.css share/jupyter/nbconvert/templates/lab/static/index.css
mv lab-${jupyterlab_theme_light_version}-theme-light.css share/jupyter/nbconvert/templates/lab/static/theme-light.css
mv lab-${jupyterlab_theme_dark_version}-theme-dark.css share/jupyter/nbconvert/templates/lab/static/theme-dark.css
mv classic-${notebook_css_version}-style.css share/jupyter/nbconvert/templates/classic/static/style.css

%if_with doc
%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with doc
export PYTHONPATH=$PWD
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if_without bootstrap
%check
export LC_ALL=en_US.UTF-8
export NO_PYPPETEER=true
PYTHONPATH=$(pwd) py.test3 -vv
%endif

%files
%doc *.md
%_bindir/*
%_datadir/jupyter
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%if_with doc
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests

%if_with doc
%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*
%endif

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.0-alt1
- Updated to upstream version 6.1.0.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.2-alt4
- drop excessive python3-module-jinja2-tests BR

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2-alt3
- Updated build dependencies.

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 6.0.2-alt2
- improve requires

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2-alt1
- Updated to upstream version 6.0.2.
- Disabled build for python-2.

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

