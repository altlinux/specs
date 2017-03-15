%define _unpackaged_files_terminate_build 1
%define dist IO-Compress
Name: perl-%dist
Version: 2.074
Release: alt1

Summary: Read and write compressed data
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PM/PMQS/%{dist}-%{version}.tar.gz

BuildArch: noarch

Provides: perl-IO-Compress-Base = %version perl-IO-Compress-Zlib = %version perl-IO-Compress-Bzip2 = %version perl-Compress-Zlib = %version
Obsoletes: perl-IO-Compress-Base < %version perl-IO-Compress-Zlib < %version perl-IO-Compress-Bzip2 < %version perl-Compress-Zlib < %version

BuildRequires: perl-Compress-Raw-Zlib >= %version
BuildRequires: perl-Compress-Raw-Bzip2 >= %version

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Test-NoWarnings perl-Test-Pod

%description
This distribution provides a Perl interface to allow reading and writing
of compressed data created with the zlib and bzip2 libraries.

%prep
%setup -q -n %{dist}-%{version}

%build
export TEST_SKIP_VERSION_CHECK=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%_bindir/zipdetails
%perl_vendor_privlib/Compress
%perl_vendor_privlib/File
%perl_vendor_privlib/IO

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.074-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.072-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.070-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.069-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.068-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.067-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.066-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.064-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.063-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.062-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.061-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.055-alt1
- 2.048 -> 2.055
- packaged /usr/bin/zipdetails, requires Encode

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
