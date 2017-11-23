%define _unpackaged_files_terminate_build 1
%define dist Compress-Raw-Zlib
Name: perl-%dist
Version: 2.076
Release: alt1

Summary: Low-level interface to the zlib compression library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PM/PMQS/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Test-NoWarnings perl-Test-Pod zlib-devel

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library.

%prep
%setup -q -n %{dist}-%{version}
rm -rv zlib-src/
rm -rv t/Test/

# disable build dependency on IO-Compress
sed -i- 's/^BEGIN$/if (0)/' t/compress/CompTestUtils.pm

cat >config.in <<EOF
BUILD_ZLIB = False
INCLUDE = %_includedir
LIB = %_libdir
OLD_ZLIB = False
GZIP_OS_CODE = 3
EOF

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.076-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.074-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.072-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.071-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.071-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.070-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.069-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.069-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.068-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.067-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.066-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.066-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.065-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.063-alt1
- automated CPAN update

* Wed Aug 21 2013 Vladimir Lettiev <crux@altlinux.ru> 2.062-alt1
- 2.061 -> 2.062

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.061-alt1
- automated CPAN update

* Thu Aug 23 2012 Vladimir Lettiev <crux@altlinux.ru> 2.056-alt1
- built for perl-5.16
- 2.048 -> 2.056

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 2.048-alt1
- 2.037 -> 2.048

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.037-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.037-alt1
- 2.033 -> 2.037
- rebuilt as plain src.rpm

* Fri Feb 11 2011 Alexey Tourbin <at@altlinux.ru> 2.033-alt1
- 2.030 -> 2.033

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt1.1
- rebuilt for perl-5.12

* Thu Aug 05 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt1
- 2.027 -> 2.030

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 2.027-alt1
- 2.025 -> 2.027

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 2.025-alt1
- 2.021 -> 2.025

* Wed Sep 16 2009 Alexey Tourbin <at@altlinux.ru> 2.021-alt1
- 2.020 -> 2.021

* Tue Jun 16 2009 Alexey Tourbin <at@altlinux.ru> 2.020-alt1
- 2.017 -> 2.020

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 2.017-alt1
- 2.012 -> 2.017

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 2.012-alt1
- 2.011 -> 2.012

* Thu Jun 12 2008 Alexey Tourbin <at@altlinux.ru> 2.011-alt1
- 2.010 -> 2.011

* Thu May 15 2008 Alexey Tourbin <at@altlinux.ru> 2.010-alt1
- initial revision
