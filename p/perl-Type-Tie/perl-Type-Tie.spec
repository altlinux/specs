%define _without_test 1
%define module_version 0.006
%define module_name Type-Tie
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(Exporter/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(Hash/FieldHash.pm) perl(Hash/Util/FieldHash.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types/Moose.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.006
Release: alt2
Summary: tie a variable to a type constraint
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Type-Tie

Source0: http://cpan.org.ua/authors/id/T/TO/TOBYINK/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc COPYRIGHT LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
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

