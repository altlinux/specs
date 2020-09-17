%define _unpackaged_files_terminate_build 1

Name: python3-module-launchpadlib
Version: 1.10.7
Release: alt3
Summary: Script Launchpad through its web services interfaces.  Officially supported.
License: gpl3
Group: Development/Python3
Url: https://launchpad.net/launchpadlib
Packager: Anatoly Kitaikin <cetus@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): /usr/bin/2to3

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
Requires: %name = %version-%release

%description tests
This package contain tools and test suites for testing launchpadlib.

%prep
%setup

%build
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build

%install
%python3_install

%files
%doc HACKING.txt README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/launchpadlib/tests

%files tests
%python3_sitelibdir/launchpadlib/tests

%changelog
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
