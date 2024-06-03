%define _unpackaged_files_terminate_build 1

%define oname ipywidgets

%def_with check

Name: python3-module-%oname
Version: 8.1.3
Release: alt2
Summary: Interactive Widgets for the Jupyter Notebook
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/ipywidgets
Vcs: https://github.com/jupyter-widgets/ipywidgets.git
BuildArch: noarch
Source: %name-%version.tar
# https://github.com/jupyter-widgets/ipywidgets/pull/3903
Patch: ipywidgets-Fix-compatibility-with-pytest-8.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-traitlets-tests
BuildRequires: python3-module-ipython
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-pytz
BuildRequires: python3-module-jsonschema
%endif

%description
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

This package contains tests for %oname.

%prep
%setup
%autopatch -p1

%build
cd python/ipywidgets/
%pyproject_build

%install
cd python/ipywidgets/
%pyproject_install

%check
cd python/ipywidgets/
%pyproject_run_pytest -v

%files
%doc README.md CONTRIBUTING.md LICENSE
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/widgets/tests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/widgets/tests

%changelog
* Fri May 31 2024 Stanislav Levin <slev@altlinux.org> 8.1.3-alt2
- Fixed FTBFS (Pytest 8.2.0).

* Tue May 28 2024 Anton Vyatkin <toni@altlinux.org> 8.1.3-alt1
- New version 8.1.3.

* Fri Mar 01 2024 Anton Vyatkin <toni@altlinux.org> 8.1.2-alt1
- New version 8.1.2.

* Sun Feb 11 2024 Grigory Ustinov <grenka@altlinux.org> 8.1.1-alt2
- Fixed FTBFS.

* Thu Sep 14 2023 Anton Vyatkin <toni@altlinux.org> 8.1.1-alt1
- New version 8.1.1.

* Wed Aug 02 2023 Anton Vyatkin <toni@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Mon Jul 10 2023 Anton Vyatkin <toni@altlinux.org> 8.0.7-alt2
- FTBFS: fix BuildRequires.

* Wed Jul 05 2023 Anton Vyatkin <toni@altlinux.org> 8.0.7-alt1
- New version 8.0.7.

* Mon Jul 03 2023 Anton Vyatkin <toni@altlinux.org> 8.0.6-alt1
- New version 8.0.6.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.3-alt1
- Initial build for ALT.
