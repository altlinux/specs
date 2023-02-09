%define pypi_name parsel

%def_enable check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1.1

Summary: XML/HTML parsing library
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name
Vcs: https://github.com/scrapy/parsel.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-w3lib
BuildRequires: python3-module-pytest-cov python3-module-sybil
BuildRequires: python3-module-six python3-module-lxml python3(cssselect)
BuildRequires: python3-module-psutil /proc}

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
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Thu Feb 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1.1
- fixed %%check

* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Oct 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- first build for Sisyphus



