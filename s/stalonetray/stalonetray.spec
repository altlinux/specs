Name: stalonetray
Version: 0.8.4
Release: alt1

Summary: STand Alone TRAY (notification area) implementation
License: GPLv2+
Group: Graphical desktop/Other

Source: %name-%version.tar.gz
Url: https://kolbusa.github.io/stalonetray/

# Automatically added by buildreq on Sun Jan 16 2022
# optimized out: docbook-dtds glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libgpg-error perl python3-base sh4 xml-common xorg-proto-devel
BuildRequires: docbook-style-xsl libICE-devel libXpm-devel python3 xsltproc

BuildRequires: libSM-devel 

%description
The stalonetray is a STAnd-aLONE system tray(notification area). It has
minimal build and run-time dependencies: the Xlib only. Beta quality
XEMBED support. Stalonetray runs under virtually any window manager.

%prep
%setup

%build
%autoreconf
%configure
%make_build dist

%install
%makeinstall_std

%check
make check

%files
%doc README.md
%doc NEWS
%doc AUTHORS
%doc stalonetrayrc.sample
%doc stalonetray.html
%doc stalonetray.xml
%_bindir/*
%_mandir/man*/*

%changelog
* Sun Jan 16 2022 Fr. Br. George <george@altlinux.ru> 0.8.4-alt1
- Autobuild version bump to 0.8.4
- Upstream switch to GH

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.8.3-alt1
- Autobuild version bump to 0.8.3

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
