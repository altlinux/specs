Name: stalonetray
Version: 0.8.2
Release: alt1

Summary: STand Alone TRAY (notification area) implementation
License: GPLv2+
Group: Graphical desktop/Other

Source: %name-%version.tar.gz
Url: http://stalonetray.sourceforge.net

BuildRequires: libSM-devel libXpm-devel xorg-cf-files

%description
The stalonetray is a STAnd-aLONE system tray(notification area). It has
minimal build and run-time dependencies: the Xlib only. Beta quality
XEMBED support. Stalonetray runs under virtually any window manager.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%check
make check

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
* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Autobuild version bump to 0.8.2

* Sun Jul 21 2013 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Autobuild version bump to 0.8.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Apr 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.6-alt1
- initial for ALT

* Thu Dec 28 2006 Roman Dubtsov <busa_ru@users.sourceforge.net>
- new upstream release
* Tue Mar 28 2006 Roman Dubtsov <busa_ru@users.sourceforge.net>
- initial rpmization
