Name: libdomainkeys
Version: 0.69
Release: alt1

Summary: DomainKey email authentication system
License: freely distributable
Group: System/Libraries

URL: http://domainkeys.sourceforge.net/
Source0: http://dl.sf.net/domainkeys/libdomainkeys-%version.tar.gz

# Automatically added by buildreq on Tue Apr 01 2008
BuildRequires: libssl-devel

%description
Library that can be easily adopted by most MTA and MUA implementers to add
DomainKeys functionality.

%prep
%setup

%build
subst 's/ -O./ %optflags/; s/\(LIBS=.*\)/\1\nLIBS+=-lresolv/' Makefile
%make_build

%install
install -pD -m644 libdomainkeys.a %buildroot%_libdir/libdomainkeys.a
install -pD -m644 domainkeys.h %buildroot%_includedir/domainkeys.h
install -pD -m644 dktrace.h %buildroot%_includedir/dktrace.h

%files
%_libdir/*
%_includedir/*

%changelog
* Tue Apr 01 2008 Victor Forsyuk <force@altlinux.org> 0.69-alt1
- 0.69

* Mon Oct 10 2005 Victor Forsyuk <force@altlinux.ru> 0.67-alt1
- 0.67

* Fri Jul 22 2005 Victor Forsyuk <force@altlinux.ru> 0.66-alt2
- Added dktrace.h.

* Wed Jul 13 2005 Victor Forsyuk <force@altlinux.ru> 0.66-alt1
- 0.66

* Wed Jun 15 2005 Victor Forsyuk <force@altlinux.ru> 0.65a-alt1
- 0.65a

* Wed May 18 2005 Victor Forsyuk <force@altlinux.ru> 0.64-alt1
- Initial build.
