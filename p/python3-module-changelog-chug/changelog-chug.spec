%define _unpackaged_files_terminate_build 1
%define pypi_name changelog-chug
%define mod_name chug

%def_without check

Name: python3-module-%pypi_name
Version: 0.0.3
Release: alt1.1
Summary: Parser library for project Change Log documents
License: AGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/changelog-chug
Vcs: https://git.sr.ht/~bignose/changelog-chug
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-semver
BuildRequires: python3-module-docutils

%if_with check
BuildRequires: python3-module-changelog-chug
BuildRequires: python3-module-coverage
BuildRequires: python3-module-testscenarios
BuildRequires: python3-module-testtools
%endif

%description
%pypi_name is a parser for project Change Log documents.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc README
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.0.3-alt1.1
- Demodernized packaging.

* Thu Nov 07 2024 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1
- 0.0.2 -> 0.0.3.

* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.
