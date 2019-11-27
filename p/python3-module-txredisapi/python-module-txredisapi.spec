%define oname txredisapi

Name: python3-module-%oname
Epoch: 1
Version: 1.2
Release: alt2

Summary: Twisted client protocol for redis
License: Apache
Group: Development/Python3
URL: https://github.com/fiorix/txredisapi.git
BuildArch: noarch

Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
%summary

%prep
%setup -n %oname-%version

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.2-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.2-alt1.git20140728.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.2-alt1.git20140728.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:1.2-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt1.git20140728
- Version 1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20101029-alt1.1
- Rebuild with Python-2.7

* Tue Feb 01 2011 Sergey Alembekov <rt@altlinux.ru> 20101029-alt1
- initial build

