%define ast_version %{get_version asterisk11-sources}

Name: asterisk11-devel-doc
Summary: Asterisk API documentation
Version: 11
Release: alt2
License: GPL
Group: System/Servers
Url: http://www.asterisk.org/

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildRequires(pre): asterisk11-sources

BuildPreReq: fonts-type1-urw
# Automatically added by buildreq on Tue May 11 2010 (-bb)
BuildRequires: asterisk11-sources dahdi-linux-headers doxygen flex fonts-type1-urw gcc-c++ graphviz gtk+-devel jackit-devel libSDL-devel libSDL_image-devel libalsa-devel libavcodec-devel libcurl-devel libfreetds-devel libgsm-devel libiksemel-devel libltdl7-devel liblua5-devel libmISDN-devel libncurses-devel libnet-snmp-devel libnewt-devel libopenr2-devel libpopt-devel libportaudio2-devel libpri-devel libpw1.11-devel libradiusclient-ng-devel libresample-devel libspandsp6-devel libspeex-devel libsqlite-devel libsqlite3-devel libss7-devel libunixODBC-devel libusb-compat-devel libvorbis-devel libvpb-devel libxml2-devel ncompress postgresql-devel wget

%description
Asterisk API documentation created by doxygen from sources

%prep
%setup -T -c

tar xfj %_usrsrc/asterisk11.tar.bz2

%build
./configure
%make_build progdocs

%files
%doc doc

%changelog
* Fri Nov 09 2012 Denis Smirnov <mithraen@altlinux.ru> 11-alt2
- Asterisk update

* Tue Sep 18 2012 Denis Smirnov <mithraen@altlinux.ru> 11-alt1
- first build for Sisyphus

