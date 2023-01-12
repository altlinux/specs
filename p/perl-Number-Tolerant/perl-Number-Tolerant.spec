%define _unpackaged_files_terminate_build 1
%define module_name Number-Tolerant
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Math/BigFloat.pm) perl(Math/BigRat.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Sub/Exporter/Util.pm) perl(Test/Builder.pm) perl(Test/More.pm) perl(Test/Tester.pm) perl(base.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.710
Release: alt1
Summary: tolerance ranges for inexact numbers
Group: Development/Perl
License: perl
URL: https://github.com/rjbs/Number-Tolerant

Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{module_name}-%{version}.tar.gz
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
%doc README Changes
%perl_vendor_privlib/T*
%perl_vendor_privlib/N*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.710-alt1
- automated CPAN update

* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 1.709-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.708-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.707-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.706-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.705-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.704-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.703-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.702-alt2
- build for Sisyphus (required for perl update)

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.702-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.701-alt1
- initial import by package builder

