%define _unpackaged_files_terminate_build 1

Name: python3-module-wadllib
Version: 1.3.5
Release: alt1
Summary: Python library for navigating WADL files
License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/wadllib
Packager: Anatoly Kitaikin <cetus@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

%add_python3_req_skip lazr
Requires: python3(lazr.uri)

BuildRequires(pre): rpm-build-python3

%description
The Web Application Description Language is an XML vocabulary
for describing the capabilities of HTTP resources. wadllib can
be used in conjunction with an HTTP library to navigate and
manipulate those resources.

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: wadllib tests
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

%prep
%setup -q

%build
#find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build

%check
%python3_build check

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/wadllib/tests
%doc HACKING.txt README.txt

%files tests
%python3_sitelibdir/wadllib/tests

%changelog
* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 1.3.5-alt1
- Release 1.3.5

* Tue Dec 08 2020 Anatoly Kitaykin <cetus@altlinux.org> 1.3.3-alt5
- Drop python 2 support

* Sun Aug 11 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.3.3-alt4
- Requirements fix

* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.3.3-alt3
- Repack

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.3.3-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.3.3-alt1
- initial build
