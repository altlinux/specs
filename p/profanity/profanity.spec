Name: profanity
Version: 0.4.2
Release: alt1
Summary: A console based jabber client inspired by irssi
Group: Networking/Instant messaging
License: GPLv3
Source: %name-%version.tar.gz
# wget -q -O- http://www.profanity.im/configuration.html | sed -n '/\[ui]/,/<\/code>/{s@ *</\?.*>@@g;p}' > profrc
Source1: profrc

# Automatically added by buildreq on Wed May 28 2014
# optimized out: glib2-devel libX11-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libncurses-devel libp11-kit libtinfo-devel pkg-config xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: libXScrnSaver-devel libcurl-devel libgnutls-devel libncursesw-devel libnotify-devel libssl-devel libstrophe-devel libxml2-devel libotr-devel

%description
%summary

%prep
%setup
touch NEWS README AUTHORS ChangeLog
cp %SOURCE1 profrc

%build
%autoreconf
%configure --with-libxml2 --enable-notifications --enable-otr

%make_build

%install
%makeinstall

%files
%doc README.md themes profrc
%_bindir/*
%_man1dir/*
%_datadir/%name

%changelog
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
