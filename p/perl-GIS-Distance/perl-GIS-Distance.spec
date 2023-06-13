%define _unpackaged_files_terminate_build 1
%define module_name GIS-Distance
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Measure/Length.pm) perl(Const/Fast.pm) perl(Math/Trig.pm) perl(Module/Build/Tiny.pm) perl(Module/Find.pm) perl(Test2/V0.pm) perl(namespace/clean.pm) perl(strictures.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.20
Release: alt1
Summary: Calculate geographic distances.
Group: Development/Perl
License: perl
URL: https://github.com/bluefeet/GIS-Distance

Source0: http://www.cpan.org/authors/id/B/BL/BLUEFEET/%{module_name}-%{version}.tar.gz
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
%doc Changes README.md
%perl_vendor_privlib/G*

%changelog
* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 0.20-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sun Mar 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- to Sisyphus as GEO-Distance dep

* Sun Mar 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated by package builder

* Sat Mar 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- updated by package builder

* Fri Mar 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

