## SPEC file for Perl module Promises

%define real_name Promises

Name: perl-Promises
Version: 1.04
Release: alt2

Summary: An implementation of Promises in Perl

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Promises/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: gem-power-assert perl perl-AnyEvent perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Data-OptList perl-Digest-SHA perl-EV perl-Encode perl-Future perl-Guard perl-IO-Compress perl-IO-Socket-IP perl-IO-Socket-SSL perl-JSON-PP perl-Net-SSLeay perl-Params-Util perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-Sereal-Decoder perl-Sereal-Encoder perl-Sub-Install perl-Sub-Uplevel perl-Test-Fatal perl-Try-Tiny perl-URI perl-Unicode-Normalize perl-common-sense perl-devel perl-parent perl-podlators python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-IO-Async perl-IO-Socket-Socks perl-Module-Runtime perl-Mojolicious perl-Role-Tiny perl-Sub-Attribute perl-Sub-Exporter perl-Test-Exception perl-Test-Pod perl-Test-Requires perl-Test-Warn

BuildRequires: perl-AnyEvent perl-Test-Fatal

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
%doc README.* Changes
%perl_vendor_privlib/Promises*

%changelog
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt2
- add BR: perl-Test-Fatal (no more required by perl-IO-Async)

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.04-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.02-alt1
- New version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.99-alt1
- New version

* Wed Aug 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.96-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.94-alt2
- Initial build for ALT Linux Sisyphus
