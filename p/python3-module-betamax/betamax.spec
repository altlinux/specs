%global pypi_name betamax
%def_without check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: VCR imitation for python-requests

Group: Development/Python3
License: Apache-2.0
URL: https://pypi.org/project/betamax
VCS: https://github.com/sigmavirus24/betamax

Source: %name-%version.tar
Patch:  betamax-system-urllib3.patch

BuildArch: noarch

BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-requests

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests
much easier.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_fixtures and not test_replays_response_from_cassette and not TestPyTestParametrizedFixtures"

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Build new version (Closes: #49596).

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Drop python2 support.

* Mon Apr 22 2019 Ivan A. Melnikov <iv@altlinux.org> 0.8.1-alt1
- 0.8.1

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
