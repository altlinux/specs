Name: waf
Version: 1.5.18
Release: alt2.1

Summary: A Python-based build system
License: BSD
Group: Development/Other

URL: http://code.google.com/p/waf/
Source: http://waf.googlecode.com/files/waf-%version.tar.bz2
Patch: waf-1.5.11-libdir.patch

# Automatically added by buildreq on Mon Aug 09 2010
BuildRequires: python-devel python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging

BuildArch: noarch

# skip file that bombs req finder
%add_findreq_skiplist /usr/bin/*

%description
Waf is a Python-based framework for configuring, compiling and installing
applications. It is a replacement for other tools such as Autotools, Scons,
CMake or Ant.

%prep
%setup
%patch -p1

%build
./configure --prefix=/usr
./waf-light --make-waf

%install
./waf install --yes --destdir=%buildroot

%files
%_bindir/*
%_datadir/waf

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.18-alt2.1
- Rebuild with Python-2.7

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.5.18-alt2
- Build with enabled req-finder (closes: #25802).

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 1.5.18-alt1
- 1.5.18

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.5.17-alt1
- 1.5.17

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 1.5.15-alt1
- 1.5.15

* Fri Feb 19 2010 Victor Forsiuk <force@altlinux.org> 1.5.13-alt1
- 1.5.13

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 1.5.12-alt1
- 1.5.12

* Sat Jan 30 2010 Victor Forsyuk <force@altlinux.org> 1.5.11-alt1
- Initial build.
