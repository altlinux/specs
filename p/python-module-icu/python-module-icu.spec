%define modulename icu

Name: python-module-%modulename
Version: 1.2
Release: alt1.1.1

%setup_python_module %modulename

Summary: Python extension wrapping the ICU C++ API
License: ISC-style
Group: Development/Python

Url: http://pyicu.osafoundation.org/
Packager: Kirill Maslinsky <kirill@altlinux.org>

%define srcname PyICU-%version
# http://pypi.python.org/packages/source/P/PyICU/%srcname.tar.gz
Source: %srcname.tar

BuildRequires: gcc-c++ libicu-devel python-dev

%description
PyICU - Python extension wrapping the ICU C++ API.

%prep
%setup -n %srcname

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%python_sitelibdir/*.egg-info
%doc README samples/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.2-alt1
- 1.2

* Tue May 31 2011 Kirill Maslinsky <kirill@altlinux.org> 1.1-alt1
- 1.1

* Fri Dec 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated to post-1.0.1 snapshot r166 to fix build with fresh ICU.

* Wed Aug 25 2010 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

