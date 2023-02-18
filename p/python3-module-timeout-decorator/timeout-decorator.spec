%define pypi_name timeout-decorator

Name:    python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Timeout decorator for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/timeout-decorator

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/timeout_decorator
%python3_sitelibdir/%{pyproject_distinfo timeout_decorator}

%changelog
* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
