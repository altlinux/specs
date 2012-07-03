Name: stalonetray
Version: 0.7.6
Release: alt1

Summary: STand Alone TRAY (notification area) implementation
License: GPLv2+
Group: Graphical desktop/Other

Source: http://belnet.dl.sourceforge.net/sourceforge/stalonetray/stalonetray_0.7.6.tar.gz
Url: http://sourceforge.net/projects/stalonetray
Packager: Vitaly Kuzetsov <vitty@altlinux.ru>

BuildRequires: libSM-devel libXpm-devel xorg-cf-files

%description
The stalonetray is a STAnd-aLONE system TRAY (notification area).
It has minimal build and run-time dependencies: the Xlib only. The XEMBED
support is planned. Stalonetray runs under virtually any window manager.

%prep
%setup

%build
%configure
%make_build
make check

%install
%makeinstall_std

%files
%doc README
%doc NEWS
%doc AUTHORS
%doc ChangeLog
%doc stalonetrayrc.sample
%doc stalonetray.html
%doc stalonetray.xml
%_bindir/*
%_mandir/man*/*

%changelog
* Sat Apr 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.6-alt1
- initial for ALT

* Thu Dec 28 2006 Roman Dubtsov <busa_ru@users.sourceforge.net>
- new upstream release
* Tue Mar 28 2006 Roman Dubtsov <busa_ru@users.sourceforge.net>
- initial rpmization
