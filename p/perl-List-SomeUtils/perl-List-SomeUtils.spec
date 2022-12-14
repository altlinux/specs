%define _unpackaged_files_terminate_build 1
%define module_name List-SomeUtils
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(Exporter/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Module/Implementation.pm) perl(Scalar/Util.pm) perl(Test/Builder/Module.pm) perl(Test/LeakTrace.pm) perl(Test/More.pm) perl(Text/ParseWords.pm) perl(Tie/Array.pm) perl(base.pm) perl(lib.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(vars.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.59
Release: alt1
Summary: Provide the stuff missing in List::Util
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/List-SomeUtils

Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module_name}-%{version}.tar.gz
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
%doc README.md Changes CONTRIBUTING.md
%perl_vendor_privlib/L*

%changelog
* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.59-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- regenerated from template by package builder

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- initial import by package builder

