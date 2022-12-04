## SPEC file for Perl module HTTP::BrowserDetect

%define real_name HTTP-BrowserDetect
%define _unpackaged_files_terminate_build 1

Name: perl-HTTP-BrowserDetect
Version: 3.37
Release: alt1

Summary: determine Web browser from an HTTP user agent string

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/HTTP-BrowserDetect/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Nov 06 2021
# optimized out: libgpg-error perl perl-Algorithm-Diff perl-CPAN-Meta-Requirements perl-Clone-Choose perl-Devel-StackTrace perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Text-Diff perl-devel perl-parent python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Clone perl-Hash-Merge perl-Module-Runtime perl-Path-Tiny perl-Test-Differences perl-Test-NoWarnings perl-Test-Warnings

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
%doc CONTRIBUTORS TODO Changes README.md examples
%perl_vendor_privlib/HTTP/BrowserDetect*

%changelog
* Sun Dec 04 2022 Nikolay A. Fetisov <naf@altlinux.org> 3.37-alt1
- New version

* Sat Nov 06 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.35-alt1
- New version

* Sun Aug 09 2020 Nikolay A. Fetisov <naf@altlinux.org> 3.31-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 3.27-alt1
- New version

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 3.23-alt1
- New version

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.21-alt1
- new version

* Sat Dec 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.16-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.14-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.08-alt1
- New version

* Sat Dec 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.07-alt1
- Initial build for ALT Linux Sisyphus
