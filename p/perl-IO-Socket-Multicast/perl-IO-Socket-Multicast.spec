%define dist IO-Socket-Multicast
Name: perl-%dist
Version: 1.12
Release: alt1.2

Summary: Send and receive multicast messages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
The IO::Socket::Multicast module subclasses IO::Socket::INET to enable
you to manipulate multicast groups.  With this module (and an
operating system that supports multicasting), you will be able to
receive incoming multicast transmissions and generate your own
outgoing multicast packets.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/IO
%perl_vendor_autolib/IO

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.12-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Sun Oct 04 2009 Michael Bochkaryov <misha@altlinux.ru> 1.07-alt1
- initial build for ALT Linux Sisyphus
