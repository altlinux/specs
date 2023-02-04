%define _unpackaged_files_terminate_build 1

%define oname jupyter_core

%def_enable check

Name: python3-module-%oname
Version: 5.2.0
Release: alt1
Summary: Jupyter core package
License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/jupyter-core

# https://github.com/jupyter/jupyter_core.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: rpm-build-python3 python3-module-hatchling
BuildRequires: python3-module-zope python3-module-pytest python3(traitlets.config) python3(mock)
BuildRequires: python3(ipython_genutils.testing)
BuildRequires: python3-module-platformdirs
BuildRequires: python3(sphinxcontrib_github_alt)
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%description
Jupyter core package. A base package on which Jupyter projects rely.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Jupyter core package. A base package on which Jupyter projects rely.

This package contains tests for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%pyproject_build

%install
%pyproject_install

%check
rm -fR build
export LC_ALL=en_US.UTF-8
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv \
    --deselect "jupyter_core/tests/test_command.py::test_not_on_path" \
    --deselect "jupyter_core/tests/test_command.py::test_path_priority" \
    --deselect "jupyter_core/tests/test_command.py::test_argv0" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_prefer_env" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_user_site" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_no_user_site" \
;

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/jupyter.py
%python3_sitelibdir/__pycache__/jupyter.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 5.2.0-alt1
- 5.1.0 -> 5.2.0

* Mon Dec 05 2022 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- 4.7.1 -> 5.1.0

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.1-alt1
- Updated to upstream version 4.7.1.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.3-alt1
- Updated to upstream version 4.6.3.
- Disabled build for python-2.

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Updated build dependencies.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream version 4.4.0.
- Enabled tests.

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2
- added conflict on python-module-jupyter

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 4.0.4-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus

