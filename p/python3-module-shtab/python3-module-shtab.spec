%define _unpackaged_files_terminate_build 1

%define modulename shtab
%def_with check

Name: python3-module-%modulename
Version: 1.6.5
Release: alt1

Summary: Automagic shell tab completion for Python CLI applications
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/shtab/
Vcs: https://github.com/iterative/shtab
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest-cov python3-module-pytest-timeout
%endif

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.rst CONTRIBUTING.md LICENCE docs/index.md docs/use.md examples

%changelog
* Mon Dec 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.6.5-alt1
- 1.6.4 -> 1.6.5

* Wed Oct 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.6.4-alt1
- 1.6.1 -> 1.6.4

* Fri May 05 2023 Alexander Stepchenko <geochip@altlinux.org> 1.6.1-alt1
- New version 1.6.1

* Tue Nov 29 2022 Alexander Stepchenko <geochip@altlinux.org> 1.5.8-alt1
- Initial build for ALT.
