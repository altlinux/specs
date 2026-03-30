%def_with check

Name: python3-module-mashumaro
Version: 3.20
Release: alt1.1

Summary: Fast and well tested serialization library
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/mashumaro
VCS: https://github.com/Fatal1ty/mashumaro

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-orjson
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-tomli-w
BuildRequires: python3-module-yaml
BuildRequires: python3-module-ciso8601
BuildRequires: python3-module-pendulum
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/mashumaro
%python3_sitelibdir/mashumaro-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.20-alt1.1
- Demodernized packaging.

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.20-alt1
- 3.20 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.17-alt1
- 3.17 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.15-alt1
- 3.15 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.14-alt1
- 3.14 released
