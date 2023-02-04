%define _unpackaged_files_terminate_build 1

%define oname nbconvert

%def_without doc
%ifarch %ix86 x86_64 aarch64
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 7.2.9
Release: alt1

Summary: Converting Jupyter Notebooks

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/nbconvert

BuildArch: noarch

VCS: https://github.com/jupyter/nbconvert.git
Source: %name-%version.tar
Source1: classic-5.4.0-style.css
Source2: lab-3.1.11-index.css
Source3: lab-3.1.11-theme-light.css
Source4: lab-3.1.11-theme-dark.css

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-jinja2 python3-module-traitlets-tests python3-module-hatchling
%if_with doc
BuildRequires: python3-module-html5lib python3(pandocfilters)
BuildRequires: python3(sphinx_rtd_theme) python3(nbsphinx) python3(pandocfilters)
BuildRequires: texlive texlive-dist
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
BuildRequires: python3-module-ipython_genutils-tests python3-module-notebook
BuildRequires: python3-module-pathlib2 python3(entrypoints) python3(bleach)

%if_with check
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-pytest-qt
BuildRequires: /usr/bin/xvfb-run
BuildRequires: python3-module-PyQtWebEngine
BuildRequires: /usr/bin/pandoc
BuildRequires: /usr/bin/xelatex
BuildRequires: python3(pandocfilters)
BuildRequires: python3(defusedxml)
BuildRequires: python3(jupyterlab_pygments)
BuildRequires: python3(nest_asyncio)
%endif

%py3_provides %oname

# from setup.py
%py3_use mistune >= 2.0.3
%py3_use mistune < 3
%py3_use jinja2 >= 2.4
# TODO: py3_use pygments >= 2.4.1
%py3_use Pygments >= 2.4.1
%py3_use jupyterlab_pygments
%py3_use traitlets >= 5.0
%py3_use jupyter_core
%py3_use nbformat >= 5.7.3
%py3_use entrypoints >= 0.2.2
%py3_use bleach
%py3_use pandocfilters >= 1.4.1
%py3_use testpath
%py3_use defusedxml
%py3_use nbclient >= 0.7.0

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
rm -rf nbconvert.egg-info
echo "nbsphinx_allow_errors = True" >> docs/source/conf.py

mkdir -p share/templates/classic/static/
mkdir -p share/templates/lab/static/
cp %SOURCE1 share/templates/classic/static/style.css
cp %SOURCE2 share/templates/lab/static/index.css
cp %SOURCE3 share/templates/lab/static/theme-light.css
cp %SOURCE4 share/templates/lab/static/theme-dark.css


%if_with doc
%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/
%endif

%build
%pyproject_build

%install
%pyproject_install

%if_with doc
export PYTHONPATH=$PWD
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
cat >tox.ini << __EOF__
[testenv]
commands =
    xvfb-run pytest {posargs:-vra}
__EOF__
# test_execute_multiple_notebooks, test_execute_widgets_from_nbconvert, test_filename_accent_pdf, test_filename_spaces,
# test_linked_images, test_pdf, test_export - no unicode-data, see alt bug #44679 
# other tests require orphaned pyppeteer
%tox_check_pyproject -- \
    -k "\
    not test_execute_multiple_notebooks and \
    not test_execute_widgets_from_nbconvert and \
    not test_filename_accent_pdf and \
    not test_filename_spaces and \
    not test_linked_images and \
    not test_pdf and \
    not test_export and \
    not test_webpdf_without_chromium and \
    not test_webpdf_with_chromium and \
    not test_no_input and \
    not test_basic_execution and \
    not test_mixed_markdown_execution and \
    not test_populate_language_info and \
    not test_preprocess_cell and \
    not test_convert_full_qualified_name and \
    not test_post_processor"

%files
%doc *.md
%_bindir/*
%_datadir/jupyter
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*.dist-info
%if_with doc
%exclude %python3_sitelibdir/%oname/pickle
%endif

%if_with doc
%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*
%endif

%changelog
* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 7.2.9-alt1
- 7.2.6 -> 7.2.9

* Mon Dec 19 2022 Anton Farygin <rider@altlinux.ru> 7.2.6-alt1
- 6.1.0 -> 7.2.6
- enabled tests

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

