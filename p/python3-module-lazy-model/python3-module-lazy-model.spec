%define pypi_name lazy-model
%define mod_name lazy_model

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Lazy parsing for Pydantic models
License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/lazy-model

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

BuildArch: noarch

Source: %name-%version.tar

%description
This library provides a lazy interface for parsing objects from dictionaries.
During the parsing, it saves the raw data inside the object and parses each
field on demand.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%doc %python3_sitelibdir/LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 07 2024 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
