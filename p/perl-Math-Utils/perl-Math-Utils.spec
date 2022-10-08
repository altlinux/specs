%define module_name Math-Utils
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Math/BigRat.pm) perl(Math/Complex.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.14
Release: alt2
Summary: Useful mathematical functions not in Perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/J/JG/JGAMBLE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTING.md LICENSE Changes README.md
%perl_vendor_privlib/M*

%changelog
* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 1.14-alt2
- to Sisyphus as perl-Geo-Gpx dep

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- updated by package builder

* Sun Nov 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- regenerated from template by package builder

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- regenerated from template by package builder

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- regenerated from template by package builder

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- regenerated from template by package builder

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- regenerated from template by package builder

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- regenerated from template by package builder

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- initial import by package builder

