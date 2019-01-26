## SPEC file for Perl module Statistics::CaseResampling

%define real_name Statistics-CaseResampling

Name: perl-Statistics-CaseResampling
Version: 0.15
Release: alt5.1

Summary: Perl module for resampling and calculation of medians with confidence intervals

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Statistics-CaseResampling

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Aug 17 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby sh3
BuildRequires: perl-CPAN-Meta

%description
Perl module Statistics::CaseResampling provides a way to calculate
the median (or in principle also other statistics) with confidence
intervals on a sample. To do that, it uses a technique called
bootstrapping. In a nutshell, it resamples the sample a lot of
times and for each resample, it calculates the median. From the
distribution of medians, it then calculates the confidence limits.

In order to implement the confidence limit calculation, various
other functions had to be implemented efficiently (both
algorithmically efficient and done in C). These functions may be
useful in their own right and are thus exposed to Perl. 
Most notably, this exposes a median (and general selection)
algorithm that works in linear time as opposed to the trivial
implementation that requires O(n*log(n)).

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Statistics/CaseResampling*
%perl_vendor_autolib/Statistics/CaseResampling*

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt5.1
- rebuild with new perl 5.28.1

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.15-alt5
- Initial build for ALT Linux Sisyphus
