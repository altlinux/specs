%define _unpackaged_files_terminate_build 1

%define pypi_name cookiecutter
%define binfile_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1

Summary: A cross-platform command-line utility that creates projects from cookiecutters
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/cookiecutter/
Vcs: https://github.com/cookiecutter/cookiecutter

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: git
%add_pyproject_deps_check_filter safety
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

# clean symbolic links in docs dir
rm -v docs/{AUTHORS.md,CODE_OF_CONDUCT.md,CONTRIBUTING.md,HISTORY.md,README.md}

# create shells completion files
export binfile="%buildroot%_bindir/%binfile_name"
export datadir="%buildroot%_datadir"
export PYTHONPATH=$PYTHONPATH:%buildroot%python3_sitelibdir_noarch
mkdir -p $datadir/zsh/site-functions
_COOKIECUTTER_COMPLETE=zsh_source \
    $binfile > $datadir/zsh/site-functions/_%binfile_name
mkdir -p $datadir/bash-completion/completions
_COOKIECUTTER_COMPLETE=bash_source \
    $binfile > $datadir/bash-completion/completions/%binfile_name
mkdir -p $datadir/fish/vendor_completions.d
_COOKIECUTTER_COMPLETE=fish_source \
    $binfile > $datadir/fish/vendor_completions.d/%binfile_name.fish

%check
# create empty pytest ini file to avoid of using unless --cov* keys
touch pytest.ini
%pyproject_run_pytest -vra

%files
%doc README.md docs/* LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_datadir/zsh/site-functions/_%binfile_name
%_datadir/bash-completion/completions/%binfile_name
%_datadir/fish/vendor_completions.d/%binfile_name.fish

%changelog
* Wed Nov 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- 2.4.0 -> 2.5.0

* Fri Oct 06 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Sat Aug 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.0-alt1
- Initial build for ALT Sisyphus

