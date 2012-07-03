Name: f4l
Version: 0.2.1
Release: alt1cvs20071120

Summary: SWF designer and generator

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL v2
Group: Publishing
Url: http://f4l.sourceforge.net/

Source: http://prdownloads.sourceforge.net/f4l/%name-%version.tar.bz2
Source1: %name.desktop
Patch: %name.patch

# Automatically added by buildreq on Tue Nov 04 2008
BuildRequires: gcc-c++ libjpeg-devel libpng-devel libqt3-devel

%description
F4L is an open source development environment for Macromedia Flash,
a multi-platform format(swf/svg) widely used for web applications and
vector animation. Basically, you can make interactive eye candy for your
web site or any other purpose while maintai

%prep
%setup -q
#patch

%build
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh
export PATH=$QTDIR/bin:$PATH
#%__subst "s,mkspecs.*,mkspecs/linux-cxx/qmake.conf," Makefile
%__subst "s,/usr/share/qt3,%_qt3dir," Makefile
%make_build

%install
#makeinstall_std
install -D f4lm/f4lm %buildroot%_bindir/%name
install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
#%doc deneme.swf
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1cvs20071120
- build cvs version (thanks, Mandriva)

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- update buildreq, enable smp build
- add desktop file (fix bug #16114), thanks to Alexandre Prokoudine

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.2
- fixes for GCC4

* Sat Apr 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1
- new version 0.2.1 (with rpmrb script)

* Wed Dec 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

