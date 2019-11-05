%define oname txredis

Name: python3-module-%oname
Version: 2.3
Release: alt2

Summary: Python/Twisted client for Redis key-value store
License: BSD
Group: Development/Python3
URL: http://ooici.net/packages/txredis/
BuildArch: noarch

Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires twisted.trial


%description
%summary

%prep
%setup -n %oname-%version

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python3_install

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3-alt2
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.3-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Version 2.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.1
- Rebuild with Python-2.7

* Mon Nov 29 2010 Sergey Alembekov <rt@altlinux.ru> 0.1.2-alt1
- initial build for ALTLinux
