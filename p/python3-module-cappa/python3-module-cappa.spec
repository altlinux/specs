%define pypi_name cappa

#1 failed, 776 passed, 2 skipped, 5 warnings
%def_disable check

Name: python3-module-%pypi_name
Version: 0.32.2
Release: alt1

Summary: Cappa is a declarative command line parsing library
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/dancardin/cappa

Vcs: https://github.com/dancardin/cappa.git
Source: https://pypi.io/packages/source/c/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)
%{?_enable_check:BuildRequires: python3(pytest) python3(pylint)
BuildRequires: python3(mypy) python3(rich) python3(type_lens)
BuildRequires: python3(docstring_parser) python3(attr) python3(docutils)
BuildRequires: python3(pydantic) python3(msgspec)}

%description
Cappa is a declarative command line parsing library, which uses runtime
type inspection to infer (default) CLI argument behavior, and provide
automatic help text generation and dynamic completion generation.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test-3 tests

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*

%changelog
* Mon Aug 10 2026 Yuri N. Sedunov <aris@altlinux.org> 0.32.2-alt1
- first build for Sisyphus

