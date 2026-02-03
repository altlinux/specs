%define _unpackaged_files_terminate_build 1
%define pypi_name git-pandas
%define mod_name gitpandas

%def_with docs
%def_with check

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1.git2789b49d

Summary: A wrapper around gitpython to produce pandas dataframes for analysis
License: BSD-3-Clause
Group: Development/Python3
Url: https://gitpandas.mcginniscommawill.com
Vcs: https://github.com/wdm0006/git-pandas

BuildArch: noarch

Source0: %name-%version-%release.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
BuildRequires: python3-module-pandas-tests
%endif
%if_with docs
BuildRequires: python3-module-sphinx
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

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Tue Feb 03 2026 Dmitry Mihalchenko <tascad@altlinux.org> 2.5.0-alt1.git2789b49d
- Initial build for ALT Sisyphus.
