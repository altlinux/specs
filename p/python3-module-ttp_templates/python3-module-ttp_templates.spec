%define pypi_name ttp_templates

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.9
Release: alt1

Summary: This repository contains a collection of TTP templates
License: MIT
Group:   Development/Python3
URL:     https://github.com/dmulyalin/ttp_templates

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-ttp
BuildRequires: python3-module-netmiko
BuildRequires: python3-module-cerberus
BuildRequires: python3-module-yaml
BuildRequires: python3-module-pydantic
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
cp -r ttp_templates/misc/{N,n}etmiko
export PYTHONPATH="$PWD"
pushd test
python3 -m pytest -k 'not (yangson or test_yang_ietf_interfaces or test_get_inventory or test_parse_output_get_parameter or test_parse_output_with_get_and_platform)'
popd

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.5.9-alt1
- New 0.5.9 version.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.3.6-alt1
- New 0.3.6 version.

* Tue Nov 14 2023 Alexander Burmatov <thatman@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus.
