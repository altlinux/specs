%def_without check

%define modulename canonicaljson
Name: python3-module-canonicaljson
Version: 1.6.0
Release: alt1

Summary: Canonical JSONs

Url: https://github.com/matrix-org/python-canonicaljson
License: ASL 2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-canonicaljson/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

# non detectable
Requires: python3(simplejson)

%description
Features:
* Encodes objects and arrays as RFC 7159 JSON.
* Sorts object keys so that you get the same result each time.
* Has no inignificant whitespace to make the output as small as possible.
* Escapes only the characters that must be escaped,
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.
* Uses the shortest escape sequence for each escaped character.
* Encodes the JSON as UTF-8.
* Can encode frozendict immutable dictionaries.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Tue Oct 13 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Tue Sep 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- add missed undetectable simplejson requires

* Fri Sep 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Fri Sep 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- separated python3 build

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- new version 1.1.4 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

