#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: asterisk11
Summary: Open source PBX
Version: 11.20.0
Release: alt1
License: GPL
Group: System/Servers
%if_with corosync
BuildRequires: libcorosync2-devel
%endif
BuildRequires: dahdi-linux-headers flex gcc-c++ graphviz libSDL_image-devel libalsa-devel libavcodec-devel libbluez-devel libcap-devel libcurl-devel libfreetds-devel libgsm-devel libgtk+2-devel libical-devel libiksemel-devel libilbc-devel libjack-devel libkeyutils-devel libltdl7-devel liblua5-devel libmISDN-devel libmysqlclient-devel libncurses-devel libneon-devel libnet-snmp-devel libnewt-devel libopenr2-devel libpopt-devel libportaudio2-devel libpri-devel libpw1.11-devel libradiusclient-ng-devel libresample-devel libsasl2-devel libspandsp6-devel libspeex-devel libsqlite-devel libsqlite3-devel libsrtp libss7-devel libtonezone-dahdi-devel libunixODBC-devel libusb-compat-devel libvorbis-devel libvpb-devel libxml2-devel ncompress openssl postgresql-devel rpm-build-gir texlive-base-bin wget zlib-devel
BuildRequires: libtiff-devel
BuildRequires: libiksemel-devel
BuildRequires: libradiusclient-ng-devel
BuildRequires: libdb1-devel
BuildRequires: libilbc-devel
%if_with ss7
BuildPreReq: libss7-devel
%endif
BuildPreReq: libkeyutils-devel
BuildPreReq: libical-devel
BuildPreReq: libbluez-devel
BuildPreReq: libcap-devel
BuildPreReq: libneon-devel
BuildPreReq: libsrtp-devel
BuildPreReq: libnl-devel libsensors3-devel
%if_with hoard
BuildPreReq: libhoard-devel
%endif
BuildPreReq: asterisk-build-hacks
BuildPreReq: libresample-devel
BuildPreReq: libvpb-devel libsqlite3-devel libsqlite-devel libfreetds-devel
BuildPreReq: libgmime-devel
BuildPreReq: libportaudio2-devel libavcodec-devel
BuildPreReq: libSDL_image-devel libSDL-devel libX11-devel libgtk+2-devel
BuildPreReq: libxml2-devel
BuildPreReq: binutils-devel
BuildPreReq: libuuid-devel
BuildPreReq: libopenr2-devel
BuildPreReq: libusb-compat-devel
BuildPreReq: uw-imap-devel
BuildPreReq: autoconf_2.60 automake_1.9
BuildPreReq: libgsm-devel
BuildPreReq: libssl-devel
BuildPreReq: gcc-c++ zlib-devel libstdc++-devel
BuildPreReq: libalsa-devel
BuildPreReq: libidn-devel libncurses-devel libnewt-devel libtinfo-devel
BuildPreReq: libogg-devel libvorbis-devel
BuildPreReq: libpopt-devel
BuildPreReq: libreadline-devel
BuildPreReq: libssl-devel libstdc++-devel libtiff-devel libtinfo-devel libunixODBC-devel
BuildPreReq: tcl-devel
BuildPreReq: libss7-devel
BuildPreReq: libtonezone-dahdi-devel
BuildPreReq: dahdi-linux-headers
BuildPreReq: libpri-devel
BuildRequires: libmISDN-devel
BuildPreReq: libspeex-devel
BuildPreReq: libspeexdsp-devel
BuildRequires: libcurl-devel
BuildPreReq: libspandsp6-devel
BuildRequires: libexpat-devel
BuildPreReq: jackit-devel
BuildPreReq: libldap-devel
BuildRequires: libMySQL-devel
BuildPreReq: libunixODBC-devel libltdl-devel
BuildPreReq: liblua5-devel
BuildPreReq: postgresql-devel libpq-devel
BuildPreReq: librpm-devel libnet-snmp-devel libwrap-devel perl-devel
%add_verify_elf_skiplist %_libdir/libasteriskssl11.so.1
%def_with debug
%def_enable debug
%def_without            vpb
%def_without		hoard
%def_without 		addons
%def_without 		corosync
%def_with			snmp
%def_with			speex
%def_with			curl
%def_with			postgresql
%def_with			misdn
%def_with			odbc
%def_with			ss7
%def_with			ldap
%def_with   			jack
%def_with			dahdi
%if_with corosync
%endif
%if_with ss7
%endif
%if_with hoard
%endif
%set_autoconf_version 2.60
%define modules_dir	%_libdir/asterisk/%version/modules
%define agi_dir     /usr/lib/asterisk/agi-bin
%define spandsp		0.0.5-alt3.pre4
%define astmodule() \
%attr(0440,root,_asterisk) %modules_dir/%1.so
%nil
%define astsample() \
%_docdir/%name-%version/samples/%1.conf
%nil
Url: http://www.asterisk.org/
Requires: asterisk-files-all
Requires: asterisk-initscript
Requires(pre): asterisk-initscript
Requires: asterisk-base-configs
Requires(pre): asterisk-base >= 0.67-alt1
Requires(pre): coreutils
Requires: pbx-streamplayer
Requires: pbx-stereorize
Source: %name-%version.tar
Source2: %name-altlinux.tar
Source3: %name.watch
Patch: %name-%version.patch
Packager: Denis Smirnov <mithraen@altlinux.ru>

%package -n aelparse11
Summary: Asterisk AEL2 parser
Group: %group
Requires: asterisk11-common

%description -n aelparse11
aelparse utility needed for converting from AEL2 config file to
old extensions.conf format.


%package ael
Summary: AEL support for Asterisk
Group: System/Servers
Requires(pre): %name = %version-%release

%description ael
AEL support for Asterisk

%if_with addons
%package app_conference
Summary: Conference application for SeirosPBX
Group: System/Servers
Requires: %name = %version-%release
Requires(pre): asterisk-base

%description app_conference
Conference application for SeirosPBX

%endif

%package app_minivm
Summary: mini voicemail application
Group: %group
Requires: %name = %version-%release
Requires: %name-res_crypto = %version-%release

%description app_minivm
mini voicemail application


%package app_voicemail
Summary: Asterisk voicemail module
Group: %group
Requires: %name = %version-%release

%description app_voicemail
VoiceMail for Asterisk


%package calendar
Summary: Calendar support for Asterisk
Group: %group
Requires: %name = %version-%release

%description calendar
Calendar support for Asterisk

%package cdr_radius
Summary: Asterisk radius CDR support
Group: %group
Requires: %name = %version-%release

%description cdr_radius
Asterisk radius CDR support


%package cdr_sqlite
Summary: Asterisk sqlite CDR support
Group: %group
Requires: %name = %version-%release

%description cdr_sqlite
Asterisk sqlite CDR support

%package cdr_tds
Summary: Asterisk FreeTDS CDR support
Group: %group
Requires: %name = %version-%release

%description cdr_tds
Asterisk FreeTDS CDR support

%package chan_alsa
Summary: Alsa channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_alsa
Alsa channel module for Asterisk

%package chan_console
Summary: Console channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_console
Console channel module for Asterisk

%if_with dahdi
%package chan_dahdi
Summary: ZAP channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_dahdi
ZAP channel module for Asterisk
%endif

%package chan_h323
Summary: H.323 channel support for Asterisk
Group: System/Servers
Requires: %name = %version

%description chan_h323
H.323 channel support for Asterisk PBX


%package chan_iax2
Summary: IAX2 channel module for Asterisk
Group: %group
Requires: %name = %version-%release
Requires: %name-res_crypto = %version-%release

%description chan_iax2
IAX2 channel module for Asterisk


%if_with misdn
%package chan_misdn
Summary: mISDN channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_misdn
mISDN channel module for Asterisk

%endif

%package chan_oss
Summary: OSS channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_oss
OSS channel module for Asterisk

%package chan_sip
Summary: SIP channel module for Asterisk
Group: %group
Requires: %name = %version-%release
Requires: %name-res_crypto = %version-%release

%description chan_sip
SIP channel module for Asterisk


%if_with vpb
%package chan_vpb
Summary: Voicetronix API channel driver
Group: %group
Requires: %name = %version-%release

%description chan_vpb
Voicetronix API channel driver
%endif

%package codec_gsm
Summary: Asterisk GSM 6.10 codec support
Group: %group
Requires: %name = %version-%release

%description codec_gsm
Asterisk GSM 6.10 codec support


%package codec_ilbc
Summary: iLBC codec support for Asterisk
Group: %group
Requires: %name = %version-%release

%description codec_ilbc
iLBC is very low bitrate codec, that can be effectivly used for IP-telephony


%if_with speex
%package codec_speex
Summary: SPEEX codec support for Asterisk
Group: %group
Requires: %name = %version-%release

%description codec_speex
SPEEX codec support for Asterisk PBX

%endif

%package common
Summary: Asterisk %version
Group: %group
BuildArch: noarch

%description common
Asterisk %version

%package complete
Summary: This virtual package requires all Asterisk subpackages
Group: %group
BuildArch: noarch
Requires: aelparse11 = %version-%release
Requires: %name-ael = %version-%release
Requires: %name-fax = %version-%release
Requires: %name-app_voicemail = %version-%release
Requires: %name-calendar = %version-%release
%if_with corosync
Requires: %name-corosync = %version-%release
%endif
Requires: %name-cdr_radius = %version-%release
Requires: %name-chan_iax2 = %version-%release
Requires: %name-jabber = %version-%release
%if_with misdn
Requires: %name-chan_misdn = %version-%release
%endif
Requires: %name-chan_sip = %version-%release
%if_with dahdi
Requires: %name-chan_dahdi = %version-%release
%endif
Requires: %name-codec_gsm = %version-%release
Requires: %name-codec_ilbc = %version-%release
Requires: %name-codec_speex = %version-%release
Requires: %name-curl = %version-%release
Requires: %name-devel = %version-%release
Requires: %name-docs = %version-%release
Requires: %name-format_ogg = %version-%release
Requires: %name-format_mp3 = %version-%release
Requires: %name-httpd = %version-%release
%if_with odbc
Requires: %name-odbc = %version-%release
%endif
Requires: %name-pgsql = %version-%release
%if_with snmp
Requires: %name-res_snmp = %version-%release
%endif
Requires: %name-sms = %version-%release
Requires: %name-chan_h323 = %version-%release
Requires: %name-mysql = %version-%release
Requires: %name-fax = %version-%release
Requires: %name-sources = %version-%release
Requires: %name-app_minivm   = %version-%release
Requires: %name-cdr_sqlite   = %version-%release
Requires: %name-sqlite3  = %version-%release
Requires: %name-cdr_tds      = %version-%release
Requires: %name-chan_console = %version-%release
%if_with vpb
Requires: %name-chan_vpb     = %version-%release
%endif
Requires: %name-jack         = %version-%release
Requires: %name-ldap         = %version-%release
Requires: %name-chan_alsa    = %version-%release
Requires: %name-chan_oss     = %version-%release
Requires: %name-meetme       = %version-%release
Requires: %name-pbx_lua      = %version-%release
Requires: conf2ael11
Requires: pbx-agi-samples
Requires: pbx-utils-all

%description complete
This virtual package requires all Asterisk subpackages

%if_with corosync
%package corosync
Summary: Device state and MWI clustering
Group: %group
Requires: %name = %version-%release

%description corosync
Device state and MWI clustering
%endif

%if_with curl
%package curl
Summary: CURL support for Asterisk
Group: %group
Requires: %name = %version-%release

%description curl
CURL support for Asterisk

%endif

%package devel
Summary: C header files for Asterisk modules development
Group: %group
Requires: asterisk11-common

%description devel
C header files for Asterisk modules development

%package docs
Summary: asterisk documentation
Group: System/Servers
BuildArch: noarch
Requires: asterisk11-common

%description docs
Asterisk documentation and sample files


%package fax
Summary: FAX send/receive/autodetect support for Asterisk
Group: %group
Requires: %name = %version-%release
Requires(pre): asterisk-base

%description fax
FAX send/receive/autodetect support for Asterisk


%package format_mp3
Summary: MP3 format for Asterisk
Group: System/Servers
PreReq: %name = %version-%release

%description format_mp3
MP3 format for Asterisk


%package format_ogg
Summary: format_ogg_vorbis support for Asterisk
Group: %group
Requires: %name = %version-%release

%description format_ogg
Ogg Vorbis support for MusicOnHold in Asterisk


%package httpd
Summary: Asterisk internal static httpd data
Group: System/Servers
BuildArch: noarch
Requires: %name = %version-%release

%description httpd
Asterisk internal static httpd data for monitoring


%package jabber
Summary: Jingle and Google Talk channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description jabber
Jingle and Google Talk channel module for Asterisk

%if_with jack
%package jack
Summary: Asterisk JACK support
Group: %group
Requires: %name = %version-%release

%description jack
Asterisk JACK support

%endif

%if_with ldap
%package ldap
Summary: Asterisk LDAP support
Group: %group
Requires: %name = %version-%release

%description ldap
Asterisk LDAP support

%endif

%if_with dahdi
%package meetme
Summary: IP PBX MeetMe conference bridge
Group: %group
Requires: %name = %version-%release

%description meetme
IP PBX MeetMe conference bridge
%endif

%package mysql
Summary: Open source PBX
Group: System/Servers
PreReq: %name = %version-%release

%description mysql
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standart-based telephony
equipment using relatively inexpensive hardware.


%if_with odbc
%package odbc
Summary: ODBC logging and config modules for Asterisk
Group: %group
Requires: %name = %version-%release

%description odbc
ODBC logging and config modules for Asterisk PBX

%endif

%package pbx_lua
Summary: LUA support for Asterisk
Group: System/Servers
Requires(pre): %name = %version-%release

%description pbx_lua
LUA support for Asterisk

%if_with postgresql
%package pgsql
Summary: PostgreSQL logging module for Asterisk
Group: %group
Requires: %name = %version-%release

%description pgsql
PostgresSQL logging module for Asterisk

%endif

%package res_crypto
Summary: OpenSSL support for Asterisk (crypto)
Group: %group
Requires: %name = %version-%release
Requires: pbx-astgenkey

%description res_crypto
res_crypto used by chan_sip and chan_iax2 for crypto support


%if_with snmp
%package res_snmp
Summary: SNMP support for Asterisk
Group: %group
Requires: %name = %version-%release

%description res_snmp
SNMP support for Asterisk

%endif

%package sms
Summary: SMS over E1 support for Asterisk
Group: System/Servers
Requires: %name = %version-%release
Requires: pbx-smsq

%description sms
SMS over E1 support for Asterisk


%package sources
Summary: Open source PBX sources
Group: System/Servers
Requires: asterisk11-common

%description sources
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standard-based telephony
equipment using relatively inexpensive hardware.


%package sqlite3
Summary: Asterisk sqlite3 support
Group: %group
Requires: %name = %version-%release

%description sqlite3
Asterisk sqlite3 support

%package -n conf2ael11
Summary: extensions.conf -> ael2 converter
Group: %group
Requires: asterisk11-common

%description -n conf2ael11
extensions.conf -> ael2 converter


%package -n libasteriskssl11
Summary: Asterisk SSL functions
Group: %group
Conflicts: libasteriskssl < %version-%release
Conflicts: libasteriskssl > %version-%release
Provides: libasteriskssl = %version-%release

%description -n libasteriskssl11
Asterisk SSL functions

%description
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standard-based telephony
equipment using relatively inexpensive hardware.


%prep
%setup -c -T
%setup -a2 -D
%patch -p1
tar cjf ../%name.tar.bz2 .
sed -i "s!ASTMODDIR[[:space:]]*=.*!ASTMODDIR=%modules_dir!" makeopts.in
sed -i "s!MODULES_DIR=.*!MODULES_DIR=%modules_dir!" Makefile
sed -i "s!AGI_DIR=.*!AGI_DIR=%agi_dir!" Makefile
sed -i 's!^[[:space:]]*ASTVARRUNDIR=.*!ASTVARRUNDIR=$(INSTALL_PREFIX)/var/run/asterisk!' Makefile
sed -i 's!uname -m!echo %_target_cpu!g' */Makefile */*/Makefile Makefile
rm -f */.*.moduleinfo
rm -f */.*.makeopts
rm -f menuselect-tree
rm -f */.moduleinfo
rm -f */.makeopts

%build
export CC=gcc
%autoreconf -I autoconf
./configure --build=%_build_alias --host=%_host_alias \
	--libdir=%_libdir \
%if_with hoard
    --with-hoard=/usr/include/hoard \
%endif
	--enable-dev-mode
make -C menuselect libdir=%_libdir
make menuselect.makeopts \
    libdir=%_libdir ||:
menuselect/menuselect  \
    --enable DETECT_DEADLOCKS \
    --enable DO_CRASH \
    --enable BETTER_BACKTRACES \
    --enable G711_NEW_ALGORITHM \
    --enable res_pktccops \
    --enable app_mysql \
    --enable app_saycountpl \
    --enable app_dahdibarge \
    --enable app_fax \
    --enable app_meetme \
    --enable app_readfile \
    --enable app_saycounted \
    --enable app_setcallerid \
    --enable cdr_mysql \
    --enable cdr_sqlite \
    --enable chan_usbradio \
    --enable chan_gtalk \
    --enable chan_jingle \
    --enable chan_mobile \
    --enable chan_ooh323 \
    --enable chan_mgcp \
    --enable chan_vpb \
    --enable codec_ilbc \
    --enable res_jabber \
    --enable res_rtp_asterisk \
    --enable res_rtp_multicast \
    --enable res_config_mysql \
    --disable chan_h323 \
    --enable format_mp3 \
    --enable aelparse \
    --enable conf2ael \
    --enable chan_misdn \
    --disable CORE-SOUNDS-EN-GSM \
    --disable MENUSELECT_MOH
%make_build libdir=%_libdir NOISY_BUILD=yes ||:
%make_build libdir=%_libdir NOISY_BUILD=yes ||:
make libdir=%_libdir NOISY_BUILD=yes

%install
mkdir -p %buildroot%_docdir/%name-%version
install -D -m644 CREDITS UPGRADE.txt BUGS CHANGES README sample.call %buildroot%_docdir/%name-%version/
%makeinstall_std datafiles
mkdir -p %buildroot%_docdir/%name-%version      \
	%buildroot/%_datadir/asterisk/sounds   \
	%buildroot/var/log/asterisk/cdr-csv    \
	%buildroot/var/log/asterisk/cdr-custom \
	%buildroot/var/spool/asterisk/outgoing \
	%buildroot/var/spool/asterisk/fax \
	%buildroot/var/run/asterisk \
	%buildroot/var/lib/asterisk \
	%buildroot%_docdir/%name-%version/samples/
cp configs/*.sample %buildroot%_docdir/%name-%version/samples/
rename '.sample' '' %buildroot%_docdir/%name-%version/samples//*.sample
install -m 755 -D utils/aelparse %buildroot%_sbindir/aelparse-%version
rm -f %buildroot%_sbindir/aelparse
install -D -m644 ../%name.tar.bz2 %buildroot%_usrsrc/%name.tar.bz2
cp -a doc/* %buildroot%_docdir/%name-%version/
cp altlinux/README.ALT %buildroot%_docdir/%name-%version/
mv %buildroot/var/lib/asterisk/static-http %buildroot%_datadir/asterisk/static-http-%version
mv %buildroot%_sbindir/asterisk   %buildroot%_sbindir/asterisk-%version
mv %buildroot%_sbindir/rasterisk  %buildroot%_sbindir/rasterisk-%version
mv %buildroot%_man8dir/asterisk.8 %buildroot%_man8dir/asterisk-%version.8
mv %buildroot%_sbindir/conf2ael   %buildroot%_sbindir/conf2ael-%version
mkdir -p %buildroot%_altdir
sed "s/@version@/%version/g" < altlinux/alternatives-asterisk > %buildroot%_altdir/asterisk-%version
sed "s/@version@/%version/g" < altlinux/alternatives-aelparse > %buildroot%_altdir/aelparse-%version
sed "s/@version@/%version/g" < altlinux/alternatives-conf2ael > %buildroot%_altdir/conf2ael-%version
mkdir -p %buildroot%_includedir/asterisk-%version
mv %buildroot%_includedir/asterisk   %buildroot%_includedir/asterisk-%version/asterisk
mv %buildroot%_includedir/asterisk.h %buildroot%_includedir/asterisk-%version/asterisk.h
mkdir -p %buildroot/usr/share/asterisk/documentation/11
mv %buildroot/var/lib/asterisk/documentation/*.xml %buildroot/usr/share/asterisk/documentation/11/
mv %buildroot/var/lib/asterisk/documentation/*.dtd %buildroot/usr/share/asterisk/documentation/11/
ln -sf libasteriskssl11.so.1 %buildroot%_libdir/libasteriskssl11.so

%preun
%preun_service asterisk

%post
%post_service asterisk

%files
%_altdir/asterisk-%version
%dir /usr/share/asterisk/documentation/11
/usr/share/asterisk/documentation/11/appdocsxml.dtd
/usr/share/asterisk/documentation/11/core-en_US.xml
%exclude /var/lib/asterisk/images/asterisk-intro.jpg
%exclude /var/lib/asterisk/images/kpad2.jpg
%exclude %_docdir/%name-%version/core-en_US.xml
%exclude %_docdir/%name-%version/appdocsxml.dtd
%exclude /usr/sbin/astcanary
%dir %_docdir/%name-%version/samples
%_docdir/%name-%version/README.ALT
%astsample cli
%astmodule res_stun_monitor
%astsample res_stun_monitor
%astmodule chan_skinny
%astsample skinny
%astmodule func_audiohookinherit
%astmodule app_readexten
%astmodule app_waituntil
%astmodule chan_unistim
%astsample unistim
%astmodule codec_resample
%astmodule func_blacklist
%astmodule func_devstate
%astmodule func_dialgroup
%astmodule func_dialplan
%astmodule func_extstate
%astmodule func_iconv
%astmodule func_lock
%astmodule func_sysinfo
%astmodule func_version
%astmodule func_vmcount
%astmodule func_volume
%astmodule res_ael_share
%astmodule res_phoneprov
%astmodule res_realtime
%astmodule app_zapateller
%astmodule app_chanspy
%astmodule pbx_dundi
%astmodule format_g723
%astmodule app_amd
%astmodule app_queue
%astmodule chan_agent
%astmodule codec_ulaw
%astmodule codec_a_mu
%astmodule codec_alaw
%astmodule codec_g722
%astmodule format_pcm
%astmodule app_speech_utils
%astmodule res_speech
%astmodule res_smdi
%astmodule app_followme
%astmodule app_adsiprog
%astmodule app_festival
%astmodule app_image
%astmodule chan_phone
%astmodule app_dictate
%astmodule app_dumpchan
%astmodule app_directed_pickup
%astmodule app_externalivr
%astmodule app_mixmonitor
%astmodule app_readfile
%astmodule app_stack
%astmodule app_waitforsilence
%astmodule app_while
%astmodule app_morsecode
%astmodule func_callerid
%astmodule func_global
%astmodule func_enum
%astmodule func_uri
%astmodule func_rand
%astmodule func_base64
%astmodule func_channel
%astmodule func_cut
%astmodule func_db
%astmodule func_env
%astmodule func_groupcount
%astmodule func_logic
%astmodule func_math
%astmodule func_shell
%astmodule func_md5
%astmodule func_sha1
%astmodule func_realtime
%astmodule func_strings
%astmodule func_timeout
%astmodule func_module
%astmodule app_alarmreceiver
%astmodule app_authenticate
%astmodule app_cdr
%astmodule app_chanisavail
%astmodule app_controlplayback
%astmodule app_db
%astmodule app_directory
%astmodule app_disa
%astmodule app_echo
%astmodule app_exec
%astmodule app_getcpeid
%astmodule app_macro
%astmodule app_milliwatt
%astmodule app_channelredirect
%astmodule app_parkandannounce
%astmodule app_playback
%astmodule app_privacy
%astmodule app_read
%astmodule app_record
%astmodule app_sayunixtime
%astmodule app_senddtmf
%astmodule app_sendtext
%astmodule app_setcallerid
%astmodule app_softhangup
%astmodule app_system
%astmodule app_talkdetect
%astmodule app_test
%astmodule app_transfer
%astmodule app_url
%astmodule app_userevent
%astmodule app_verbose
%astmodule app_waitforring
%astmodule cdr_csv
%astmodule cdr_custom
%astmodule cdr_manager
%astmodule func_cdr
%astmodule app_forkcdr
%astmodule codec_adpcm
%astmodule format_vox
%astmodule codec_g726
%astmodule format_g726
%astmodule codec_lpc10
%astmodule format_h263
%astmodule format_h264
%astmodule format_jpeg
%astmodule pbx_loopback
%astmodule pbx_realtime
%astmodule res_adsi
%astmodule res_monitor
%astmodule res_convert
%astmodule res_clioriginate
%astmodule app_dial
%astmodule chan_local
%astmodule format_g729
%astmodule format_g719
%astmodule format_sln
%astmodule format_wav
%astmodule pbx_config
%astmodule pbx_spool
%astmodule res_agi
%astmodule res_musiconhold
%astmodule res_limit
%exclude %astmodule app_mp3
%if_with addons
%astmodule app_devstate
%astmodule app_pickup2
%astmodule app_segfault
%astmodule app_mwanalyze
%endif
%astmodule app_ices
%astmodule app_nbscat
%astmodule app_confbridge
%astsample confbridge
%astmodule bridge_builtin_features
%astmodule bridge_multiplexed
%astmodule bridge_simple
%astmodule bridge_softmix
%astmodule chan_bridge
%astmodule app_originate
%astmodule app_playtones
%astmodule format_siren14
%astmodule format_siren7
%astmodule func_aes
%astmodule func_config
%astmodule func_speex
%astmodule func_sprintf
%astmodule res_clialiases
%astmodule res_curl
%astsample res_curl
%astmodule func_frame_trace
%astmodule res_timing_dahdi
%astmodule res_timing_pthread
%astmodule res_timing_timerfd
%astmodule chan_multicast_rtp
%astmodule func_callcompletion
%astmodule func_pitchshift
%astmodule func_srv
%astmodule res_mutestream
%exclude %_sbindir/autosupport
%exclude %_sbindir/safe_asterisk
%exclude %_docdir/%name-%version/samples/cdr_pgsql.conf
%dir %_docdir/%name-%version
%dir %_libdir/asterisk
%dir %_libdir/asterisk/%version
%dir %modules_dir
%_sbindir/asterisk-%version
%_sbindir/rasterisk-%version
%_man8dir/asterisk-%version.8.*
%exclude %_docdir/%name-%version/samples/muted.conf
%astmodule chan_mgcp
%astmodule res_pktccops
%astsample res_pktccops
%astmodule app_celgenuserevent
%astmodule cdr_syslog
%astmodule cel_custom
%astmodule cel_manager
%astmodule res_rtp_asterisk
%astmodule res_rtp_multicast
%astmodule res_security_log
%astmodule res_srtp
%_docdir/%name-%version/IAX2-security.pdf
%_docdir/%name-%version/api-1.6.0-changes.odt
%_docdir/%name-%version/asterisk.8
%dir %_docdir/%name-%version/lang
%_docdir/%name-%version/lang/language-criteria.txt
%exclude %_docdir/%name-%version/lang/hebrew.ods
%exclude %_docdir/%name-%version/lang/urdu.ods
%exclude %_docdir/%name-%version/lang/vietnamese.ods
%astsample asterisk
%astsample ccss
%astsample cdr_syslog
%astsample cel
%astsample cel_custom
%astsample cel_sqlite3_custom
%astsample cel_tds
%astsample chan_mobile
%astsample cli_aliases
%astsample cli_permissions
%astsample dbsep
%astsample dsp
%astsample meetme
%_docdir/%name-%version/samples/extensions.lua
%astsample res_config_sqlite
%astsample phoneprov
%astsample queuerules
%astmodule app_saycountpl
%astmodule chan_mobile
%astmodule app_saycounted
%astmodule func_jitterbuffer
%astmodule res_format_attr_celt
%astmodule res_format_attr_silk
%astmodule res_http_post
%astmodule func_hangupcause
%astmodule func_presencestate
%astmodule res_format_attr_h263
%astmodule res_format_attr_h264
%astmodule res_http_websocket
%astsample acl
%exclude %astsample app_skel
%exclude %astsample config_test
%exclude %_docdir/%name-%version/Makefile
%exclude %_man8dir/astgenkey.*
%exclude %_man8dir/autosupport.*
%exclude %_man8dir/safe_asterisk.*
%exclude %_sbindir/astdb2bdb
%exclude %_sbindir/astdb2sqlite3

%files -n aelparse11
%_sbindir/aelparse-%version
%_altdir/aelparse-%version

%files ael
%astmodule pbx_ael

%if_with addons
%files app_conference
%astmodule app_conference
%endif

%files app_minivm
%astmodule app_minivm
%dir %_docdir/%name-%version/samples
%astsample minivm
%astsample extensions_minivm

%files app_voicemail
%dir %attr(3770,root,_asterisk) /var/spool/asterisk/voicemail
%astmodule app_voicemail
%astsample voicemail

%files calendar
%astmodule res_calendar
%astmodule res_calendar_caldav
%astmodule res_calendar_ews
%astmodule res_calendar_exchange
%astmodule res_calendar_icalendar
%astsample calendar

%files cdr_radius
%astmodule cdr_radius
%astmodule cel_radius

%files cdr_sqlite
%astmodule cdr_sqlite
%astmodule res_config_sqlite

%files cdr_tds
%astmodule cdr_tds
%astmodule cel_tds

%files chan_alsa
%astmodule chan_alsa
%dir %_docdir/%name-%version/samples
%astsample alsa

%files chan_console
%astmodule chan_console
%astsample console

%if_with dahdi
%files chan_dahdi
%astmodule chan_dahdi
%astmodule codec_dahdi
%astmodule app_dahdibarge
%astmodule app_dahdiras
%astmodule app_flash
%astsample chan_dahdi
%endif

%files chan_h323
%astmodule chan_ooh323
%astsample ooh323
%exclude %astsample h323

%files chan_iax2
%astmodule chan_iax2
%dir %_docdir/%name-%version/samples
%astsample iax

%if_with misdn
%files chan_misdn
%astmodule chan_misdn
%dir %_docdir/%name-%version/samples
%astsample misdn
%endif

%files chan_oss
%astmodule chan_oss

%files chan_sip
%astmodule chan_sip
%dir %_docdir/%name-%version/samples
%astsample sip
%astsample sip_notify
%astsample udptl

%if_with vpb
%files chan_vpb
%astmodule chan_vpb
%endif

%files codec_gsm
%astmodule format_gsm
%astmodule format_wav_gsm
%astmodule codec_gsm

%files codec_ilbc
%astmodule codec_ilbc
%astmodule format_ilbc

%if_with speex
%files codec_speex
%astmodule codec_speex
%endif

%files common

%files complete

%if_with corosync
%files corosync
%astmodule res_corosync
%astsample res_corosync
%endif

%if_with curl
%files curl
%astmodule func_curl
%astmodule res_config_curl
%endif

%files devel
%_includedir/asterisk-%version
%_libdir/libasteriskssl11.so

%files docs
%_docdir/%name-%version/Asterisk-Admin-Guide.pdf
%_docdir/%name-%version/Asterisk-Admin-Guide
%_docdir/%name-%version/CODING-GUIDELINES
%dir %_docdir/%name-%version
%dir %_docdir/%name-%version/samples
%attr(0644,root,root) %_docdir/%name-%version/sample.call
%attr(0644,root,root) %_docdir/%name-%version/BUGS
%attr(0644,root,root) %_docdir/%name-%version/CHANGES
%attr(0644,root,root) %_docdir/%name-%version/README
%attr(0644,root,root) %_docdir/%name-%version/asterisk.sgml
%_docdir/%name-%version/*.txt
%_docdir/%name-%version/CREDITS
%astsample amd
%astsample users
%astsample queues
%astsample sla
%astsample agents
%_docdir/%name-%version/samples/extensions.ael
%astsample smdi
%astsample followme
%astsample mgcp
%astsample rtp
%astsample adsi
%astsample alarmreceiver
%astsample cdr
%astsample cdr_custom
%astsample cdr_manager
%exclude %_docdir/%name-%version/samples/cdr_tds.conf
%astsample codecs
%astsample dnsmgr
%astsample dundi
%astsample enum
%astsample extconfig
%astsample extensions
%astsample features
%astsample festival
%astsample iaxprov
%exclude %_docdir/%name-%version/samples/indications.conf
%astsample logger
%astsample manager
%astsample modules
%astsample musiconhold
%astsample osp
%astsample oss
%astsample phone
%astsample say
%astsample vpb

%files fax
%dir %attr(3770,root,_asterisk) /var/spool/asterisk/fax
%astmodule app_fax
%astsample res_fax

%files format_mp3
%astmodule format_mp3

%files format_ogg
%astmodule format_ogg_vorbis

%files httpd
%astsample http
%_datadir/asterisk/static-http-%version

%files jabber
%astmodule chan_jingle
%astmodule chan_gtalk
%astmodule res_jabber
%astmodule chan_motif
%astmodule res_xmpp
%dir %_docdir/%name-%version/samples
%astsample jabber
%astsample jingle
%astsample gtalk
%astsample xmpp
%astsample motif

%if_with jack
%files jack
%astmodule app_jack
%endif

%if_with ldap
%files ldap
%astmodule res_config_ldap
%attr(0444,root,_asterisk) %_docdir/%name-%version/samples/res_ldap.conf
%endif

%if_with dahdi
%files meetme
%dir %attr(3770,root,_asterisk) /var/spool/asterisk/meetme
%astmodule app_meetme
%astmodule app_page
%endif

%files mysql
%astmodule app_mysql
%astsample app_mysql
%astmodule cdr_mysql
%astsample cdr_mysql
%astmodule res_config_mysql
%astsample res_config_mysql

%if_with odbc
%files odbc
%astmodule func_odbc
%astmodule cdr_odbc
%astmodule cdr_adaptive_odbc
%astmodule cel_odbc
%astsample cel_odbc
%astmodule res_odbc
%astmodule res_config_odbc
%dir %_docdir/%name-%version/samples
%astsample cdr_odbc
%astsample cdr_adaptive_odbc
%astsample func_odbc
%astsample res_odbc
%endif

%files pbx_lua
%astmodule pbx_lua

%if_with postgresql
%files pgsql
%astmodule cdr_pgsql
%astsample cdr_pgsql
%astmodule res_config_pgsql
%astsample res_pgsql
%astmodule cel_pgsql
%astsample cel_pgsql
%endif

%files res_crypto
%astmodule res_crypto

%if_with snmp
%files res_snmp
%astmodule res_snmp
%dir %_docdir/%name-%version/samples
%astsample res_snmp
%endif

%files sms
%astmodule app_sms

%files sources
%_usrsrc/%name.tar.bz2

%files sqlite3
%astmodule cel_sqlite3_custom
%astmodule cdr_sqlite3_custom
%astmodule res_config_sqlite3
%astsample cdr_sqlite3_custom
%astsample res_config_sqlite3

%files -n conf2ael11
%_sbindir/conf2ael-%version
%_altdir/conf2ael-%version

%files -n libasteriskssl11
%_libdir/libasteriskssl11.so.1

%changelog
* Fri Jan 15 2016 Denis Smirnov <mithraen@altlinux.ru> 11.20.0-alt1
- new version 11.20.0

* Sat Apr 11 2015 Denis Smirnov <mithraen@altlinux.ru> 11.17.1-alt1
- new version 11.17.1

* Wed Apr 08 2015 Denis Smirnov <mithraen@altlinux.ru> 11.17.0-alt1
- new version 11.17.0

* Mon Apr 06 2015 Denis Smirnov <mithraen@altlinux.ru> 11.16.0-alt2
- remove requires to mithraen-pbx-fax (ALT 30906)
- remove DONT_OPTIMIZE and DEBUG_THREADS options (ALT 30898)

* Sat Feb 07 2015 Denis Smirnov <mithraen@altlinux.ru> 11.16.0-alt1
- new version 11.16.0

* Sat Jan 31 2015 Denis Smirnov <mithraen@altlinux.ru> 11.15.1-alt1
- new version 11.15.1

* Tue Dec 16 2014 Denis Smirnov <mithraen@altlinux.ru> 11.15.0-alt1
- new version 11.15.0

* Mon Dec 15 2014 Denis Smirnov <mithraen@altlinux.ru> 11.14.2-alt2
- exclude music/sounds from src.rpm

* Thu Dec 11 2014 Denis Smirnov <mithraen@altlinux.ru> 11.14.2-alt1
- new version 11.14.2

* Thu Nov 27 2014 Denis Smirnov <mithraen@altlinux.ru> 11.14.1-alt2
- fix armh support
- cleanup

* Thu Nov 27 2014 Denis Smirnov <mithraen@altlinux.ru> 11.14.1-alt1
- new version 11.14.1

* Thu Sep 25 2014 Denis Smirnov <mithraen@altlinux.ru> 11.13.0-alt1
- new version 11.13.0

* Sat Sep 20 2014 Denis Smirnov <mithraen@altlinux.ru> 11.12.1-alt1
- new version 11.12.1

* Wed Aug 20 2014 Denis Smirnov <mithraen@altlinux.ru> 11.12.0-alt1
- new version 11.12.0

* Sat Jul 12 2014 Denis Smirnov <mithraen@altlinux.ru> 11.11.0-alt1
- new version 11.11.0

* Mon Jun 23 2014 Denis Smirnov <mithraen@altlinux.ru> 11.10.2-alt1
- new version 11.10.2

* Sat Jun 21 2014 Denis Smirnov <mithraen@altlinux.ru> 11.10.0-alt2
- add watch-file to rpm

* Sat Jun 07 2014 Denis Smirnov <mithraen@altlinux.ru> 11.10.0-alt1
- new version 11.10.0

* Sun May 11 2014 Denis Smirnov <mithraen@altlinux.ru> 11.9.0-alt2
- use pbx-astgenkey

* Sat Apr 26 2014 Denis Smirnov <mithraen@altlinux.ru> 11.9.0-alt1
- new version 11.9.0

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 11.8.1-alt1
- new version 11.8.1

* Wed Jan 15 2014 Denis Smirnov <mithraen@altlinux.ru> 11.7.0-alt1
- new version 11.7.0

* Thu Sep 05 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.1-alt3
- use if_with for corosync buildrequires

* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.1-alt2
- use if_with for corosync module

* Sun Sep 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.1-alt1
- new version 11.5.1

* Thu Aug 29 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.0-alt3
- rebuild with libcorosync2

* Tue Aug 27 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.0-alt2
- compatibility with asterisk-base 0.67

* Thu Aug 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11.5.0-alt1
- new version 11.5.0

* Sun May 19 2013 Denis Smirnov <mithraen@altlinux.ru> 11.4.0-alt1
- new version 11.4.0

* Sat Apr 20 2013 Denis Smirnov <mithraen@altlinux.ru> 11.3.0-alt2
- enable BETTER_BACKTRACES and G711_NEW_ALGORITHM

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 11.3.0-alt1
- new version 11.3.0

* Thu Feb 07 2013 Denis Smirnov <mithraen@altlinux.ru> 11.2.1-alt2
- exclude unneeded man pages

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 11.2.1-alt1
- new version 11.2.1

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 11.2.0-alt2
- move astdb2sqlite3 to pbx-utils-astdb package
- rename libasteriskssl.so -> libasteriskssl11.so
- build with res_corosync module

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 11.2.0-alt1
- new version 11.2.0

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 11.1.2-alt1
- 11.1.2

* Tue Dec 11 2012 Denis Smirnov <mithraen@altlinux.ru> 11.1.0-alt1
- 11.1.0

* Wed Nov 07 2012 Denis Smirnov <mithraen@altlinux.ru> 11.0.1-alt1
- 11.0.1

* Thu Nov 01 2012 Denis Smirnov <mithraen@altlinux.ru> 11.0.0-alt2
- 11.0.0 release

* Mon Sep 24 2012 Denis Smirnov <mithraen@altlinux.ru> 11.0.0-alt1.beta2
- 11.0.0-beta2
- disable build with -march=native

* Sun Aug 26 2012 Denis Smirnov <mithraen@altlinux.ru> 11-alt1.beta1
- first build for Sisyphus

