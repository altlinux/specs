## SPEC file for Perl module Time::Duration
## Used in ikiwiki

%define version    1.06
%define release    alt1

Name: perl-Time-Duration
Version: %version
Release: alt1.1

Summary: rounded or exact English expression of durations  

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~avif/Time-Duration/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Time-Duration
Source: %real_name-%version.tar.bz2

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses perl-devel

# Automatically added by buildreq on Mon Feb 18 2008
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Time::Duration provides functions for expressing 
durations in rounded or exact terms.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%exclude /.perl.req
%perl_vendor_privlib/Time/Duration*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt0.1
- Initial build
