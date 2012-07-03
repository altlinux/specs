%define dist Encode-HanExtra
Name: perl-%dist
Version: 0.23
Release: alt3

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

# test: Encode should load Encode::HanExtra implicitly
perl -Mblib -MEncode <<\__EOF__
encode("euc-tw", "utf8_data") or die;
decode("euc-tw", "euc_tw_data") or die;
encode("gb18030", "utf8_data") or die;
decode("gb18030", "euc_tw_data") or die;
__EOF__

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Encode
%perl_vendor_autolib/Encode

%changelog
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
