## SPEC file for Perl module PerlIO::utf8_strict

Name: perl-PerlIO-utf8_strict
Version: 0.005
Release: alt1

Summary: fast and correct UTF-8 IO module

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/PerlIO-utf8_strict/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name PerlIO-utf8_strict
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: libcloog-isl4 perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-IPC-Run3 perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Sub-Uplevel perl-devel perl-podlators
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-Exception perl-Test-Script

%description
Perl module PerlIO::utf8_strict provides a fast and correct UTF-8
PerlIO layer. Unlike perl's default :utf8 layer it checks the
input for correctness.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO*
%perl_vendor_autolib/PerlIO*

%changelog
* Sun Nov 16 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- New version

* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt1
- Initial build for ALT Linux Sisyphus
