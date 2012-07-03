%define dist IO-Compress
Name: perl-%dist
Version: 2.048
Release: alt1

Summary: Read and write compressed data
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

Provides: perl-IO-Compress-Base = %version perl-IO-Compress-Zlib = %version perl-IO-Compress-Bzip2 = %version perl-Compress-Zlib = %version
Obsoletes: perl-IO-Compress-Base < %version perl-IO-Compress-Zlib < %version perl-IO-Compress-Bzip2 < %version perl-Compress-Zlib < %version

BuildRequires: perl-Compress-Raw-Zlib >= %version
BuildRequires: perl-Compress-Raw-Bzip2 >= %version

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Test-NoWarnings perl-Test-Pod

%description
This distribution provides a Perl interface to allow reading and writing
of compressed data created with the zlib and bzip2 libraries.

%prep
%setup -q -n %dist-%version

%build
export TEST_SKIP_VERSION_CHECK=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/Compress
%perl_vendor_privlib/File
%perl_vendor_privlib/IO

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 2.048-alt1
- 2.037 -> 2.048

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.037-alt1
- 2.033 -> 2.037
- rebuilt as plain src.rpm

* Sat Feb 12 2011 Alexey Tourbin <at@altlinux.ru> 2.033-alt1
- 2.030 -> 2.033

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt2
- disabled ZLIB_VERSION check

* Sat Aug 07 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt1
- 2.027 -> 2.030

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 2.027-alt1
- initial revision
- provides and obsoletes: perl-IO-Compress-Base
  perl-IO-Compress-Zlib perl-IO-Compress-Bzip2 perl-Compress-Zlib
