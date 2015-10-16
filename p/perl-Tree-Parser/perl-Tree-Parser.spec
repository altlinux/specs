%define module_version 0.15
%define module_name Tree-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Array/Iterator.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Tree/Simple.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.15
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/ST/STEVAN/%{module_name}-%{module_version}.tar.gz
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
* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- to Sisyphus as dep for Devel-PerlySense

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- initial import by package builder

