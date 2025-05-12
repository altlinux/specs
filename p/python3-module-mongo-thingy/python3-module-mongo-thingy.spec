%define pypi_name mongo-thingy
%define mod_name mongo_thingy

# need network
%def_without check

Name:    python3-module-%pypi_name
Version: 0.17.2
Release: alt2

Summary: Powerful schema-less ODM for MongoDB and Python (sync + async)
License: MIT
Group:   Development/Python3
URL:     https://github.com/Refty/mongo-thingy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Mongo-Thingy is the most idiomatic and friendly-yet-powerful way to use MongoDB
with Python.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-%version.dist-info/

%changelog
* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 0.17.2-alt2
- Fix build.

* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.17.2-alt1
- Initial build for Sisyphus.
