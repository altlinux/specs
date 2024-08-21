%define pypi_name mkdocs-autorefs
%define mod_name mkdocs_autorefs

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Automatically link across pages in MkDocs
License: ISC
Group:   Development/Python3
URL:     https://pypi.org/project/mkdocs-autorefs
VCS:     https://github.com/mkdocstrings/autorefs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm-backend
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-markdown
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-pymdown-extensions
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 21 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
