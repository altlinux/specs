%define _unpackaged_files_terminate_build 1
%define oname notebook

%def_with check
%def_without doc

Name: python3-module-%oname
Version: 6.5.4
Release: alt1
Summary: Jupyter Interactive Notebook
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/notebook
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-jupyter-packaging
BuildRequires: python3-module-nbclassic

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-testpath
BuildRequires: python3-module-requests
BuildRequires: python3-module-traitlets-tests

BuildRequires: python3-module-send2trash
BuildRequires: python3-module-nbconvert
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-nest-asyncio
BuildRequires: python3-module-tornado
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-argon2-cffi
BuildRequires: python3-module-terminado
BuildRequires: python3-module-nbclassic
BuildRequires: python3-module-requests-unixsocket
BuildRequires: /dev/pts
%endif

%if_with doc
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3(nbsphinx) python3-module-sphinx_rtd_theme
%endif

Conflicts: python-module-%oname

%description
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains documentation for %oname.

%prep
%setup
# remove selenium tests
rm -rf notebook/tests/selenium

%if_with doc
%prepare_sphinx3 docs
ln -s ../objects.inv ../python3/docs/source/
%endif

%build
%pyproject_build

%install
%pyproject_install

%if_with doc
export PYTHONPATH=$PWD
%make -C docs pickle SPHINXBUILD=py3_sphinx-build
%make -C docs html SPHINXBUILD=py3_sphinx-build
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export LANG=en_US.UTF-8
# trash tests doesn't seem to work
%pyproject_run_pytest -v -k "\
not test_kernels_api \
and not test_checkpoints_follow_file \
and not test_delete \
and not test_delete_dirs \
and not test_delete_non_empty_dir \
and not test_list_formats"

%files
%doc *.md
%_bindir/jupyter-bundlerextension
%_bindir/jupyter-nbextension
%_bindir/jupyter-notebook
%_bindir/jupyter-serverextension
%_desktopdir/jupyter-notebook.desktop
%_iconsdir/hicolor/scalable/apps/notebook.svg
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests
%if_with doc
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests

%if_with doc
%files pickles
%python3_sitelibdir/%oname/pickle/

%files docs
%doc ../python3/docs/build/html/*
%endif

%changelog
* Tue Jun 13 2023 Anton Vyatkin <toni@altlinux.org> 6.5.4-alt1
- New version 6.5.4

* Tue Apr 18 2023 Anton Vyatkin <toni@altlinux.org> 6.4.12-alt2
- Fix BuildRequires

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 6.4.12-alt1
- new version 6.4.12 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 6.4.8-alt1
- new version 6.4.8 (with rpmrb script)

* Fri Oct 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.4.4-alt1
- Updated to upstream version 6.4.4.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 6.4.0-alt1
- new version 6.4.0 (with rpmrb script)

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 6.1.4-alt1
- separate build python3 module, cleanup spec
- new version 6.1.4 (with rpmrb script)
- switch to build from tarball

* Thu Jan 31 2019 Stanislav Levin <slev@altlinux.org> 5.2.2-alt4
- Applied upstream patches for Tornado5 support (closes: #35982, #35983).

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.2.2-alt3
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.2.2-alt2.2
- off build requires for nmu

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.2.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

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

