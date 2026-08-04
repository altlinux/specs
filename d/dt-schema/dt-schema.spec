%define _unpackaged_files_terminate_build 1
%def_with check
%define py_name dtschema

Name: dt-schema
Version: 2026.06
Release: alt1

Summary: Devicetree Schema Tools
License: BSD-2-Clause
Group: Development/Tools
Url: https://github.com/devicetree-org/dt-schema
Vcs: https://github.com/devicetree-org/dt-schema.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm

%if_with check
BuildRequires: python3-module-pytest

BuildRequires: python3(ruamel.yaml)
BuildRequires: python3(jsonschema)
BuildRequires: python3(rfc3987)
BuildRequires: python3(libfdt)

BuildRequires: dtc
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
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run ./test/test-dt-validate.py

%files
%_bindir/*

%files -n python3-module-%py_name
%python3_sitelibdir_noarch/%{py_name}*

%changelog
* Tue Aug 04 2026 Ivan A. Melnikov <iv@altlinux.org> 2026.06-alt1
- build for Sisyphus
