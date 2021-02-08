%define module_version 1.7
%define module_name LWP-Protocol-socks
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IO/Socket/SSL.pm) perl(IO/Socket/Socks.pm) perl(LWP.pm) perl(LWP/Protocol.pm) perl(LWP/Protocol/http.pm) perl(LWP/Protocol/https.pm) perl(Net/HTTP.pm) perl(Net/HTTPS.pm) perl(Test/More.pm) perl(URI/Escape.pm) perl(URI/http.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.7
Release: alt2
Summary: adds support for the socks protocol and proxy facility
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SC/SCR/%{module_name}-%{module_version}.tar.gz
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
%perl_vendor_privlib/L*
%perl_vendor_privlib/U*

%changelog
* Tue Feb 09 2021 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2
- to Sisyphus as shutter dep

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- initial import by package builder

