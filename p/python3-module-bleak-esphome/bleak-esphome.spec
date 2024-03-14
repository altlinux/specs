Name: python3-module-bleak-esphome
Version: 1.0.0
Release: alt1

Summary: Bleak backend of ESPHome
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak-esphome/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(aioesphomeapi)
BuildRequires: python3(habluetooth)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(lru)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/bleak_esphome
%python3_sitelibdir/bleak_esphome-%version.dist-info

%changelog
* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
