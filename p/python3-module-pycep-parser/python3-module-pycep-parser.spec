%define pypi_name pycep-parser
%define module_name pycep

%def_with check

Name:    python3-module-%pypi_name
Version: 0.7.1
Release: alt2

Summary: A Python based Bicep parser
License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pycep-parser/
VCS:     https://github.com/gruebel/pycep

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-uv-build

# missing runtime dependecy
%py3_requires regex

%if_with check
BuildRequires: python3-module-assertpy
BuildRequires: python3-module-lark
BuildRequires: python3-module-regex
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
A parser for Azure Bicep files leveraging Lark.

%prep
%setup

# Upstream tag 0.7.1 still contains version 0.7.1.dev11.
sed -i 's/^version = "0\.7\.1\.dev11"$/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 08 2026 Evgeniy Serov <scala@altlinux.org> 0.7.1-alt2
- Added missing runtime dependency on python3-module-regex.

* Thu Oct 01 2026 Evgeniy Serov <scala@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
