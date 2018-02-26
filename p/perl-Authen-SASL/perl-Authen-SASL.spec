%define dist Authen-SASL
Name: perl-%dist
Version: 2.15
Release: alt3

Summary: SASL authentication framework for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# not yet
%add_findreq_skiplist */GSSAPI.pm

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Crypt-RC4 perl-Digest-HMAC perl-devel

%description
SASL is the Simple Authentication and Security Layer (RFC 2222), a
method for adding authentication support to connection-based protocols.
To use SASL, a protocol includes a command for identifying and
authenticating a user to a server and for optionally negotiating
protection of subsequent protocol interactions.  If its use is
negotiated, a security layer is inserted between the protocol and the
connection.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	api.txt Changes example_pl
%dir	%perl_vendor_privlib/Authen
	%perl_vendor_privlib/Authen/SASL.pm
%doc	%perl_vendor_privlib/Authen/SASL.pod
%dir	%perl_vendor_privlib/Authen/SASL
	%perl_vendor_privlib/Authen/SASL/*.pm
%doc	%perl_vendor_privlib/Authen/SASL/*.pod
%dir	%perl_vendor_privlib/Authen/SASL/Perl
	%perl_vendor_privlib/Authen/SASL/Perl/*.pm

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.15-alt3
- disabled build dependency on perl-Module-Install

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.15-alt2
- rebuilt as plain src.rpm

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 2.15-alt1
- 2.14 -> 2.15

* Wed Mar 17 2010 Alexey Tourbin <at@altlinux.ru> 2.14-alt1
- 2.13 -> 2.14

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.12 -> 2.13

* Sat Nov 01 2008 Alexey Tourbin <at@altlinux.ru> 2.12-alt1
- 2.11 -> 2.12

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 2.11-alt1
- 2.09 -> 2.11

* Wed Apr 27 2005 Alexey Tourbin <at@altlinux.ru> 2.09-alt1
- 2.08 -> 2.09
- built against system Test::More (removed inc/Test)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.08-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 2.08-alt1
- 2.07 -> 2.08

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- 2.05 -> 2.07

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.05

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.04
- buildreq re-applied (fixes build in the hasher)
- descriptions updated

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 2.03-alt1
- 2.03

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 2.02-alt1
- Inital Build for ALT
