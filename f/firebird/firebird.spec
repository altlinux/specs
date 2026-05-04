%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# LTO causes errors, disable it
%global optflags_lto %nil

%define major 5.0.4
%define minor 0
%define pkgname Firebird
%define pkgversion %major-%minor
%define fbroot %_libdir/%name

Name: firebird
Version: %major
Release: alt1
Summary: Firebird SQL Database, fork of InterBase
Group: Databases
License: IPL
Url: https://www.firebirdsql.org/

VCS: https://github.com/FirebirdSQL/firebird.git
Source: %name-%version.tar
Source1: %name.init
Source2: %name.tmpfiles.conf.in
Source3: %name-logrotate
Patch0: %name-%version-%release.patch

# from OpenSuse
Patch101: %name-5.0.3-fedora-add-pkgconfig-files.patch

# from Debian to be sent upstream
Patch205: %name-5.0.3-debian-cloop-honour-build-flags.patch

# ALT patches
Patch1001: %name-5.0.3-alt-dont-link-libstdcxx-statically.patch
Patch1003: %name-5.0.3-alt-disable-examples.patch

# Elbrus
Patch2000: %name-5.0.3-e2k.patch

Requires: libfbclient = %EVR
# altbug #55658
Requires: libicu

BuildRequires(pre): rpm-build-compat
BuildRequires: libtinfo-devel libicu-devel libedit-devel
BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: cmake
BuildRequires: libtool
BuildRequires: libncurses-devel
BuildRequires: zlib-devel libtommath-devel
BuildRequires: libtomcrypt-devel
BuildRequires: libre2-devel
BuildRequires: unzip

Obsoletes: %name-superserver < %EVR
Conflicts: %name-superserver < %EVR
Provides: %name-superserver = %EVR
Obsoletes: %name-classic < %EVR
Conflicts: %name-classic < %EVR
Provides: %name-classic = %EVR

%description
This is the Firebird SQL Database shared files.

%package devel
Summary: Development Libraries for Firebird SQL Database
Group: Development/Databases
Requires: %name = %EVR

%description devel
Development libraries for firebird.

%package utils
Summary: Client programs for Firebird SQL Database
Group: Databases
Requires: %name = %EVR
Obsoletes: %name-client-embedded <= 2.0
Obsoletes: %name-utils-superserver < %EVR
Conflicts: %name-utils-superserver < %EVR
Provides: %name-utils-superserver = %EVR
Obsoletes: %name-utils-classic < %EVR
Conflicts: %name-utils-classic < %EVR
Provides: %name-utils-classic = %EVR

%description utils
Client access tools for firebird.

%package -n libfbclient
Summary: Multi-threaded, non-local client libraries for Firebird SQL Database
Group: System/Libraries

%description -n libfbclient
Multi-threaded, non-local client libraries for Firebird SQL Database

%package server
Summary: Server for Firebird SQL Database
Group: Databases
Requires: %name = %EVR
Obsoletes: %name-server-superserver < %EVR
Conflicts: %name-server-superserver < %EVR
Provides: %name-server-superserver = %EVR
Obsoletes: %name-server-classic < %EVR
Conflicts: %name-server-classic < %EVR
Provides: %name-server-classic = %EVR
Obsoletes: %name-server-common < %EVR
Conflicts: %name-server-common < %EVR
Provides: %name-server-common = %EVR
%add_findreq_skiplist %_sbindir/changeServerMode.sh

%description server
This is the server for the Firebird SQL Database.
It can also be used as an embedded server, when paired with the
client-embedded package.

It does not include any client access tools, nor does it include the
multi-threaded client library.

%package doc
Summary: Documentation for Firebird SQL server
Group: Databases
Requires: %name-server = %EVR
BuildArch: noarch

%description doc
Documentation for Firebird SQL server.

%package examples
Summary: Examples for Firebird SQL server
Group: Databases
Requires: %name-server = %EVR

%description examples
Examples for Firebird SQL server.

%prep
%setup
%patch0 -p1
%patch101 -p1
%patch205 -p1
%patch1001 -p1
%patch1003 -p1
%ifarch %e2k
%patch2000 -p1
%endif

# sed vs patch for portability and addtional location changes
# based on FIREBIRD=%_libdir/firebird
check_sed() {
	MSG="sed of $3, required $2 line(s) modified $1"
	echo "${MSG}"
	[[ $1 -ge $2 ]] || { echo "${MSG}" ; exit -1 ; }
}

check_sed "$(sed -i -e 's:"isql :"isql-fb :w /dev/stdout' \
	src/isql/isql.epp | wc -l)" "1" "src/isql/isql.epp" # 1 line

find . -name \*.sh -exec chmod +x {} + || { echo "chmod failed" ; exit -1 ; }
rm -rf ./extern/{editline,libtomcrypt,libtommath,re2,zlib} || { echo "rm -rf failed" ; exit -1 ;}

%build
%add_optflags -fno-sized-deallocation
%add_optflags -fno-delete-null-pointer-checks
%add_optflags -fno-strict-aliasing
%add_optflags -Wno-deprecated -Wno-switch
%add_optflags -I%_includedir/tommath
%add_optflags -I%_includedir/tomcrypt
%ifarch %e2k
# required to enable GNU extensions from fenv.h
%add_optflags -D_GNU_SOURCE
# workaround for "Include file for re2 not found"
export CXXFLAGS="%{optflags} -std=c++17"
%endif

%autoreconf
%configure \
	--disable-rpath \
	--disable-static \
	--prefix=%fbroot \
	--with-system-editline \
	--with-system-re2 \
	--with-fbbin=%_bindir \
	--with-fbsbin=%_sbindir \
	--with-fbconf=%_sysconfdir/%name \
	--with-fblib=%_libdir \
	--with-fbinclude=%_includedir \
	--with-fbdoc=%_defaultdocdir/%name \
	--with-fbsample=%_defaultdocdir/%name/sample \
	--with-fbsample-db=%_localstatedir/%name/data/ \
	--with-fbhelp=%_localstatedir/%name/system/ \
	--with-fbintl=%_libdir/%name/intl \
	--with-fbmisc=%_datadir/%name/misc \
	--with-fbsecure-db=%_localstatedir/%name/secdb/ \
	--with-fbmsg=%_localstatedir/%name/system/ \
	--with-fblog=%_logdir/%name \
	--with-fbglock=%_runtimedir/%name \
	--with-fbplugins=%_libdir/%name/plugins \
	--with-fbtzdata=%_localstatedir/%name/tzdata \
	%nil

%make

pushd gen
%make -f Makefile.install buildRoot
chmod -R u+w buildroot%{_docdir}/%{name}
chmod u+rw,a+rx buildroot/usr/include/firebird/impl
popd

%install
mkdir -p %buildroot
cp -r gen/buildroot/* %buildroot/

# prepare dir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%fbroot/intl
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_sysconfdir/profile.d
mkdir -p %buildroot%_localstatedir/%name/backup
mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_tmpfilesdir

cp -a src/misc/upgrade %buildroot%_datadir/%name

install -m 0644 gen/install/misc/firebird.service %buildroot%_unitdir/

sed -e "s|@runtimedir@|%_runtimedir|g" -e "s|@name@|%name|g" %SOURCE2 > %buildroot%_tmpfilesdir/%name.conf

cp -v gen/install/misc/*.pc %buildroot%_pkgconfigdir

pushd gen/Release/%name
# intl
cp intl/libfbintl.so %buildroot%fbroot/intl/fbintl.so
cp -a bin/posixLibrary.sh %buildroot%_datadir/%name
# examples
cp -a examples %buildroot%_datadir/%name
popd

mv %buildroot%fbroot/intl/fbintl.conf %buildroot%_sysconfdir/%name/fbintl.conf
ln -sf $(relative %_sysconfdir/%name/fbintl.conf %fbroot/intl/fbintl.conf) %buildroot%fbroot/intl/fbintl.conf
ln -sf fbintl.so %buildroot%fbroot/intl/libfbintl.so
ln -sf $(relative %fbroot/intl/fbintl.so %_sysconfdir/%name/libfbintl.so) %buildroot%_sysconfdir/%name/libfbintl.so

# services
install -m 755 %SOURCE1 %buildroot%_initdir/%name

# log
touch %buildroot%_logdir/%name/%name.log

# logrotate
mkdir -p %buildroot%_sysconfdir/logrotate.d
sed "s@%name.log@%_logdir/%name/%name.log@g" %SOURCE3 > %buildroot%_sysconfdir/logrotate.d/%name

mv %buildroot%_bindir/isql %buildroot%_bindir/isql-fb
mv %buildroot%_bindir/gstat %buildroot%_bindir/gstat-fb
mv %buildroot%_sbindir/fb_config %buildroot%_bindir/fb_config
mv %buildroot%_sysconfdir/%name/{*.md,*.txt} %buildroot%_docdir/%name/

rm -f %buildroot%_sbindir/FirebirdUninstall.sh
rm -rf %buildroot%_datadir/%name/misc/upgrade
rm -f %buildroot%_datadir/%name/misc/firebird.service
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.debian
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.generic
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.gentoo
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.mandrake
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.slackware
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.suse
rm -f %buildroot%_datadir/%name/misc/rc.config.firebird

# -----------------------------------------------------------------------------
# server-common scripts
# -----------------------------------------------------------------------------
%post server
if [ ! -f %_sysconfdir/gds_hosts.equiv ]; then
	echo localhost > %_sysconfdir/gds_hosts.equiv
fi
%post_service %name

%preun server
%preun_service %name

%pre
%_sbindir/groupadd -f -r %name 2>/dev/null ||:
%_sbindir/useradd -d %_localstatedir/%name -g %name -s /dev/null -r %name 2>/dev/null ||:

# Add gds_db to %_sysconfdir/services if needed
FileName=%_sysconfdir/services
newLine="gds_db          3050/tcp  # Firebird SQL Database Remote Protocol"
oldLine=`grep "^gds_db" $FileName`
if [ -z "$oldLine" ]; then
	echo $newLine >> $FileName
fi

%triggerun -- %name-server < 4.0.0.2496.0-alt1
if [ $2 -gt 0 ]; then
# This is firebird upgrade.
	SYSTEMCTL=/bin/systemctl
	if /sbin/sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1 ; then
# collect service states
		enable_server=0

		if "$SYSTEMCTL" is-enabled firebird-superserver.service >/dev/null 2>&1 ; then
			enable_server=1
		fi

# disable services with old names
		"$SYSTEMCTL" disable --now firebird-superserver.service ||:

# re-enable services with new names
		if [ $enable_server -eq 1 ] ; then
			"$SYSTEMCTL" enable --now firebird.service
		fi
	fi
fi

%files
%_docdir/%name/IDPLicense.txt
%_docdir/%name/IPLicense.txt
%doc doc/*
%dir %fbroot
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/databases.conf
%config(noreplace) %_sysconfdir/%name/fbtrace.conf
%config(noreplace) %_sysconfdir/%name/firebird.conf
%config(noreplace) %_sysconfdir/%name/plugins.conf
%config(noreplace) %_sysconfdir/%name/replication.conf
%dir %attr(2775,root,%name) %_localstatedir/%name
%dir %attr(2775,root,%name) %_localstatedir/%name/secdb
%dir %attr(2775,root,%name) %_localstatedir/%name/system
%dir %attr(2775,root,%name) %_localstatedir/%name/backup
%attr(0660,firebird,firebird) %config(noreplace) %_localstatedir/%name/secdb/security5.fdb
%attr(0664,firebird,firebird) %_localstatedir/%name/system/firebird.msg
%dir %_localstatedir/%name/tzdata
%_localstatedir/%name/tzdata/*.res
%dir %_datadir/%name
%dir %_datadir/%name/upgrade
%_datadir/%name/upgrade/*
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*
%dir %_datadir/%name/misc
%_datadir/%name/misc/*.sql

%files devel
%attr (0755,root,root) %_bindir/fb_config
%_bindir/gpre
%_includedir/*
%_libdir/libfbclient.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/gbak
%_bindir/gfix
%_bindir/gstat-fb
%_bindir/isql-fb
%_bindir/fbtracemgr

%files -n libfbclient
%_libdir/libfbclient.so.*

%files server
%config(noreplace) %_sysconfdir/logrotate.d/%name
%attr(0644,root,root) %_tmpfilesdir/%name.conf
%dir %fbroot/intl
%config(noreplace) %_sysconfdir/%name/fbintl.conf
%_sysconfdir/%name/libfbintl.so
%attr(0755,root,root) %_initdir/%name
%_unitdir/*
%dir %attr (2770,root,%name) %_logdir/%name
%attr (0660,%name,%name) %_logdir/%name/%name.log
%fbroot/intl/*
%_bindir/gsplit
%_bindir/nbackup
%_bindir/gsec
%_bindir/fbsvcmgr
%attr (0755,root,root) %_sbindir/*.sh
%_sbindir/fb_lock_print
%_sbindir/fbguard
%_sbindir/firebird
%_libdir/libib_util.so
%_datadir/%name/*.sh

%files doc
%_docdir/%name
%exclude %_docdir/%name/IDPLicense.txt
%exclude %_docdir/%name/IPLicense.txt
%exclude %_docdir/%name/sample

%files examples
%_docdir/%name/sample
%_datadir/%name/examples

%changelog
* Mon May 04 2026 Anton Farygin <rider@altlinux.org> 5.0.4-alt1
- 5.0.3 -> 5.0.4 (Fixes: CVE-2026-40342, CVE-2026-35215, CVE-2026-34232,
- CVE-2026-33337, CVE-2026-28224, CVE-2026-27890, CVE-2026-28214, CVE-2026-28212,
- CVE-2025-65104)

* Wed Jan 22 2026 Anton Farygin <rider@altlinux.com> 5.0.3-alt1
- 4.0.6 -> 5.0.3
- removed patches applied upstream: c++17, noexcept, loongarch
- adapted patches for new version

* Mon Sep 15 2025 Anton Farygin <rider@altlinux.com> 4.0.6-alt1
- 4.0.5 -> 4.0.6
- added an explicit dependency on libicu to prevent startup errors (closes: #55658)
- fixed the incorrect path to the intl module in the default fbintl config file (closes: #55673)

* Wed Oct 09 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.0.5-alt2
- e2k build fix

* Thu Aug 29 2024 Anton Farygin <rider@altlinux.ru> 4.0.5-alt1
- 4.0.0.2496.0 -> 4.0.5
- moved /var/lib/firebird from firefebird-server
  to the firebird package (closes: #47619)

* Sun Dec 03 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.0.0.2496.0-alt5
- NMU: LoongArch support (compile tested only).

* Tue Aug 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.2496.0-alt4
- Disabled LTO.

* Sat Aug 14 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.0.0.2496.0-alt3
- Added patch for Elbrus.

* Thu Aug 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.2496.0-alt2
- Updated include files location.

* Tue Aug 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.2496.0-alt1
- Updated to upstream version 4.0.0.2496-0.
- Built with system re2 library.

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.7.33374.0-alt1
- Updated to upstream version 3.0.7.33374-0.

* Mon Jul 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.6.33328.0-alt2
- Fixed runtime directory creation (Closes: #38722).

* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.6.33328.0-alt1
- Updated to upstream version 3.0.6.33328-0.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.5.33220.0-alt1
- Updated to upstream version 3.0.5.33220-0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.4.33054.0-alt1.qa1
- NMU: applied repocop patch

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.4.33054.0-alt1
- Updated to upstream version 3.0.4.33054-0.

* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt4
- Rebuilt with new libtommath.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt3
- Fixed init script once more (closes: #34060).
- Fixed issue with firebird not finding INTL module.
- Fixed config for xinetd.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt2
- Fixed init script (closes: #34060).
- Updated provides and obsoletes.

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt1
- Updated to upstream version 3.0.2.32703-0 (closes: #30271).

* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.5.18497.0-alt2.1
- Rebuild with new icu

* Thu Apr 04 2013 Dmitry V. Levin <ldv@altlinux.org> 2.1.5.18497.0-alt2
- Fixed build.

* Wed Apr 03 2013 Boris Savelev <boris@altlinux.org> 2.1.5.18497.0-alt1
- new version

* Fri Mar 16 2012 Boris Savelev <boris@altlinux.org> 2.1.4.18393.0-alt1
- new version

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 2.1.3.18185.0-alt4.3
- rebuilt for debuginfo
- enabled strict dependencies between subpackages

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.3.18185.0-alt4.2.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3.18185.0-alt4.2
- Rebuilt for soname set-versions

* Tue Mar 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt4.1
- rebuild with icu 4.4

* Sat Jan 23 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt4
- move %%_var/run/%%name to %%name-server-common (closes: #17689)
- fix permission on %%_sysconfdir/xinet.d/%%name

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt3
- fix owner on %%utilsshell

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt2
- fix perm on fbscripts (closes: #22751)
- move %%utilsshell to %%_bindir

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt1
- new version
- fix fbscripts (closes: #22596)

* Wed Jun 03 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt3
- fix gcc44 build

* Tue May 12 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt2
- fix #19660

* Thu Apr 09 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt1
- new verison
- fix #19448

* Fri Nov 07 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt6
- move adding service desription from firebird-server-common to firebird

* Sat Sep 27 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt5
- add functions library for shell scripts in share for server-common

* Thu Aug 21 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt4
- fix directory permissions
- move gpre to devel
- move common files of servers and utils to package firebird

* Tue Aug 19 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt3
- rename libfbintl.so to fbintl.so
- rename isql to fbsql (conflicts with unixODBC)

* Thu Aug 14 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt2
- close #16681

* Wed Aug 06 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt1
- initial build for Sisyphus
