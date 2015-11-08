Url: http://www.altlinux.org/Appliances
Name: appliance-build-asterisk
Summary: Packages required for build Asterisk
BuildArch: noarch
Version: 4.0.2
Release: alt4
License: GPL
Group: System/Base

Requires: asterisk11-devel
Requires: asterisk11-sources
Requires: asterisk-build-hacks
Requires: autoconf_2.60
Requires: automake_1.9
Requires: binutils-devel
Requires: dahdi-linux-headers
Requires: doxygen
Requires: flex
Requires: fonts-type1-urw
Requires: gcc-c++
Requires: graphviz
Requires: gtk+-devel
Requires: jackit-devel
Requires: libalsa-devel
Requires: libavcodec-devel
Requires: libbluez-devel
Requires: libcap-devel
Requires: libcorosync2-devel
Requires: libcurl-devel
Requires: libdb1-devel
Requires: libexpat-devel
Requires: libfreetds-devel
Requires: libgmime-devel
Requires: libgsm-devel
Requires: libgtk+2-devel
Requires: libical-devel
Requires: libidn-devel
Requires: libiksemel-devel
Requires: libilbc-devel
Requires: libjack-devel
Requires: libkeyutils-devel
Requires: libldap-devel
Requires: libltdl7-devel
Requires: libltdl-devel
Requires: liblua5-devel
Requires: libmISDN-devel
Requires: libmysqlclient-devel
Requires: libMySQL-devel
Requires: libncurses-devel
Requires: libneon-devel
Requires: libnet-snmp-devel
Requires: libnewt-devel
Requires: libnl-devel
Requires: libogg-devel
Requires: libopenr2-devel
Requires: libpopt-devel
Requires: libportaudio2-devel
Requires: libpq-devel
Requires: libpri-devel
Requires: libpw1.11-devel
Requires: libradiusclient-ng-devel
Requires: libreadline-devel
Requires: libresample-devel
Requires: librpm-devel
Requires: libsasl2-devel
Requires: libSDL-devel
Requires: libSDL_image-devel
Requires: libsensors3-devel
Requires: libspandsp6-devel
Requires: libspeex-devel
Requires: libsqlite3-devel
Requires: libsqlite-devel
Requires: libsrtp-devel
Requires: libss7-devel
Requires: libssl-devel
Requires: libstdc++-devel
Requires: libtiff-devel
Requires: libtinfo-devel
Requires: libtonezone-dahdi-devel
Requires: libunixODBC-devel
Requires: libusb-compat-devel
Requires: libvorbis-devel
Requires: libvpb-devel
Requires: libwrap-devel
Requires: libX11-devel
Requires: libxml2-devel
Requires: ncompress
Requires: openssl
Requires: perl-devel
Requires: postgresql-devel
Requires: rpm-build-gir
Requires: tcl-devel
Requires: texlive-base-bin
Requires: uw-imap-devel
Requires: wget
Requires: zlib-devel

%description
%summary

%files

%changelog
* Sun Nov 08 2015 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt4
- libsrtp -> libsrtp-devel

* Thu Aug 29 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt3
- libcorosync-devel -> libcorosync2-devel

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt2
- add Url tag

* Thu Apr 11 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt1
- script for autogenerate deps list

* Thu Apr 11 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt3
- use Asterisk 11 (last LTS release)

* Thu Apr 11 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- use Asterisk 1.8

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 4.0.1-alt1.1
- NMU: fixed MySQL client library dependency

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

