%define _unpackaged_files_terminate_build 1

%define pypi_name bibtexparser

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.3
Release: alt1

Summary: Bibtex parser for Python 3
License: MIT
Group: Development/Python3
URL: https://github.com/sciunto-org/python-bibtexparser

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(sphinx)

%if_with check
BuildRequires: python3(pylatexenc)
BuildRequires: python3(pyparsing)
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The bibtexparser module provides parsing and writing of BibTeX files
functionality. The parsed data is returned as a simple BibDatabase object
with the main attribute being entries representing bibliographic sources
such as books and journal articles.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc CHANGELOG CONTRIBUTING.md COPYING README.rst RELEASE
%doc docs/build/html
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus
