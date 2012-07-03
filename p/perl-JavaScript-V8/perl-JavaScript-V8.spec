Name: perl-JavaScript-V8
Version: 0.06.50
Release: alt2

Summary: JavaScript::V8 - Perl interface to the V8 JavaScript engine
Group: Development/Perl
License: Perl

Url: %CPAN JavaScript-V8
Source: %name-%version.tar

BuildRequires: perl-devel gcc-c++ perl-ExtUtils-XSpp libv8-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/JavaScript/V8*
%perl_vendor_autolib/JavaScript/V8*
%doc Changes README 

%changelog
* Sat Jun 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.06.50-alt2
- Rebuild with libv8-3.10.8.18

* Thu Mar 15 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06.50-alt1
- 0.06.50 (fd227ee9)

* Tue Mar 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build
