%define module IO-Multiplex

Name: perl-%module
Version: 1.13
Release: alt1

Summary: IO::Multiplex - Manage IO on many file handles
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/IO-Multiplex-1.13.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-devel

%description
IO::Multiplex is designed to take the effort out of managing multiple file
handles. It is essentially a really fancy front-end to the C<select> system
call. In addition to maintaining the C<select> loop, it buffers all input and
output to/from the file handles. It can also accept incoming connections on one
or more listen sockets.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
install -pDm755 contrib/portfw %buildroot%_bindir/portfw

%files
%_bindir/*
%perl_vendor_privlib/IO

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.12-alt1
- 1.12

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Oct 09 2009 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10
- Install portfw.

* Wed Feb 16 2005 LAKostis <lakostis at altlinux.ru> 1.08-alt1
- first build for Sisyphus.
