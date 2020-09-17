%define _unpackaged_files_terminate_build 1

Name: python3-module-lazr.restfulclient
Version: 0.14.2
Release: alt5
Summary: A programmable lazr.restful client library
License: lgpl3
Group: Development/Python3
Url: https://launchpad.net/lazr.restfulclient
Packager: Anatoly Kitaikin <cetus@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): /usr/bin/2to3

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

%build
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/lazr/restfulclient/tests
%doc HACKING.rst README.rst

%files tests
%python3_sitelibdir/lazr/restfulclient/tests

%changelog
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
