%define _unpackaged_files_terminate_build 1
%define module_name Data-Dmp
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Deparse.pm) perl(Data/Dump.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Regexp/Stringify.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.242
Release: alt1
Summary: Dump Perl data structures
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Data-Dmp

Source0: http://www.cpan.org/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz
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
%doc Changes README
%perl_vendor_privlib/D*

%changelog
* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 0.242-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 0.241-alt1
- automated CPAN update

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.240-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- to Sisyphus

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- regenerated from template by package builder

* Fri Jan 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- regenerated from template by package builder

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- regenerated from template by package builder

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

