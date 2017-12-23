## SPEC file for Perl module HTTP::BrowserDetect

%define real_name HTTP-BrowserDetect

Name: perl-HTTP-BrowserDetect
Version: 3.16
Release: alt1

Summary: determine Web browser from an HTTP user agent string

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/HTTP-BrowserDetect/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Dec 23 2017
# optimized out: perl perl-Algorithm-Diff perl-CPAN-Meta-Requirements perl-Class-Data-Inheritable perl-Devel-StackTrace perl-Encode perl-Exception-Class perl-JSON-PP perl-Parse-CPAN-Meta perl-Sub-Uplevel perl-Test-Deep perl-Test-Differences perl-Test-Exception perl-Test-Warn perl-Text-Diff perl-devel perl-parent python-base python-modules python3 python3-base
BuildRequires: perl-CPAN-Meta perl-Path-Tiny perl-Test-FailWarnings perl-Test-Most perl-Test-NoWarnings

%description
Perl module HTTP::BrowserDetect does a number of tests on an HTTP
user agent string. The results of these tests are available via
methods of the object.

This module was originally based upon the JavaScript browser
detection code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html .


%prep
%setup -q -n %real_name-%version

# Tests runs fine with our List::Util 1.46_02
sed -e '/List::Util/ s/1\.49/1.46/' -i t/00-report-prereqs.dd
sed -e '/List::Util/ s/1\.49/1.46/' -i t/01-detect.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTORS TODO Changes
%perl_vendor_privlib/HTTP/BrowserDetect*

%changelog
* Sat Dec 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.16-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.14-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.08-alt1
- New version

* Sat Dec 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.07-alt1
- Initial build for ALT Linux Sisyphus
