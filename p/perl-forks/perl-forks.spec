%define dist forks
Name: perl-%dist
Version: 0.36
Release: alt1.1.1.1.1

Summary: Drop-in replacement for Perl threads using fork()
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RY/RYBSKEJ/forks-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Acme-Damn perl-Attribute-Handlers perl-Devel-Symdump perl-List-MoreUtils perl-Sys-SigAction perl-devel perl-threads

%description
The forks.pm module is a drop-in replacement for threads.pm.  It has the
same syntax as the threads.pm module (it even takes over its namespace).

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/forks*
%perl_vendor_autolib/forks
%perl_vendor_archlib/threads

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1
- rebuild with new perl 5.20.1

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.34-alt2
- rebuilt for perl-5.14

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- initial build for ALT Linux Sisyphus
