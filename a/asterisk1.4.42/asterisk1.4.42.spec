Name: asterisk1.4.42
Summary: Open source PBX
Version: 1.4.42
Release: alt3
License: GPL
Group: System/Servers
BuildRequires: binutils-devel flex gcc-c++ graphviz gtk+-devel libalsa-devel libcap-devel libcurl-devel libgcrypt-devel libgnutls-devel libgsm-devel libgtk+2-devel libiksemel-devel libltdl7-devel libncurses-devel libnet-snmp-devel libnewt-devel libnl-devel libopenh323_1.19-devel libpopt-devel libpri-devel libpw1.11-devel libradiusclient-ng-devel libsasl2-devel libsensors3-devel libspeex-devel libsqlite-devel libtonezone-dahdi-devel libunixODBC-devel libusb-compat-devel libvorbis-devel libvpb-devel ncompress postgresql-devel wget
BuildPreReq: asterisk-build-hacks
BuildPreReq: libss7-devel
BuildPreReq: libtonezone-dahdi-devel
BuildPreReq: dahdi-linux-headers
BuildPreReq: libpri-devel
BuildPreReq: libopenh323_1.19-devel libpw1.11-devel
BuildPreReq: libSDL_sound-devel libexpat-devel
BuildRequires: libmISDN-devel
BuildPreReq: libspeex-devel
BuildRequires: libcurl-devel
BuildRequires: libMySQL-devel
BuildPreReq: libunixODBC-devel libltdl-devel
BuildPreReq: postgresql-devel libpq-devel
BuildPreReq: librpm-devel libnet-snmp-devel libwrap-devel perl-devel
%def_with debug
%def_enable debug
%def_without		hoard
%def_without 		addons
%def_with			snmp
%def_with			speex
%def_with			curl
%def_with			postgresql
%def_without			misdn
%def_with			odbc
%def_with			h323
%def_without		ss7
%def_with			ldap
%def_with   		jack
%def_with			dahdi
%set_autoconf_version 2.60
%define modules_dir	%_libdir/asterisk/%version/modules
%define agi_dir     /usr/lib/asterisk/agi-bin
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
Requires(pre): asterisk-base >= 0.6-alt1
Requires(pre): coreutils
Requires: pbx-streamplayer
Requires: pbx-stereorize
Source: %name-%version.tar
Source2: %name-altlinux.tar
Packager: Denis Smirnov <mithraen@altlinux.ru>

%package -n aelparse1.4.42
Summary: Asterisk AEL2 parser
Group: %group
Requires: %name-common

%description -n aelparse1.4.42
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

%package app_voicemail
Summary: Asterisk voicemail module
Group: %group
Requires: %name = %version-%release

%description app_voicemail
VoiceMail for Asterisk


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

%package chan_alsa
Summary: Alsa channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_alsa
Alsa channel module for Asterisk

%if_with dahdi
%package chan_dahdi
Summary: ZAP channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_dahdi
ZAP channel module for Asterisk
%endif

%if_with h323
%package chan_h323
Summary: H.323 channel support for Asterisk
Group: System/Servers
Requires: %name = %version

%description chan_h323
H.323 channel support for Asterisk PBX

%endif

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


%if_with ss7
%package chan_ss7
Summary: SS7 channel module for Asterisk
Group: %group
Requires: %name = %version-%release

%description chan_ss7
SS7 module by Sifira, updated to Asterisk 1.4 by mithraen@

%endif

%package chan_vpb
Summary: Voicetronix API channel driver
Group: %group
Requires: %name = %version-%release

%description chan_vpb
Voicetronix API channel driver

%package codec_gsm
Summary: Asterisk GSM 6.10 codec support
Group: %group
Requires: %name = %version-%release

%description codec_gsm
Asterisk GSM 6.10 codec support


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
Requires: aelparse%version = %version-%release
Requires: %name-ael = %version-%release
Requires: %name-app_voicemail = %version-%release
Requires: %name-cdr_radius = %version-%release
Requires: %name-chan_iax2 = %version-%release
%if_with misdn
Requires: %name-chan_misdn = %version-%release
%endif
Requires: %name-chan_sip = %version-%release
%if_with dahdi
Requires: %name-chan_dahdi = %version-%release
%endif
Requires: %name-codec_gsm = %version-%release
Requires: %name-codec_speex = %version-%release
Requires: %name-crypto = %version-%release
Requires: %name-curl = %version-%release
Requires: %name-devel = %version-%release
Requires: %name-docs = %version-%release
Requires: %name-format_ogg = %version-%release
Requires: %name-httpd = %version-%release
%if_with odbc
Requires: %name-odbc = %version-%release
%endif
Requires: %name-pgsql = %version-%release
Requires: %name-res_crypto = %version-%release
%if_with snmp
Requires: %name-res_snmp = %version-%release
%endif
Requires: %name-sms = %version-%release
%if_with h323
Requires: %name-chan_h323 = %version-%release
%endif
Requires: %name-sources = %version-%release
%if_with ss7
Requires: %name-chan_ss7 = %version-%release
%endif
Requires: %name-cdr_sqlite   = %version-%release
Requires: %name-chan_vpb     = %version-%release
Requires: %name-chan_alsa    = %version-%release
Requires: %name-chan_oss     = %version-%release
Requires: %name-meetme       = %version-%release
Requires: pbx-agi-samples
Requires: pbx-utils-all

%description complete
This virtual package requires all Asterisk subpackages

%package crypto
Summary: OpenSSL support for Asterisk (crypto)
Group: %group
BuildArch: noarch
Requires: %name-res_crypto = %version-%release

%description crypto
res_crypto used by chan_sip and chan_iax2 for crypto support


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
Requires: %name-common

%description devel
C header files for Asterisk modules development

%package docs
Summary: asterisk documentation
Group: System/Servers
BuildArch: noarch
Requires: %name-common

%description docs
Asterisk documentation and sample files


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


%if_with dahdi
%package meetme
Summary: IP PBX MeetMe conference bridge
Group: %group
Requires: %name = %version-%release

%description meetme
IP PBX MeetMe conference bridge
%endif

%if_with addons
%package mysql
Summary: Open source PBX
Group: System/Servers
PreReq: %name = %version-%release

%description mysql
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standart-based telephony
equipment using relatively inexpensive hardware.

%endif

%if_with odbc
%package odbc
Summary: ODBC logging and config modules for Asterisk
Group: %group
Requires: %name = %version-%release

%description odbc
ODBC logging and config modules for Asterisk PBX

%endif

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
BuildArch: noarch
Requires: asterisk%version-common

%description sources
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standard-based telephony
equipment using relatively inexpensive hardware.


%description
Asterisk is a complete PBX in software. It provides all of the features
you would expect from PBX and more. Asterisk does voice over IP in three
protocols, and can interoperate with almost all standard-based telephony
equipment using relatively inexpensive hardware.


%prep
%setup -c -T
%setup -a2 -D
tar cjf ../%name.tar.bz2 .
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
%if_with h323
	--with-h323
%else
	--without-h323
%endif
pushd menuselect
make libdir=%_libdir
popd
make menuselect.makeopts libdir=%_libdir ||:
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
mkdir -p %buildroot%_altdir
sed "s/@version@/%version/g" < altlinux/alternatives-asterisk > %buildroot%_altdir/asterisk-%version
sed "s/@version@/%version/g" < altlinux/alternatives-aelparse > %buildroot%_altdir/aelparse-%version
sed "s/@version@/%version/g" < altlinux/alternatives-conf2ael > %buildroot%_altdir/conf2ael-%version
mkdir -p %buildroot%_includedir/asterisk-%version
mv %buildroot%_includedir/asterisk   %buildroot%_includedir/asterisk-%version/asterisk
mv %buildroot%_includedir/asterisk.h %buildroot%_includedir/asterisk-%version/asterisk.h
mkdir -p %buildroot/var/lib/asterisk/sounds
mkdir -p %buildroot/var/lib/asterisk/moh

%preun
%preun_service asterisk

%post
%post_service asterisk

%files
%_altdir/asterisk-%version
%exclude /var/lib/asterisk/images/asterisk-intro.jpg
%exclude /var/lib/asterisk/keys/freeworlddialup.pub
%exclude /var/lib/asterisk/keys/iaxtel.pub
%exclude /usr/sbin/astman
%exclude /usr/sbin/muted
%exclude /usr/sbin/smsq
%exclude /usr/sbin/stereorize
%exclude /usr/sbin/streamplayer
%dir %exclude /var/lib/asterisk/moh
%dir %exclude /var/lib/asterisk/sounds
%astmodule app_hasnewvoicemail
%astmodule app_lookupblacklist
%astmodule app_lookupcidname
%astmodule app_random
%astmodule app_realtime
%astmodule app_setcdruserfield
%astmodule app_settransfercapability
%astmodule format_ilbc
%astmodule func_language
%astmodule func_moh
%astmodule res_features
%astmodule res_indications
%dir %_docdir/%name-%version/samples
%_docdir/%name-%version/README.ALT
%astmodule chan_skinny
%astsample skinny
%astmodule func_audiohookinherit
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
%astmodule format_pcm
%astmodule app_speech_utils
%astmodule res_speech
%astmodule res_smdi
%astmodule app_followme
%astmodule app_adsiprog
%astmodule app_festival
%astmodule app_image
%astmodule chan_mgcp
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
%astmodule func_md5
%astmodule func_sha1
%astmodule func_realtime
%astmodule func_strings
%astmodule func_timeout
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
%astmodule format_sln
%astmodule format_wav
%astmodule pbx_config
%astmodule pbx_spool
%astmodule res_agi
%astmodule res_musiconhold
%exclude %astmodule app_mp3
%if_with addons
%astmodule app_devstate
%astmodule app_pickup2
%astmodule app_segfault
%astmodule app_mwanalyze
%endif
%astmodule app_ices
%astmodule app_nbscat
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
%exclude %agi_dir/*

%files -n aelparse1.4.42
%_sbindir/aelparse-%version
%_altdir/aelparse-%version

%files ael
%astmodule pbx_ael

%if_with addons
%files app_conference
%astmodule app_conference
%endif

%files app_voicemail
%dir %attr(3770,root,_asterisk) /var/spool/asterisk/voicemail
%astmodule app_voicemail
%astsample voicemail

%files cdr_radius
%astmodule cdr_radius

%files cdr_sqlite
%astmodule cdr_sqlite

%files chan_alsa
%astmodule chan_alsa
%dir %_docdir/%name-%version/samples
%astsample alsa

%if_with dahdi
%files chan_dahdi
%astmodule chan_dahdi
%astmodule codec_dahdi
%astmodule app_dahdibarge
%astmodule app_dahdiscan
%astmodule app_dahdiras
%astmodule app_flash
%astsample chan_dahdi
%endif

%if_with h323
%files chan_h323
%astmodule chan_h323
%attr(0444,root,_asterisk) %_docdir/%name-%version/samples/h323.conf
%endif

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

%if_with ss7
%files chan_ss7
%astmodule chan_ss7
%endif

%files chan_vpb
%astmodule chan_vpb

%files codec_gsm
%astmodule format_gsm
%astmodule format_wav_gsm
%astmodule codec_gsm

%if_with speex
%files codec_speex
%astmodule codec_speex
%endif

%files common

%files complete

%files crypto
%_sbindir/astgenkey

%if_with curl
%files curl
%astmodule func_curl
%endif

%files devel
%_includedir/asterisk-%version

%files docs
%dir %_docdir/%name-%version
%dir %_docdir/%name-%version/samples
%attr(0644,root,root) %_docdir/%name-%version/sample.call
%attr(0644,root,root) %_docdir/%name-%version/BUGS
%attr(0644,root,root) %_docdir/%name-%version/CHANGES
%attr(0644,root,root) %_docdir/%name-%version/CODING-GUIDELINES
%attr(0644,root,root) %_docdir/%name-%version/PEERING
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
%astsample rpt
%astsample rtp
%astsample adsi
%astsample adtranvofr
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

%files format_ogg
%astmodule format_ogg_vorbis

%files httpd
%astsample http
%_datadir/asterisk/static-http-%version

%if_with dahdi
%files meetme
%dir %attr(3770,root,_asterisk) /var/spool/asterisk/meetme
%astmodule app_meetme
%astmodule app_page
%endif

%if_with addons
%files mysql
%astmodule app_addon_sql_mysql
%astmodule res_config_mysql
%astmodule cdr_addon_mysql
%endif

%if_with odbc
%files odbc
%astmodule func_odbc
%astmodule cdr_odbc
%astmodule res_odbc
%astmodule res_config_odbc
%dir %_docdir/%name-%version/samples
%astsample cdr_odbc
%astsample func_odbc
%astsample res_odbc
%endif

%if_with postgresql
%files pgsql
%astmodule cdr_pgsql
%astmodule res_config_pgsql
%dir %_docdir/%name-%version/samples
%astsample cdr_pgsql
%astsample res_pgsql
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

%changelog
* Mon Jun 25 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.42-alt3
- fix build (rebuild without jabber support)

* Mon Feb 13 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.42-alt2
- rebuild without chan_misdn

* Thu Jul 28 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.42-alt1
- 1.4.42

* Tue May 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.40-alt2
- fix build

* Thu Mar 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.40-alt1
- first build for Sisyphus

