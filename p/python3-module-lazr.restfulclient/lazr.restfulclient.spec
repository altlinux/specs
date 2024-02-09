%define _unpackaged_files_terminate_build 1

%define oname lazr.restfulclient

%def_with check

Name: python3-module-%oname
Version: 0.14.5
Release: alt2

Summary: A programmable lazr.restful client library

License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/lazr.restfulclient

BuildArch: noarch

Source: %name-%version.tar
Patch: lazr.restfulclient-0.14.5-ConfigParser-fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-wsgi_intercept
BuildRequires: python3-module-httplib2
BuildRequires: python3-module-oauthlib
BuildRequires: python3-module-wadllib
BuildRequires: python3-module-distro
BuildRequires: python3-module-zope.testrunner
%endif

%py3_provides lazr.restfulclient

%description
A programmable client library that takes advantage of the commonalities
among lazr.restful web services to provide added functionality on top of wadllib.

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: lazr.restfulclient tests
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf src/lazr/restfulclient/tests/test_docs.py
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.rst
%python3_sitelibdir/lazr/restfulclient
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/%oname-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/lazr/restfulclient/tests

%files tests
%python3_sitelibdir/lazr/restfulclient/tests

%changelog
* Fri Feb 09 2024 Anton Vyatkin <toni@altlinux.org> 0.14.5-alt2
- (NMU) Add support for python3.12.
- Moved on modern pyproject macros.
- Build with check.

* Sun Oct 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.14.5-alt1
- Automatically updated to 0.14.5.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.14.4-alt1
- Automatically updated to 0.14.4.

* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 0.14.3-alt1
- Release 0.14.3

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 0.14.2-alt5
- Drop python2 support.

* Sun Aug 11 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt4
- Requirements fix

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt3
- Repack

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 0.14.2-alt1
- initial build
