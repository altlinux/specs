## SPEC file for Perl module Log::Dispatchouli

Name: perl-Log-Dispatchouli
Version: 2.005
Release: alt1

Summary: a simple wrapper around Log::Dispatch

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Log-Dispatchouli/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Log-Dispatchouli
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-JSON perl-JSON-XS perl-Log-Dispatch perl-Params-Util perl-Params-Validate perl-Sub-Exporter perl-Sub-Install perl-Try-Tiny perl-common-sense perl-devel
BuildRequires: perl-Log-Dispatch-Array perl-String-Flogger perl-Sub-Exporter-GlobExporter perl-Test-Deep perl-Test-Fatal

%description
Perl module Log::Dispatchouli is a thin layer above Log::Dispatch
and meant to make it dead simple to add logging to a program
without having to think much about categories, facilities, levels,
or things like that. It is meant to make logging just configurable
enough that you can find the logs you want and just easy enough
that you will actually log things.

Log::Dispatchouli can log to syslog (if you specify a facility),
standard error or standard output, to a file, or to an array in
memory. That last one is mostly useful for testing.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Log/Dispatchouli*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.005-alt1
- Initial build for ALT Linux Sisyphus

