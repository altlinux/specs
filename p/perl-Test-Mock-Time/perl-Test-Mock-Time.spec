%define _unpackaged_files_terminate_build 1

Name: perl-Test-Mock-Time
Version: 0.2.0
Release: alt1
Summary: Deterministic time & timers for event loop tests
License: MIT
Group: Development/Perl
Url: https://metacpan.org/release/Test-Mock-Time
Source0: http://www.cpan.org/authors/id/P/PO/POWERMAN/Test-Mock-Time-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-devel perl(Module/Build/Tiny.pm) perl(Export/Attrs.pm) perl(Test/MockModule.pm) perl(bignum.pm) perl(Test/Exception.pm) perl(EV.pm) perl(Mojolicious.pm) perl(Mojo/IOLoop.pm) perl(AnyEvent.pm)

%description
This module replaces actual time with simulated time everywhere (core
time(), Time::HiRes, EV, AnyEvent with EV, Mojolicious) and provide
a way to write deterministic tests for event loop based applications
with timers.

%prep
%setup -q -n Test-Mock-Time-v%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorlib/Test*

%changelog
* Tue Aug 22 2023 Igor Vlasenko <viy@altlinux.org> 0.2.0-alt1
- automated CPAN update

* Wed Dec 02 2020 Alexandr Antonov <aas@altlinux.org> 0.1.7-alt1
- initial build for ALT
