%define ast_version %{get_version asterisk11-sources}

Name: asterisk11-devel-doc
Summary: Asterisk API documentation
Version: 11
Release: alt19
License: GPL
Group: System/Servers
Url: http://www.asterisk.org/

#BuildArch: noarch

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
* Thu Dec 11 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt19
- Asterisk update

* Thu Nov 27 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt18
- Asterisk update

* Thu Sep 25 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt17
- Asterisk update

* Sat Sep 20 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt16
- Asterisk update

* Sat Jul 12 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt15
- Asterisk update

* Mon Jun 23 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt14
- Asterisk update

* Sat Jun 07 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt13
- Asterisk update

* Sat Apr 26 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt12
- Asterisk update

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt11
- Asterisk update

* Wed Jan 15 2014 Denis Smirnov <mithraen@altlinux.ru> 11-alt10
- Asterisk update

* Sun Sep 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt9
- Asterisk update

* Thu Aug 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt8
- Asterisk update

* Sun May 19 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt7
- Asterisk update

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt6
- Asterisk update

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt5
- Asterisk update

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt4
- Asterisk update

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 11-alt3
- Asterisk update

* Fri Nov 09 2012 Denis Smirnov <mithraen@altlinux.ru> 11-alt2
- Asterisk update

* Tue Sep 18 2012 Denis Smirnov <mithraen@altlinux.ru> 11-alt1
- first build for Sisyphus

