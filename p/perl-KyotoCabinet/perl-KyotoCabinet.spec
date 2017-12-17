Name: perl-KyotoCabinet
Version: 1.20
Release: alt3.1.1.1.1
Summary: a straightforward implementation of DBM

Group: Development/Perl
License: GPLv3
Url: http://fallabs.com/kyotocabinet/perlpkg/

Source: kyotocabinet-perl-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libkyotocabinet-devel perl-devel

%description
%summary

%prep
%setup -q -n kyotocabinet-perl-%version

%build
%def_without test
%perl_vendor_build LIBS='-lkyotocabinet'

%install
%perl_vendor_install

rm %buildroot%perl_vendor_archlib/*.pl

%files
%doc COPYING README
%perl_vendor_archlib/KyotoCabinet*
%perl_vendor_autolib/KyotoCabinet

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.20-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.20-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt3
- built for perl 5.18
- temporary disabled tests

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.16

* Thu Jul 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.20-alt1
- New version 1.20

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.18-alt3
- Rebuilt for perl-5.14

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt2
- Rebuild

* Tue Jul 12 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt1
- New version 1.18

* Thu Jun 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.17-alt1
- New version 1.17

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- New version 1.16

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 1.15-alt1
- initial build

