%define pypi_name mkdocs-git-authors-plugin
%define mod_name mkdocs_git_authors_plugin

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.2
Release: alt1

Summary: MkDocs plugin to display git authors of a page
License: MIT
Group:   Development/Python3
URL:     https://github.com/timvink/mkdocs-git-authors-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-GitPython
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-mkapi
BuildRequires: python3-module-mkdocs-git-revision-date-localized-plugin
BuildRequires: python3-module-mkdocs-macros-plugin
BuildRequires: python3-module-click
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Lightweight MkDocs plugin to display git authors of a markdown page.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
if [ ! -d .git ]; then
    git init
    git config user.email vinktim@gmail.com
    git config user.name 'Tim Vink'
    git add .
    git commit -m 'release'
    git tag '%version'
fi
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus.
