%define _unpackaged_files_terminate_build 1

%define oname lazr.restfulclient

Name: python3-module-%oname
Version: 0.14.4
Release: alt1

Summary: A programmable lazr.restful client library

License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/lazr.restfulclient

Packager: Anatoly Kitaikin <cetus@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

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
%python3_build

%install
%python3_install

%files
%doc HACKING.rst README.rst
%python3_sitelibdir/lazr/restfulclient
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%python3_sitelibdir/%oname-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/lazr/restfulclient/tests

%files tests
%python3_sitelibdir/lazr/restfulclient/tests

%changelog
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
