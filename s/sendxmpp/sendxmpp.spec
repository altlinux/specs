Name: sendxmpp
Version: 0.0.8
Release: alt2.1
BuildArch: noarch

Summary: sendxmpp is a tool to send XMPP (jabber) messages from scripts
Group: Networking/Instant messaging
License: GPL
Source: http://www.djcbsoftware.nl/code/sendxmpp/%name-%version.tar.gz
Url: http://www.djcbsoftware.nl/code/sendxmpp/

# Automatically added by buildreq on Wed Feb 08 2006 (-bb)
BuildRequires: perl-Authen-SASL perl-Digest-SHA1 perl-Encode perl-Net-DNS perl-Net-XMPP perl-XML-Stream perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
sendxmpp is a perl-script to send XMPP (jabber) messages, similar to
what mail(1) does for mail. XMPP is an open, non-proprietary protocol
for instant messaging. See www.jabber.org for more information.

Obviously, you also need a jabber account; they are freely available
at jabber.org, but you can also install your own servers.

sendxmpp is already in use for monitoring remote servers (servers can
warn by sending xmpp-messages), and watching CVS commit messages
(developers are all connected to a XMPP-chatroom to which messages are
sent. 

%prep
%setup

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes
%_bindir/%name
%_man1dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 20 2009 Denis Klimov <zver@altlinux.org> 0.0.8-alt2
- new version from upstream cvs repo
- remove needless -q and -n  params from setup macro
- remove Packager tag

* Wed Feb 08 2006 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- First build for Sisyphus.
