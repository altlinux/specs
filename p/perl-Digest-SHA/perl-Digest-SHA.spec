%define _unpackaged_files_terminate_build 1
%define module Digest-SHA

Name: perl-%module
Version: 5.98
Release: alt1.1

Summary: Perl extension for SHA-1/224/256/384/512
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/M/MS/MSHELOR/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description

Digest::SHA is a complete implementation of the NIST Secure Hash
Standard. It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests. The
module can handle all types of input, including partial-byte data.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc examples/dups Changes README examples
%_bindir/*
%perl_vendor_archlib/Digest/
%perl_vendor_autolib/Digest/
%_man1dir/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.98-alt1.1
- rebuild with new perl 5.26.1

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 5.98-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 5.97-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.96-alt1.1
- rebuild with new perl 5.24.1

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 5.96-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 5.95-alt1.1
- rebuild with new perl 5.22.0

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 5.95-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 5.93-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 5.93-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 5.92-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 5.91-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 5.90-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.89-alt1
- automated CPAN update

* Tue Mar 18 2014 Igor Vlasenko <viy@altlinux.ru> 5.88-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 5.87-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 5.86-alt1
- automated CPAN update

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 5.85-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 5.85-alt1
- automated CPAN update

* Tue Jan 15 2013 Vladimir Lettiev <crux@altlinux.ru> 5.81-alt1
- Security fixes: RT#82655
- 5.72 -> 5.81

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 5.72-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 5.71-alt2
- rebuilt for perl-5.16

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
