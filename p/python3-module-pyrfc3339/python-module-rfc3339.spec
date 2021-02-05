%global srcname pyRFC3339

Name: python3-module-pyrfc3339
Version: 1.1
Release: alt2

Summary: Generate and parse RFC 3339 timestamps

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyRFC3339

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.python.org/packages/source/p/pyRFC3339/pyRFC3339-%version.tar.gz
Source: %srcname-%version.tar

BuildArch: noarch

Provides: python3-module-rfc3339 = %EVR
Obsoletes: python3-module-rfc3339


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

# --- unit tests ---
#BuildRequires: python3-nose
#BuildRequires: python3-pytz

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%check
#__python setup.py test
#if_with python3
#__python3 setup.py test
#endif

%files
%doc README.rst
%doc LICENSE.txt
%python3_sitelibdir/pyrfc3339/
%python3_sitelibdir/%srcname-%version-*.egg-info

%changelog
* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- build python3 package separately

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 1.0-2
- epel7: Only build python2 package

* Tue Nov 10 2015 James Hogarth <james.hogarth@gmail.com>    - 1.0-1
- Add installed tests back as per review
- Update to new 1.0 PyPi release
- Add external license file
* Sun Nov 08 2015 James Hogarth <james.hogarth@gmail.com>    - 0.2-2
- Update to follow the python guidelines
* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2-1
- initial packaging
