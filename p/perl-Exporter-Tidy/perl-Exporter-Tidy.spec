# Spec file for Perl module Exporter::Tidy

Name: perl-Exporter-Tidy
Version: 0.07
Release: alt1

Summary: Perl module Exporter::Tidy
Summary(ru_RU.UTF-8): модуль Perl Exporter::Tidy

%define real_name Exporter-Tidy

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Exporter-Tidy/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2011
BuildRequires: perl-devel perl-threads

%description
Perl module Exporter::Tidy provides an another way of exporting
symbols and serves as an easy, clean alternative to Exporter.

%description -l ru_RU.UTF-8
Модуль Perl Exporter::Tidy представляет альтернативный способ
экспортирования символов и является простой и понятной 
альтернативой модуля Exporter.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Exporter/*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- Initial build for ALT Linux Sisyphus

* Sun May 07 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt0
- First build

