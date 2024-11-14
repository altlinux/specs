%define pypi_name mkdocs-git-revision-date-localized-plugin
%define mod_name mkdocs_git_revision_date_localized_plugin

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: MkDocs plugin to add a last updated date to your site pages
License: MIT
Group:   Development/Python3
URL:     https://github.com/timvink/mkdocs-git-revision-date-localized-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-babel
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-GitPython
BuildRequires: python3-module-mkdocs-git-authors-plugin
BuildRequires: python3-module-pytz
BuildRequires: python3-module-click
BuildRequires: python3-module-mkdocs-gen-files
BuildRequires: python3-module-mkdocs-static-i18n
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
git config --global user.email author@example.com
git config --global user.name author
git init
git add .
git commit -m 'release'
git tag '%version'
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
