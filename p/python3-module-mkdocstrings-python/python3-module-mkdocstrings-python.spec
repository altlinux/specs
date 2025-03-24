%define pypi_name mkdocstrings-python
%define mod_name mkdocstrings_handlers

%def_with check

Name:    python3-module-%pypi_name
Version: 1.16.8
Release: alt1

Summary: A Python handler for mkdocstrings
License: ISC
Group:   Development/Python3
URL:    https://pypi.org/project/mkdocstrings-python
VCS:     https://github.com/mkdocstrings/python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-forked
BuildRequires: python3-module-markdown
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-griffe
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-inline-snapshot
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
# "None" meaning particular formatter not installed according Gentoo
%pyproject_run_pytest --deselect "tests/test_rendering.py::test_format_code[None-print('Hello')]"\
    --deselect "tests/test_rendering.py::test_format_code[None-aaaaa(bbbbb, ccccc=1) + ddddd.eeeee[ffff] or {ggggg: hhhhh, iiiii: jjjjj}]"

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 25 2025 Grigory Ustinov <grenka@altlinux.org> 1.16.8-alt1
- Automatically updated to 1.16.8.

* Thu Mar 20 2025 Grigory Ustinov <grenka@altlinux.org> 1.16.7-alt1
- Automatically updated to 1.16.7.

* Tue Mar 11 2025 Grigory Ustinov <grenka@altlinux.org> 1.16.5-alt1
- Automatically updated to 1.16.5.

* Mon Mar 10 2025 Grigory Ustinov <grenka@altlinux.org> 1.16.3-alt1
- Automatically updated to 1.16.3.

* Wed Feb 26 2025 Grigory Ustinov <grenka@altlinux.org> 1.16.2-alt1
- Automatically updated to 1.16.2.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.8.0-alt1
- New 1.8.0 version.

* Tue Dec 19 2023 Alexander Burmatov <thatman@altlinux.org> 1.7.5-alt1
- Update version to 1.7.5.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 1.7.3-alt1
- Initial build for Sisyphus.
