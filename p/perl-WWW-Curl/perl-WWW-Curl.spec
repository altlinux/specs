%define dist WWW-Curl
Name: perl-%dist
Version: 4.17
Release: alt8

Summary: Perl extension interface for libcurl 
License: MPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz
Patch0: WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=941915
Patch1: WWW-Curl-4.17-define-CURL-as-void.patch
# Adapt to changes in cURL 7.69.0, bug #1812910, CPAN RT#132197
Patch2: WWW-Curl-4.17-Adapt-to-changes-in-cURL-7.69.0.patch
# Adapt to changes in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch3: WWW-Curl-4.17-Adapt-to-curl-7.87.0.patch
# Workound a bug in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch4: WWW-Curl-4.17-Work-around-a-macro-bug-in-curl-7.87.0.patch
Patch5: WWW-Curl-4.17-alt-no-win32.patch
# http://www.cpan.org/authors/id/S/SR/SREZIC/patches/WWW-Curl-4.17-PR24-ERRONEOUS1.patch
Patch6: http://www.cpan.org/authors/id/S/SR/SREZIC/patches/WWW-Curl-4.17-PR24-ERRONEOUS1-alt.patch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: libcurl-devel perl-Test-Pod perl-Test-Pod-Coverage perl(inc/Module/Install.pm)

%description
The perl module WWW::Curl provides an interface to the cURL library "libcurl".

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

rm -rf inc && sed -i -e '/^inc\//d' MANIFEST

# XXX tests fail
rm t/19multi.t

%ifdef __BTE
# disable network-dependent tests
%def_without test
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/WWW
%perl_vendor_autolib/WWW

%changelog
* Fri Mar 31 2023 Igor Vlasenko <viy@altlinux.org> 4.17-alt8
- support of curl 8 (closes: #41027)

* Mon Feb 27 2023 Igor Vlasenko <viy@altlinux.org> 4.17-alt7
- fixed build - Adapt to changes in cURL 7.69.0

* Wed Sep 29 2021 Anton Farygin <rider@altlinux.ru> 4.17-alt6
- added curl-7.66+ compatibility patch (closes: #41027)

* Sat Apr 04 2020 Igor Vlasenko <viy@altlinux.ru> 4.17-alt5
- fixed build

* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.17-alt4
- fixed build

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.17-alt3.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.17-alt3.1
- rebuild with new perl 5.26.1

* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 4.17-alt3
- fix for perl 5.26

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.17-alt2.1
- rebuild with new perl 5.24.1

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 4.17-alt2
- fixed build

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.17-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.17-alt1.1
- rebuild with new perl 5.20.1

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 4.17-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 4.15-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 4.15-alt3
- rebuilt for perl-5.16

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 4.15-alt2
- disabled build dependency on perl-Module-Install

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 4.15-alt1
- 4.11 -> 4.15
- built for perl-5.14
- disabled network-depndent test in hasher

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 4.11-alt1.1
- rebuilt with perl 5.12
- disabled a failing test for a while

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.11-alt1
- new version

* Tue Apr 07 2009 Anton Farygin <rider@altlinux.ru> 4.06-alt1
- new version
- manpage added

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 4.05-alt1
- new version
- revert back ssl tests

* Wed Nov 08 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt2.1
- fix build in gear.

* Wed Nov 08 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt2
- disable ssl tests (cause openssl not ready for it);
- prepare for gear.

* Mon Aug 14 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt1
- initial build for ALTLinux;
- don't package man pages (use perldoc instead).

