%define _unpackaged_files_terminate_build 1

Name: python3-module-lazr.uri
Version: 1.0.3
Release: alt5
Summary: A self-contained, easily reusable library for parsing, manipulating, and generating URIs
License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/lazr.restfulclient
Packager: Anatoly Kitaikin <cetus@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

%add_python3_req_skip lazr

%py3_provides lazr.uri

BuildRequires(Pre): rpm-build-python3

%description
%summary

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: lazr.uri tests
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
%exclude %python3_sitelibdir/lazr/uri/tests
%doc HACKING.txt README.txt

%files tests
%python3_sitelibdir/lazr/uri/tests

%changelog
* Tue Dec 08 2020 Anatoly Kitaykin <cetus@altlinux.org> 1.0.3-alt5
- Drop python2 support

* Sat Aug 10 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.0.3-alt4
- Requirements fix

* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.0.3-alt3
- Repack

* Sat Jul 20 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.0.3-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.0.3-alt1
- initial build
