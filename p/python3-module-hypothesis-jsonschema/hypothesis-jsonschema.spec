%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-jsonschema
%define mod_name hypothesis_jsonschema

%def_with check

Name:    python3-module-%pypi_name
Version: 0.23.1
Release: alt1

Summary:   Generate test data from JSON schemata with Hypothesis
License:   MPL-2.0
Group:     Development/Python3
Url:       https://github.com/python-jsonschema/hypothesis-jsonschema
Vcs:       https://github.com/python-jsonschema/hypothesis-jsonschema.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-hypothesis
%endif

%description
A Hypothesis strategy for generating data that matches some JSON schema.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -n auto

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jan 15 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.23.1-alt1
  - Initial build for ALT.
