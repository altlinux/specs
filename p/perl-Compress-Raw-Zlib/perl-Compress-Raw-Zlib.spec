%define dist Compress-Raw-Zlib
Name: perl-%dist
Version: 2.048
Release: alt1

Summary: Low-level interface to the zlib compression library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Test-NoWarnings perl-Test-Pod zlib-devel

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library.

%prep
%setup -q -n %dist-%version
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
