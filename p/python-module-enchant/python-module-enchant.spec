Name: python-module-enchant
Version: 1.6.5
Release: alt1.1
%setup_python_module enchant

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



%prep
%setup -q -n pyenchant-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/enchant


%changelog
* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.5-alt1
- initial build for sisyphus

