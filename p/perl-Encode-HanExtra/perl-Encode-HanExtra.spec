%define dist Encode-HanExtra
Name: perl-%dist
Version: 0.23
Release: alt5.1.1.1.1

Summary: Extra sets of Chinese encodings
License: MIT
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode-devel perl-devel

%description
The Encode::HanExtra module implements additional Chinese encodings:
big5-1984, big5ext, big5plus, cccii, cns11643-1, cns11643-2, cns11643-3,
cns11643-4, cns11643-5, cns11643-6, cns11643-7, cns11643-f, euc-tw,
gb18030, unisys, unisys-sosi1, unisys-sosi2.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Encode
%perl_vendor_autolib/Encode

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt5.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt5
- built for perl 5.18
- removed manual test for implicit load of Encode::HanExtra by Encode

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt4
- rebuilt for perl-5.16

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt3
- disabled build dependency on perl-Module-Install

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt1.1.1
- rebuilt with perl 5.12

* Wed Nov 25 2009 Alexey Tourbin <at@altlinux.ru> 0.23-alt1.1
- rebuilt

* Wed Nov 21 2007 Alexey Tourbin <at@altlinux.ru> 0.23-alt1
- 0.10 -> 0.23
- license was changed to MIT

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 0.10-alt2
- rebuild

* Sun Aug 07 2005 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- initial revision
