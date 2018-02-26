## SPEC file for Perl module AnyEvent:BDB

Name: perl-AnyEvent-BDB
Version: 1.1
Release: alt1

Summary: asynchronous berkeley db access

License: %perl_license
Group: Development/Perl

%define real_name AnyEvent-BDB
URL: http://search.cpan.org/~mlehmann/AnyEvent-BDB/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Nov 27 2010
BuildRequires: perl-AnyEvent perl-BDB

%description
Perl module AnyEvent:BDB provides transparent integration of BDB
into AnyEvent.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/AnyEvent/BDB*

%changelog
* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.1-alt1
- Initial build for ALT Linux Sisyphus
