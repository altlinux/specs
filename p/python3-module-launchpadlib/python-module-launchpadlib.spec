%define _unpackaged_files_terminate_build 1

%define oname launchpadlib

%def_with check

Name: python3-module-launchpadlib
Version: 1.11.0
Release: alt1
Summary: Script Launchpad through its web services interfaces.  Officially supported.
License: LGPL-3
Group: Development/Python3
Url: https://launchpad.net/launchpadlib
Packager: Anatoly Kitaikin <cetus@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-httplib2
BuildRequires: python3-module-lazr.uri
BuildRequires: python3-module-lazr.restfulclient
BuildRequires: python3-module-distro
BuildRequires: python3-module-coverage
BuildRequires: python3-module-testresources
%endif

%py3_provides launchpadlib

%description
launchpadlib is a standalone Python library for scripting Launchpad through
its web services interface.  It is the officially supported bindings to the
Launchpad web service, but there may be third party bindings that provide
scriptability for other languages.

This module is built for python %_python_version

%package tests
Summary: launchpadlib tests
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contain tools and test suites for testing launchpadlib.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc CONTRIBUTING.rst README.rst NEWS.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Mon Mar 06 2023 Anton Vyatkin <toni@altlinux.org> 1.11.0-alt1
- NMU: new version 1.11.0

* Fri Oct 21 2022 Anatoly Kitaykin <cetus@altlinux.org> 1.10.17-alt1
- Release 1.10.17

* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 1.10.13-alt1
- Release 1.10.13

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 1.10.7-alt3
- Drop python2 support.

* Sun Aug 11 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.7-alt2
- Requirements fix

* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.7-alt1
- Release 1.10.7

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.6-alt2
- Python3 support added

* Tue Mar 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.10.6-alt1
- Initial build
