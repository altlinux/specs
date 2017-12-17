%define _unpackaged_files_terminate_build 1
%define dist Cache-FastMmap
Name: perl-%dist
Version: 1.46
Release: alt1.1

Summary: Uses an mmap'ed file to act as a shared memory interprocess cache
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RO/ROBM/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-IO-Compress perl-devel

%description
In multi-process environments (eg mod_perl, forking daemons,
etc), it's common to want to cache information, but have that
cache shared between processes.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Cache
%perl_vendor_autolib/Cache

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1.1
- rebuild with new perl 5.24.1

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1.1
- rebuild with new perl 5.22.0

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.40-alt2.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.40-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.40-alt1
- 1.39 -> 1.40
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.35 -> 1.39
- built for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.35-alt1.1
- rebuilt with perl 5.12

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.28 -> 1.35

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.28-alt1
- 1.28 version
- fix directory ownership violation

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 1.26-alt1
- 1.26 version

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 1.14-alt1
- first build for ALT Linux Sisyphus

