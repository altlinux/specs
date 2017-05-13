%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/DNS.pm) perl(AnyEvent/HTTP.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name AnyEvent-CacheDNS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Simple DNS resolver with caching
Group: Development/Perl
License: perl
URL: http://github.com/potyl/perl-AnyEvent-CacheDNS

Source0: http://cpan.org.ua/authors/id/P/PO/POTYL/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/A*

%changelog
* Sat May 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

