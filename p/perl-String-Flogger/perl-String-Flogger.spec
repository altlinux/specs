## SPEC file for Perl module String::Flogger

Name: perl-String-Flogger
Version: 1.101243
Release: alt1

Summary: string munging for loggers

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/String-Flogger/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name String-Flogger
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Feb 03 2013
# optimized out: perl-Data-OptList perl-IPC-Run3 perl-JSON-XS perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Sub-Install perl-common-sense perl-devel
BuildRequires: perl-JSON perl-Sub-Exporter perl-Test-Pod perl-Test-Script

%description
Perl module String::Flogger provides string munging for loggers.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/String/Flogger*

%changelog
* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.101243-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.101242-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.101241-alt1
- Initial build for ALT Linux Sisyphus

