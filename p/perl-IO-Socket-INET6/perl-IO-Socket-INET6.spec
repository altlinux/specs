%define module IO-Socket-INET6

# Tests not guaranteed to succeed!
%def_without test

Name: perl-%module
Version: 2.69
Release: alt1

Summary: Object interface for AF_INET/AF_INET6 domain sockets
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Module-Build perl-Socket6

%description
IO::Socket::INET6 provides an object interface to creating and using sockets
in either AF_INET or AF_INET6 domains. It is built upon the IO::Socket
interface and inherits all the methods defined by IO::Socket.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IO

%changelog
* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 2.69-alt1
- 2.69

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 2.67-alt1
- 2.67

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.65-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 2.65-alt1
- 2.65

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 2.61-alt1
- 2.61

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 2.57-alt1
- 2.57

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 2.56-alt1
- 2.56

* Wed Sep 10 2008 Victor Forsyuk <force@altlinux.org> 2.54-alt2
- Fix directory ownership violation.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 2.54-alt1
- 2.54

* Tue Aug 14 2007 Victor Forsyuk <force@altlinux.org> 2.51-alt1
- Initial build.
