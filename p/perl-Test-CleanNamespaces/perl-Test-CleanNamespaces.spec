%define _unpackaged_files_terminate_build 1
%define module_version 0.19
%define module_name Test-CleanNamespaces
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/MOP/Class.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Find/Rule.pm) perl(File/Find/Rule/Perl.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Moose.pm) perl(Moose/Exporter.pm) perl(Moose/Role.pm) perl(MooseX/Role/Parameterized.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(Package/Stash.pm) perl(Role/Tiny.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Sub/Identify.pm) perl(Test/Builder.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Test/Tester.pm) perl(Test/Warnings.pm) perl(constant.pm) perl(if.pm) perl(lib.pm) perl(metaclass.pm) perl(namespace/clean.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm) perl(Module/Metadata.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.19
Release: alt1
Summary: Check for uncleaned imports
Group: Development/Perl
License: perl
URL: https://github.com/karenetheridge/Test-CleanNamespaces

Source: http://www.cpan.org/authors/id/E/ET/ETHER/Test-CleanNamespaces-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- moved to Sysiphus as dependency

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

