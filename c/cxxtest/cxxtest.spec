Name: cxxtest
Summary: CxxTest Testing Framework for C++
Version: 4.0
Release: alt1.svn.153.1
License: LGPL
Url: http://cxxtest.tigris.org/
Group: Development/C++
Packager: Egor Glukhov <kaman@altlinux.org>

Source: %name-%version-%release.tar
BuildArch: noarch
BuildRequires: python-devel

%description
CxxTest is a JUnit/CppUnit/xUnit-like framework for C++.
Its advantages over existing alternatives are that it:
 - Doesn't require RTTI
 - Doesn't require member template functions
 - Doesn't require exception handling
 - Doesn't require any external libraries (including memory management,
   file/console I/O, graphics libraries)

%prep
%setup

%build
cd python
%python_build

%install
install -m 755 -d %buildroot%_bindir %buildroot%_includedir/%name
install -m 755 python/scripts/cxxtestgen %buildroot%_bindir
ln -s cxxtestgen %buildroot%_bindir/cxxtestgen.py
install -m 644 %name/* %buildroot%_includedir/%name
cd python
%python_install

%files
%doc README
%doc sample
%_includedir/%name
%_bindir/*
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0-alt1.svn.153.1
- Rebuild with Python-2.7

* Tue Jul 13 2010 Egor Glukhov <kaman@altlinux.org> 4.0-alt1.svn.153
- initial build


