# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Devel/Declare.pm) perl(Devel/Declare/Context/Simple.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Module/Runtime.pm) perl(Moose.pm) perl(Moose/Meta/Class.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Method/Signatures.pm) perl(MooseX/Method/Signatures/Meta/Method.pm) perl(MooseX/Method/Signatures/Types.pm) perl(MooseX/Role/Parameterized.pm) perl(MooseX/Types/Moose.pm) perl(MooseX/Types/Structured.pm) perl(Parse/Method/Signatures.pm) perl(Parse/Method/Signatures/Param/Placeholder.pm) perl(Sub/Exporter.pm) perl(Sub/Install.pm) perl(Test/Moose.pm) perl(Test/More.pm) perl(aliased.pm) perl(constant.pm) perl(if.pm) perl(lib.pm) perl(namespace/autoclean.pm) perl(namespace/clean.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
BuildRequires: perl-devel
# END SourceDeps(oneline)
%define module_version 0.43
%define module_name MooseX-Declare
%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Module/Build.pm)
%define dist MooseX-Declare
Name: perl-%dist
Version: 0.43
Release: alt2.1

Summary: Declarative syntax for Moose
License: perl
Group: Development/Perl

URL: https://github.com/moose/MooseX-Declare
Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/ET/ETHER/%{module_name}-%{module_version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Method-Signatures perl-MooseX-Role-Parameterized perl-Test-Exception perl-Test-NoWarnings perl(Test/Fatal.pm) perl(Test/CheckDeps.pm)
Provides: perl(MooseX/Declare/Context/WithOptions.pm) = 0.390

%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5.  When used, it sets up the "class" and "role" keywords.

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/MooseX

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2.1
- rebuild to restore role requires

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2
- fixed provides

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
