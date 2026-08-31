%define _unpackaged_files_terminate_build 1
%define pypi_name posthog

Name: python3-module-%pypi_name
Version: 7.45.1
Release: alt1

Summary: Send usage data from your Python code to PostHog
License: MIT
Group: Development/Python3

Url: https://github.com/posthog/posthog-python
Vcs: https://github.com/posthog/posthog-python
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# do not package tests (no clients)
rm -r %buildroot%python3_sitelibdir/posthog/test

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README.md

%changelog
* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 7.45.1-alt1
- NMU: Updated to 7.45.1.

* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 3.24.1-alt1
- Initial build
