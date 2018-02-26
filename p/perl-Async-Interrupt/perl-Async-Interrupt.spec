%define module Async-Interrupt

Name: perl-%module
Version: 1.05
Release: alt1.2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Allow C/XS libraries to interrupt perl asynchronously  
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%module-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-common-sense perl-devel

%description
This module implements asynchronous notifications that enable you to signal
running perl code from another thread, asynchronously, and sometimes even
without using a single syscall.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Async
%perl_vendor_autolib/Async

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Fri Jun 25 2010 Victor Forsiuk <force@altlinux.org> 1.05-alt1
- 1.05

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
