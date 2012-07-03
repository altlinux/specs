Name: dhcdrop
Version: 0.5
Release: alt1
Summary: Drop dhcp offers from illegitimate dhcp server.
Group: System/Servers
License: GPL
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://www.netpatch.ru/projects/dhcdrop/
Source0: http://www.netpatch.ru/projects/dhcdrop/%name-%version.tar.bz2

# Automatically added by buildreq on Tue Jul 14 2009 (-bi)
BuildRequires: libpcap-devel

%description
Drop dhcp offers from illegitimate dhcp server

%prep
%setup -q

%build
%configure --bindir=%_sbindir --enable-static=no

%make

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL
%_sbindir/%name
%_man8dir/*
%_mandir/ru/man8/*

%changelog
* Wed Aug 19 2009 Andrew Clark <andyc@altlinux.org> 0.5-alt1
- initial build for ALT.

