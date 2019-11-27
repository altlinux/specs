%define oname ftputil

Name: python3-module-%oname
Version: 3.4
Release: alt2

Summary: high-level interface to the ftplib module
License: GPL
Group: Development/Python3
Url: http://ftputil.sschwarzer.net/trac
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/f/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
The ftputil Python library is a high-level interface to the ftplib
module. The FTPHost objects generated with ftputil allow many operations
similar to those of os  and os.path

%prep
%setup

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc doc/*
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.4-alt2
- python2 disabled

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4 (with rpmrb script)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.3-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.2.3-alt1.1
- Rebuilt with python-2.5.

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- initial build for ALT Linux Sisyphus
