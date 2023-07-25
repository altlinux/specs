## SPEC file for Perl module Perl-PrereqScanner

Name: perl-Perl-PrereqScanner
Version: 1.100
Release: alt1

Summary: a tool to scan Perl code for its prerequisites

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Perl-PrereqScanner/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

%define real_name Perl-PrereqScanner
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Tue Jul 25 2023
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Clone perl-Data-OptList perl-Encode perl-Exporter-Tiny perl-Getopt-Long-Descriptive perl-JSON-PP perl-Module-Implementation perl-Module-Runtime perl-Moo perl-PPI perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-Role-Tiny perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Quote perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-clean perl-parent perl-podlators python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Module-Path perl-PPI-XS perl-Ref-Util-XS perl-String-RewritePrefix perl-Type-Tiny perl-namespace-autoclean

BuildRequires: perl-podlators

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

%_man1dir/scan*

%changelog
* Tue Jul 25 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.100-alt1
- New version

* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.025-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.024-alt1
- New version

* Thu May 09 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.023-alt2
- Update BuildRequires to fix package build

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.023-alt1
- New version

* Sun Nov 16 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.021-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.020-alt1
- New version

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

