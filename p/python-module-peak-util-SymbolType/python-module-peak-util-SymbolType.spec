%define oname SymbolType
Name: python-module-peak-util-%oname
Version: 1.0
Release: alt1.1

Summary: Simple "symbol" type, useful for enumerations or sentinels

License: PSF or ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/%oname/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools

Requires: python-module-peak

%setup_python_module %oname

Source: http://pypi.python.org/packages/source/S/%oname/%oname-%version.tar

%description
Installing SymbolType (using "easy_install SymbolType" or "setup.py
install") gives you access to the peak.util.symbols module, previously
available only by installing the full PEAK toolkit. peak.util.symbols
provides a Symbol type and two built-in symbols that are used by PEAK:
NOT_FOUND and NOT_GIVEN. You can create your own symbol objects using
the Symbol type, by giving it the symbol name and the name of the module
where the symbol is being created:

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/util/*
%python_sitelibdir/%{oname}*.egg-info
%python_sitelibdir/%{oname}*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

