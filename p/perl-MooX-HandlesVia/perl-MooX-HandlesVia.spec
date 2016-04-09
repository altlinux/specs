%define module_version 0.001008
%define module_name MooX-HandlesVia
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Method/Modifiers.pm) perl(Data/Dumper.pm) perl(Data/Perl.pm) perl(Data/Perl/Role/Bool.pm) perl(Data/Perl/Role/Collection/Array.pm) perl(Data/Perl/Role/Collection/Hash.pm) perl(Data/Perl/Role/Number.pm) perl(Data/Perl/Role/String.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/Types/MooseLike/Base.pm) perl(Pod/Coverage/TrustPod.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Test/Exception.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(namespace/autoclean.pm) perl(namespace/clean.pm) perl(overload.pm) perl(strictures.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001008
Release: alt1.1
Summary: NativeTrait-like behavior for Moo.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MATTP/%{module_name}-%{module_version}.tar.gz
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
%doc LICENSE README.mkdn Changes TODO
%perl_vendor_privlib/M*
%perl_vendor_privlib/D*

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.001008-alt1.1
- rebuild to restore role requires

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.001008-alt1
- regenerated from template by package builder

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.001006-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.001005-alt2
- moved to Sisyphus for perl update

* Mon Dec 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.001005-alt1
- regenerated from template by package builder

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.001004-alt1
- initial import by package builder

