# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Accessor/Fast.pm) perl(Data/Page.pm) perl(Module/Build.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 1.02
%define module_name Data-Page-Pageset
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt2
Summary: change long page list to be shorter and well navigate
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/C/CH/CHUNZI/%module_name-%module_version.tar.gz
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
%doc Changes
%perl_vendor_privlib/D*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2
- to Sisyphus

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- initial import by package builder

