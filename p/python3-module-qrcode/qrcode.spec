%define oname qrcode

%def_with check

Name: python3-module-%oname
Version: 7.4.2
Release: alt2

Summary: Python module to generate QR Codes

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/lincolnloop/python-qrcode

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
Buildrequires: python3-module-pytest
Buildrequires: python3-module-Pillow
Buildrequires: python3-module-typing_extensions
Buildrequires: python3-module-pypng
%endif

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
This module uses image libraries, Python Imaging Library (PIL) by default,
to generate QR Codes.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -s qrcode

%files
%doc README.rst LICENSE CHANGES.rst
%_bindir/qr
%_man1dir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Tue Feb 14 2023 Grigory Ustinov <grenka@altlinux.org> 7.4.2-alt2
- Fixed qrcode.image.pure, pymaging problem was solved.

* Mon Feb 13 2023 Grigory Ustinov <grenka@altlinux.org> 7.4.2-alt1
- Automatically updated to 7.4.2.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 7.3.1-alt1
- Build new version.

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
