%define pypi_name google-crc32c

%def_with check

Name:    python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: A python wrapper of the C library 'Google CRC32C'

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/google-crc32c
VCS:     https://github.com/googleapis/python-crc32c

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libcrc32c-devel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/google_crc32c
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus.
