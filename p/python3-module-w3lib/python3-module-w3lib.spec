%define pypi_name w3lib

%def_enable check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Python library of web-related functions
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name
Vcs: https://github.com/scrapy/w3lib.git

Source: https://pypi.io/packages/source/w/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-tox python3-module-pytest
BuildRequires: python3-module-pytest-cov python3-module-flake8 python3-module-mypy
BuildRequires: python3-module-pylint python3-module-black}

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



