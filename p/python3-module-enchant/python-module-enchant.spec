Name: python3-module-enchant
Version: 1.6.5
Release: alt4.1
# XXX this is ugly, need to change when python3 macros set developes
%ifdef setup_python3_module
%setup_python3_module enchant
%endif

Summary: PyEnchant is a spellchecking library for Python
License: GPLv2+
Group: Development/Python3
Url: http://packages.python.org/pyenchant/
BuildArch: noarch

Source: pyenchant-%version.tar

BuildPreReq: python3-devel rpm-build-python3 python3-module-setuptools
BuildRequires: libenchant-devel

%description
PyEnchant combines all the functionality of the underlying Enchant
library with the flexibility of Python and a nice "Pythonic"
object-oriented interface. It also aims to provide some higher-level
functionality than is available in the C API.

%ifdef setup_python3_module
%package gui
Summary: PyEnchant GUI dialogs
Group: Development/Python3
%description gui
PyEnchant GUI dialogs
%endif

%prep
%setup -q -n pyenchant-%version
sed -i '/use_setuptools/d' setup.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/enchant
%exclude %python3_sitelibdir/enchant/checker/*CheckerDialog*
%exclude %python3_sitelibdir/enchant/checker/tests.py

%ifdef setup_python3_module
%files gui
%python3_sitelibdir/enchant/checker/*CheckerDialog*
%python3_sitelibdir/enchant/checker/tests.py
%endif

%changelog
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

