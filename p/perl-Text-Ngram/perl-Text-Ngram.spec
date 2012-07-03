%define dist Text-Ngram
Name: perl-%dist
Version: 0.13
Release: alt2

Summary: Ngram analysis of text
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
n-Gram analysis is a field in textual analysis which uses sliding window
character sequences in order to aid topic analysis, language
determination and so on. The n-gram spectrum of a document can be used
to compare and filter documents in multiple languages, prepare word
prediction networks, and perform spelling correction.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt2
- fix directory ownership violation
- disable man packaging

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for ALT Linux Sisyphus
