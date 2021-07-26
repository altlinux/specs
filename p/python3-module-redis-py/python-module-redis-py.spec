%define module_name redis
%define oname redis-py

Name: python3-module-%oname
Version: 3.4.1
Release: alt2
Group: Development/Python3
License: MIT
Summary: The Python interface to the Redis key-value store
URL: http://github.com/andymccurdy/redis-py
Packager: Vladimir Didenko <cow@altlinux.org>
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
The Python interface to the Redis key-value store

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES LICENSE README.rst
%python3_sitelibdir/%module_name/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt2
- drop python2 support

* Tue Mar 24 2020 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- new version
- fix license name

* Mon Oct 28 2019 Vladimir Didenko <cow@altlinux.org> 3.3.11-alt1
- new version

* Wed Oct 2 2019 Vladimir Didenko <cow@altlinux.org> 3.3.8-alt1
- new version

* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.org> 3.3.7-alt1
- new version

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- new version

* Thu Nov 29 2018 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- new version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 2.10.6-alt1
- new version

* Mon Jul 25 2016 Vladimir Didenko <cow@altlinux.org> 2.10.5-alt1
- new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.10.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.10.3-alt2.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt2
- Don't exclude .egg-info

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt1
- Version 2.10.3

* Mon Jun 23 2014 Vladimir Didenko <cow@altlinux.org> 2.10.1-alt1
- new version
- python 3 support

* Tue Aug 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.6.0-alt1
- new version

* Sat May 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.13-alt1
- build for ALT
