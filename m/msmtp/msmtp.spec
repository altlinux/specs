#%define ssl_libs openssl
%define ssl_libs gnutls

Name: msmtp
Version: 1.4.27
Release: alt1

Summary: Mail delivering agent (MDA) that uses customizable SMTP-server
License: GPLv3+
Group: Networking/Mail

Url: http://msmtp.sourceforge.net/
Source: http://download.sourceforge.net/sourceforge/msmtp/msmtp-%version.tar.bz2

# Automatically added by buildreq on Wed May 04 2011
# optimized out: glib2-devel libgnome-keyring libgpg-error pkg-config
# for gnutls libs:
BuildRequires: libgnome-keyring-devel libgnutls-devel libgsasl-devel libidn-devel

# for openssl ssl libs:
#BuildRequires: libgnome-keyring-devel libgsasl-devel libidn-devel libssl-devel

%description
msmtp is an SMTP client: it transmits a mail to an SMTP server
(for example, at a free mail provider) which does the delivery.
To use this program with your mail user agent (MUA),
create a configuration file with your mail account(s)
and tell your MUA to call msmtp instead of /usr/sbin/sendmail.

Features include:
- Sendmail compatible interface (command line options and exit codes)
- Many authentication methods: PLAIN, LOGIN, CRAM-MD5, EXTERNAL.
  With GNU SASL, GSSAPI, DIGEST-MD5 and NTLM are also allowed.
- TLS/SSL encrypted connections (including server certificate verification
  and optional sending of client certificate) in separate %name-ssl package
- DSN (Delivery Status Notification) support
- RMQS (Remote Message Queue Starting) support (ETRN keyword)
- PIPELINING support for increased transmission speed
- IPv6 support
- LMTP support
- support for multiple accounts

%prep
%setup

%build
%configure --with-ssl=%ssl_libs --with-gnome-keyring
%make_build

%install
%makeinstall_std

%find_lang msmtp

%files -f msmtp.lang
%_bindir/msmtp
%_man1dir/*
%_infodir/msmtp.*
%doc NEWS README doc/Mutt+msmtp.txt doc/msmtprc-*.example

%changelog
* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.4.27-alt1
- 1.4.27

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 1.4.26-alt1
- 1.4.26

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 1.4.25-alt1
- 1.4.25

* Wed May 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.24-alt1
- 1.4.24

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.4.23-alt1
- 1.4.23

* Fri Dec 31 2010 Victor Forsiuk <force@altlinux.org> 1.4.22-alt1
- 1.4.22

* Mon Sep 20 2010 Victor Forsiuk <force@altlinux.org> 1.4.21-alt1
- 1.4.21

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.16-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for msmtp
  * postclean-05-filetriggers for spec file

* Sat Sep 27 2008 Ilya Evseev <evseev@altlinux.ru> 1.4.16-alt1
- updated to new version 1.4.16

* Thu Mar 27 2008 Ilya Evseev <evseev@altlinux.ru> 1.4.14-alt1
- updated to new version 1.4.14

* Wed Aug  1 2007 Ilya Evseev <evseev@altlinux.ru> 1.4.13-alt1
- updated to new version 1.4.13

* Mon Jun 25 2007 Ilya Evseev <evseev@altlinux.ru> 1.4.12-alt1
- updated to new version 1.4.12

* Tue Apr 10 2007 Ilya Evseev <evseev@altlinux.ru> 1.4.11-alt1
- updated to new version 1.4.11

* Mon Jan 22 2007 Ilya Evseev <evseev@altlinux.ru> 1.4.10-alt1
- updated to new version 1.4.10

* Mon Nov  6 2006 Ilya Evseev <evseev@altlinux.ru> 1.4.9-alt1
- updated to new version 1.4.9

* Mon Aug 21 2006 Ilya Evseev <evseev@altlinux.ru> 1.4.7-alt1
- updated to new version 1.4.7

* Fri Jun 23 2006 Ilya Evseev <evseev@altlinux.ru> 1.4.6-alt1
- updated to new version 1.4.6

* Fri Feb 17 2006 Ilya Evseev <evseev@altlinux.ru> 1.4.5-alt1
- initial build for ALTLinux
