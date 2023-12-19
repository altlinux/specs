%define pypi_name mkdocstrings-python
%define mod_name mkdocstrings_handlers

%def_with check

Name:    python3-module-%pypi_name
Version: 1.7.5
Release: alt1

Summary: A Python handler for mkdocstrings
License: ISC
Group:   Development/Python3
URL:     https://github.com/mkdocstrings/python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-forked
BuildRequires: python3-module-markdown
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-griffe
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-mkdocs-material
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The Python handler uses Griffe to collect documentation from Python source code.
The word "griffe" can sometimes be used instead of "signature" in French.
Griffe is able to visit the Abstract Syntax Tree (AST) of the source code to
extract useful information. It is also able to execute the code
(by importing it) and introspect objects in memory when source code is not
available. Finally, it can parse docstrings following different styles.

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
* Tue Dec 19 2023 Alexander Burmatov <thatman@altlinux.org> 1.7.5-alt1
- Update version to 1.7.5.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 1.7.3-alt1
- Initial build for Sisyphus.
