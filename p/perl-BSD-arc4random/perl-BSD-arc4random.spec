%define module_version 1.50
%define module_name BSD-arc4random

%define _unpackaged_files_terminate_build 1

# BEGIN SourceDeps(oneline):
BuildRequires: perl(DynaLoader.pm) perl(Exporter.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

BuildRequires: rpm-build-licenses

Name: perl-%module_name
Version: %module_version
Release: alt3.1.1
Summary: This module provides a Perl API for the BSDs' arc4random(3) suite of functions
Group: Development/Perl
License: %perl_license
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SJ/SJSZ/%module_name-%module_version.tar.gz

%description
This module provides a Perl API for the BSDs' arc4random(3) suite
of functions and adds a few high-level functions, such as the new
arc4random_uniform(3). The Perl functions are ithreads-safe (only
if threads::shared is required). Scalars can be tied to this pak-
kage, yielding uniformly distributed random numbers with an arbi-
trary upper bound on read access, contributing to the RC4 entropy
pool on write access. An exported global $RANDOM variable returns
15-bit unsigned random numbers, from [0; 32767], similar to mksh.
Furthermore, Perl's internal PRNG is seeded with entropy obtained
from the arc4random generator once on module load time.

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README TODO
%perl_vendor_archlib/B*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.50-alt3.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.50-alt3.1
- rebuild with new perl 5.24.1

* Thu Apr 07 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.50-alt3
- imported from autoimports
- spec's cleanups

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.50-alt2.1
- rebuilt with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 1.50-alt2
- rebuilt to get rid of unmets

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.50-alt1.1
- rebuilt with new perl

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- initial import by package builder

