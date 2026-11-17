%define _unpackaged_files_terminate_build 1
%define pypi_name ezgb
%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1

Summary: Python library for working with git-bug repositories
License: GPL-2.0-or-later
Group: Development/Python3
Url: https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git/
Vcs: https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyproject-installer
BuildRequires: python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest python3-module-pygit2
BuildRequires: python3-module-typing_extensions
BuildRequires: git-core
# git-bug is unavailable on i586; integration tests skip without its CLI.
# Use the build host CPU because the package itself is noarch.
%if "%_host_cpu" != "i586"
BuildRequires: git-bug
%endif
%endif

%description
ezgb is a standalone Python library for working with git-bug repositories.
It reads bugs directly from native Git objects via pygit2 and uses the
git-bug command-line interface for writes, keeping its operation DAG and
Lamport clocks consistent.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
%if_with check
%pyproject_run_pytest -vra tests
%endif

%files
%doc README.md CHANGELOG.rst COPYING
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 16 2026 Vladislav Tatjanin <l27001@altlinux.org> 0.2.1-alt1
- Initial build.
