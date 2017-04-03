%define _unpackaged_files_terminate_build 1
%define dist SMS-Send-DeviceGsm

Name: perl-%dist
Version: 1.08
Release: alt1

Summary: An SMS::Send driver for Device::Gsm
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-licenses

BuildRequires: perl-devel perl-SMS-Send perl-Device-Gsm
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
SMS::Send::DeviceGsm is an SMS::Send driver that uses Device::Gsm
to deliver messages via attached hardware.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes Changes.old examples
%perl_vendor_privlib/*

%changelog
* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Sat Apr 02 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.06-alt1
- initial build
