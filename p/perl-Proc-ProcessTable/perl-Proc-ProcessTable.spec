%define _unpackaged_files_terminate_build 1
%define dist Proc-ProcessTable
Name: perl-%dist
Version: 0.55
Release: alt1

Summary: Perl extension to access the unix process table
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JW/JWB/%{dist}-%{version}.tar.gz

# mount /proc in hasher
BuildRequires: /proc

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Perl interface to the unix process table.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README README.aix README.bsdi README.cygwin README.darwin README.dec_osf README.freebsd-kvm README.freebsd-procfs README.hpux README.linux README.netbsd README.openbsd README.solaris README.sunos README.unixware
%perl_vendor_archlib/Proc
%perl_vendor_autolib/Proc

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Fri Dec 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.48-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt1.1
- rebuilt with perl 5.12

* Wed Apr 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- first build for ALT Linux Sisyphus
