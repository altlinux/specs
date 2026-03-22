%define pypi_name w3lib

%def_enable check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1

Summary: Python library of web-related functions
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/scrapy/w3lib.git

Source: https://pypi.io/packages/source/w/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

#Provides: python3(%pypi_name) = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest)
BuildRequires: python3-module-pytest-cov python3(flake8) python3(mypy)
BuildRequires: python3(pylint) python3(black)}

%description
This package provides Python library of web-related functions, such as:

remove comments, or tags from HTML snippets
extract base url from HTML snippets
translate entites on HTML strings
convert raw HTTP headers to dicts and vice-versa
construct HTTP auth header
converting HTML pages to unicode
sanitize urls (like browsers do)
extract arguments from urls

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sun Mar 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Thu Jan 29 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Jan 28 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Jan 27 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Wed Jun 12 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Jun 05 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Aug 03 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Thu Jun 22 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1.1
- fixed tests with Python 3.11.4

* Fri Dec 09 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Mon Nov 28 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Thu Oct 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus



