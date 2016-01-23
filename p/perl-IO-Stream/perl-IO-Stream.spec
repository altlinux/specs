## SPEC file for Perl module IO::Stream

%define real_name IO-Stream

Name: perl-IO-Stream
Version: 1.0.10
Release: alt1

Summary:  Perl module for non-blocking I/O streams based on EV

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/IO-Stream/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Feb 21 2014
# optimized out: perl-Devel-Symdump perl-EV perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Sub-Uplevel perl-common-sense perl-devel
BuildRequires: perl-Data-Alias perl-EV-ADNS perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module IO::Stream designed to give user ability to work
with I/O streams on higher level, using input/output buffers
(just scalars) and high-level events like CONNECTED, SENT or
EOF. As same time it doesn't hide low-level things, and user
still able to work on low-level without any limitations.

Architecture of this module make it ease to write plugins,
which will alter I/O stream in any way - route it through
proxies, encrypt, log, etc.

# There are no network available inside hasher
%ifdef __BTE
%def_without test
%endif

%prep
%setup -q -n %real_name-%version

%build
# Bad tests...
rm -f -- t/err-rw.t t/timeout-write-slowclient.t
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/IO/Stream*

%changelog
* Sat Jan 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.10-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt1
- New version

* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.7-alt1
- Initial build for ALT Linux Sisyphus
