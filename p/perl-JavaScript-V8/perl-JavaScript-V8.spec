%define v8abi 3.15

Name: perl-JavaScript-V8
Version: 0.070
Release: alt6.1

Summary: JavaScript::V8 - Perl interface to the V8 JavaScript engine
License: Perl
Group: Development/Perl

Url: %CPAN JavaScript-V8
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel gcc-c++ perl-ExtUtils-XSpp libv8-devel = %{v8abi}

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.070-alt6.1
- rebuild with new perl 5.26.1

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.070-alt6
- build with v8abi 3.15

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.070-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.070-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.070-alt5.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.070-alt5
- built for perl 5.18

* Mon Aug 05 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.070-alt4
- Rebuild with versioned v8

* Fri Jul 26 2013 Andrey Cherepanov <cas@altlinux.org> 0.070-alt3
- Rebuild with v8-3.18.5.9

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 0.070-alt2
- Rebuild with new version of v8

* Wed Apr 17 2013 Andrey Cherepanov <cas@altlinux.org> 0.070-alt1
- New version 0.07
- Replace deprecated V8 functions

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
