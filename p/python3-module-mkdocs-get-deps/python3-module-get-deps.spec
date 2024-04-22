%define pypi_name get-deps

%def_with check

Name: python3-module-mkdocs-%pypi_name
Version: 0.2.0
Release: alt1

Summary: An extra command for MkDocs that infers required PyPI packages from `plugins` in mkdocs.yml
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-get-deps
Vcs: https://github.com/mkdocs/get-deps
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-yaml
BuildRequires: python3-module-mergedeep
BuildRequires: python3-module-platformdirs
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
%_bindir/mkdocs-get-deps
%python3_sitelibdir/mkdocs_get_deps
%python3_sitelibdir/mkdocs_get_deps-%version.dist-info

%changelog
* Mon Apr 22 2024 Anton Vyatkin <toni@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
