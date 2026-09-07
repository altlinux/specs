%define _unpackaged_files_terminate_build 1
%def_with check
%define py_name libkirk

Name: kirk
Version: 4.1.0
Release: alt1

Summary: Devicetree Schema Tools
License: BSD-2-Clause
Group: Development/Tools
Url: https://kirk.readthedocs.io/en/latest/
Vcs: https://github.com/linux-test-project/kirk.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio

BuildRequires: /proc
BuildRequires: ltp-testsuite
%endif

%description
The dtschema module contains tools and schema data for Devicetree
schema validation using the json-schema vocabulary. The tools
validate Devicetree files using DT binding schema files. The tools
also validate the DT binding schema files. Schema files are written
in a JSON compatible subset of YAML to be both human and machine
readable.

This pacakges contains dt-schema tools.


%package -n python3-module-%py_name
Summary: Python library for devicetree schema tools
Group: Development/Python

%description -n python3-module-%py_name
The dtschema module contains tools and schema data for Devicetree
schema validation using the json-schema vocabulary. The tools
validate Devicetree files using DT binding schema files. The tools
also validate the DT binding schema files. Schema files are written
in a JSON compatible subset of YAML to be both human and machine
readable.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/*

%files -n python3-module-%py_name
%python3_sitelibdir_noarch/%{py_name}*
%python3_sitelibdir_noarch/%{name}*

%changelog
* Mon Sep 07 2026 Ivan A. Melnikov <iv@altlinux.org> 4.1.0-alt1
- build for Sisyphus
- fix test_com tests on slower machines
- set defalut LTPROOT to /usr/lib/ltp to match ALT ltp-suite packaging
