%define pypi_name pymox
%define mod_name mox

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Pymox - Powerful and intuitive mock object framework for Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/ivancrneto/pymox

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
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
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-0.0.0.dist-info/

%changelog
* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
