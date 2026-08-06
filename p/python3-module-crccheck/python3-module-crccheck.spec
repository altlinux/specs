%define modulename crccheck
%def_with check

Name: python3-module-crccheck
Version: 1.3.1
Release: alt1

Summary: Python library implementing CRC and checksum algorithms
License: MIT
Group: Development/Python3
URL: https://github.com/MartinScharrer/crccheck
VCS: https://github.com/MartinScharrer/crccheck

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Python classes to calculate CRCs and checksums from binary data.
The module implements all CRCs listed in the Catalogue of parametrised
CRC algorithms, as well as additive and XOR checksums with 8, 16
and 32 bit (Checksum8, Checksum16, Checksum32, etc)

%prep
%setup 

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-*.dist-info

%changelog
* Wed Aug 05 2026 Dina Tagantseva <dinchik@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.

