%define _unpackaged_files_terminate_build 1
%define module_name Params-ValidationCompiler
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Const/Fast.pm) perl(DateTime.pm) perl(Eval/Closure.pm) perl(Exception/Class.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Hash/Util.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Params/Validate.pm) perl(Scalar/Util.pm) perl(Specio.pm) perl(Test/More.pm) perl(Test/Without/Module.pm) perl(Test2/Bundle/Extended.pm) perl(Test2/Plugin/NoWarnings.pm) perl(Test2/Require/Module.pm) perl(Type/Params.pm) perl(Types/Standard.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.26
Release: alt1
Summary: Build an optimized subroutine parameter validator once, use it forever
Group: Development/Perl
License: artistic_2
URL: http://metacpan.org/release/Params-ValidationCompiler

Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This is very alpha. The module name could change. Everything could
change. You have been warned.

Create a customized, optimized, non-lobotomized, uncompromised, and thoroughly
specialized parameter checking subroutine.

=for Pod::Coverage compile
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes CONTRIBUTING.md
%perl_vendor_privlib/P*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- to Sisyphus

* Sun Sep 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Mon Sep 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

