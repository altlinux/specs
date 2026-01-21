%define pypi_name vunit

%def_with check

Name: python3-module-%pypi_name
Version: 4.7.0
Release: alt1

Summary: Open source unit testing framework
License: MPL-2.0
Group: Development/Python3
Url: https://vunit.github.io/
VCS: https://github.com/VUnit/vunit

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-colorama

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
VUnit is an open source unit testing framework
for VHDL/SystemVerilog.
It features the functionality needed to realize
continuous and automated testing of your HDL code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests/unit

%files
%doc LICENSE.rst
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/*.dist-info
%exclude %python3_sitelibdir/tests/*

%changelog
* Thu Dec 7 2023 Danila Skachedubov <skachedubov@altlinux.org> 4.7.0-alt1
- Initial build for ALT.
