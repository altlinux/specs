%define _unpackaged_files_terminate_build 1
%define _without_test 1
%define module_name Type-Tie
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(Exporter/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(Hash/FieldHash.pm) perl(Hash/Util/FieldHash.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types/Moose.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.013
Release: alt1
Summary: tie a variable to a type constraint
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Type-Tie

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
%doc COPYRIGHT LICENSE README Changes CREDITS
%perl_vendor_privlib/T*

%changelog
* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Thu Jun 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency
- bootstrap (w/o tests) circ.dep. on Type-Tiny

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt0.1
- initial import by package builder
- bootstrap (w/o tests) circ.dep. on Type-Tiny

