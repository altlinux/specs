%define oname qrcode

Name: python3-module-%oname
Version: 6.1.0
Release: alt3

Summary: Python module to generate QR Codes

License: BSD
Group: Development/Python3
Url: https://github.com/lincolnloop/python-qrcode

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/q/qrcode/qrcode-4.0.4.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
This module uses image libraries, Python Imaging Library (PIL) by default,
to generate QR Codes.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE CHANGES.rst
%_bindir/*
%_man1dir/*
%python3_sitelibdir/%oname/
# pure.py requires pymaging module that is not ready for release
%exclude %python3_sitelibdir/%oname/image/pure.py
%python3_sitelibdir/*.egg-*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt3
- Drop python2 support.

* Mon Oct 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.1.0-alt2
- NMU: Do not exclude egg files: side modules rely on them.

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.org> 6.1.0-alt1
- new version

* Tue Oct 9 2018 Vladimir Didenko <cow@altlinux.org> 6.0.0-alt1
- new version

* Fri Jul 22 2016 Vladimir Didenko <cow@altlinux.org> 5.3.0-alt1
- new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 5.1.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Vladimir Didenko <cow@altlinux.ru> 5.1.0-alt1
- new version

* Tue Sep 16 2014 Vladimir Didenko <cow@altlinux.ru> 5.0.1-alt1
- new version

* Mon Apr 28 2014 Vladimir Didenko <cow@altlinux.ru> 4.0.4-alt3
- don't pack sample script

* Thu Apr 24 2014 Vladimir Didenko <cow@altlinux.ru> 4.0.4-alt2
- explicitly set python version for sample application

* Thu Jan 16 2014 Vladimir Didenko <cow@altlinux.ru> 4.0.4-alt1
- initial build for Sisyphus
