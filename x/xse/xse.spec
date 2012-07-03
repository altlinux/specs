Name: xse
Version: 2.1
Release: alt4
Summary: Interface to XSendEvent
Summary(uk_UA.CP1251): ²םעונפויס המ XSendEvent
License: distributable
Group: System/X11
Source: xsendevent-%version.tar.gz
Patch: %name-%version-alt4.patch
URL: ftp://ftp.cs.rochester.edu/pub/packages/xsendevent/

# Automatically added by buildreq on Sat Jun 18 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel xorg-xproto-devel
BuildRequires: gccmakedep imake libXaw-devel libXext-devel libXpm-devel xorg-cf-files

%description
Xse provides an interface to XSendEvent(); sort of an inverse of
xev(1). It provides three interfaces depending on how it is invoked.


%prep
%setup
%patch -p3


%build
xmkmf -a -DHAVE_STRTOL
%make


%install
%make_install DESTDIR=%buildroot install install.man
install -D Ad2c/ad2c.man %buildroot%_man1dir/ad2c.1
install -D -m 755 Ad2c/ad2c.script %buildroot%_bindir/ad2c

%files
%doc README 
%_bindir/*
%config %_x11appconfdir/*
%_man1dir/*


%changelog
* Sat Jun 18 2011 Fr. Br. George <george@altlinux.ru> 2.1-alt4
- Resurrect from orphaned
- Add ad2c
* Tue Dec 02 2008 Led <led@altlinux.ru> 2.1-alt3
- updated BuildRequires

* Sun Nov 09 2008 Led <led@altlinux.ru> 2.1-alt2
- rebuild with libXaw.so.7
- cleaned up spec
- updated BuildRequires

* Thu Jun 01 2006 Led <led@altlinux.ru> 2.1-alt1
- initial build
