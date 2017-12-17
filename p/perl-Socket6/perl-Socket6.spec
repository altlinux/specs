%define _unpackaged_files_terminate_build 1
%define module Socket6

Name: perl-%module
Version: 0.28
Release: alt1.1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Socket6 Perl module
License: BSD-like
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/U/UM/UMEMOTO/Socket6-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
Socket6 is a module that implements a IPv6 API for Perl programs.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Socket6.pm
%perl_vendor_autolib/Socket6

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1.1
- rebuild with new perl 5.24.1

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1.1
- rebuild with new perl 5.20.1

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt3
- built for perl 5.18

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt2
- rebuild for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt1.2
- rebuilt for perl-5.14

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.23-alt1.1
- rebuilt for perl-5.12

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.23-alt1
- 0.23

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 0.22-alt1
- 0.22

* Thu Mar 06 2008 Victor Forsyuk <force@altlinux.org> 0.20-alt1
- 0.20

* Mon Aug 13 2007 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- Initial build.
