%define _unpackaged_files_terminate_build 1
%define module_name Exporter-Tiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.006002
Release: alt1
Summary: an exporter with the features of Sub::Exporter but only core dependencies
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Exporter-Tiny

Source0: http://www.cpan.org/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYRIGHT examples CREDITS
%perl_vendor_privlib/E*

%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 1.006002-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 1.006000-alt1
- automated CPAN update

* Sun Oct 16 2022 Igor Vlasenko <viy@altlinux.org> 1.004004-alt1
- automated CPAN update

* Fri Sep 30 2022 Igor Vlasenko <viy@altlinux.org> 1.004003-alt1
- automated CPAN update

* Mon Sep 19 2022 Igor Vlasenko <viy@altlinux.org> 1.004002-alt1
- automated CPAN update

* Sun Sep 11 2022 Igor Vlasenko <viy@altlinux.org> 1.004001-alt1
- automated CPAN update

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 1.004000-alt1
- automated CPAN update

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 1.002002-alt1
- automated CPAN update

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- automated CPAN update

* Wed Mar 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.030-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- initial import by package builder

