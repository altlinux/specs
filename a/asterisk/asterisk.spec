# -*- mode: rpm-spec; mode: folding -*-

%ifarch %e2k
# doesn't compile with EDG frontend
%def_with clang
# -O3 is the default for e2k
%global _optlevel 2
%else
%def_without clang
%endif

Name: asterisk
Version: 20.5.0
Release: alt1

Summary: Open source PBX
License: GPLv2
Group: System/Servers
Url: https://www.asterisk.org/

Provides: asterisk-base = %version-%release
Obsoletes: asterisk-base

BuildRequires: curl gcc-c++
BuildRequires: libedit-devel libncurses-devel libuuid-devel libjansson-devel
BuildRequires: libsqlite3-devel libxml2-devel liburiparser-devel libxslt-devel
BuildRequires: libpopt-devel libspandsp-devel libfftw3-devel
BuildRequires: libcurl-devel libsrtp2-devel libjansson-devel
BuildRequires: libiksemel-devel libldap-devel libradiusclient-ng-devel
BuildRequires: libunixODBC-devel postgresql-devel zlib-devel
BuildRequires: libnet-snmp-devel libsystemd-devel
BuildRequires: rpm-build-python3
BuildRequires: gnu-config
%if_with clang
BuildRequires: clang clang-devel llvm llvm-devel
BuildRequires: libBlocksRuntime-devel
%endif

Source0: %name-%version-%release.tar

%package jabber
Summary: Google Talk and Jingle support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package ldap
Summary: LDAP support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package odbc
Summary: ODBC support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package pgsql
Summary: PostgreSQL support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package radius
Summary: RADIUS support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package snmp
Summary: SNMP support for Asterisk
Group: System/Servers
Requires: %name = %version-%release

%package devel
Summary: Development part for asterisk
Group: Development/C
Requires: %name = %version-%release

#{{{

%define desc Asterisk is an Open Source PBX and telephony toolkit.\
It is, in a sense, middleware between Internet and telephony channels\
on the bottom, and Internet and telephony applications at the top.\
However, Asterisk supports more telephony interfaces than just\
Internet telephony.  Asterisk also has a vast amount of support\
for traditional PSTN telephony, as well.

%description
%desc

%description jabber
%desc
This package provides Google Talk and Jingle support for Asterisk.

%description ldap
%desc
This package provides LDAP support for Asterisk.

%description odbc
%desc
This package provides ODBC support for Asterisk.

%description pgsql
%desc
This package provides PostgreSQL support for Asterisk.

%description radius
%desc
This package provides RADIUS support for Asterisk.

%description snmp
%desc
This package provides SNMP support for Asterisk.

%description devel
%desc
This package contains development part of Asterisk.

#}}}

%prep
%setup
%ifarch %e2k
# undefined reference to `llvm.objectsize.i64.p0i8'
sed -i "s/_FORTIFY_SOURCE=2/_FORTIFY_SOURCE=0/" configure{,.ac}
%endif

%build
export EXTERNALS_CACHE_DIR=$(pwd)/.gear
sh bootstrap.sh
cp -a /usr/share/gnu-config/config.{sub,guess} .
cp -a /usr/share/gnu-config/config.{sub,guess} menuselect/
# XXX: config.{sub,guess} from the top level source directory
# are automatically copied into third-party/pjproject/source directory
# cp -a /usr/share/gnu-config/config.{sub,guess} 'third-party/pjproject/source/'

%configure \
%if_with clang
	CC=clang \
	CXX=clang++ \
%endif
	--localstatedir=/var
%make_build

%install
%makeinstall_std install-headers
install -pm0755 -D alt/asterisk.init %buildroot%_initdir/asterisk
install -pm0644 -D alt/asterisk.service %buildroot%_unitdir/asterisk.service
install -pm0644 -D alt/asterisk.sysconfig %buildroot%_sysconfdir/sysconfig/asterisk
install -pm0644 -D alt/asterisk.tmpfiles %buildroot%_tmpfilesdir/asterisk.conf
cp -av alt/config/* %buildroot%_sysconfdir/asterisk
fgrep -rl '/usr/bin/env python' %buildroot%_datadir|xargs sed -i 's,env python,python3,'

#{{{

%pre
%_sbindir/groupadd -r -f _asterisk &> /dev/null
%_sbindir/useradd -r -g _asterisk -d /dev/null -s /dev/null -c 'Asterisk IP PBX' -n _asterisk &> /dev/null ||:

%post
%post_service asterisk

%preun
%preun_service asterisk

#}}}

# reqs finder chokes on shell with embedded python
%add_findreq_skiplist %_datadir/asterisk/scripts/ast_coredumper
%add_findreq_skiplist %_datadir/asterisk/scripts/ast_logescalator
%add_findreq_skiplist %_datadir/asterisk/scripts/ast_loggrabber
%add_findreq_skiplist %_datadir/asterisk/scripts/refcounter.py

#{{{

%files
%doc ChangeLogs/ChangeLog-20.5.0.md COPYING CREDITS LICENSE README* UPGRADE*.txt
%doc configs/samples configs/basic-pbx

%_initdir/asterisk
%_unitdir/asterisk.service
%config(noreplace) %_sysconfdir/sysconfig/asterisk

%dir %_sysconfdir/asterisk
%config(noreplace) %_sysconfdir/asterisk/acl.conf
%config(noreplace) %_sysconfdir/asterisk/asterisk.conf
%config(noreplace) %_sysconfdir/asterisk/cdr.conf
%config(noreplace) %_sysconfdir/asterisk/cdr_custom.conf
%config(noreplace) %_sysconfdir/asterisk/cel.conf
%config(noreplace) %_sysconfdir/asterisk/confbridge.conf
%config(noreplace) %_sysconfdir/asterisk/features.conf
%config(noreplace) %_sysconfdir/asterisk/indications.conf
%config(noreplace) %_sysconfdir/asterisk/logger.conf
%config(noreplace) %_sysconfdir/asterisk/modules.conf
%config(noreplace) %_sysconfdir/asterisk/pjproject.conf
%config(noreplace) %_sysconfdir/asterisk/pjsip.conf
%config(noreplace) %_sysconfdir/asterisk/pjsip_notify.conf
%config(noreplace) %_sysconfdir/asterisk/stasis.conf
%config(noreplace) %_sysconfdir/asterisk/udptl.conf

%_sbindir/astdb2bdb
%_sbindir/astdb2sqlite3
%_sbindir/asterisk
%_sbindir/rasterisk
%_sbindir/astcanary
%_sbindir/astgenkey
%_sbindir/astversion
%_sbindir/autosupport
%_sbindir/safe_asterisk

%_libdir/libasteriskpj.so.2
%_libdir/libasteriskssl.so.1

%dir %_libdir/asterisk
%_libdir/asterisk/modules

%exclude %_libdir/asterisk/modules/chan_motif.so
%exclude %_libdir/asterisk/modules/res_xmpp.so
%exclude %_libdir/asterisk/modules/res_config_ldap.so
%exclude %_libdir/asterisk/modules/cdr_radius.so
%exclude %_libdir/asterisk/modules/cel_radius.so
%exclude %_libdir/asterisk/modules/cdr_adaptive_odbc.so
%exclude %_libdir/asterisk/modules/cdr_odbc.so
%exclude %_libdir/asterisk/modules/cel_odbc.so
%exclude %_libdir/asterisk/modules/func_odbc.so
%exclude %_libdir/asterisk/modules/res_config_odbc.so
%exclude %_libdir/asterisk/modules/res_odbc.so
%exclude %_libdir/asterisk/modules/res_odbc_transaction.so
%exclude %_libdir/asterisk/modules/cdr_pgsql.so
%exclude %_libdir/asterisk/modules/cel_pgsql.so
%exclude %_libdir/asterisk/modules/res_config_pgsql.so
%exclude %_libdir/asterisk/modules/cdr_radius.so
%exclude %_libdir/asterisk/modules/cel_radius.so
%exclude %_libdir/asterisk/modules/res_snmp.so

%_libexecdir/asterisk/agi-bin

%_datadir/asterisk/documentation
%_datadir/asterisk/firmware
%_datadir/asterisk/images
%_datadir/asterisk/keys
%_datadir/asterisk/moh
%_datadir/asterisk/phoneprov
%_datadir/asterisk/rest-api
%_datadir/asterisk/scripts
%_datadir/asterisk/sounds
%_datadir/asterisk/static-http
%_datadir/asterisk/third-party

%_man8dir/astdb2bdb.8*
%_man8dir/astdb2sqlite3.8*
%_man8dir/asterisk.8*
%_man8dir/astgenkey.8*
%_man8dir/autosupport.8*
%_man8dir/safe_asterisk.8*

%dir %attr(0770,root,_asterisk) %_localstatedir/asterisk

%dir %attr(0770,root,_asterisk) %_logdir/asterisk
%dir %attr(0770,root,_asterisk) %_logdir/asterisk/cdr-csv
%dir %attr(0770,root,_asterisk) %_logdir/asterisk/cdr-custom
%dir %attr(0770,root,_asterisk) %_logdir/asterisk/cel-custom

%dir %_spooldir/asterisk
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/dictate
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/meetme
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/monitor
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/recording
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/system
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/tmp
%dir %attr(0770,root,_asterisk) %_spooldir/asterisk/voicemail

# /var/run/asterisk
%_tmpfilesdir/asterisk.conf

%files jabber
%config(noreplace) %_sysconfdir/asterisk/motif.conf
%config(noreplace) %_sysconfdir/asterisk/xmpp.conf
%_libdir/asterisk/modules/chan_motif.so
%_libdir/asterisk/modules/res_xmpp.so

%files ldap
%config(noreplace) %_sysconfdir/asterisk/res_ldap.conf
%_libdir/asterisk/modules/res_config_ldap.so

%files odbc
%config(noreplace) %_sysconfdir/asterisk/cdr_adaptive_odbc.conf
%config(noreplace) %_sysconfdir/asterisk/cdr_odbc.conf
%config(noreplace) %_sysconfdir/asterisk/cel_odbc.conf
%config(noreplace) %_sysconfdir/asterisk/func_odbc.conf
%config(noreplace) %_sysconfdir/asterisk/res_odbc.conf
%_libdir/asterisk/modules/cdr_adaptive_odbc.so
%_libdir/asterisk/modules/cdr_odbc.so
%_libdir/asterisk/modules/cel_odbc.so
%_libdir/asterisk/modules/func_odbc.so
%_libdir/asterisk/modules/res_config_odbc.so
%_libdir/asterisk/modules/res_odbc.so
%_libdir/asterisk/modules/res_odbc_transaction.so

%files pgsql
%config(noreplace) %_sysconfdir/asterisk/cdr_pgsql.conf
%config(noreplace) %_sysconfdir/asterisk/cel_pgsql.conf
%config(noreplace) %_sysconfdir/asterisk/res_pgsql.conf
%_libdir/asterisk/modules/cdr_pgsql.so
%_libdir/asterisk/modules/cel_pgsql.so
%_libdir/asterisk/modules/res_config_pgsql.so

%files radius
%_libdir/asterisk/modules/cdr_radius.so
%_libdir/asterisk/modules/cel_radius.so

%files snmp
%config(noreplace) %_sysconfdir/asterisk/res_snmp.conf
%_libdir/asterisk/modules/res_snmp.so

%files devel
%_includedir/asterisk.h
%_includedir/asterisk
%_libdir/libasteriskpj.so
%_libdir/libasteriskssl.so

#}}}

%changelog
* Thu Nov 02 2023 Alexei Takaseev <taf@altlinux.org> 20.5.0-alt1
- 20.5.0

* Thu Nov 02 2023 Alexei Takaseev <taf@altlinux.org> 20.2.1-alt1
- 20.2.1 (ALT#46017)

* Fri Oct 20 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 17.5.1-alt2.4
- NMU: fixed FTBFS on LoongArch (use fresh config.guess/sub).

* Fri Jul 28 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 17.5.1-alt2.3
- configure.ac: removed the use of the AC_HEADER_STDC macro to address build
  issues with autoconf 2.70+.

* Tue Jul 25 2023 Artyom Bystrov <arbars@altlinux.org> 17.5.1-alt2.2
- Use working version of autoconf

* Thu Jan 27 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 17.5.1-alt2.1
- fixed build for Elbrus

* Tue May 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5.1-alt2
- fix build with recent changes in rpm-build-python*

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5.1-alt1
- 17.5.1 released

* Wed Aug 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.4.1-alt1
- 16.4.1 released
- built with bundled pjproject (closes: 37149)

* Thu Jun 27 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.4.0-alt1
- 16.4.0 released

* Fri Apr 05 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.6.1-alt2
- drop redundant libpq-devel BR

* Thu Sep 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.6.1-alt1
- 15.6.1 released
