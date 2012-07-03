%define dist Net-Jabber
Name: perl-%dist
Version: 2.0
Release: alt3

Summary: Jabber Perl Library
License: GPL or Artistic or LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Time::Timezone always loaded when available
Requires: perl-Time-modules

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Net-XMPP perl-Time-modules perl-devel

%description
Net::Jabber provides a Perl user with access to the Jabber Instant Messaging
protocol.  For more information about Jabber visit: http://www.jabber.org

%prep
%setup -q -n %dist-%version
rm -rv t/lib/Test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Net

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 2.0-alt3
- added dependency on perl-Time-modules

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.0-alt2
- rebuilt

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 2.0-alt1
- 1.30 -> 2.0
- build against system Test::More (removed t/lib/Test)
- manual pages not packaged (use perldoc)

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.29 -> 1.30

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- initial revision
