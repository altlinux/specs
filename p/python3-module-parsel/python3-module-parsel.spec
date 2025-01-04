%define pypi_name parsel

%def_enable check

Name: python3-module-%pypi_name
Version: 1.10.0
Release: alt1

Summary: XML/HTML parsing library
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/scrapy/parsel.git

#Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
Source: https://github.com/scrapy/parsel/archive/v%version/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools
%{?_enable_check:BuildRequires: python3(tox) python3-module-tox-no-deps python3-module-tox-console-scripts
BuildRequires: python3(lxml) python3(cssselect) python3(psutil) python3(jmespath)
BuildRequires: python3(w3lib) python3(sybil) python3(pytest_cov) /proc}

%description
Parsel is a Python library to extract and remove data from HTML and XML
using XPath and CSS selectors, optionally combined with regular
expressions.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Mon Apr 08 2024 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Fri Mar 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Apr 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu Feb 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1.1
- fixed %%check

* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Oct 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- first build for Sisyphus



