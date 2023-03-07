%define oname pyenchant

Name: python3-module-enchant
Version: 3.2.2
Release: alt1

Summary: PyEnchant is a spellchecking library for Python

License: LGPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyenchant

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libenchant-devel
# used dynamically
Requires: libenchant

%description
PyEnchant combines all the functionality of the underlying Enchant
library with the flexibility of Python and a nice "Pythonic"
object-oriented interface. It also aims to provide some higher-level
functionality than is available in the C API.

%if "@pyver@"==""
%package gui
Summary: PyEnchant GUI dialogs
Group: Development/Python@pyver@
%description gui
PyEnchant GUI dialogs
%endif

%prep
%setup
sed -i '/use_setuptools/d' setup.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/enchant
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/enchant/checker/*CheckerDialog*

# TODO
%if "@pyver@"==""
%files gui
%python3_sitelibdir/enchant/checker/*CheckerDialog*
%endif

%changelog
* Wed Mar 08 2023 Vitaly Lipatov <lav@altlinux.ru> 3.2.2-alt1
- new version 3.2.2 (with rpmrb script)

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt2
- NMU: restore missed libenchant

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- NMU: cleanup spec
- NMU: new version 3.2.1 (with rpmrb script)

* Thu Mar 15 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Add packaging egg-info.

* Wed Mar 14 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.
- Get rid of ugly macros.
- Add missing Requires.
- Change url, license.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.5-alt5
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 25 2014 Fr. Br. George <george@altlinux.ru> 1.6.5-alt4
- Fix build

* Wed May 22 2013 Fr. Br. George <george@altlinux.ru> 1.6.5-alt3
- Change specsubst scheme
- Separate GUI dialogs

* Mon May 13 2013 Fr. Br. George <george@altlinux.ru> 1.6.5-alt2
- Implement specsubst scheme
- Build for python3 also

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.5-alt1
- initial build for sisyphus

