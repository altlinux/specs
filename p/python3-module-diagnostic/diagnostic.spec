%define pypi_name diagnostic

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.0
Release: alt1

Summary: Build command line tools with great error reporting

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/diagnostic
VCS:     https://github.com/pradyunsg/diagnostic

Source: %name-%version.tar
Patch: python-diagnostic-test.patch

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-rich
BuildRequires: python3-module-yaml
%endif

BuildArch: noarch

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Feb 08 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
