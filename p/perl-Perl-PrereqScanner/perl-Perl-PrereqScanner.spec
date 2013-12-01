## SPEC file for Perl module Perl-PrereqScanner

Name: perl-Perl-PrereqScanner
Version: 1.018
Release: alt1

Summary: a tool to scan Perl code for its prerequisites

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Perl-PrereqScanner/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Perl-PrereqScanner
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sun Oct 06 2013
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Clone perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-IO-String perl-IPC-Run3 perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-devel perl-namespace-autoclean perl-namespace-clean
BuildRequires: perl-CPAN-Meta-Requirements perl-Getopt-Long-Descriptive perl-Module-Path perl-Moose perl-PPI perl-String-RewritePrefix perl-Test-Pod perl-Test-Script perl-Variable-Magic

%description
Perl module Perl-PrereqScanner is the scanner that extracts loosely
distribution prerequisites from files.
The extraction may not be perfect but tries to do its best.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Perl/PrereqScanner*

%_bindir/scan_prereqs
%_bindir/scan-perl-prereqs

%changelog
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.018-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.017-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.016-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.015-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.014-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.009-alt1
- Initial build for ALT Linux Sisyphus

