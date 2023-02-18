%define oname cattrs

# some problems with hypothesis
%def_without check

Name:    python3-module-%oname
Version: 22.2.0
Release: alt1

Summary: Complex custom class converters for attrs.
License: MIT
Group:   Development/Python3
URL:     https://github.com/python-attrs/cattrs

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-immutables
BuildRequires: python3-module-bson
BuildRequires: python3-module-ujson
BuildRequires: python3-module-orjson
%endif

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

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/cattr
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus.
