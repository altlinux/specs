%define _unpackaged_files_terminate_build 1

%define pypi_name typer
%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt2

Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
License: MIT
Group: Development/Python3
Url: https://typer.tiangolo.com/
Vcs: https://github.com/tiangolo/typer

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: /proc
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%endif

%description
Typer is a library for building CLI applications that users will love
using and developers will love creating. Based on Python 3.6+ type hints.

The key features are:
* Intuitive to write: Great editor support. Completion everywhere. Less
  time debugging. Designed to be easy to use and learn. Less time reading
  docs.
* Easy to use: It's easy to use for the final users. Automatic help, and
  automatic completion for all shells.
* Short: Minimize code duplication. Multiple features from each parameter
  declaration. Fewer bugs.
* Start simple: The simplest example adds only 2 lines of code to your app:
  1 import, 1 function call.
* Grow large: Grow in complexity as much as you want, create arbitrarily
  complex trees of commands and groups of subcommands, with options and
  arguments.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
# Delete completion for click7 because of there is click > 8 in sisyphus
rm -v typer/_completion_click7.py
%pyproject_build

%install
%pyproject_install

%check
# Clean of the using coverage module, because we don't needs to it.
find tests -name *.py -type f -exec sed -i 's/-m coverage run //g' {} \; \
    -exec sed -i 's/"-m", "coverage", "run",//g' {} \; \
    -exec sed -i -e '/"-m",$/,+2d' {} \;
# Increase terminal line size, because some tests (test_not_exists from
# test_tutorial002.py and test_tutorial002_an.py) don't pass at narrow
# terminals.
export COLUMNS=135
## test_show_completion and test_install_completion
# Deselect these tests because of typer doesn't support SH, but this shell is
# run in hasher.
%pyproject_run_pytest \
    --deselect="tests/test_completion/test_completion.py::test_show_completion" \
    --deselect="tests/test_completion/test_completion.py::test_install_completion"

%files
%doc README.md docs
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Oct 21 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.0-alt2
- Fixed FTBFS: deselect some tests for bash completion

* Thu Sep 14 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus
