%define real_name Test-LWP-UserAgent

Name: perl-%real_name
Version: 0.036
Release: alt1

Summary: A LWP::UserAgent suitable for simulating and testing network calls

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
# Configure requirements.
BuildRequires: perl-CPAN-Meta-Requirements
BuildRequires: perl-Module-Metadata
# Runtime requires (also needed at build/test time, as the module loads them).
BuildRequires: perl-HTTP-Message
BuildRequires: perl-libwww
BuildRequires: perl-Safe-Isa
BuildRequires: perl-Try-Tiny
BuildRequires: perl-URI
BuildRequires: perl-namespace-clean
# Test requirements.
BuildRequires: perl-Path-Tiny
BuildRequires: perl-Test-Deep
BuildRequires: perl-Test-Fatal
BuildRequires: perl-Test-Needs
BuildRequires: perl-Test-RequiresInternet
BuildRequires: perl-Test-Warnings

%description
Test::LWP::UserAgent is a LWP::UserAgent suitable for simulating and testing
network calls. It can be used to test client code that uses LWP::UserAgent
without making real HTTP requests, by registering predictable responses for
given request patterns.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENCE
%perl_vendor_privlib/Test/LWP/UserAgent*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.036-alt1
- initial build for Sisyphus
