%define pypi_name lizard

%def_without version_fix
%def_with check

Name:    python3-module-%pypi_name
Version: 1.18.0
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

Source: %name-%version.tar

%description
Lizard is an extensible Cyclomatic Complexity Analyzer for many programming
languages including C/C++ (doesn't require all the header files or Java
imports). It also does copy-paste detection (code clone detection/code
duplicate detection) and many other forms of static code analysis.

%prep
%setup

%if_with version_fix
# Upstream often forget to bump version every release
# This is permanent fix of this problem
sed -i '2i## %version' CHANGELOG.md
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not testFortran and not test_gitignore_filter'

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/lizard_ext/
%python3_sitelibdir/lizard_languages/
%python3_sitelibdir/lizard-%version.dist-info/
%python3_sitelibdir/__pycache__/

%changelog
* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 1.18.0-alt1
- Automatically updated to 1.18.0.

* Thu Jun 26 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.31-alt1
- Automatically updated to 1.17.31.

* Mon May 12 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.30-alt1
- Automatically updated to 1.17.30.

* Tue May 06 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.28-alt1
- Automatically updated to 1.17.28.

* Sun Apr 27 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.27-alt1
- Automatically updated to 1.17.27.

* Thu Apr 24 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.26-alt1
- Automatically updated to 1.17.26.

* Mon Apr 21 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.25-alt1
- Automatically updated to 1.17.25.

* Mon Apr 14 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.24-alt1
- Automatically updated to 1.17.24.

* Tue Apr 01 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.23-alt1
- Automatically updated to 1.17.23.

* Thu Mar 27 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.22-alt1
- Automatically updated to 1.17.22.

* Thu Feb 27 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.20-alt1
- Automatically updated to 1.17.20.

* Sun Feb 09 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.18-alt1
- Automatically updated to 1.17.18.

* Wed Feb 05 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.17-alt1
- Automatically updated to 1.17.17.

* Fri Jan 31 2025 Grigory Ustinov <grenka@altlinux.org> 1.17.14-alt1
- Automatically updated to 1.17.14.

* Fri Nov 15 2024 Grigory Ustinov <grenka@altlinux.org> 1.17.13-alt1
- Automatically updated to 1.17.13.

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 1.17.10-alt2
- NMU: fixed FTBFS.

* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 1.17.10-alt1
- Initial build for Sisyphus.
