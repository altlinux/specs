Name: freeswitch
Version: 1.0.7
Release: alt0.5

Summary: FreeSWITCH open source telephony platform
License: MPL
Group: System/Servers
Url: http://www.freeswitch.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libalsa-devel
BuildRequires: libgnutls-devel libncurses-devel libssl-devel libunixODBC-devel
BuildRequires: gdbm-devel db4-devel libldap-devel libcurl-devel libsofia-sip-devel
BuildRequires: libspandsp6-devel libspeex-devel libsqlite3-devel libsrtp
BuildRequires: libxmlrpc-devel libyaml-devel libiksemel-devel libedit-devel
BuildRequires: libsndfile-devel libpcre-devel libapr1-devel libaprutil1-devel
BuildRequires: libilbc1-devel libjs-devel libjson-devel flite-devel
BuildRequires: libtiff-devel libldap-devel libsoundtouch-devel libldns-devel
BuildRequires: libpcap-devel libunimrcp-devel perl-devel python-devel
BuildRequires: libcelt-devel libmpg123-devel liblame-devel libshout2-devel
BuildRequires: libpri-devel libopenr2.3-devel libnet-snmp-devel libnl-devel
BuildRequires: libsensors3-devel erlang-devel postgresql-devel
BuildRequires: java-common java-1.6.0-openjdk-devel /proc

%description
FreeSWITCH is an open source telephony platform designed to facilitate
the creation of voice and chat driven products scaling from a soft-phone
up to a soft-switch.  It can be used as a simple switching engine, a media
gateway or a media server to host IVR applications using simple scripts
or XML to control the callflow.
It supports various communication technologies such as SIP, H.323 and 
GoogleTalk making it easy to interface with other open source PBX systems
such as sipX, OpenPBX, Bayonne, YATE or Asterisk.

%package -n lib%name
Summary: FreeSWITCH shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: Development package for FreeSWITCH
Group: Development/C
Requires: lib%name = %version-%release

%package -n libfreetdm
Summary: FreeTDM is a library to interface to Digium and Sangoma boards.
Group: System/Libraries

%package -n libfreetdm-devel
Summary: Development package for FreeTDM
Group: Development/C
Requires: libfreetdm = %version-%release

%package daemon
Summary: FreeSWITCH daemon
Group: System/Servers
Requires: lib%name = %version-%release
Requires: freeswitch-sounds-default

%package freetdm
Summary: FreeTDM modules
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-de
Summary: German language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-en
Summary: English language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-fr
Summary: French language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-he
Summary: Hebrew language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-ru
Summary: Russian language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package java
Summary: Java support for the FreeSWITCH open source telephony platform
Group: Development/Java
Requires: %name-daemon = %version-%release
Requires: java >= 1.6.0

%package lua
Summary: Lua support for the FreeSWITCH open source telephony platform
Group: Development/Other
Requires: %name-daemon = %version-%release

%package perl
Summary: Perl support for the FreeSWITCH open source telephony platform
Group: Development/Perl
Requires: %name-daemon = %version-%release

%package python
Summary: Python support for the FreeSWITCH open source telephony platform
Group: Development/Python
Requires: %name-daemon = %version-%release

%package spidermonkey
Summary: JavaScript support for the FreeSWITCH open source telephony platform
Group: Development/Other
Requires: %name-daemon = %version-%release

# {{{ descriptions

%description -n lib%name
FreeSWITCH shared library

%description -n lib%name-devel
FreeSWITCH development files

%description -n libfreetdm
FreeTDM is a library implementing unified high level API for both signaling
and I/O for multiple telephony boards (Digium and Sangoma are most popular).
See http://wiki.freeswitch.org/wiki/FreeTDM for details

%description -n libfreetdm-devel
FreeTDM development part

%description daemon
FreeSWITCH is an open source telephony platform designed to facilitate the creation of voice 
and chat driven products scaling from a soft-phone up to a soft-switch.  It can be used as a
simple switching engine, a media gateway or a media server to host IVR applications using 
simple scripts or XML to control the callflow. 

%description freetdm
FreeTDM modules for FreeSWITCH

%description spidermonkey
JavaScript support for the FreeSWITCH open source telephony platform

%description java
Java support for the FreeSWITCH open source telephony platform

%description lua
Lua support for the FreeSWITCH open source telephony platform

%description perl
Perl support for the FreeSWITCH open source telephony platform

%description python
Python support for the FreeSWITCH open source telephony platform

%description lang-de
German language phrases module and directory structure for say module and voicemail

%description lang-en
English language phrases module and directory structure for say module and voicemail

%description lang-fr
French language phrases module and directory structure for say module and voicemail

%description lang-he
Hebrew language phrases module and directory structure for say module and voicemail

%description lang-ru
Russian language phrases module and directory structure for say module and voicemail

# }}}

%prep
%setup

%build
%autoreconf
%configure \
    --localstatedir=%_var \
    --enable-core-libedit-support \
    --enable-core-odbc-support \
    --with-erlang=%_bindir/erl \
    --with-libcurl \
    --with-openssl \
    --disable-static \
    #
make

%install
%make_install sysconfdir=%_sysconfdir/freeswitch DESTDIR=%buildroot install
install -pm0755 -D freeswitch.init %buildroot%_initdir/freeswitch
install -pm0644 -D freeswitch.sysconfig %buildroot%_sysconfdir/sysconfig/freeswitch

mkdir -p \
    %buildroot%_sbindir \
    %buildroot%_var/lib/freeswitch/recordings \
    %buildroot%_logdir/freeswitch/{cdr-csv,xml_cdr}

mv %buildroot%_bindir/freeswitch %buildroot%_sbindir/

find %buildroot%_libdir/%name -name \*.la -delete
%add_python_req_skip _freeswitch

#---------------------------------------------------------------
%pre daemon
/usr/sbin/groupadd -r -f _pbx &>/dev/null
/usr/sbin/useradd -r -g _pbx -d /dev/null -s /dev/null \
    -c "freeswitch" -M -n _pbx &>/dev/null ||:

%post daemon
%post_service %name

%preun daemon
%preun_service %name

#---------------------------------------------------------------
%files -n lib%name
%_libdir/libfreeswitch*.so.*

%files -n lib%name-devel
%_bindir/fsxs
%_includedir/freeswitch
%_libdir/libfreeswitch*.so
%_pkgconfigdir/freeswitch.pc

%files -n libfreetdm
%dir %_sysconfdir/freetdm
%config(noreplace) %_sysconfdir/freetdm/*

%_libdir/libfreetdm.so.*

%dir %_libdir/freetdm
%_libdir/freetdm/ftmod_analog.so
%_libdir/freetdm/ftmod_analog_em.so
%_libdir/freetdm/ftmod_r2.so
%_libdir/freetdm/ftmod_skel.so
%_libdir/freetdm/ftmod_zt.so

%files -n libfreetdm-devel
%_includedir/freetdm
%_libdir/libfreetdm.so
%_pkgconfigdir/freetdm.pc

%files daemon
%_initdir/freeswitch

%config(noreplace) %_sysconfdir/sysconfig/freeswitch

%dir %attr(0750, root, _pbx) %_sysconfdir/%name

%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/*.tpl
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/*.ttml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/*.conf
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/mime.types

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/autoload_configs
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/acl.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/alsa.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/blacklist.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/callcenter.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/cidlookup.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/cdr_csv.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/cdr_pg_csv.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/cdr_sqlite.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/conference.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/console.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/db.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/dialplan_directory.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/dingaling.conf.xml 
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/directory.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/distributor.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/easyroute.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/enum.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/event_multicast.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/event_socket.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/erlang_event.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/fax.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/fifo.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/hash.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/http_cache.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/ivr.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/lcr.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/local_stream.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/logfile.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/memcache.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/modules.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/nibblebill.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/opal.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/osp.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/pocketsphinx.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/portaudio.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/post_load_modules.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/redis.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/rss.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/rtmp.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/sangoma_codec.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/shout.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/skinny.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/sofia.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/spandsp.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/switch.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/syslog.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/timezones.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/tts_commandline.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/unicall.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/unimrcp.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/voicemail.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/xml_cdr.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/xml_curl.conf.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/xml_rpc.conf.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/zeroconf.conf.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/directory
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/directory/default
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/directory/default.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/directory/default/default.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/directory/default/example.com.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/directory/default/skinny-example.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/directory/default/usertemplate.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/dialplan
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/dialplan/default
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/dialplan/public
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/default.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/default/99998_example.com.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns/20-Demo.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns/20-Local_extension.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns/90-External.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/skinny-patterns/99-Default_Drop.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/public.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/public/00_inbound_did.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/dialplan/features.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/ivr_menus
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/ivr_menus/*.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/jingle_profiles
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/jingle_profiles/*.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/mrcp_profiles
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/mrcp_profiles/*.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/sip_profiles
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/sip_profiles/internal
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/sip_profiles/external
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/sip_profiles/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/sip_profiles/internal/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/sip_profiles/external/*.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/skinny_profiles
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/skinny_profiles/*.xml

%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang

%_sbindir/freeswitch
%_bindir/fs_cli
%_bindir/fs_ivrd

%dir %_libdir/%name
%_libdir/%name/mod_alsa.so
%_libdir/%name/mod_blacklist.so
%_libdir/%name/mod_amr.so
%_libdir/%name/mod_bv.so
%_libdir/%name/mod_callcenter.so
%_libdir/%name/mod_cidlookup.so
%_libdir/%name/mod_cdr_csv.so
%_libdir/%name/mod_cdr_sqlite.so
%_libdir/%name/mod_cdr_pg_csv.so
%_libdir/%name/mod_celt.so
%_libdir/%name/mod_cluechoo.so
%_libdir/%name/mod_commands.so
%_libdir/%name/mod_conference.so
%_libdir/%name/mod_console.so
%_libdir/%name/mod_curl.so
%_libdir/%name/mod_db.so
%_libdir/%name/mod_dahdi_codec.so
%_libdir/%name/mod_dialplan_asterisk.so
%_libdir/%name/mod_dialplan_directory.so
%_libdir/%name/mod_dialplan_xml.so
%_libdir/%name/mod_dingaling.so
%_libdir/%name/mod_directory.so
%_libdir/%name/mod_distributor.so
%_libdir/%name/mod_dptools.so
%_libdir/%name/mod_easyroute.so
%_libdir/%name/mod_enum.so
%_libdir/%name/mod_erlang_event.so
%_libdir/%name/mod_esf.so
%_libdir/%name/mod_event_multicast.so
%_libdir/%name/mod_event_socket.so
%_libdir/%name/mod_expr.so
%_libdir/%name/mod_fax.so
%_libdir/%name/mod_fifo.so
%_libdir/%name/mod_flite.so
%_libdir/%name/mod_fsk.so
%_libdir/%name/mod_fsv.so
%_libdir/%name/mod_g723_1.so
%_libdir/%name/mod_g729.so
%_libdir/%name/mod_h26x.so
%_libdir/%name/mod_hash.so
%_libdir/%name/mod_http_cache.so
%_libdir/%name/mod_ilbc.so
%_libdir/%name/mod_lcr.so
%_libdir/%name/mod_ldap.so
%_libdir/%name/mod_limit.so
%_libdir/%name/mod_local_stream.so
%_libdir/%name/mod_logfile.so
%_libdir/%name/mod_loopback.so
#_libdir/%name/mod_memcache.so
%_libdir/%name/mod_native_file.so
%_libdir/%name/mod_nibblebill.so
%_libdir/%name/mod_redis.so
%_libdir/%name/mod_rss.so
%_libdir/%name/mod_rtmp.so
%_libdir/%name/mod_siren.so
%_libdir/%name/mod_shell_stream.so
%_libdir/%name/mod_shout.so
%_libdir/%name/mod_silk.so
%_libdir/%name/mod_skinny.so
%_libdir/%name/mod_snapshot.so
%_libdir/%name/mod_sndfile.so
%_libdir/%name/mod_snipe_hunt.so
%_libdir/%name/mod_snmp.so
%_libdir/%name/mod_snom.so
%_libdir/%name/mod_stress.so
%_libdir/%name/mod_sofia.so
%_libdir/%name/mod_soundtouch.so
%_libdir/%name/mod_spandsp.so
%_libdir/%name/mod_speex.so
%_libdir/%name/mod_spy.so
%_libdir/%name/mod_syslog.so
%_libdir/%name/mod_timerfd.so
%_libdir/%name/mod_tone_stream.so
%_libdir/%name/mod_tts_commandline.so
%_libdir/%name/mod_unimrcp.so
%_libdir/%name/mod_valet_parking.so
%_libdir/%name/mod_vmd.so
%_libdir/%name/mod_voicemail.so
%_libdir/%name/mod_voipcodecs.so
%_libdir/%name/mod_xml_cdr.so
%_libdir/%name/mod_xml_curl.so
%_libdir/%name/mod_yaml.so

%dir %_datadir/%name
%dir %_datadir/%name/scripts
%dir %_datadir/%name/sounds
%dir %_datadir/%name/htdocs
%dir %_datadir/%name/grammar
#dir %_datadir/%name/grammar/model
#dir %_datadir/%name/grammar/model/communicator
#dir %_datadir/%name/grammar/model/wsj1

%dir %attr(0770, root, _pbx) %_spooldir/%name

%dir %attr(0770, root, _pbx) %_localstatedir/%name
%dir %attr(0770, root, _pbx) %_localstatedir/%name/db

%dir %attr(0770, root, _pbx) %_logdir/%name
%dir %attr(0770, root, _pbx) %_logdir/%name/cdr-csv
%dir %attr(0770, root, _pbx) %_logdir/%name/xml_cdr

%dir %attr(0770, root, _pbx) %_var/run/%name

%files freetdm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/freetdm.conf.xml
%_libdir/%name/mod_freetdm.so

%files spidermonkey
%_libdir/%name/mod_spidermonkey*.so*
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/spidermonkey.conf.xml

%files java
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/java.conf.xml
%_libdir/%name/mod_java.so*
%_datadir/%name/scripts/%name.jar

%files lua
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/lua.conf.xml
%_libdir/%name/mod_lua.so*

%files perl
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/perl.conf.xml
%_libdir/%name/mod_perl.so*
%perl_vendor_archlib/freeswitch.pm
%perl_vendor_autolib/freeswitch

%files python
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/python.conf.xml
%_libdir/%name/mod_python.so*
%python_sitelibdir/freeswitch.py*

%files lang-de
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de
#dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/*.xml
#config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/vm/*.xml
%_libdir/%name/mod_say_de.so*

%files lang-en
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/ivr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/ivr/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/vm/*.xml
%_libdir/%name/mod_say_en.so*

%files lang-fr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/vm/*.xml
%_libdir/%name/mod_say_fr.so*

%files lang-he
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/vm/*.xml
#_libdir/%name/mod_say_he.so*

%files lang-ru
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/vm/*.xml
%_libdir/%name/mod_say_ru.so*

%changelog
* Thu Nov 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.5
- updated from git b9e28f85

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt0.4.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 1.0.7-alt0.4
- rebuilt for perl-5.14

* Wed Aug 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.3
- updated from git 6d1d4a9c

* Wed Jun 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.1
- 1.0.7 (rolling) released
- obsolete openzap stuff removed

* Wed Jun 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt9
- mod_memcache temporarily dropped

* Tue Apr 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt8
- mod_perl again due to perl changes

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt7
- resurrect mod_perl module

* Mon Mar 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt6
- rebuilt with recent libmemcached

* Wed Mar 16 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt5
- exclude mod_erlang_event from build

* Wed Dec 01 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt4
- updated from upstream git.2343f685

* Sun Nov 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt3
- rebuilt with recent libcelt

* Sat May 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt2
- fixed build with recent libmpg123

* Fri May  7 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt1
- 1.0.6 released

* Mon Apr 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt4
- fixed python module packaging

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt2
- 1.0.4 released

* Wed Jul 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt3
- rebuilt due spandsp soname change

* Sat May 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Wed Jan 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- first build for ALTLinux
