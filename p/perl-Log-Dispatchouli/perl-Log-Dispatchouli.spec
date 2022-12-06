## SPEC file for Perl module Log::Dispatchouli

Name: perl-Log-Dispatchouli
Version: 3.001
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

# Automatically added by buildreq on Fri Sep 17 2021
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Class-Data-Inheritable perl-Cpanel-JSON-XS perl-Data-OptList perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Role-Tiny perl-Specio perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Log-Dispatch-Array perl-Ref-Util perl-Ref-Util-XS perl-String-Flogger perl-Sub-Exporter-GlobExporter perl-Test-Deep perl-Test-Fatal

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
%perl_vendor_privlib/Log/Fmt.pm

%changelog
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 3.001-alt1
- New version

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.023-alt2
- update BR

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.023-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.022-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.019-alt1
- New version

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.017-alt1
- New version

* Sun Mar 04 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.016-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.015-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.012-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.010-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.008-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.006-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.005-alt1
- Initial build for ALT Linux Sisyphus

