%define major 2.1.4.18393
%define minor 0
%define pkgname Firebird
%define pkgversion %major-%minor
%define fbroot %_libdir/%name
%define workdir %_builddir/work/%pkgname-%pkgversion
# all binary utils exept isql. isql rename to fbsql.
%define utilsbin gdef gbak gfix gstat qli
%define serverbin gsec fb_lock_print fbsvcmgr
%define utilsshell changeDBAPassword.sh createAliasDB.sh
Name: firebird
Version: %major.%minor
Release: alt1
Summary: Firebird SQL Database, fork of InterBase
Group: Databases
License: IPL
Url: http://www.firebirdsql.org/
Packager: Boris Savelev <boris@altlinux.org>
Source: %pkgname-%pkgversion.tar
Source1: %name.init
Source2: %name.xinetd

Patch: firebird-2.1.2.18118.0-deps-flags-libs.patch
Patch1: firebird-gcc44-build.patch
Patch2: firebird-update-valgrind.patch
Patch3: firebird-scl.epp.patch
Patch4: firebird-alt-buffer.patch

Requires: libfbclient = %version-%release
Requires: libfbembed = %version-%release

BuildPreReq: rpm-build-compat
BuildRequires: libtinfo-devel libicu-devel libedit-devel
BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: libtool
BuildRequires: libncurses-devel

%description
This is the Firebird SQL Database shared files.

%files
%doc work/%pkgname-%pkgversion/doc/*
%dir %fbroot
%dir %fbroot/help
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/aliases.conf
%config(noreplace) %_sysconfdir/%name/firebird.conf
%fbroot/*.msg
%fbroot/help/*
%dir %_datadir/%name
%dir %_datadir/%name/upgrade
%_datadir/%name/upgrade/*
%dir %_datadir/%name/examples
%_datadir/%name/examples/*

%package classic
Summary: Meta-package for Firebird SQL Classic Database (xinetd based)
Group: Databases
Provides: %name-arch = %version-%release
Requires: %name-server-classic = %version
Requires: %name-utils-classic = %version
Conflicts: %name-superserver

%description classic
This is a meta-package for easy selecting the Classic arch for Firebird 2

%files classic
%package superserver
Summary: Meta-package for Firebird SQL SuperServer Database (standalone)
Group: Databases
Provides: %name-arch = %version-%release
Requires: %name-server-superserver = %version
Requires: %name-utils-superserver = %version
Conflicts: %name-classic

%description superserver
This is a meta-package for easy selecting the SuperServer arch for Firebird 2

%files superserver
#
# Development headers and static libraries
#
%package devel
Summary: Development Libraries for Firebird SQL Database
Group: Development/Databases
Requires: %name = %version-%release

%description devel
Development libraries for firebird.

%files devel
%attr (0755,root,root) %_bindir/fb_config
%_bindir/gpre
%_includedir/*
%_libdir/*.so

#
# Standard client programs
#

#
# Utils programs (classic)
#
%package utils-classic
Summary: Client programs for Firebird SQL Database
Group: Databases
Requires: %name = %version-%release
Provides: %name-utils = %version-%release
Conflicts: %name-utils-superserver
Obsoletes: %name-client-embedded <= 2.0

%description utils-classic
Client access tools for firebird.

%files utils-classic
%_bindir/gbak.classic
%_bindir/gdef.classic
%_bindir/gfix.classic
%_bindir/gstat.classic
%_bindir/fbsql.classic
%_bindir/qli.classic

#
# Utils programs (superserver)
#
%package utils-superserver
Summary: Client programs for Firebird SQL Database
Group: Databases
Requires: %name = %version-%release
Provides: %name-utils = %version-%release
Conflicts: %name-utils-classic

%description utils-superserver
Client access tools for firebird.

%files utils-superserver
%_bindir/gbak.superserver
%_bindir/gdef.superserver
%_bindir/gfix.superserver
%_bindir/gstat.superserver
%_bindir/fbsql.superserver
%_bindir/qli.superserver

#
# Multi-threaded, independant client libraries
#
%package -n libfbclient
Summary: Multi-threaded, non-local client libraries for Firebird SQL Database
Group: System/Libraries

%description -n libfbclient
Multi-threaded, non-local client libraries for Firebird SQL Database

%files -n libfbclient
%_libdir/libfbclient.so.*

#
# Multi-process, independant client libraries
#
%package -n libfbembed
Summary: Multi-process, non-local client libraries for Firebird SQL Database
Group: System/Libraries

%description -n libfbembed
Multi-process, non-local client libraries for Firebird SQL Database

%files -n libfbembed
%_libdir/libfbembed.so.*

#
# Classic server programs
#
%package server-classic
Summary: Classic (xinetd) server for Firebird SQL Database
Group: Databases
Provides: firebird-server = %version-%release
Requires: xinetd
Requires: %name-server-common = %version-%release
Conflicts: %name-server-superserver

%description server-classic
This is the classic (xinetd) server for the Firebird SQL Database.
It can also be used as an embedded server, when paired with the
client-embedded package.

It does not include any client access tools, nor does it include the
multi-threaded client library.

%files server-classic
%config(noreplace) %attr(640,root,root) %_sysconfdir/xinetd.d/%name
%_bindir/fb_inet_server
%_bindir/fb_lock_mgr
%_bindir/fb_lock_print.classic
%_bindir/gds_drop
%_bindir/gsec.classic
%_bindir/fbsvcmgr.classic

#
# Super server programs
#
%package server-superserver
Summary: Superserver (single process) server for Firebird SQL Database
Group: Databases
Provides: firebird-server = %version-%release
#Requires: %name
Requires: %name-server-common = %version-%release
Conflicts: %name-server-classic

%description server-superserver
This is the Superserver (single process) for the Firebird SQL Database.

It does not include any client access tools, nor does it include the
multi-threaded client library.

%files server-superserver
%attr(0755,root,root) %_initdir/%name
%_bindir/fb_lock_print.superserver
%_bindir/fbguard
%_bindir/fbmgr.bin
%_bindir/fbmgr
%_bindir/fbserver
%_bindir/gsec.superserver
%_bindir/fbsvcmgr.superserver

#
# Server's common files
#
%package server-common
Summary: Common files for Firebird SQL Database servers
Group: Databases
Conflicts: firebird-server-classic < 2.0
Obsoletes: %name-server-superserver < 2.0.1.12855.0
Requires: %name = %version-%release

%description server-common
This package contains common files between firebird-server-classic and
firebird-server-superserver. You will need this if you want to use either one.

%files server-common
%dir %attr(2775,root,%name) %_var/run/%name
%dir %attr(2775,root,%name) %_localstatedir/%name/backup
%dir %attr(2775,root,%name) %_localstatedir/%name
#ghost %_sysconfdir/gds_hosts.equiv
%dir %fbroot/UDF
%dir %fbroot/intl
%config %attr (0660,%name,%name) %_sysconfdir/%name/security2.fdb
%config(noreplace) %_sysconfdir/%name/fbintl.conf
%dir %attr (2770,root,%name) %_logdir/%name
%attr (0660,%name,%name) %_logdir/%name/%name.log
%fbroot/UDF/*
%fbroot/intl/*
# in mandriva they in common. is they different?
# %_bindir/gdef
# %_bindir/gsec
%_bindir/gsplit
%_bindir/nbackup
%attr (0755,root,root) %_bindir/*.sh
%_datadir/%name/*.sh

%prep
rm -rf %_builddir/work
mkdir -p %_builddir/work
tar -xf %SOURCE0
mv %pkgname-%pkgversion work
cd %workdir
%patch0 -p1
%patch1 -p2
%patch2 -p0
%patch3 -p3
%patch4 -p2

# compile time relative path hacks, ew :(
for d in ../etc usr var/log/firebird var/run/firebird ; do
    rm -rf %workdir/../$d
    mkdir -p %workdir/../$d
done
cd "%workdir/../usr"; ln -sf "%workdir/gen/firebird/bin"
cd "%workdir/../../etc"; ln -sf "%workdir/gen/firebird" firebird
cd "%workdir"

function check_sed() {
        MSG="sed of $3, required $2 lines modified $1"
        [[ $1 -ge $2 ]]
}
# sed vs patch for portability and addtional location changes
# based on FIREBIRD=%_libdir/firebird
	check_sed "$(sed -i -e 's:"aliases.conf":"../../..%_sysconfdir/firebird/aliases.conf":w /dev/stdout' \
		src/jrd/db_alias.cpp | wc -l )" "1" "src/jrd/db_alias.cpp" # 1 line
	check_sed "$(sed -i -e 's:"isc_event1:"../../../var/run/firebird/isc_event1:w /dev/stdout' \
		-e 's:"isc_lock1:"../../../var/run/firebird/isc_lock1:w /dev/stdout' \
		-e 's:"isc_init1:"../../../var/run/firebird/isc_init1:w /dev/stdout' \
		-e 's:"isc_guard1:"../../../var/run/firebird/isc_guard1:w /dev/stdout' \
		-e 's:"isc_monitor1:"../../../var/run/firebird/isc_monitor1:w /dev/stdout' \
		-e 's:"firebird.log":"../../../var/log/firebird/firebird.log":w /dev/stdout' \
		-e 's:"security2.fdb":"../../..%_sysconfdir/firebird/security2.fdb":w /dev/stdout' \
		src/jrd/file_params.h | wc -l)" "12" "src/jrd/file_params.h" # 12 lines
	check_sed "$(sed -i -e 's:"security2.fdb":"../../..%_sysconfdir/firebird/security2.fdb":w /dev/stdout' \
		src/jrd/jrd_pwd.h | wc -l)" "1" "src/jrd/jrd_pwd.h" # 1 line
	check_sed "$(sed -i -e 's:"firebird.conf":"../../..%_sysconfdir/firebird/firebird.conf":w /dev/stdout' \
		src/jrd/os/config_root.h | wc -l)" "1" "src/jrd/os/config_root.h" # 1 line
	check_sed "$(sed -i -e 's:"bin/fb_cache_print":"../../..%_bindir/fb_cache_print":w /dev/stdout' \
		-e 's:"bin/fb_lock_print":"../../..%_bindir/fb_lock_print":w /dev/stdout' \
		-e 's:"bin/fb_cache_manager":"../../..%_bindir/fb_cache_manager":w /dev/stdout' \
		-e 's:"bin/gstat":"../../..%_bindir/gstat":w /dev/stdout' \
		-e 's:"bin/gbak":"../../..%_bindir/gbak":w /dev/stdout' \
		-e 's:"bin/gdef":"../../..%_bindir/gdef":w /dev/stdout' \
		-e 's:"bin/gsec":"../../..%_bindir/gsec":w /dev/stdout' \
		-e 's:"bin/gjrn":"../../..%_bindir/gjrn":w /dev/stdout' \
		-e 's:"bin/gfix":"../../..%_bindir/gfix":w /dev/stdout' \
		src/jrd/svc.cpp | wc -l)" "26" "src/jrd/svc.cpp" # 26 lines
	check_sed "$(sed -i -e 's:"bin/fb_lock_mgr":"../../..%_bindir/fb_lock_mgr":w /dev/stdout' \
		src/lock/lock.cpp | wc -l)" "1" "src/lock/lock.cpp" # 1 line
	check_sed "$(sed -i -e 's:m_Root_Path + "firebird.conf":"../../..%_sysconfdir/firebird/firebird.conf":w /dev/stdout' \
		src/utilities/fbcpl/fbdialog.cpp | wc -l)" "1" "src/utilities/fbcpl/fbdialog.cpp" # 1 line
	check_sed "$(sed -i -e 's:"security2.fdb":"../../..%_sysconfdir/firebird/security2.fdb":w /dev/stdout' \
		src/utilities/gsec/security.epp | wc -l)" "1" "src/utilities/gsec/security.epp" # 1 line
	check_sed "$(sed -i -e 's:"bin/fbserver":"../../..%_bindir/fbserver":w /dev/stdout' \
		src/utilities/guard/guard.cpp | wc -l)" "1" "src/utilities/guard/guard.cpp" # 1 line
	check_sed "$(sed -i -e 's:"bin/fbguard":"../../..%_bindir/fbguard":w /dev/stdout' \
		src/utilities/ibmgr/ibmgr.h | wc -l)" "1" "src/utilities/ibmgr/ibmgr.h" # 1 line
	check_sed "$(sed -i -e 's:$FIREBIRD/firebird.log:/var/log/firebird/firebird.log:w /dev/stdout' \
		src/utilities/ibmgr/srvrmgr.cpp | wc -l)" "1" "src/utilities/ibmgr/srvrmgr.cpp" # 1 line

# Rename references to isql to fbsql
	check_sed "$(sed -i -e 's:"isql :"fbsql :w /dev/stdout' \
		src/isql/isql.epp | wc -l)" "1" "src/isql/isql.epp" # 1 line
	check_sed "$(sed -i -e 's:isql :fbsql :w /dev/stdout' \
		src/msgs/history.sql | wc -l)" "4" "src/msgs/history.sql" # 4 lines
	check_sed "$(sed -i -e 's:isql :fbsql :w /dev/stdout' \
		src/msgs/history2.sql | wc -l)" "4" "src/msgs/history2.sql" # 4 lines
	check_sed "$(sed -i -e 's:isql :fbsql :w /dev/stdout' \
		-e 's:ISQL :FBSQL :w /dev/stdout' \
		src/msgs/messages.sql | wc -l)" "4" "src/msgs/messages.sql" # 4 lines
	check_sed "$(sed -i -e 's:--- ISQL:--- FBSQL:w /dev/stdout' \
		-e 's:isql :fbsql :w /dev/stdout' \
		-e 's:ISQL :FBSQL :w /dev/stdout' \
		src/msgs/messages2.sql | wc -l)" "6" "src/msgs/messages2.sql" # 6 lines

find . -name \*.sh -print0 | xargs -0 chmod +x
rm -rf extern/{editline,icu}

%build
# server-superserver
cd %workdir
mkdir -p m4
%autoreconf
%configure \
--prefix=%fbroot \
--with-system-editline \
--with-system-icu \
--enable-superserver
# Can't use %%make as itsparallel build is broken
make
mv gen/%name gen/superserver

# server-classic
cd %workdir
%configure \
--prefix=%fbroot \
--with-system-editline \
--with-system-icu
# Can't use %%make as itsparallel build is broken
make
ln -sf %name gen/classic

%install
function installbin() {
# goto fbroot
    cd %workdir/gen/$1
# remove scripts
    rm -rf bin/*.sh
# different binaries on classic and super
    for f in %utilsbin %serverbin isql; do
	mv bin/$f bin/$f.$1
    done
    cp -a bin/* %buildroot%_bindir
}

# prepare dir
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sysconfdir/xinetd.d
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%fbroot/help
mkdir -p %buildroot%fbroot/UDF
mkdir -p %buildroot%fbroot/intl
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_sysconfdir/profile.d
mkdir -p %buildroot%_var/run/%name
mkdir -p %buildroot%_localstatedir/%name/backup
mkdir -p %buildroot%_logdir/%name/
cd %workdir/gen/%name
# scripts
for f in %utilsshell ; do
    mv bin/$f %buildroot%_bindir
done
mv bin/posixLibrary.sh %buildroot%_datadir/%name
# libs
cp -a lib/* %buildroot%_libdir
cp *.msg %buildroot%fbroot
cp help/*.fdb %buildroot%fbroot/help
cp include/* %buildroot%_includedir
# etc
cp misc/* %buildroot%_sysconfdir/%name
cp ../install/misc/aliases.conf %buildroot%_sysconfdir/%name
%__subst 's|%_libdir|%_datadir|g' %buildroot%_sysconfdir/%name/aliases.conf
cp security2.fdb %buildroot%_sysconfdir/%name
# UDF
cp UDF/* %buildroot%fbroot/UDF
# intl
cp intl/libfbintl.so %buildroot%fbroot/intl/fbintl.so
cp ../install/misc/fbintl.conf %buildroot%_sysconfdir/%name
ln -sf %_sysconfdir/%name/fbintl.conf %buildroot%fbroot/intl/fbintl.conf
# services
install -m 755 %SOURCE1 %buildroot%_initdir/%name
install -m 755 %SOURCE2 %buildroot%_sysconfdir/xinetd.d/%name
# depended
installbin classic
installbin superserver
mv %buildroot%_bindir/isql.classic %buildroot%_bindir/fbsql.classic
mv %buildroot%_bindir/isql.superserver %buildroot%_bindir/fbsql.superserver
ln -sf %_bindir/fbmgr.bin %buildroot%_bindir/fbmgr
# log
touch %buildroot%_logdir/%name/%name.log
# examples
cp -a examples %buildroot%_datadir/%name
cp -a %workdir/src/misc/upgrade %buildroot%_datadir/%name

#touch %buildroot%_sysconfdir/gds_hosts.equiv

# -----------------------------------------------------------------------------
# server-common scripts
# -----------------------------------------------------------------------------
%post server-common
if [ ! -f %_sysconfdir/gds_hosts.equiv ]; then
	echo localhost > %_sysconfdir/gds_hosts.equiv
fi
# -----------------------------------------------------------------------------
# server-classic scripts
# -----------------------------------------------------------------------------
%post server-classic
for f in %serverbin; do
    if [ -e %_bindir/$f.classic ]; then
	ln -sf %_bindir/$f.classic %_bindir/$f
    fi
done
%post_service xinetd

%preun server-classic
%preun_service xinetd
for f in %serverbin; do
    if [ "$(readlink %_bindir/$f)" = "%_bindir/$f.classic" ]; then
	rm -f %_bindir/$f
    fi
done
# -----------------------------------------------------------------------------
# server-superserver scripts
# -----------------------------------------------------------------------------
%post server-superserver
for f in %serverbin; do
    if [ -e %_bindir/$f.superserver ]; then
	ln -sf %_bindir/$f.superserver %_bindir/$f
    fi
done
%post_service %name

%preun server-superserver
%preun_service %name
for f in %serverbin; do
    if [ "$(readlink %_bindir/$f)" = "%_bindir/$f.superserver" ]; then
	rm -f %_bindir/$f
    fi
done
# -----------------------------------------------------------------------------
# utils-classic scripts
# -----------------------------------------------------------------------------
%post utils-classic
for f in %utilsbin fbsql ; do
    if [ -e %_bindir/$f.classic ]; then
	ln -sf %_bindir/$f.classic %_bindir/$f
    fi
done

%preun utils-classic
for f in %utilsbin fbsql ; do
    if [ "$(readlink %_bindir/$f)" = "%_bindir/$f.classic" ]; then
	rm -f %_bindir/$f
    fi
done
# -----------------------------------------------------------------------------
# utils-superserver scripts
# -----------------------------------------------------------------------------
%post utils-superserver
for f in %utilsbin fbsql ; do
    if [ -e %_bindir/$f.superserver ]; then
	ln -sf %_bindir/$f.superserver %_bindir/$f
    fi
done

%preun utils-superserver
for f in %utilsbin fbsql ; do
    if [ "$(readlink %_bindir/$f)" = "%_bindir/$f.superserver" ]; then
	rm -f %_bindir/$f
    fi
done
# -----------------------------------------------------------------------------
# server-common scripts
# -----------------------------------------------------------------------------
%pre server-common
# Create the firebird group if it doesn't exist
%_sbindir/groupadd -f -r %name 2>/dev/null ||:
%_sbindir/useradd -d %_localstatedir/%name -g %name -s /dev/null -r %name 2>/dev/null ||:

# -----------------------------------------------------------------------------
# firebird scripts
# -----------------------------------------------------------------------------
%pre
# Add gds_db to %_sysconfdir/services if needed
FileName=%_sysconfdir/services
newLine="gds_db          3050/tcp  # Firebird SQL Database Remote Protocol"
oldLine=`grep "^gds_db" $FileName`
if [ -z "$oldLine" ]; then
	echo $newLine >> $FileName
fi

%changelog
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
- move %_var/run/%name to %name-server-common (closes: #17689)
- fix permission on %_sysconfdir/xinet.d/%name

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt3
- fix owner on %utilsshell

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt2
- fix perm on fbscripts (closes: #22751)
- move %utilsshell to %_bindir

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

* Tue Mar 11 2008 Tiago Salem <salem@mandriva.com.br> 2.0.3.12981.0-2mdv2008.1
+ Revision: 186539
- Fix initscript and create %_sysconfdir/gds_hosts.equiv on %%post to fix bug #34267
- bump release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 13 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.3.12981.0-1mdv2008.0
+ Revision: 84989
- New upstream: 2.0.3.12981, fixing an annoying bug.

* Fri Aug 24 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.2.12964.0-3mdv2008.0
+ Revision: 71056
- New upstream: 2.0.2

* Fri Aug 17 2007 Funda Wang <fundawang@mandriva.org> 2.0.1.12855.0-3mdv2008.0
+ Revision: 64705
- fix obsoletes old package

* Wed Aug 15 2007 Funda Wang <fundawang@mandriva.org> 2.0.1.12855.0-2mdv2008.0
+ Revision: 63722
- Fix file conflict

* Wed May 09 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.1.12855.0-1mdv2008.0
+ Revision: 25665
- New upstream: 2.0.1
- Removed patch amd64: applied upstream.

* Fri Jan 19 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-8mdv2007.0
+ Revision: 110615
- Improve firebird-classic and firebird-superserver summaries in order
  to explicit their difference: xinetd and standalone.

* Fri Nov 24 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-7mdv2007.1
+ Revision: 86946
- Added /var/lib/firebird and /var/lib/firebird/backup to server-common
  package.

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-6mdv2007.1
+ Revision: 84834
- Try libncurses-devel instead
- Added buildrequires to libncurses5-devel
- New upstream: 2.0.0.12748 (2.0.0 final)
- Fully disabled parallel build, as it is broken for now.
- Bumped release, in order to be able to rebuild for x86_64.
- Added missing BuildRequires to libtermcap-devel, as required by included
  readline.

* Wed Sep 13 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-4mdv2007.0
+ Revision: 61079
- Added Conflicts in firebird-server-common to firebird-firebird-server-classic
  < 2.0 due to moved files.
- Fix binaries ownership in firebird-server-classic. They should be owned by
  root:root and not firebird:firebird.

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-3mdv2007.0
+ Revision: 59998
- Applied Philippe Makowski suggestions:
  * Include example employee.fdb
  * -devel should requires libfbclient
  * Tagged security2.fdb as config.

* Tue Sep 05 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-2mdv2007.0
+ Revision: 59875
- Disabled parallel build: it's broken.
- Import firebird

* Sat Sep 02 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-1mdv2007.0
- Major packaging restructuring, following debian style.
- Enabled superserver flavor.
- Enhanced pre/post sections.
- Do not remove firebird user on package removal: we may leave some files on
  the filesystem.

* Thu Aug 24 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 2.0.0.12724-0.1mdk
- Update to Firebird2

* Tue Jul 26 2005 Stew Benedict <sbenedict@mandriva.com> 1.5.2.4731-0.3mdk
- fix provides in lib package

* Fri Jan 28 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2.4731-0.2mdk
- add deps
- little spec cleaning

* Wed Jan 12 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2.4731-0.1mdk
- from Philippe Makowski <makowski@firebird-fr.eu.org> :
	- adapted to Mandrake
	- updated from the CVS tree
- libification
- bzip2 patches
- use configure macros
- requires on versions not on releases

* Wed Aug 18 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.1.4481-0.fdr.1
- updated to 1.5.1 official source release
- minimized install patch intrusiveness, move files in .spec file instead
- don't try to remove the user/group on install, just leave the mess

* Wed Feb 04 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.0.4280-postRC8.1
- updated to CVS code
- remove lock files from post/postun
- set target arch to match prefix.linux settings
- add dependencies to firebird RPM

* Tue Feb 03 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.0.4201-1
- updated to RC8 code
- added gds_db service entry to %_sysconfdir/services if necessary in post
- fix isql link

