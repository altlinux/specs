%define _unpackaged_files_terminate_build 1
%define dist IO-Socket-Socks

Name: perl-%dist
Version: 0.73
Release: alt1

Summary: This module seeks to provide a full implementation of the SOCKS protocol
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/O/OL/OLEG/IO-Socket-Socks-%{version}.tar.gz

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
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.67-alt1
- initial build
