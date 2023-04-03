%define _unpackaged_files_terminate_build 1
%define module_name Validation-Class
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Forward.pm) perl(Class/Method/Modifiers.pm) perl(Clone.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Hash/Flatten.pm) perl(Hash/Merge.pm) perl(List/MoreUtils.pm) perl(Module/Find.pm) perl(Module/Runtime.pm) perl(Perl/Critic.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 7.900059
Release: alt1
Summary: Centralized Data Validation Framework
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/Validation-Class/

Source0: http://www.cpan.org/authors/id/C/CK/CKRAS/%{module_name}-%{version}.tar.gz
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
%doc README.mkdn README Changes
%perl_vendor_privlib/V*

%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 7.900059-alt1
- automated CPAN update

* Thu Jun 23 2022 Igor Vlasenko <viy@altlinux.org> 7.900058-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 7.900057-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 7.900056-alt1
- automated CPAN update

* Fri Feb 28 2014 Igor Vlasenko <viy@altlinux.ru> 7.900055-alt1
- automated CPAN update

* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 7.900054-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 7.900054-alt1
- regenerated from template by package builder

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 7.900052-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 4.01003514-alt1
- initial import by package builder

