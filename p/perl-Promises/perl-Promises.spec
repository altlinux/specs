## SPEC file for Perl module Promises

%define real_name Promises

Name: perl-Promises
Version: 0.94
Release: alt2

Summary: An implementation of Promises in Perl

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Promises/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Sep 18 2016
# optimized out: perl perl-AnyEvent perl-Data-OptList perl-Digest-SHA perl-EV perl-Encode perl-Guard perl-IO-Socket-IP perl-Net-SSLeay perl-Params-Util perl-Sub-Install perl-Try-Tiny perl-URI perl-common-sense perl-devel perl-parent python-base python-modules python3
BuildRequires: perl-IO-Socket-SSL perl-IO-Socket-Socks perl-Module-Runtime perl-Mojolicious perl-Sub-Exporter perl-Test-Fatal
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
* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.94-alt2
- Initial build for ALT Linux Sisyphus
