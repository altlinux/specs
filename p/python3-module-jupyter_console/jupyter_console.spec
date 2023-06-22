%define _unpackaged_files_terminate_build 1
%define oname jupyter_console

%def_with docs
%def_with check

Name: python3-module-%oname
Version: 6.6.3
Release: alt2

Summary: Jupyter Terminal Console
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/jupyter-console/
Vcs: https://github.com/jupyter/jupyter_console.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-traitlets-tests
BuildRequires: python3-module-jupyter_core
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-ipython
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-zmq
BuildRequires: python3-module-flaky
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-prompt_toolkit
BuildRequires: python3-module-Pygments
%endif

%if_with docs
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib_github_alt
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif

%py3_provides %oname

%description
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

This package contains tests for %oname.

%prep
%setup

sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
    $(find ./ -type f \( -name '*.py' -o -name 'jupyter-console' \))

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html
%endif

%check
%pyproject_run_pytest -v

%files
%doc *.md
%if_with docs
%doc docs/_build/html
%endif
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Jun 22 2023 Michael Shigorin <mike@altlinux.org> 6.6.3-alt2
- fix build --without check

* Wed Jun 14 2023 Anton Vyatkin <toni@altlinux.org> 6.6.3-alt1
- New version 6.6.3

* Thu Apr 20 2023 Anton Vyatkin <toni@altlinux.org> 6.2.0-alt3
- Fix BuildRequires

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt2
- Updated build dependencies.
- Disabled tests due to broken aarch64 builder.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.
- Enabled build of documentation.
- Enabled tests.

* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt2
- build for python2 disabled

* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.0-alt1
- Updated to upstream version 5.2.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150812
- Initial build for Sisyphus

