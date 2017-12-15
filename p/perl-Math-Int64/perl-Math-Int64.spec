## SPEC file for Perl module Math::Int64

%define real_name Math-Int64

Name: perl-Math-Int64
Version: 0.54
Release: alt1.1.1

Summary: Perl module to manipulate 64 bits integers

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Math-Int64/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 29 2015
# optimized out: perl-CPAN-Meta-Requirements perl-IPC-Cmd perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-devel perl-parent
BuildRequires: perl-CPAN-Meta perl-ExtUtils-CBuilder perl-File-Slurp-Tiny

%description
Perl module Math::Int64 adds support for 64 bit integers,
signed and unsigned, to Perl on 32-bit platforms.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_archlib/Math/Int64*
%perl_vendor_archlib/Math/UInt64*
%perl_vendor_autolib/Math/Int64*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1.1
- rebuild with new perl 5.24.1

* Tue Jan 05 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.54-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1
- rebuild with new perl 5.22.0

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.53-alt1
- Initial build for ALT Linux Sisyphus
