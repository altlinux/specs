%def_without examples
## SPEC file for Perl module IO::Stream
%define real_name IO-Stream

Name: perl-IO-Stream
Version: 2.0.2
Release: alt2

Summary:  Perl module for non-blocking I/O streams based on EV

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/IO-Stream/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2016
# optimized out: perl-Algorithm-Diff perl-AnyEvent perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-Guard perl-IO-AIO perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Sub-Uplevel perl-Term-ANSIColor perl-Text-Diff perl-common-sense perl-devel perl-parent python3 python3-base
BuildRequires: perl-AnyEvent-AIO perl-EV perl-Module-Build-Tiny perl-Test-Differences perl-Test-Exception
%if_with examples
BuildRequires: perl-Data-Alias
%endif

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
%if_without examples
%exclude %perl_vendor_privlib/IO/Stream/Noop*.pm
%endif

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2
- removed Noop* example plugins as Data::Alias is no more in 5.24

* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.2-alt1
- New version

* Sat Jan 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.10-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt1
- New version

* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.7-alt1
- Initial build for ALT Linux Sisyphus
