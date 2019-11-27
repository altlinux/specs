%define oname iptools

Name: python3-module-%oname
Version: 0.6.1
Release: alt2

Summary: Utilities for manipulating IPv4 and IPv6 addresses
License: BSD
Group: Development/Python3
Url: https://github.com/bd808/python-iptools/
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Utilities for manipulating IPv4 and IPv6 addresses including a class that
can be used to include CIDR network blocks in Django's INTERNAL_IPS setting.

%prep
%setup -n %oname-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/*.egg-*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 10 2013 Vladimir Didenko <cow@altlinux.ru> 0.6.1-alt1
- initial build for Sisyphus
