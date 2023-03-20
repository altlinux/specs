%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/TAP/DOM.pm
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    TAP-DOM
%define upstream_version 0.97

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.98
Release:    alt1

Summary:    Accessors for TAP::DOM summary part
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/S/SC/SCHWIGON/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/String.pm)
BuildRequires: perl(IO/Zlib.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(TAP/Parser/Aggregator.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(YAML/Tiny.pm)
BuildRequires: perl(blib.pm)
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
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0.98-alt1
- automated CPAN update

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.97-alt1_1
- update by mgaimport

* Thu Jun 16 2022 Igor Vlasenko <viy@altlinux.org> 0.97-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 0.95-alt1
- automated CPAN update

* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0.93-alt1_1
- update by mgaimport

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.93-alt1
- automated CPAN update

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_1
- update by mgaimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- update by mgaimport

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update by mgaimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update by mgaimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update by mgaimport

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

