# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    String-Koremutake
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt4_9

Summary:	Convert to/from Koremutake Memorable Random Strings
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{upstream_name}-%{upstream_version}.tar.bz2


BuildRequires:	perl(Test/Exception.pm)
BuildRequires:  perl(Error.pm)
BuildArch:	noarch
Source44: import.info


%description
The String::Koremutake module converts to and from Koremutake Memorable Random
Strings.

The term "Memorable Random String" was thought up by Sean B. Palmer as a name
for those strings like dopynl, glargen, glonknic, spoopwiddle, and kebble etc.
that don't have any conventional sense, but can be used as random identifiers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendor_privlib}/String/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.30-alt4_9
- to Sisyphus as perl-Devel-Trepan dep

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_9
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_8
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.30-alt3_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.30-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_1
- converted for ALT Linux by srpmconvert tools

