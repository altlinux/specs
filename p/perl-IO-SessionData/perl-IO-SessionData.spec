# BEGIN SourceDeps(oneline):
BuildRequires: perl(IO/Handle.pm) perl(IO/Select.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.03
%define module_name IO-SessionData
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel

Name: perl-%module_name
Version: 1.03
Release: alt1
Summary: supporting module for SOAP::Lite
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PH/PHRED/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/I*

%changelog
* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- initial import by package builder

