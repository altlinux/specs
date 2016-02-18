%define dist IO-Socket-Socks

Name: perl-%dist
Version: 0.67
Release: alt1

Summary: This module seeks to provide a full implementation of the SOCKS protocol
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
BuildRequires: perl-Encode perl-IO-Socket-IP perl-devel

%description
This module seeks to provide a full implementation of the SOCKS protocol
while behaving like a regular socket as much as possible.

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
* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.67-alt1
- initial build
