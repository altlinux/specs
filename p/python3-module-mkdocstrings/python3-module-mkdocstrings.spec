%define pypi_name mkdocstrings

%def_with check

Name:    python3-module-%pypi_name
Version: 0.23.0
Release: alt2

Summary: Automatic documentation from sources, for MkDocs
License: ISC
Group:   Development/Python3
URL:     https://github.com/mkdocstrings/mkdocstrings

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-pdm-backend
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-markdown
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-pymdown-extensions
BuildRequires: python3-module-mkdocs-autorefs
BuildRequires: python3-module-mkdocs-material-extensions
BuildRequires: python3-module-mkdocstrings-python
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mkdocs-coverage
BuildRequires: python3-module-mkdocs-git-committers-plugin
BuildRequires: python3-module-mkdocs-redirects
BuildRequires: python3-module-mkdocs-minify-plugin
BuildRequires: python3-module-markdown-callouts
BuildRequires: python3-module-markdown-exec
BuildRequires: python3-module-mkdocs-gen-files
BuildRequires: python3-module-mkdocs-literate-nav
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 27 2023 Alexander Burmatov <thatman@altlinux.org> 0.23.0-alt2
- Enable check.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.23.0-alt1
- Initial build for Sisyphus.
