Name: perl-Sub-Exporter-Progressive
Version: 0.001006
Release: alt1

Summary: Sub::Exporter::Progressive - Only use Sub::Exporter if you need it
Group: Development/Perl
License: Perl

Url: %CPAN Sub-Exporter-Progressive
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Sub/Exporter/Progressive*
%doc Changes README 

%changelog
* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.001006-alt1
- initial build
