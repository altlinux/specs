Name: fakeroot-ng
Version: 0.17
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Software that fools a program into thinking it is running as root
License: GPLv2+
Group: Development/Other

Url: http://sourceforge.net/projects/fakerootng
Source: http://downloads.sourceforge.net/fakerootng/fakeroot-ng-%version.tar.gz
Patch: fakeroot-ng-0.17-alt-glibc-2.16.patch
Patch1: fakeroot-ng-0.17-alt-gcc4.7.patch

# Automatically added by buildreq on Mon Sep 22 2008
BuildRequires: gcc-c++

%description
Fakeroot-ng uses the debug interface (PTRACE) to fool programs into thinking
they are running with root permission.

%prep
%setup
%patch -p2
%patch1 -p2

%build
# Fix check for supported platforms
%__subst 's/i686/i786|i686/' configure
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.1
- Fixed build with glibc 2.16 and gcc 4.7

* Thu Jul 02 2009 Victor Forsyuk <force@altlinux.org> 0.17-alt1
- 0.17

* Wed Jun 24 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Sat Jun 20 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15

* Mon Sep 22 2008 Victor Forsyuk <force@altlinux.org> 0.14-alt1
- Initial build.
