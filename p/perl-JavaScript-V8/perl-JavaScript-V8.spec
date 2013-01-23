Name: perl-JavaScript-V8
Version: 0.065
Release: alt1.030f7c7.1

Summary: JavaScript::V8 - Perl interface to the V8 JavaScript engine
License: Perl
Group: Development/Perl

Url: %CPAN JavaScript-V8
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel gcc-c++ perl-ExtUtils-XSpp libv8-devel

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/JavaScript/V8*
%perl_vendor_autolib/JavaScript/V8*
%doc Changes README

%changelog
* Sun Jan 20 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.065-alt1.030f7c7.1
- Rebuild with new version of v8

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.065-alt1.030f7c7
- fixed version
- updated source to git 030f7c7
- fixed build on x86_32

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06.50-alt3
- rebuilt for perl-5.16
- fixed test t/basic.t

* Sat Jun 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.06.50-alt2
- Rebuild with libv8-3.10.8.18

* Thu Mar 15 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06.50-alt1
- 0.06.50 (fd227ee9)

* Tue Mar 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build
