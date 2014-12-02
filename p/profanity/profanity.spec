Name: profanity
Version: 0.4.5
Release: alt1
Summary: A console based jabber client inspired by irssi
Group: Networking/Instant messaging
License: GPLv3
Source: %name-%version.tar.gz
# wget -q -O- http://www.profanity.im/configuration.html | sed -n '/\[ui]/,/<\/code>/{s@ *</\?.*>@@g;p}' > profrc
Source1: profrc
Url: http://www.profanity.im

BuildRequires: libcmocka-devel

# Automatically added by buildreq on Wed Nov 05 2014
# optimized out: glib2-devel libX11-devel libcloog-isl4 libgcrypt-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgpg-error-devel libncurses-devel libtinfo-devel pkg-config xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: libXScrnSaver-devel libcurl-devel libncursesw-devel libnotify-devel libotr-devel libssl-devel libstrophe-devel libxml2-devel

%description
%summary
  Supports XMPP chat services
  Command driven user interface
  MUC chat room support
  OTR message encryption
  Roster management
  Flexible resource and priority settings
  Desktop notifications
  Unicode support

%package X11
Group: Networking/Instant messaging
Summary: A console based jabber client inspired by irssi (X11 support)
Requires: %name = %version-%release
%description X11
XScrnSaver and notify support for %name

%prep
%setup
touch NEWS README AUTHORS ChangeLog
cp %SOURCE1 profrc.exmaple2

%build
%autoreconf
%configure --with-libxml2 --enable-notifications --enable-otr

%make_build
mv %name %name.app

make distclean
%configure --with-libxml2 --disable-notifications --enable-otr --without-xscreensaver
%make_build

%install
%makeinstall
install %name.app %buildroot%_bindir/%name.app

%check
%make check

%files
%doc themes profrc.example*
%_bindir/%name
%_man1dir/*
%_datadir/%name

%files X11
%_bindir/%name.app

%changelog
* Tue Dec 02 2014 Fr. Br. George <george@altlinux.ru> 0.4.5-alt1
- Autobuild version bump to 0.4.5

* Wed Nov 05 2014 Fr. Br. George <george@altlinux.ru> 0.4.4-alt2
- Separate X11-required package
- Provide check session

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 0.4.4-alt1
- Autobuild version bump to 0.4.4

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 0.4.3-alt1
- Autobuild version bump to 0.4.3
- Fix build

* Wed May 28 2014 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Autobuild version bump to 0.4.2
- Fix buildreq and rc obtaining spec cmdline

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.4.0-alt1
- Autobuild version bump to 0.4.0

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1

* Tue Aug 27 2013 Fr. Br. George <george@altlinux.ru> 0.3.0-alt2
- Add themes and sample config file

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Autobuild version bump to 0.3.0

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Autobuild version bump to 0.2.1
- Fix buildreq

* Thu Jan 10 2013 Fr. Br. George <george@altlinux.ru> 0.1.10-alt1
- Autobuild version bump to 0.1.10

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 0.1.9-alt1
- Autobuild version bump to 0.1.9 (initial build)
