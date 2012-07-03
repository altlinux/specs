%define php5_extension xmpphp
%define ver rc2-r77

Name: php5-xmpphp
Version: 0.1
Release: alt1rc2

Summary: XMPPHP is the successor to Class.Jabber.PHP
License: GPL
Group: System/Servers

Url: http://code.google.com/p/xmpphp/
Source: http://xmpphp.googlecode.com/files/%php5_extension-%version%ver.tar

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires(pre): rpm-build-php5

BuildArch: noarch

Requires: php5-openssl

%description
XMPPHP is the successor to Class.Jabber.PHP.

Some of the features include:
 * Connect to any XMPP 1.0 server (Google Talk, LJ Talk, jabber.org, etc)
 * Supports TLS encryption
 * Several XML processing approaches and supported styles (process indefinitely,
   processUntil an event, processTime for a number of seconds),
   waiting on events or map them, etc.

%prep
%setup -n %php5_extension-%version%ver

%install
mkdir -p %buildroot/%php5_moddir/XMPPHP/
cp -a XMPPHP/*.php %buildroot/%php5_moddir/XMPPHP/

%files
%doc README *.php
%php5_moddir/XMPPHP/

%changelog
* Sat Dec 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1rc2
- initial build for ALT Linux Sisyphus

