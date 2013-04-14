Name: perl-Time-Duration
Version: 1.1
Release: alt1
Epoch: 1

Summary: rounded or exact English expression of durations

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~avif/Time-Duration/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Time-Duration
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Apr 14 2013
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
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
* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1:1.1-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt0.1
- Initial build
