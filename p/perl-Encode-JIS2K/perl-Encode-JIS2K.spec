%define _unpackaged_files_terminate_build 1
%define dist Encode-JIS2K
Name: perl-%dist
Version: 0.03
Release: alt1.1.1.1

Summary: JIS X 0212 (aka JIS 2000) encodings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Encode-JP perl-Encode-devel perl-devel

%description
The Encode::JIS2K module implements encodings that covers JIS X 0213
charset (AKA JIS 2000): euc-jisx0213, shiftjisx0123, iso-2022-jp-3,
jis0213-1-raw, jis0213-2-raw.

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1.1
- rebuilt with perl 5.12

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
