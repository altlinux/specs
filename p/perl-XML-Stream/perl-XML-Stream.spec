%define dist XML-Stream
Name: perl-%dist
Version: 1.23
Release: alt1

Summary: XML Stream connection and data parser Perl modules
License: LGPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 20 2010
BuildRequires: perl-Authen-SASL perl-Encode perl-IO-Socket-SSL perl-Net-DNS perl-devel

%description
This module provides the user with methods to connect to a remote
server, send a stream of XML to the server, and receive/parse an XML
stream from the server.  It is primarily based work for the Etherx XML
router developed by the Jabber Development Team.  For more information
about this project visit http://etherx.jabber.org/stream/.

%prep
%setup -q -n %dist-%version
%__rm -rfv t/lib/Test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	CHANGES INFO README
%dir	%perl_vendor_privlib/XML
%dir	%perl_vendor_privlib/XML/Stream
	%perl_vendor_privlib/XML/Stream.pm
	%perl_vendor_privlib/XML/Stream/*

%changelog
* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.23-alt1
- 1.22 -> 1.23

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 1.22-alt2
- rebuild in new environment
- build against system Test::More (removed t/lib/Test)
- manual pages not packaged (use perldoc)

* Wed Oct 13 2004 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.17 -> 1.21

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- initial revision
