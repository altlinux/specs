# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Test/Deep.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Hash-Slice
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_12

Summary:    Make a hash from a deep slice of another hash
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp/Clan.pm)
BuildRequires: perl(Clone.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(inc/Module/Install.pm)
BuildRequires: perl(Storable.pm)
BuildRequires: perl(Test/Most.pm)
BuildArch: noarch
Source44: import.info

%description
Hash::Slice lets you easily make a deep slice of a hash, specifically a
hash containing one or more nested hashes. Instead of just taking a slice
of the first level of a hash in an all-or-nothing manner, you can use slice
to take a slice of the first level, then take a particular slice of the
second level, and so on.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%perl_vendor_privlib/*




%changelog
* Tue Oct 31 2023 Igor Vlasenko <viy@altlinux.org> 0.03-alt2_12
- moved to Sisyphus as perl-App-Asciio dep

* Sun Apr 10 2022 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt1_12
- update by mgaimport

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_11
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_10
- update by mgaimport

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_9
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_8
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt3_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- converted for ALT Linux by srpmconvert tools

