%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    WebService-MusicBrainz
%define upstream_version 1.0.3

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    1.0.4
Release:    alt1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/B/BF/BFAIST/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Mojolicious.pm)
BuildArch:  noarch
Source44: import.info

%description
This module will act as a factory using static methods to return specific
web service objects;

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%check
# (tv) those tests needs networking and thus fails with iurt-0.7:
exit 0
make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README.md
%perl_vendor_privlib/*

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1
- automated CPAN update

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- update by mgaimport

* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1
- automated CPAN update

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3
- update by mgaimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_8
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_2
- build for Sisyphus

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_1
- build for Sisyphus

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1_1
- converted for ALT Linux by srpmconvert tools

