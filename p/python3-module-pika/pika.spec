%define oname pika

Name: python3-module-%oname
Version: 1.3.2
Release: alt1

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.

License: BSD-3-Clause
Group: Development/Python3
Url: http://github.com/pika/pika

BuildArch: noarch

# Source-git: https://github.com/pika/pika.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_requires twisted.internet tornado

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%pyproject_build

# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

# Delete tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%files docs
%doc html/*

%changelog
* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Sat May 29 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Sat May 02 2020 Pavel Vasenkov <pav@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.14-alt1.git20141201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.14-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20141201
- New snapshot

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20140711
- Version 0.9.14
- Added module for Python 3

* Tue Jan 17 2012 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1.git20120106
- initial build

