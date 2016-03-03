%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/TAP/DOM.pm
%define upstream_name    TAP-DOM
%define upstream_version 0.13

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.13
Release:    alt1

Summary:    Accessors for TAP::DOM summary part
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/S/SC/SCHWIGON/TAP-DOM-%{version}.tar.gz

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(TAP/Parser/Aggregator.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
The purpose of this module is A) to define a *reliable* data structure and
B) to help create this structure from TAP.

That is useful when you want to analyze the TAP in detail with "data
exploration tools", like Data::DPath.

``Reliable'' means that this structure is kind of an API that will not
change, so your data tools can, well, rely on it.

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
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1
- update by mgaimport

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update by mgaimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- mageia import by cas@ requiest

