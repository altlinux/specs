Name: perl-Data-MessagePack
Version: 0.41
Release: alt1

Summary: MessagePack serialising/deserialising
License: Perl
Group: Development/Perl

URL: %CPAN Data-MessagePack
Source: %name-%version.tar

BuildRequires: perl-devel perl-Encode perl-Test-Requires

%description
This module converts Perl data structures to MessagePack and vice versa.

MessagePack is a binary-based efficient object serialization format. It
enables to exchange structured objects between many languages like JSON.
But unlike JSON, it is very fast and small.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Data/MessagePack*
%perl_vendor_autolib/Data/MessagePack

%changelog
* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.41-alt1
- New version 0.41

* Tue Dec 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- New version 0.39

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.34 -> 0.38
- built for perl-5.14

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- initial build
