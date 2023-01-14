## SPEC file for Perl module Mixin::Linewise

%define real_name Mixin-Linewise

Name: perl-Mixin-Linewise
Version: 0.111
Release: alt1

Summary: Perl module to work with handle-like string objects

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Mixin-Linewise/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Jun 07 2015
# optimized out: perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Install
BuildRequires: perl-CPAN-Meta perl-PerlIO-utf8_strict perl-Sub-Exporter perl-devel

%description
Perl module Mixin::Linewise simplifies the way to deal with opening
files for IO, converting strings to handle-like objects, and all
that. With Mixin::Linewise::Readers and Mixin::Linewise::Writers,
you can just write a method to handle handles, and methods for
handling strings and filenames are added for you.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Mixin/Linewise*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.111-alt1
- New version

* Sun Jun 27 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.110-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.109-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.108-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.106-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.102-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- Initial build for ALT Linux Sisyphus
