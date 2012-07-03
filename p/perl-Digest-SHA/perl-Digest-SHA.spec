%define module Digest-SHA

Name: perl-%module
Version: 5.71
Release: alt1

Summary: Perl extension for SHA-1/224/256/384/512
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/%module-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description

Digest::SHA is a complete implementation of the NIST Secure Hash
Standard. It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests. The
module can handle all types of input, including partial-byte data.

%prep
%setup -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc examples/dups
%_bindir/*
%perl_vendor_archlib/Digest/
%perl_vendor_autolib/Digest/
%_man1dir/*

%changelog
* Fri Mar 23 2012 Victor Forsiuk <force@altlinux.org> 5.71-alt1
- 5.71

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 5.62-alt2
- rebuilt for perl-5.14

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 5.62-alt1
- 5.62

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 5.61-alt1
- 5.61

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 5.50-alt1
- 5.50

* Mon Dec 13 2010 Victor Forsiuk <force@altlinux.org> 5.49-alt1
- 5.49

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 5.48-alt1.1
- rebuilt with perl 5.12

* Mon Jan 25 2010 Victor Forsyuk <force@altlinux.org> 5.48-alt1
- 5.48

* Thu May 29 2008 Victor Forsyuk <force@altlinux.org> 5.47-alt1
- 5.47

* Tue Jun 26 2007 Victor Forsyuk <force@altlinux.org> 5.45-alt1
- 5.45

* Thu Dec 14 2006 Victor Forsyuk <force@altlinux.org> 5.44-alt1
- 5.44

* Thu Aug 31 2006 Victor Forsyuk <force@altlinux.ru> 5.43-alt1
- Initial build.
