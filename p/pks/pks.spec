Summary: OpenPGP Public Key Server
Name: pks
Version: 0.9.6
Release: alt1
License: BSD-like (with advertising clause)
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dl.sf.net/sourceforge/pks/%name-%version.tar.bz2
Source1: %name.init
Patch0: mkpksdconf.in.patch
Requires: %name-db = %version
BuildPreReq: rpm-build-compat

# Automatically added by buildreq on Thu Apr 03 2008
BuildRequires: libwrap-devel

%description
This is a OpenPGP Public Key Server. It allows users to store and lookup
OpenPGP public keys from the server's database. Additionally, it can
synchronize with other servers to make a distributed, replicated
database of public keys.

This package provides only the server side. The client side is usually
an OpenPGP application (like PGP or GPG), although a simple HTML form
is provided to allow queries from a web page.

%package utils
Summary: OpenPGP Public Key Server Utilities
Group: System/Configuration/Other
Requires: %name = %version
%description utils
This package contains optional utilities for use with the
OpenPGP Public Key Server.

%package db
Summary: OpenPGP Public Key Server Database Engine
Group: Databases
Requires: %name = %version
%description db
This package contains the database utilities for use with the
OpenPGP Public Key Server.

%package db-devel
Summary: OpenPGP Public Key Server Database Libraries
Group: Development/Databases
Requires: %name = %version
%description db-devel
This package contains the database headers and libraries for use with the
OpenPGP Public Key Server.

%prep
%setup
%patch -p0

%build
%configure  \
            --datadir=%_datadir/pks \
            --sharedstatedir=/var/lib/%name \
            --localstatedir=/var/lib/%name \
            --with-libwrap
%make
%make all-utils

%install
make DESTDIR="%buildroot" install
make DESTDIR="%buildroot" install-utils
install -pm 0755 -D %SOURCE1 %buildroot%_initdir/%name
cp db2-sleepycat/LICENSE db2-sleepycat-LICENSE
cp db2-sleepycat/README db2-sleepycat-README
mkdir -p  %buildroot%_var/run/pks %buildroot%_var/lib/pks/incoming %buildroot%_var/lib/pks/db

%pre
/usr/sbin/groupadd -f -r _pks >/dev/null 2>&1 || :
/usr/sbin/useradd -r -g _pks -d /var/lib/%name -s /dev/null \
    -c "PKS user" -M -n _pks >/dev/null 2>&1 || :

%files
%doc README NEWS LICENSE db2-sleepycat-LICENSE db2-sleepycat-README
%doc mail_intro
%doc pks_help.de pks_help.dk pks_help.en pks_help.es pks_help.fi pks_help.fr pks_help.no
%doc MRHKP

%verify(not md5 size mtime) %config %_sysconfdir/pksd.conf
%_initdir/pks
%_datadir/pks
%_bindir/pksclient
%_sbindir/pksd
%_bindir/pksdctl
%_bindir/pgpsplit
%_bindir/pks-mail.sh
%_bindir/pks-queue-run.sh
%_man5dir/*.5.gz
%_man8dir/*.8.gz
%_var/lib/pks/index.html
%attr(2770,root,_pks) %dir %_var/run/pks
%attr(2770,root,_pks) %dir %_var/lib/pks
%attr(2770,root,_pks) %dir %_var/lib/pks/incoming

%files utils
%_bindir/pksmailreq
%_bindir/wwwtest
%_bindir/pgpdump
%_bindir/kvcv
%_bindir/kxa
%_bindir/pkscheck
%_bindir/pksdump

%files db
%_bindir/db_archive
%_bindir/db_checkpoint
%_bindir/db_deadlock
%_bindir/db_dump
%_bindir/db_load
%_bindir/db_printlog
%_bindir/db_recover
%_bindir/db_stat
%attr(2770,root,_pks) %dir %_var/lib/pks/db

%files db-devel
%_includedir/db2/db.h
%_includedir/db2/db_185.h
%_includedir/db2/db_cxx.h

%changelog
* Mon Mar 10 2008 Boris Savelev <boris@altlinux.org> 0.9.6-alt1
- initial build
