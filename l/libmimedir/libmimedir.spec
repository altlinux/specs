Name: libmimedir
Version: 0.5.1
Release: alt3
Epoch: 20110121

Summary: MIME Directory Profile parser library
License: BSD
Group: Communications

Url: http://libmimedir.sf.net
Source0: %name-%version.tar.gz
Packager: SynCE Development Team <synce@packages.altlinux.org>

# Automatically added by buildreq on Fri Jan 21 2011
BuildRequires: gcc-c++

%description
RFC2425 MIME Directory Profile parser library.
Static-only version (should be %name-devel{,-static}).

%prep
%setup

%build
%configure
# SMP incompatible build
make CFLAGS="$CFLAGS -fPIC"

%install
mkdir -p %buildroot{%_libdir,%_includedir}
install -pDm644 libmimedir.h %buildroot%_includedir/libmimedir.h
install -pDm644 libmimedir.a %buildroot%_libdir/libmimedir.a

%files
%_libdir/*
%_includedir/*

# TODO: http://cvs.pld-linux.org/cgi-bin/cvsweb.cgi/~checkout~/packages/libmimedir/

%changelog
* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 20110121:0.5.1-alt3
- 0.5.1 (thanks force@)
- buildreq

* Thu Mar 23 2006 Eugene V. Horohorin <genix@altlinux.ru> 20060323:0.4-alt3
- yet another x86_64 fix

* Sun Feb 26 2006 Eugene V. Horohorin <genix@altlinux.ru> 20060226:0.4-alt2
- x86_64 support:
  * wrong buildreq removed
  * spec clean-up

* Sun Apr 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 20050424:0.4-alt1
- new version

* Sat Nov 29 2003 Michael Shigorin <mike@altlinux.ru> 20031129:0.3-alt1
- built for ALT Linux (SynCE dependency)

