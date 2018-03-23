Name: bitlbee-facebook
Version: 1.1.2
Release: alt1.g553593d
Group: Networking/IRC
License: GPLv2
Url: https://wiki.bitlbee.org/HowtoFacebookMQTT
Summary: MQTT (Facebook) plugin for bitlbee
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: bitlbee-devel libjson-glib-devel zlib-devel

%description
As an alternative to the now (mostly-)defunct XMPP service provided by
facebook, jgeboski (who also wrote bitlbee-steam) made a new plugin based on
the facebook messenger mobile client (which uses a protocol called MQTT).  It
also happens to work much better than the XMPP service ever did, and supports
groupchats.

%prep
%setup
%patch -p1

%build
%autoreconf
./configure \
    --with-plugindir=%_libdir/bitlbee
%make_build

%install
%makeinstall DESTDIR=%buildroot libdir=%_libdir/bitlbee

%files
%doc README NEWS ChangeLog COPYING AUTHORS
%_libdir/bitlbee/facebook.so

%changelog
* Fri Mar 23 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt1.g553593d
- Updated to 1.1.2 553593d GIT.

* Tue Sep 15 2015 L.A. Kostis <lakostis@altlinux.ru> 0.1.0-alt1
- Initial build for ALTLinux.
