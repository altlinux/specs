%define ast_version %{get_version asterisk1.6.2-sources}

Name: asterisk1.6.2-devel-doc
Summary: Asterisk API documentation
Version: 1.6.2
Release: alt19
License: GPL
Group: System/Servers
Url: http://www.asterisk.org/

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildRequires(pre): asterisk1.6.2-sources

BuildPreReq: fonts-type1-urw
# Automatically added by buildreq on Tue May 11 2010 (-bb)
BuildRequires: asterisk1.6.2-sources dahdi-linux-headers doxygen flex fonts-type1-urw gcc-c++ graphviz gtk+-devel jackit-devel libSDL-devel libSDL_image-devel libalsa-devel libavcodec-devel libcurl-devel libfreetds-devel libgsm-devel libiksemel-devel libltdl7-devel liblua5-devel libmISDN-devel libncurses-devel libnet-snmp-devel libnewt-devel libopenh323_1.19-devel libopenr2-devel libpopt-devel libportaudio2-devel libpri-devel libpw1.11-devel libradiusclient-ng-devel libresample-devel libspandsp6-devel libspeex-devel libsqlite-devel libsqlite3-devel libss7-devel libunixODBC-devel libusb-compat-devel libvorbis-devel libvpb-devel libxml2-devel ncompress postgresql-devel wget

%description
Asterisk API documentation created by doxygen from sources

%prep
%setup -T -c

tar xfj %_usrsrc/asterisk1.6.2.tar.bz2

%build
./configure
%make_build progdocs

%files
%doc doc

%changelog
* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt19
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt18
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt17
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt16
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt15
- Asterisk update

* Mon Dec 20 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt14
- Asterisk update

* Sun Dec 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt13
- Asterisk update

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt12
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt11
- Asterisk update

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt10
- Asterisk update

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt9
- Asterisk update

* Fri Sep 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt8
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt7
- Asterisk update

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt6
- Asterisk update

* Sat Jul 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt5
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt4
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt3
- Asterisk update

* Tue May 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt2
- update build requires

* Tue May 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt1
- first build for Sisyphus
