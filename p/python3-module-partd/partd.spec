%define pypi_name partd

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Concurrent appendable key-value storage

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/partd
VCS:     https://github.com/dask/partd

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-locket
BuildRequires: python3-module-toolz
%endif

BuildArch: noarch

Source: %name-%version.tar
Patch: partd-no-versioneer.patch

%description
%summary.

%prep
%setup

# workaround for versioneer
%patch -p1
sed -i 's/@VERSION@/%version/' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
