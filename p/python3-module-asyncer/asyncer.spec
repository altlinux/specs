%define _unpackaged_files_terminate_build 1
%define pypi_name asyncer
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.19
Release: alt1

Summary: Asyncer, async and await, focused on developer experience
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/asyncer/
Vcs: https://github.com/fastapi/asyncer
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

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
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --session-timeout=600

%files
%doc LICENSE README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.19-alt1
- Updated to 0.0.19.

* Wed Jul 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.18-alt1
- Updated to 0.0.18.

* Thu Mar 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.17-alt1
- Initial build for ALT Sisyphus.

