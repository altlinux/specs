Name: callweaver
Version: 1.2
Release: alt1.svn5593.1.2

Summary: CallWeaver IP PBX
License: GPL
Group: System/Servers
Url: http://callweaver.org/
Packager: Eugene Prokopiev <enp@altlinux.ru>

%define modules_dir %_libexecdir/%name/modules

PreReq: chkconfig

%add_findprov_lib_path %_libdir/%name

Source0: %name-%version.tar
Source1: %name-%version-statup.tar
Source2: %name-%version-conf.tar

# Hiawei SoftX specific patches which are can't applied by upstream
#Patch0: %name-%version-silencesupp.patch
Patch1: %name-%version-huawei-rfc2833.patch
Patch2: %name-%version-buffer-overflow.patch

BuildRequires: gcc-c++ libcap-devel libpopt-devel libreadline-devel libspandsp6-devel libspeex-devel libssl-devel libtiff-devel libvorbis-devel zlib-devel libsqlite3-devel libMySQL-devel postgresql-devel libltdl7-devel
Requires: service libcap libpopt libreadline libspandsp6 libspeex libssl libtiff libvorbis zlib libsqlite3 monit-base

%description
CallWeaver is a community-driven vendor-independent cross-platform open source PBX software project 
(formerly known as OpenPBX.org). It was originally derived from Asterisk. Now it supports analog and 
digital PSTN telephony, multi-protocol voice over IP telephony, fax, software-fax, T.38 fax over IP 
and many telephony applications such as IVR, conferencing and callcenter queue management.

See /usr/share/doc/%name-%version/QUICKSTART.ru_RU.UTF-8 for details.

%package mysql
Summary: MySQL resources for CallWeaver IP PBX
Group: System/Servers
Requires: %name = %version-%release
%description mysql
MySQL resources for CallWeaver IP PBX

%package pgsql
Summary: PostgreSQL resources for CallWeaver IP PBX
Group: System/Servers
Requires: %name = %version-%release
%description pgsql
PostgreSQL resources for CallWeaver IP PBX

%package docs
Summary: CallWeaver IP PBX documentation and configuration samples
Group: System/Servers
Requires: %name = %version-%release
%description docs
CallWeaver IP PBX documentation and configuration samples

%package devel
Summary: CallWeaver IP PBX header files
Group: System/Servers
Requires: %name = %version-%release
%description devel
CallWeaver IP PBX devel

%package full
Summary: CallWeaver full set
Group: System/Servers
Requires: %name = %version-%release %name-mysql %name-pgsql %name-docs %name-devel %name-sounds pbx-music
%description full
CallWeaver full set


%prep
%setup
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./bootstrap.sh
%configure \
    --enable-postgresql \
    --enable-mysql \
    --enable-udpfromto \
    --enable-iax-trunking \
    --enable-builin-sqlite3=no \
    --with-pbx_ael \
    --with-cdr_mysql \
    --with-cdr_pgsql \
    --with-cdr_pgsql_custom \
    --with-res_config_mysql \
    --with-res_config_pgsql \
    --with-res_sqlite  \
    --with-pgsql-inc=/usr/include/pgsql \
    --enable-rtp-payload-97

%make_build

%install
%make DESTDIR=%buildroot install
%ifarch x86_64
mkdir -p %buildroot/%modules_dir
mv %buildroot/%_libdir/%name/modules/*.so %buildroot/%modules_dir/
rm -rf %buildroot/%_libdir/%name/modules
%endif
cp -a %buildroot/%_localstatedir/* %buildroot/var/
rm -rf %buildroot/%_datadir/%name/ogi/*
rm -rf %buildroot/%_datadir/%name/doc
mkdir -p %buildroot/%_docdir/%name-%version
cp -a LICENSE AUTHORS BUGS CREDITS ChangeLog HARDWARE README SECURITY %buildroot/%_docdir/%name-%version/
mkdir -p %buildroot/%_docdir/%name-docs-%version/samples
mv %buildroot/%_sysconfdir/%name/* %buildroot/%_docdir/%name-docs-%version/samples
cp -a sample.call doc/* %buildroot/%_docdir/%name-docs-%version/
mkdir -p %buildroot/%_docdir/%name-docs-%version/ogi
cp ogi/*.ogi ogi/*.c %buildroot/%_docdir/%name-docs-%version/ogi/
tar -xf %SOURCE1
mkdir -p %buildroot/%_initdir
cp %name-%version-statup/%name.init %buildroot/%_initdir/%name
mkdir -p %buildroot/%_sysconfdir/monitrc.d/
cp %name-%version-statup/%name.monit %buildroot/%_sysconfdir/monitrc.d/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
cp %name-%version-statup/%name.logrotate %buildroot/%_sysconfdir/logrotate.d/%name
tar -xf %SOURCE2
cp %name-%version-conf/* %buildroot/%_sysconfdir/%name/
mv %buildroot/%_sysconfdir/%name/QUICKSTART.ru_RU.UTF-8 %buildroot/%_docdir/%name-%version/

%pre
%_sbindir/groupadd -r -f _callweaver
%_sbindir/useradd -r -g _callweaver -r -c "CallWeaver IP PBX" -s /dev/null -d /dev/null -n _callweaver > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %_sysconfdir/%name/*
%_initdir/%name
%_sysconfdir/monitrc.d/%name
%_sysconfdir/logrotate.d/%name
%_sbindir/callweaver
%_sbindir/callweaver_cli
%_libdir/%name/*.so*
%modules_dir/app_adsiprog.so
%modules_dir/app_amd.so
%modules_dir/app_authenticate.so
%modules_dir/app_backgrounddetect.so
%modules_dir/app_cdr.so
%modules_dir/app_changrab.so
%modules_dir/app_chanisavail.so
%modules_dir/app_chanspy.so
%modules_dir/app_controlplayback.so
%modules_dir/app_db.so
%modules_dir/app_devstate.so
%modules_dir/app_dial.so
%modules_dir/app_dictate.so
%modules_dir/app_directed_pickup.so
%modules_dir/app_directory.so
%modules_dir/app_disa.so
%modules_dir/app_dumpchan.so
%modules_dir/app_echo.so
%modules_dir/app_enumlookup.so
%modules_dir/app_eval.so
%modules_dir/app_exec.so
%modules_dir/app_faxdetect.so
%modules_dir/app_forkcdr.so
%modules_dir/app_getcpeid.so
%modules_dir/app_getdevstate.so
%modules_dir/app_getextstate.so
%modules_dir/app_groupcount.so
%modules_dir/app_hasnewvoicemail.so
%modules_dir/app_lookupblacklist.so
%modules_dir/app_lookupcidname.so
%modules_dir/app_milliwatt.so
%modules_dir/app_muxmon.so
%modules_dir/app_nconference.so
%modules_dir/app_pipe.so
%modules_dir/app_playback.so
%modules_dir/app_privacy.so
%modules_dir/app_proc.so
%modules_dir/app_queue.so
%modules_dir/app_random.so
%modules_dir/app_read.so
%modules_dir/app_record.so
%modules_dir/app_rxfax.so
%modules_dir/app_sayunixtime.so
%modules_dir/app_senddtmf.so
%modules_dir/app_sendtext.so
%modules_dir/app_setcallerpres.so
%modules_dir/app_setcdruserfield.so
%modules_dir/app_setrdnis.so
%modules_dir/app_settransfercapability.so
%modules_dir/app_sms.so
%modules_dir/app_softhangup.so
%modules_dir/app_stack.so
%modules_dir/app_system.so
%modules_dir/app_t38gateway.so
%modules_dir/app_transfer.so
%modules_dir/app_txfax.so
%modules_dir/app_userevent.so
%modules_dir/app_verbose.so
%modules_dir/app_voicemail.so
%modules_dir/app_waitfordigits.so
%modules_dir/app_waitforring.so
%modules_dir/app_waitforsilence.so
%modules_dir/app_while.so
%modules_dir/cdr_csv.so
%modules_dir/cdr_custom.so
%modules_dir/cdr_manager.so
%modules_dir/cdr_sqlite3.so
%modules_dir/chan_agent.so
%modules_dir/chan_features.so
%modules_dir/chan_iax2.so
%modules_dir/chan_local.so
%modules_dir/chan_mgcp.so
%modules_dir/chan_sip.so
%modules_dir/chan_woomera.so
%modules_dir/codec_a_mu.so
%modules_dir/codec_alaw.so
%modules_dir/codec_dvi_adpcm.so
%modules_dir/codec_g722.so
%modules_dir/codec_g722_16k_8k.so
%modules_dir/codec_g726.so
%modules_dir/codec_gsm.so
%modules_dir/codec_lpc10.so
%modules_dir/codec_oki_adpcm.so
%modules_dir/codec_speex.so
%modules_dir/codec_ulaw.so
%modules_dir/format_au.so
%modules_dir/format_g723_1.so
%modules_dir/format_g726.so
%modules_dir/format_g729.so
%modules_dir/format_gsm.so
%modules_dir/format_h263.so
%modules_dir/format_jpeg.so
%modules_dir/format_ogg_vorbis.so
%modules_dir/format_pcm.so
%modules_dir/format_pcm_alaw.so
%modules_dir/format_sln.so
%modules_dir/format_wav.so
%modules_dir/format_wav_gsm.so
%modules_dir/func_callerid.so
%modules_dir/func_cdr.so
%modules_dir/func_config.so
%modules_dir/func_db.so
%modules_dir/func_enum.so
%modules_dir/func_env.so
%modules_dir/func_fileexists.so
%modules_dir/func_groupcount.so
%modules_dir/func_language.so
%modules_dir/func_logic.so
%modules_dir/func_math.so
%modules_dir/func_md5.so
%modules_dir/func_moh.so
%modules_dir/func_strings.so
%modules_dir/func_timeout.so
%modules_dir/func_uri.so
%modules_dir/pbx_ael.so
%modules_dir/pbx_config.so
%modules_dir/pbx_dundi.so
%modules_dir/pbx_loopback.so
%modules_dir/pbx_realtime.so
%modules_dir/pbx_spool.so
%modules_dir/res_adsi.so
%modules_dir/res_crypto.so
%modules_dir/res_features.so
%modules_dir/res_indications.so
%modules_dir/res_monitor.so
%modules_dir/res_musiconhold.so
%modules_dir/res_ogi.so
%modules_dir/res_sqlite.so
%doc %_docdir/%name-%version/*
%_man8dir/%name.8.gz
%_datadir/%name/*
%attr(3770,root,_callweaver) /var/lib/%name
%attr(3770,root,_callweaver) /var/log/%name
%attr(3770,root,_callweaver) /var/spool/%name
%attr(3770,root,_callweaver) /var/run/%name
%dir %_docdir/callweaver-%version 

%files pgsql
%modules_dir/app_sql_postgres.so
%modules_dir/cdr_pgsql.so
%modules_dir/cdr_pgsql_custom.so
%modules_dir/res_config_pgsql.so

%files mysql
%modules_dir/app_sql_mysql.so
%modules_dir/cdr_mysql.so
%modules_dir/res_config_mysql.so

%files docs
%doc %_docdir/%name-docs-%version/*
%dir %_docdir/callweaver-docs-%version 

%files devel
%_includedir/%name/*

%files full

%changelog
* Fri Dec 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1.svn5593.1.2
- rebuilt with recent spandsp

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.svn5593.1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Mon Mar 01 2010 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5593.1
- new version

* Tue Sep 22 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.6
- add callweaver-full

* Thu Sep 17 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.5
- add lsb init header
- remove zaptel because it is unsupported now

* Mon Aug 03 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.4
- remove smsq and streamplayer - see pbx-utils package

* Thu Jul 30 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.3
- rebuilt due spandsp soname change

* Wed Jul 15 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.2
- fix "will always overflow destination buffer" problem with gcc 4.4 - thanks to wrar@

* Fri Jun 26 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5399.1
- new version

* Fri May 22 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5342.5
- new libtool support

* Fri May 22 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5342.4
- apply repocop patch to own docdir subdirectory

* Fri Feb 06 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5342.3
- less destructive patch to change Hiawei SoftX DTMF support
  + this patch can be turned on/off with ./configure now
  + turning it on brokes iLBC support
- rename and turn off patch to hide silenceSupp:off

* Thu Feb 05 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5342.2
- modify patch to change Hiawei SoftX payload type for RFC2833

* Thu Feb 05 2009 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5342.1
- new version
- apply patch to change Hiawei SoftX payload type for RFC2833
- use spandsp6

* Tue Jul 29 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn5072.1
- new version

* Tue Jun 03 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt1.svn4782.1
- new version

* Fri Apr 11 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt0.svn4616.5
- add minimal working configuration with QUICKSTART
- docs subpackage changed

* Wed Apr 09 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt0.svn4616.4
- add configuration files

* Wed Apr 09 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt0.svn4616.3
- add startup files

* Wed Apr 09 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt0.svn4616.2
- apply patch to hide silenceSupp:off because some broken peers such as Hiawei SoftX can't handle it

* Tue Apr 08 2008 Eugene Prokopiev <enp@altlinux.ru> 1.2-alt0.svn4616.1
- first build for Sisyphus from git-svn

