%define _unpackaged_files_terminate_build 1
%define dist SQL-Abstract
Name: perl-%dist
Version: 1.85
Release: alt1

Summary: Generate SQL from Perl data structures
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/SQL-Abstract/
Source0: http://www.cpan.org/authors/id/I/IL/ILMARI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 13 2011 (-bi)
BuildRequires: perl-DBIx-Class perl-Module-Install perl-Term-ANSIColor perl-Test-Deep perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Warn

%description
This module was inspired by the excellent DBIx::Abstract.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes examples README
%perl_vendor_privlib/DBIx*
%perl_vendor_privlib/SQL*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.85-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.84-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.81-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.77-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.75-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.73-alt1
- 1.72 -> 1.73

* Thu Jan 13 2011 Alexey Tourbin <at@altlinux.ru> 1.72-alt1
- 1.67 -> 1.72

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.65 -> 1.66

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 1.65-alt1
- 1.63 -> 1.65

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 1.63-alt1
- 1.60 -> 1.63

* Mon Oct 26 2009 Michael Bochkaryov <misha@altlinux.ru> 1.60-alt1
- 1.60 version

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.24-alt1
- fix directory ownership violation

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 1.22-alt1
- first build for ALT Linux Sisyphus

