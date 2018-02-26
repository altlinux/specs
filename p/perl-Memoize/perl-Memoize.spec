%define dist Memoize
Name: perl-%dist
Version: 1.02
Release: alt1

Summary: Perl functions speedup by caching return values
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FL/FLORA/Memoize-1.02.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 26 2010
BuildRequires: perl-DBM perl-Storable perl-devel

%description
`Memoizing' a function makes it faster by trading space for time.
It does this by caching the return values of the function in a table.
If you call the function again with the same arguments, memoize
jumps in and gives you the value out of the table, instead of letting
the function compute the value all over again.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Memoize*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Mon Apr 26 2010 Alexey Tourbin <at@altlinux.ru> 1.01-alt3
- decoupled perl-Memoize-ExpireLRU

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.01-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon May 17 2004 Alexey Tourbin <at@altlinux.ru> 1.01-alt2
- BuildArch: noarch
- fixed typos (RLU -> LRU)

* Mon Apr 19 2004 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision, an offspring of perl-DBM
- packaged %dist-ExpireLRU-0.55 (laziness is virtue)
