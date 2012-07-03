%define dovecot_version 2.1
%define dovecot_nextversion 2.2
Name: dovecot-pigeonhole
Version: 0.3.1
Serial: 1
Release: alt1
Summary: Sieve language and the ManageSieve protocol for the Dovecot Secure IMAP Server
Group: System/Servers
License: LGPL v2.1
Source: dovecot-2.1-pigeonhole-%version.tar.gz
Source1: postfix+sieve.patch
Url: http://pigeonhole.dovecot.org/

Requires: dovecot >= %dovecot_version, dovecot < %dovecot_nextversion

BuildRequires: dovecot-devel >= %dovecot_version, dovecot-devel < %dovecot_nextversion

%description
This package is part of the Pigeonhole project
(http://pigeonhole.dovecot.org). It adds support for the Sieve language
(RFC 5228) and the ManageSieve protocol (RFC 5804) to the Dovecot Secure
IMAP Server. In the literal sense, a pigeonhole is a a hole or recess
inside a dovecot for pigeons to nest in. It is, however, also the name
for one of a series of small, open compartments in a cabinet used for
filing or sorting mail. As a verb, it describes the act of putting an
item into one of those pigeonholes. The name `Pigeonhole' therefore well
describes an important part of the functionality that this project adds
to Dovecot: sorting and filing e-mail messages.

This package provides Sieve support as a plugin to Dovecot's Local
Delivery Agent (LDA) and Dovecot's LMTP service. The ManageSieve
protocol is provided is an additional service, next to Dovecot's own
POP3 and IMAP services.

%package devel
Group: Development/C
Summary: Development file for %name, %summary
%description devel
Development file for %name, %summary

%prep
%setup -n dovecot-%dovecot_version-pigeonhole-%version
cp %SOURCE1 .

%build
export ACLOCAL='aclocal -I .'
%autoreconf
%configure --with-dovecot=%_libdir/dovecot --disable-static
%make_build

%check
make test

%install
make DESTDIR=%buildroot install dovecot_docdir=%_defaultdocdir/dovecot-%dovecot_version
install -pD -m 644 %buildroot/%_defaultdocdir/dovecot-%dovecot_version/example-config/conf.d/20-managesieve.conf %buildroot/%_sysconfdir/dovecot/conf.d/20-managesieve.conf
install -pD -m 644 %buildroot/%_defaultdocdir/dovecot-%dovecot_version/example-config/conf.d/90-sieve.conf %buildroot/%_sysconfdir/dovecot/conf.d/90-sieve.conf

# XXX behold, verifyelf
( cd %buildroot/%_libdir; ln -s dovecot/lib*.so.* . )

%files
%doc README AUTHORS NEWS TODO *.patch
%doc %_defaultdocdir/dovecot-%dovecot_version/example-config/conf.d/*
%doc %_defaultdocdir/dovecot-%dovecot_version/sieve
%exclude %_libdir/dovecot/*.la
%_bindir/*
%prefix/libexec/*
%_mandir/*/*
# XXX behold, verifyelf
%_libdir/lib*.so.*
%_libdir/dovecot/lib*.so.*
%_libdir/dovecot/modules/lib90_sieve_plugin.*
%_libdir/dovecot/modules/settings/lib*
%config(noreplace) %_sysconfdir/dovecot/conf.d/20-managesieve.conf
%config(noreplace) %_sysconfdir/dovecot/conf.d/90-sieve.conf

%files devel
%dir %_includedir/dovecot/sieve
%_includedir/dovecot/sieve/*
%_libdir/dovecot/lib*.so

%changelog
* Tue Jun 05 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.1-alt1
- Autobuild version bump to 0.3.1
- Add patchfile as a documentation

* Mon May 14 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.0-alt1
- Initial separate build for ALT

