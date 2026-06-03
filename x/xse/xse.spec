Name: xse
Version: 2.1
Release: alt6
Summary: Interface to XSendEvent
License: BSD
Group: System/X11
Source: xsendevent-%version.tar.gz
Patch: %name-%version-alt4.patch
URL: ftp://ftp.cs.rochester.edu/pub/packages/xsendevent/

# Automatically added by buildreq on Sat Jun 18 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel xorg-xproto-devel
BuildRequires: gccmakedep imake libXaw-devel libXext-devel libXpm-devel xorg-cf-files gcc14

%description
Xse provides an interface to XSendEvent(); sort of an inverse of
xev(1). It provides three interfaces depending on how it is invoked.


%prep
%set_gcc_version 14
%setup
%patch -p3
for f in `grep -sl dprintf *.*`; do sed -i 's/dprintf/DPrintf/g' $f; done

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
* Wed May 27 2026 Fr. Br. George <george@altlinux.org> 2.1-alt6
- Freeze gcc14 buildreq

* Wed May 27 2026 Fr. Br. George <george@altlinux.org> 2.1-alt5

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 2.1-alt5
- Fix dprintf redefinition

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
