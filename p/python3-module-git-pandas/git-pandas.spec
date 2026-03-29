%define _unpackaged_files_terminate_build 1
%define pypi_name git-pandas
%define mod_name gitpandas

%def_with docs
%def_with check

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt2.git2789b49d

Summary: A wrapper around gitpython to produce pandas dataframes for analysis
License: BSD-3-Clause
Group: Development/Python3
Url: https://gitpandas.mcginniscommawill.com
Vcs: https://github.com/wdm0006/git-pandas

BuildArch: noarch

Source0: %name-%version-%release.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-gitpython
BuildRequires: python3-module-joblib
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pandas
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-redis
BuildRequires: python3-module-requests
BuildRequires: python3-module-ruff
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pandas-tests
%endif

%description
Git-Pandas is a powerful Python library that transforms Git repository
data into pandas DataFrames, making it easy to analyze and visualize
your codebase's history, contributors, and development patterns.

Built on top of GitPython, it provides a simple yet powerful interface
for extracting meaningful insights from your Git repositories.

%prep
%setup
%autopatch -p1


%build
%pyproject_build
%if_with docs
%make -C ./docs man
%endif

%install
%pyproject_install
install -pDv -m644 docs/build/man/%pypi_name.1 %buildroot%_man1dir/%pypi_name.1

%check
# Some tests require this settings
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# Disable tests with internet
%pyproject_run_pytest \
    -m "not remote" \
    --deselect="tests/test_examples.py::test_example_scripts"

%files
%if_with docs
%_man1dir/%pypi_name.1*
%endif
%doc README.md LICENSE.md
%python3_sitelibdir_noarch/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt2.git2789b49d
- Demodernized packaging.

* Tue Feb 03 2026 Dmitry Mihalchenko <tascad@altlinux.org> 2.5.0-alt1.git2789b49d
- Initial build for ALT Sisyphus.
