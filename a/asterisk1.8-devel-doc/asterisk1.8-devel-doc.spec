%define ast_version %{get_version asterisk1.8-sources}

Name: asterisk1.8-devel-doc
Summary: Asterisk API documentation
Version: 1.8
Release: alt18
License: GPL
Group: System/Servers
Url: http://www.asterisk.org/

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildRequires(pre): asterisk1.8-sources

BuildPreReq: fonts-type1-urw
# Automatically added by buildreq on Tue May 11 2010 (-bb)
BuildRequires: asterisk1.8-sources dahdi-linux-headers doxygen flex fonts-type1-urw gcc-c++ graphviz gtk+-devel jackit-devel libSDL-devel libSDL_image-devel libalsa-devel libavcodec-devel libcurl-devel libfreetds-devel libgsm-devel libiksemel-devel libltdl7-devel liblua5-devel libmISDN-devel libncurses-devel libnet-snmp-devel libnewt-devel libopenh323_1.19-devel libopenr2-devel libpopt-devel libportaudio2-devel libpri-devel libpw1.11-devel libradiusclient-ng-devel libresample-devel libspandsp6-devel libspeex-devel libsqlite-devel libsqlite3-devel libss7-devel libunixODBC-devel libusb-compat-devel libvorbis-devel libvpb-devel libxml2-devel ncompress postgresql-devel wget

%description
Asterisk API documentation created by doxygen from sources

%prep
%setup -T -c

tar xfj %_usrsrc/asterisk1.8.tar.bz2

%build
./configure
%make_build progdocs

%files
%doc doc

%changelog
* Sat May 05 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt18
- Asterisk update

* Thu Feb 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt17
- Asterisk update

* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt16
- Asterisk update

* Sat Dec 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt15
- Asterisk update

* Wed Oct 26 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt14
- Asterisk update

* Wed Oct 05 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt13
- Asterisk update

* Fri Sep 02 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt12
- Asterisk update

* Sun Feb 27 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt11
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt10
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt9
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt8
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt7
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt6
- Asterisk update

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt5
- Asterisk update

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt4
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt3
- Asterisk update

* Tue Jul 27 2010 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt2
- Asterisk update

* Mon Jul 26 2010 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt1
- first build for Sisyphus
