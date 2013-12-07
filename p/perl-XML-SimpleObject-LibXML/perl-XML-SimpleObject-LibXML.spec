# BEGIN SourceDeps(oneline):
BuildRequires: perl(XML/LibXML.pm) perl(XML/LibXML/Common.pm)
# END SourceDeps(oneline)
%define module_version 0.60
%define module_name XML-SimpleObject-LibXML
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.60
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DB/DBRIAN/%module_name-%module_version.tar.gz
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
%doc README Changes
%perl_vendor_privlib/X*

%changelog
* Sat Dec 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.60-alt2
- Rebuild for sisyphus

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- initial import by package builder

