%define _unpackaged_files_terminate_build 1
Name: perl-Sub-Exporter-Progressive
Version: 0.001013
Release: alt1

Summary: Sub::Exporter::Progressive - Only use Sub::Exporter if you need it
Group: Development/Perl
License: Perl

Url: %CPAN Sub-Exporter-Progressive
Source: http://www.cpan.org/authors/id/F/FR/FREW/Sub-Exporter-Progressive-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n Sub-Exporter-Progressive-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Sub/Exporter/Progressive*
%doc Changes README 

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.001013-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.001012-alt1
- automated CPAN update

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.001011-alt1
- automated CPAN update

* Tue Oct 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.001010-alt1
- 0.001006 -> 0.001010

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.001006-alt1
- initial build
