## SPEC file for Perl module Authen::Radius

%define real_name Authen-Radius
%define dist_name RadiusPerl

Name: perl-Authen-Radius
Version: 0.20
Release: alt1

Summary: provide simple Radius client facilities

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/~manowar/RadiusPerl/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

Provides: perl-%dist_name

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses

BuildRequires: perl-Data-HexDump

%description
Perl module Authen::Raduis allows you to communicate with a Radius
server from Perl.  You can  just authenticate  usernames/passwords
via Radius, or comletely imitate AAA requests and process server 
response.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%exclude /.perl.req
%perl_vendor_privlib/Authen/Radius*


%changelog
* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version 0.20

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.17-alt1
- New version 0.17

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt1
- New version 0.15

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- Initial build for ALT Linux Sisyphus
