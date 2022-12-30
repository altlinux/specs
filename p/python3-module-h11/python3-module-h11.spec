%define  modulename h11

Name:    python3-module-%modulename
Version: 0.14.0
Release: alt1

Summary: A pure-Python, bring-your-own-I/O implementation of HTTP/1.1

License: BSD 3-Clause License
Group:   Development/Python3
URL:     https://github.com/python-hyper/h11

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/python-hyper/h11/archive/v%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
This is a little HTTP/1.1 library written from scratch in Python,
heavily inspired by hyper-h2.

It's a "bring-your-own-I/O" library; h11 contains no IO code whatsoever.
This means you can hook h11 up to your favorite network API,
and that could be anything you want: synchronous, threaded, asynchronous,
or your own implementation of RFC 6214 -- h11 won't judge you.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/tests
%python3_sitelibdir/*.egg-info/

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt1
- new version 0.14.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Fri Nov 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt2
- exclude tests from package due to excessive reqs

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- initial build for Sisyphus
