## SPEC file for Perl module Perl-PrereqScanner

Name: perl-Perl-PrereqScanner
Version: 1.015
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


# Automatically added by buildreq on Sun Oct 14 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Clone perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-IO-String perl-IPC-Run3 perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Probe-Perl perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-clean
BuildRequires: perl-CPAN-Meta-Requirements perl-PPI perl-String-RewritePrefix perl-Test-Script perl-namespace-autoclean

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

%changelog
* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.015-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.014-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.009-alt1
- Initial build for ALT Linux Sisyphus

