%define _unpackaged_files_terminate_build 1
%define pypi_name asyncer
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.18
Release: alt1

Summary: Asyncer, async and await, focused on developer experience
License: MIT
Group: Development/Python3
Url: https://asyncer.tiangolo.com/
Vcs: https://github.com/fastapi/asyncer
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Asyncer is a small library built on top of AnyIO.

Asyncer has a small number of utility functions that allow working with
async, await, and concurrent code in a more convenient way under my
(@tiangolo - Sebastian Ramirez) very opinionated and subjective point of
view.

The main goal of Asyncer is to improve developer experience by providing
better support for autocompletion and inline errors in the editor, and
more certainty that the code is bug-free by providing better support for
type checking tools like mypy.

Asyncer also tries to improve convenience and simplicity when working
with async code mixed with regular blocking code, allowing to use them
together in a simpler way... again, under my very subjective point of
view.

%prep
%setup
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.18-alt1
- Updated to 0.0.18.

* Thu Mar 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.17-alt1
- Initial build for ALT Sisyphus.

