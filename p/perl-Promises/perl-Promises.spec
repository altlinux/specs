## SPEC file for Perl module Promises

%define real_name Promises

Name: perl-Promises
Version: 0.96
Release: alt1

Summary: An implementation of Promises in Perl

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Promises/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed Aug 30 2017
# optimized out: perl perl-AnyEvent perl-Data-OptList perl-Digest-SHA perl-EV perl-Encode perl-Future perl-Guard perl-IO-Socket-IP perl-Net-SSLeay perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-Sereal-Decoder perl-Sereal-Encoder perl-Sub-Install perl-Sub-Uplevel perl-Test-Fatal perl-Try-Tiny perl-URI perl-common-sense perl-devel perl-parent perl-podlators python-base python-modules python3 python3-base ruby ruby-stdlibs
BuildRequires: perl-IO-Async perl-IO-Socket-SSL perl-IO-Socket-Socks perl-Module-Runtime perl-Mojolicious perl-Sub-Exporter perl-Test-Requires perl-Test-Warn

BuildRequires: perl-AnyEvent

%description
Perl module Promises provides an implementation of the "Promise/A+"
pattern for asynchronous programming. Promises are meant to be
a way to better deal with the resulting callback spaghetti that
can often result in asynchronous programs.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Promises*

%changelog
* Wed Aug 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.96-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.94-alt2
- Initial build for ALT Linux Sisyphus
