%define  oname certomancer

%def_with check

Name:    python3-module-%oname
Version: 0.9.1
Release: alt1

Summary: PKI testing tool

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/certomancer

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-yaml
BuildRequires: python3-module-pytz
BuildRequires: python3-module-pyHanko-certvalidator
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-tzlocal
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-tzdata
BuildRequires: python3-module-pytest-asyncio
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
Quickly construct, mock & deploy PKI test configurations using
simple declarative configuration. Includes CRL, OCSP and time stamping
service provisioning.

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
%doc *.md
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt1
- Automatically updated to 0.9.1.

* Sun Aug 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Sat Jul 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.3-alt1
- Automatically updated to 0.8.3.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus.
