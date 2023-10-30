%define pypi_name httmock

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: A mocking library for requests
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/patrys/httmock

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-requests
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
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/__pycache__/httmock*
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
