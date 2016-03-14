Name: python-module-enchant
Version: 1.6.5
Release: alt4.1
# XXX this is ugly, need to change when python3 macros set developes
%ifdef setup_python_module
%setup_python_module enchant
%endif

Summary: PyEnchant is a spellchecking library for Python
License: GPLv2+
Group: Development/Python
Url: http://packages.python.org/pyenchant/
BuildArch: noarch

Source: pyenchant-%version.tar

BuildPreReq: python-devel rpm-build-python python-module-setuptools
BuildRequires: libenchant-devel

%description
PyEnchant combines all the functionality of the underlying Enchant
library with the flexibility of Python and a nice "Pythonic"
object-oriented interface. It also aims to provide some higher-level
functionality than is available in the C API.

%ifdef setup_python_module
%package gui
Summary: PyEnchant GUI dialogs
Group: Development/Python
%description gui
PyEnchant GUI dialogs
%endif

%prep
%setup -q -n pyenchant-%version
sed -i '/use_setuptools/d' setup.py

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/enchant
%exclude %python_sitelibdir/enchant/checker/*CheckerDialog*
%exclude %python_sitelibdir/enchant/checker/tests.py

%ifdef setup_python_module
%files gui
%python_sitelibdir/enchant/checker/*CheckerDialog*
%python_sitelibdir/enchant/checker/tests.py
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

