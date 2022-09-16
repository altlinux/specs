%define  oname certomancer

%def_with check

Name:    python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: PKI testing tool

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/certomancer

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-pytest-runner
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
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.md
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sun Aug 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Sat Jul 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.3-alt1
- Automatically updated to 0.8.3.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus.
