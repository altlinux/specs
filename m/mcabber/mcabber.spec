Name: mcabber
Version: 0.10.1
Release: alt1

Summary: console Jabber client
License: GPL
Group: Networking/Instant messaging
Url: http://www.lilotux.net/~mikael/mcabber/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Thu Sep 30 2010
BuildRequires: libenchant-devel libgpgme-devel libloudmouth-devel libncursesw-devel libotr-devel

%description
mcabber is a small Jabber console client for Linux, maintained by Mikael BERTHE.
mcabber includes features such as SSL support, history logging, commands completion
and external actions triggers. Please read the manual page (manpage link below)
for more information.

%package devel
Summary: %summary
Group: %group

%description devel
mcabber is a small Jabber console client for Linux, maintained by Mikael BERTHE.
mcabber includes features such as SSL support, history logging, commands completion
and external actions triggers. Please read the manual page (manpage link below)
for more information.

%prep
%setup
# not yet
cp macros/missing/libotr.m4 macros

%build
%autoreconf
%configure --enable-aspell --with-ssl --enable-sigwinch --enable-otr --enable-xep0022 --enable-enchant
%make_build

%install
%makeinstall

%files
%doc contrib AUTHORS ChangeLog TODO mcabberrc.example
%_libdir/%name
%_bindir/*
%_man1dir/*
%_datadir/%name

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 0.10.1-alt1
- 10.0.1

* Thu Sep 30 2010 Denis Smirnov <mithraen@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.4-alt0.1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.4-alt0.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.6.4-alt0.1
initial build for Sisyphus
