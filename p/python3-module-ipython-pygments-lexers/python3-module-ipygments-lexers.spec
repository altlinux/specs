%define pypi_name ipython-pygments-lexers

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Pygments lexers for syntax-highlighting IPython code & sessions
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/ipython-pygments-lexers/
Vcs: https://github.com/ipython/ipython-pygments-lexers

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pygments
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/__pycache__/ipython_pygments_lexers.*.pyc
%python3_sitelibdir/ipython_pygments_lexers.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Mar 07 2025 Anton Vyatkin <toni@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
