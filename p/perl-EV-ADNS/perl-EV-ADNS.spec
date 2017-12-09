## SPEC file for Perl module EV::ADNS

%define real_name EV-ADNS

Name: perl-EV-ADNS
Version: 3.0
Release: alt1

Summary: Perl module for lightweight asynchronous DNS queries using EV and libadns

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/HTML-Tidy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

Patch0: %real_name-2.2-alt-gcc_warnings_fix.patch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Dec 09 2017
# optimized out: perl perl-common-sense perl-devel python-base python-modules python3 python3-base
BuildRequires: libadns-devel perl-Canary-Stability perl-EV perl-Encode

%description
Perl module EV::ADNS provides a simple interface to libadns
(asynchronous dns) that integrates well and automatically
into the EV event loop.

%prep
%setup -q -n %real_name-%version

%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%exclude /.perl.req
%perl_vendor_autolib/EV/ADNS*
%perl_vendor_archlib/EV/ADNS*


%changelog
* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.0-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1.1
- rebuild with new perl 5.22.0

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.3-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.1
- rebuild with new perl 5.20.1

* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- Initial build for ALT Linux Sisyphus
