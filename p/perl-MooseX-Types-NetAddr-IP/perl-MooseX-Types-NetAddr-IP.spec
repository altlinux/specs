%define module_version 0.07
%define module_name MooseX-Types-NetAddr-IP
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Module/Runtime.pm) perl(Moose.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types.pm) perl(MooseX/Types/Moose.pm) perl(NetAddr/IP.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(namespace/clean.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: NetAddr::IP related types and coercions for Moose
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TC/TCAINE/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
This package provides internet address types for Moose..

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/M*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.07-alt2
- import for Sisyphus

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- rebuild to restore role requires

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

