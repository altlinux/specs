%define pypi_name lizard

%def_with check

Name:    python3-module-%pypi_name
Version: 1.17.10
Release: alt1

Summary: A simple code complexity analyser without caring about the C/C++ header files or Java imports, supports most of the popular languages
License: MIT
Group:   Development/Python3
URL:     https://github.com/terryyin/lizard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-jinja2
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Lizard is an extensible Cyclomatic Complexity Analyzer for many programming
languages including C/C++ (doesn't require all the header files or Java
imports). It also does copy-paste detection (code clone detection/code
duplicate detection) and many other forms of static code analysis.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not testFortran'

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/lizard_ext/
%python3_sitelibdir/lizard_languages/
%python3_sitelibdir/lizard-1.17.9.dist-info/
%python3_sitelibdir/__pycache__/%pypi_name.cpython-311.*

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 1.17.10-alt1
- Initial build for Sisyphus.
