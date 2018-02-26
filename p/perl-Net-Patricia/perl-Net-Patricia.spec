%define module Net-Patricia
Name: perl-%module
Version: 1.19
Release: alt2

Summary: Patricia Trie perl module for fast IP address lookups
License: GPL
Group: Development/Perl

URL: %CPAN %module
Source: %module-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Net-CIDR-Lite perl-Socket6 perl-devel

%description
This module uses a Patricia Trie data structure to quickly
perform IP address prefix matching for applications such as
IP subnet, network or routing table lookups.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README demo
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt2
- rebuilt for perl-5.14

* Sun Dec 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.19-alt1
- New version 1.19
- Updated buildrequires
- Fixed files section

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.014-alt2.1
- rebuilt with perl 5.12

* Fri Sep 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.014-alt2
- list of packaged directories fixed

* Fri Jan 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.014-alt1
- 1.014

* Fri Sep 03 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.010-alt1
- initial package for ALT Linux
