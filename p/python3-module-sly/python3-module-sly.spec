%define pypi_name sly

%def_with check

Name: python3-module-sly
Version: 0.5
Release: alt1

Summary: SLY - Sly Lex Yacc

License: MIT
Group: Development/Python3
URL: https://github.com/dabeaz/sly
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
SLY - Sly Lex Yacc.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m pytest -v tests

%files
%doc README*
%python3_sitelibdir/sly/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- initial build for Sisyphus
