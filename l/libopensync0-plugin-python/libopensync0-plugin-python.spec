%define orig_name libopensync-plugin-python
Name: libopensync0-plugin-python
Version: 0.22
Release: alt2.1.1

Summary: Python plugin for OpenSync
License: GPL
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %orig_name-%version.tar.bz2
Patch0: python_module.c.diff

Requires: python-base  
Requires: libopensync0 = %version

# Automatically added by buildreq on Thu Oct 16 2008
BuildRequires: gcc-c++ gcc-fortran glib2-devel glibc-devel-static libopensync0-devel python-devel

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q -n %orig_name-%version
%patch -p1

%build
%configure
%make

%install
%makeinstall install DESTDIR=%buildroot
rm -f %buildroot%_libdir/opensync/plugins/*.la

%files
%_libdir/opensync/plugins/*.so
%dir %_libdir/opensync/python-plugins
%_libdir/opensync/python-plugins/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2.1
- Rebuilt with python 2.6

* Thu Oct 16 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version.

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanip spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Tue Jul 18 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060718
- svn version 20060718

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060529
- svn version 20060529

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
