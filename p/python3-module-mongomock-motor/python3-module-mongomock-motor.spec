%define pypi_name mongomock-motor
%define mod_name mongomock_motor

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.36
Release: alt2

Summary: Library for mocking AsyncIOMotorClient built on top of mongomock
License: MIT
Group:   Development/Python3
URL:     https://github.com/michaelkryukov/mongomock_motor

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-bson
BuildRequires: python3-module-pymongo
BuildRequires: python3-module-marshmallow
BuildRequires: python3-module-mongomock
BuildRequires: python3-module-anyio
BuildRequires: python3-module-beanie
BuildRequires: python3-module-mongo-thingy
BuildRequires: python3-module-umongo
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's/version = "0.0.0"/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_bulk_write and not test_umongo'

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.36-alt2
- Fix tests.

* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.36-alt1
- New 0.0.36 version.

* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.35-alt1
- Initial build for Sisyphus.
