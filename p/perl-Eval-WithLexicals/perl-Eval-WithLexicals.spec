# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(B.pm) perl(Term/ReadLine.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Eval-WithLexicals
%define upstream_version 1.003005

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_3

Summary:    Persist compile hints between evals
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Eval/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Moo.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(strictures.pm)
BuildArch:  noarch
Source44: import.info

%description
Persist pragams and other compile hints between evals (for example the the
strict manpage and the warnings manpage flags in effect).

Saves and restores the '$^H' and '%^H' variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README
%{_mandir}/man*/*
%{perl_vendor_privlib}/*
/usr/bin/tinyrepl

%changelog
* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.003005-alt2_3
- to Sisyphus

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.003005-alt1_3
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.003005-alt1_2
- update by mgaimport

* Tue Oct 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.003005-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.003000-alt2_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.003000-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.003000-alt2_1
- rebuild to get rid of unmets

* Sat Aug 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.003000-alt1_1
- update by mgaimport

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.002000-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1.002000-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.002000-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.002000-alt1_1
- converted for ALT Linux by srpmconvert tools

