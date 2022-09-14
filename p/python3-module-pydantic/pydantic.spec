%def_with check

%define  oname pydantic

Name:    python3-module-%oname
Version: 1.10.2
Release: alt1

Summary: Data parsing and validation using Python type hints

License: MIT
Group:   Development/Python3
URL:     https://github.com/pydantic/pydantic

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-mypy
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3 -v

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus.
