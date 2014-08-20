# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Module/Install.pm) perl(Module/Install/Base.pm) perl(Test/Base.pm) perl(Test/More.pm) perl(Test/Pod.pm)
# END SourceDeps(oneline)
%define module_version 0.86
%define module_name Module-Install-TestBase
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.86
Release: alt1
Summary: Module Install Support for Test::Base
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/module-install-testbase-pm

Source0: http://cpan.org.ua/authors/id/I/IN/INGY/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/M*

%changelog
* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- initial import by package builder

