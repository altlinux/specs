%define	dist Text-Kakasi
Name: perl-%dist
Version: 2.04
Release: alt2.2

Summary: Perl frontend to kakasi
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: kakasi-devel perl-Encode-JP perl-devel

%description
This module provides interface to kakasi (kanji kana simple inverter).
kakasi is a set of programs and libraries which does what Japanese
input methods do in reverse order.  You feed Japanese and kakasi
converts it to phonetic representation thereof.  kakasi can also be
used to tokenizing Japanese text. To find more about kakasi, see
<http://kakasi.namazu.org/>.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README*
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.04-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.04-alt2.1
- rebuilt with perl 5.12

* Sat Apr 02 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.04-alt2
- Minor fixes

* Sun Mar 27 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.04-alt1
- ALTLinux build
