Name: profanity
# configure.ac:AC_INIT([profanity], [0.1.10], [boothj5web@gmail.com])
Version: 0.2.1
Release: alt1
Summary: A console based jabber client inspired by irssi
Group: Networking/Instant messaging
License: GPLv3
Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Apr 01 2013
# optimized out: glib2-devel libX11-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libncurses-devel libtinfo-devel pkg-config xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: libXScrnSaver-devel libcurl-devel libncursesw-devel libnotify-devel libssl-devel libstrophe-devel libxml2-devel

%description
%summary

%prep
%setup
touch NEWS README AUTHORS ChangeLog

%build
%autoreconf
%configure --with-libxml2
%make_build

%install
%makeinstall

%files
%doc README.md
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Autobuild version bump to 0.2.1
- Fix buildreq

* Thu Jan 10 2013 Fr. Br. George <george@altlinux.ru> 0.1.10-alt1
- Autobuild version bump to 0.1.10

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 0.1.9-alt1
- Autobuild version bump to 0.1.9 (initial build)
