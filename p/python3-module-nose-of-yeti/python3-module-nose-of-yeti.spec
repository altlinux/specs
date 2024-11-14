%define pypi_name nose-of-yeti
%define mod_name noseOfYeti

%def_with check

Name:    python3-module-%pypi_name
Version: 2.4.9
Release: alt1

Summary: Provides an RSpec inspired dsl for python tests
License: MIT
Group:   Development/Python3
URL:     https://github.com/delfick/nose-of-yeti

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-helpers-namespace
BuildRequires: python3-module-alt-pytest-asyncio
%endif

%add_python3_req_skip pyls

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's|nose.plugins|nose2.plugins|g' pyproject.toml noseOfYeti/plugins/nosetests.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/noy_black.pth
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Oct 14 2024 Alexander Burmatov <thatman@altlinux.org> 2.4.9-alt1
- Initial build for Sisyphus.
