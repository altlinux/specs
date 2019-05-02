## SPEC file for Perl module Log::Dispatchouli

Name: perl-Log-Dispatchouli
Version: 2.017
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

# Automatically added by buildreq on Thu May 02 2019
# optimized out: gem-power-assert perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Class-Data-Inheritable perl-Cpanel-JSON-XS perl-Data-OptList perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Role-Tiny perl-Specio perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Test-Fatal perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Log-Dispatch-Array perl-Ref-Util perl-Ref-Util-XS perl-String-Flogger perl-Sub-Exporter-GlobExporter perl-Test-Deep

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

