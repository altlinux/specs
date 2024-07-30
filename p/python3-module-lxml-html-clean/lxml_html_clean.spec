%define oname lxml-html-clean
%define pypi_name lxml_html_clean

%def_with check

Name:    python3-module-%oname
Version: 0.2.0
Release: alt1

Summary: Separate project for HTML cleaning functionalities copied from lxml.html.clean.

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/lxml-html-clean
VCS:     https://github.com/fedora-python/lxml_html_clean

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-lxml
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This project was initially a part of lxml. Because HTML cleaner is designed as
blocklist-based, many reports about possible security vulnerabilities were filed
for lxml and that make the project problematic for security-sensitive environments.
Therefore we decided to extract the problematic part to a separate project.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE.txt *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1
- Automatically updated to 0.2.0.

* Fri Apr 05 2024 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt1
- Automatically updated to 0.1.1.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
