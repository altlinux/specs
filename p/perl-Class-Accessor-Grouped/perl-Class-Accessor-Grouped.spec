%define dist Class-Accessor-Grouped
Name: perl-Class-Accessor-Grouped
Version: 0.10003
Release: alt1

Summary: Lets you build groups of accessors
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Class-Accessor-Grouped/
Source: http://www.cpan.org/authors/id/F/FR/FREW/Class-Accessor-Grouped-0.10003.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 27 2010 (-bi)
BuildRequires: perl-Class-Inspector perl-Class-XSAccessor perl-MRO-Compat perl-Module-Install perl-Sub-Name perl-Test-Exception

%description
This class lets you build groups of accessors that will call
different getters and setters.

%prep
%setup -q -n %dist-%version
# hack to avoid dependency on pod2text, see Makefile.PL
rm -f MANIFEST.SKIP

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10003-alt1
- automated CPAN update

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 0.10002-alt1
- 0.09003 -> 0.10002

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1
- automated CPAN update

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.09002-alt1
- 0.09002 version

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08001-alt2
- fix directory ownership violation

* Sat May 24 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08001-alt1
- 0.08001 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
