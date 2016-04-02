%define dist SMS-Send

Name: perl-%dist
Version: 1.06
Release: alt1

Summary: Driver-based API for sending SMS messages
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-licenses

BuildRequires: perl-devel perl-Module-Pluggable perl-Params-Util perl-Class-Adapter

%description
"SMS::Send" is intended to provide a driver-based single API for
sending SMS and MMS messages. The intent is to provide a single
API against which to write the code to send an SMS message.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/*

%changelog
* Sat Apr 02 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.06-alt1
- initial build
