%define modname ipaddr

Name: python3-module-%modname
Version: 2.2.0
Release: alt2

Summary: Library for working with IP addressess, both IPv4 and IPv6
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/google/ipaddr-py
BuildArch: noarch

Source: ipaddr-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%prep
%setup -n ipaddr-%version

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
./ipaddr_test.py

%files
%doc README COPYING wiki/*
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.10-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.10-alt2.1
- NMU: Use buildreq for BR.

* Thu Aug  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.10-alt2
- Update sources to current trunk (git commit c813f47)

* Thu Aug  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.10-alt1
- 2.1.10
- Update URL
- %%check section added

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.7-alt1.1
- Added module for Python 3

* Mon Jan 30 2012 Liudmila Butorina <lbutorina@altlinux.org> 2.1.7-alt1
- Initial build
