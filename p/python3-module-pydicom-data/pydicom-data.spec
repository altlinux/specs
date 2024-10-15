%define pypi_name pydicom-data

%def_with check

Name:           python3-module-%pypi_name
Version:        1.0.0
Release:        alt0.6.git8da482f

Summary:        Test files for pydicom

License:        MIT
Group:          Development/Python3
URL:            https://pypi.org/project/pydicom-data
VCS:            https://github.com/pydicom/pydicom-data

Source:         %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Test files used by pydicom and other packages by the same organisation.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/data_store
%python3_sitelibdir/pydicom_data-%version.dist-info

%changelog
* Tue Oct 15 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt0.6.git8da482f
- Initial build for Sisyphus.
