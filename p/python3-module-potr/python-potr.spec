Name: python3-module-potr
Version: 1.0.2
Release: alt1
Summary: Python Off-The-Record encryption
Group: Development/Python3
License: LGPLv3+
Url: http://python-otr.pentabarf.de
BuildArch: noarch
Source: python-potr-%version.zip

BuildRequires(pre): rpm-build-python3 unzip

%description
This is a pure Python OTR implementation; it does not bind to libotr.

%prep
%setup -n python-potr-%version

%build
%python3_build

%install
%python3_install

%files
%doc src/tools/convertkey.py CHANGELOG PKG-INFO
%python3_sitelibdir/*

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Autobuild version bump to 1.0.0

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.9.9-alt1
- Initial build from scratch

