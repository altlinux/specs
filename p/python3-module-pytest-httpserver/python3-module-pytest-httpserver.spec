%define pypi_name pytest_httpserver

%def_enable check

Name: python3-module-pytest-httpserver
Version: 1.0.11
Release: alt1

Summary: HTTP server for pytest
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://www.github.com/csernazs/pytest-httpserver.git
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel python3-module-poetry-core >= 1.1
%{?_enable_check:
BuildRequires: python3-module-werkzeug python3-module-pytest python3-module-flake8
BuildRequires: python3-module-pytest python3-module-pytest-cov python3-module-coverage
BuildRequires: python3-module-requests python3-module-mypy python3-module-toml}

%description
This library is designed to help to test http clients without contacting
the real http server. In other words, it is a fake http server which is
accessible via localhost can be started with the pre-defined expected
http requests and their responses.

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
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc CHANGES* README* LICENSE

%changelog
* Sat Jul 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt1
- 1.0.11

* Sun Feb 25 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Mon May 22 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed May 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Sat Jul 30 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5
- ported to %%pyproject* macros, enabled %%check

* Fri Jan 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sun Dec 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Oct 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Aug 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus



