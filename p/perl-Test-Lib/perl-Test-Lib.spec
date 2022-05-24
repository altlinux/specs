%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Test-Lib
%define upstream_version 0.002

Name:       perl-%{upstream_name}
Version:    0.003
Release:    alt1

Summary:    Use libraries from a t/lib directory
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/H/HA/HAARG/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
Searches upward from the calling module for a directory _t_ with a _lib_
directory inside it, and adds it to the module search path. Looks upward up
to 5 directories. This is intended to be used in test modules either
directly in _t_ or in a subdirectory to find their included testing
libraries located in _t/lib_.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%perl_vendor_privlib/*

%changelog
* Tue May 24 2022 Igor Vlasenko <viy@altlinux.org> 0.003-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 0.002-alt3_7
- to Sisyphus as Dancer2 dep

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_7
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_6
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_5
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.002-alt2_1
- rebuild to get rid of unmets

* Sat Aug 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_1
- update by mgaimport

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1_1
- converted for ALT Linux by srpmconvert tools

