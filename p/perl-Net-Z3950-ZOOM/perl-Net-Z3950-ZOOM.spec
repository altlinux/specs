%define dist Net-Z3950-ZOOM
Name: perl-%dist
Version: 1.30
Release: alt1.1.1.1

Summary: Perl extension implementing the ZOOM API for Information Retrieval
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
# Source-url: http://search.cpan.org/CPAN/authors/id/M/MI/MIRK/Net-Z3950-ZOOM-%version.tar.gz
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011 (-bi)
BuildRequires: libssl-devel libwrap-devel libyaz-devel perl-MARC-Record perl-XML-LibXML perl-devel

BuildRequires: libyaz-devel >= 4.0.0

%description
This distribution contains three Perl modules for the price of one.
They all provide facilities for building information retrieval clients
using the standard Z39.50 and SRW/U protocols, but do so using
different APIs.

%prep
%setup -n %dist-%version

%ifdef __BTE
# disable network-dependent tests
grep -lZ connect t/*.t |xargs -r0 rm -v
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/zselect
%_bindir/zoomdump
%_bindir/zoom-delete-records
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net
%perl_vendor_archlib/ZOOM*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1.1
- rebuild with new perl 5.22.0

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt1
- new version 1.30 (with rpmrb script)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- rebuilt for perl-5.14

* Wed Jul 13 2011 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt1
- Updated to 1.28.
- Updated build dependencies.

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.25-alt1.1.1
- rebuilt with perl 5.12

* Mon Oct 27 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.25-alt1.1
- rebuild w/o test

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.25-alt1
- new version

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.24-alt2
- fixed build

* Tue Jul 01 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.24-alt1
- new version

* Wed Aug 01 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.19-alt1
- new version

* Mon Jun 11 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.18-alt1
- first build for ALT Linux Sisyphus
