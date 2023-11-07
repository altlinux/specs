%define _unpackaged_files_terminate_build 1

%define oname qtconsole

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.5.0
Release: alt1
Summary: Jupyter Qt console
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/qtconsole/
Vcs: https://github.com/jupyter/qtconsole

BuildArch: noarch

Source: %name-%version.tar

Requires: python3-module-PyQt5

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires: python3-module-qtpy
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-ipython
BuildRequires: python3(sphinx_rtd_theme)
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif
%if_with check
BuildRequires: python3-module-qtpy
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-qt
BuildRequires: python3-module-pytest-xvfb
BuildRequires: python3-module-flaky
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-traitlets-tests
BuildRequires: /usr/bin/xvfb-run
%endif

%py3_provides %oname
%py3_requires traitlets jupyter_core jupyter_client pygments ipykernel

%description
Qt-based console for Jupyter with support for rich media output.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Qt-based console for Jupyter with support for rich media output.

This package contains tests for %oname.

%prep
%setup

%if_with docs
%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/
%endif

%build
%pyproject_build

%install
%pyproject_install

# Install icon
mkdir -p %buildroot%_datadir/icons/hicolor/scalable/apps
cp qtconsole/resources/icon/JupyterConsole.svg \
   %buildroot%_datadir/icons/hicolor/scalable/apps/JupyterQtConsole.svg

# TODO
# Modify and install .desktop file
# sed -i "s/^Icon=.*$/Icon=JupyterQtConsole.svg/" examples/jupyter-qtconsole.desktop
# mkdir -p %buildroot%_desktopdir
# cp examples/jupyter-qtconsole.desktop %buildroot%_desktopdir/

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html
%endif

%check
# all tests pass, but strange AttributeError happens
# https://github.com/jupyter/qtconsole/issues/582
%pyproject_run -- xvfb-run -s '-nolisten local' pytest -v qtconsole \
--ignore qtconsole/tests/test_inprocess_kernel.py


%files
%doc README.* LICENSE
%if_with docs
%doc docs/build/html
%endif
%_bindir/*
%python3_sitelibdir/%{pyproject_distinfo %oname}
%python3_sitelibdir/%oname/
%dir %_datadir/icons/hicolor/scalable/apps
%_datadir/icons/hicolor/scalable/apps/JupyterQtConsole.svg
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 5.5.0-alt1
- New version 5.5.0.

* Wed Sep 06 2023 Anton Vyatkin <toni@altlinux.org> 5.4.4-alt1
- New version 5.4.4.

* Mon Jul 10 2023 Anton Vyatkin <toni@altlinux.org> 5.4.3-alt1
- New version 5.4.3.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 5.2.2-alt2
- Fixed BuildRequires.

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.2-alt1
- Updated to upstream version 5.2.2.

* Fri Oct 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt2
- Updated build dependencies.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt1
- Updated to upstream version 5.1.1.
- Enabled tests.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt2
- Updated build dependencies.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

