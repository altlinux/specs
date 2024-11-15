%define pypi_name lizard

%def_with check

Name:    python3-module-%pypi_name
Version: 1.17.13
Release: alt1

Summary: A simple code complexity analyser without caring about the C/C++ header files or Java imports, supports most of the popular languages
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/lizard
VCS:     https://github.com/terryyin/lizard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-pygments
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
# There no significant difference between 1.17.12 and 1.17.13
%python3_sitelibdir/lizard-1.17.12.dist-info/
%python3_sitelibdir/__pycache__/

%changelog
* Fri Nov 15 2024 Grigory Ustinov <grenka@altlinux.org> 1.17.13-alt1
- Automatically updated to 1.17.13.

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 1.17.10-alt2
- NMU: fixed FTBFS.

* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 1.17.10-alt1
- Initial build for Sisyphus.
