Name: xtreemfs
Version: 1.5.1
Release: alt1

Summary: XtreemFS base package

License: BSD-3-Clause
Group: System/Servers
Url: http://www.XtreemFS.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.xtreemfs.org/downloads/XtreemFS-%version.tar

BuildRequires: ant >= 1.6.5 java-devel >= 1.6.0

# Client dependencies.
BuildRequires: gcc-c++ >= 4.1 fuse >= 2.6 libfuse-devel >= 2.6 libssl-devel >= 0.9.8 cmake >= 2.6 boost-program_options-devel >= 1.35 libattr-devel >= 2
BuildRequires: boost-interprocess-devel boost-asio-devel

Requires(pre):  %_sbindir/groupadd %_sbindir/useradd /bin/mkdir /bin/grep /bin/chmod /bin/chown /bin/chgrp %_bindir/stat

%description
XtreemFS is a distributed and replicated file system for the internet. For more details, visit www.xtreemfs.org.

%package client
Summary: XtreemFS client
Group: File tools
#Requires:       %name == %version-%release
Requires: fuse >= 2.6
Requires: attr >= 2

%description client
XtreemFS is a distributed and replicated file system for the internet. For more details, visit www.xtreemfs.org.

This package contains the XtreemFS client module.

%package backend
Summary: XtreemFS backend modules and libraries
Group: System/Servers
#Requires:       %name == %version-%release
Requires: jre >= 1.6.0

%description backend
XtreemFS is a distributed and replicated file system for the internet. For more details, visit www.xtreemfs.org.

This package contains the backend modules and libraries shared between the server and tools sub-packages.

%package server
Summary: XtreemFS server components (DIR, MRC, OSD)
Group: System/Servers
Requires: %name-backend = %version-%release
Requires: grep
Requires: jre >= 1.6.0
Requires(post): util-linux

%description server
XtreemFS is a distributed and replicated file system for the internet. For more details, visit www.xtreemfs.org.

This package contains the XtreemFS server components (DIR, MRC, OSD).

%package tools
Summary: XtreemFS administration tools
Group: File tools
Requires: %name-backend == %version-%release
Requires: attr >= 2
Requires: jre >= 1.6.0

%description tools
XtreemFS is a distributed and replicated file system for the internet. For more details, visit www.xtreemfs.org.

This package contains XtreemFS administration tools.

%prep
%setup -n XtreemFS-%version

%build
export ANT_OPTS=-D"file.encoding=UTF-8"
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS=$CFLAGS

%make_build

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true

%makeinstall_std
ln -sf %_bindir/mount.xtreemfs %buildroot/sbin/mount.xtreemfs
ln -sf %_bindir/umount.xtreemfs %buildroot/sbin/umount.xtreemfs

# add /etc/xos/xtreemfs/truststore/certs/ folder used for storing certificates
mkdir -p %buildroot/etc/xos/xtreemfs/truststore/certs/

# Create log directory.
mkdir -p %buildroot/var/log/xtreemfs

# remove copyright notes (let rpm handle that)
rm %buildroot%_docdir/xtreemfs-client/LICENSE
rmdir %buildroot%_docdir/xtreemfs-client
rm %buildroot%_docdir/xtreemfs-server/LICENSE
rmdir %buildroot%_docdir/xtreemfs-server
rm %buildroot%_docdir/xtreemfs-tools/LICENSE
rmdir %buildroot%_docdir/xtreemfs-tools

rm %buildroot/etc/xos/xtreemfs/postinstall_setup.sh

%pre server
%_sbindir/groupadd xtreemfs 2>/dev/null || :
%_sbindir/useradd -r --home /var/lib/xtreemfs -g xtreemfs xtreemfs 2>/dev/null || :
%_sbindir/usermod -g xtreemfs xtreemfs 2>/dev/null || :

%post server
#$XTREEMFS_CONFIG_DIR/postinstall_setup.sh
#!/bin/bash
set -e

XTREEMFS_LOG_DIR=/var/log/xtreemfs
XTREEMFS_HOME=/var/lib/xtreemfs
XTREEMFS_ETC=/etc/xos/xtreemfs
XTREEMFS_USER=xtreemfs
XTREEMFS_GROUP=xtreemfs
XTREEMFS_GENERATE_UUID_SCRIPT="${XTREEMFS_ETC}/generate_uuid"

# When executed during POST installation, do not be verbose.
VERBOSE=0
script_name=$(basename "$0")
if [ "$script_name" = "postinstall_setup.sh" ]
then
  VERBOSE=1
fi

# generate UUIDs
if [ -x "$XTREEMFS_GENERATE_UUID_SCRIPT" ]; then
  for service in dir mrc osd; do
    "$XTREEMFS_GENERATE_UUID_SCRIPT" "${XTREEMFS_ETC}/${service}config.properties"
    [ $VERBOSE -eq 1 ] && echo "Generated UUID for service: $service"
  done
else
  echo "UUID can't be generated automatically. Please enter a correct UUID in each config file of an XtreemFS service."
fi

group_exists=`grep -c $XTREEMFS_GROUP /etc/group || true`
if [ $group_exists -eq 0 ]; then
    groupadd $XTREEMFS_GROUP
    [ $VERBOSE -eq 1 ] && echo "created group $XTREEMFS_GROUP"
fi
exists=`grep -c $XTREEMFS_USER /etc/passwd || true`
if [ $exists -eq 0 ]; then
    mkdir $XTREEMFS_HOME
    useradd -r --home $XTREEMFS_HOME -g $XTREEMFS_GROUP $XTREEMFS_USER
    chown $XTREEMFS_USER $XTREEMFS_HOME
    [ $VERBOSE -eq 1 ] && echo "created user $XTREEMFS_USER and data directory $XTREEMFS_HOME"
fi
if [ ! -d $XTREEMFS_HOME ]; then
    mkdir -m750 $XTREEMFS_HOME
    chown $XTREEMFS_USER $XTREEMFS_HOME
    [ $VERBOSE -eq 1 ] && echo "user $XTREEMFS_USER exists but data directory $XTREEMFS_HOME had to be created"
fi
owner=`stat -c %U $XTREEMFS_HOME`
if [ "$owner" != "$XTREEMFS_USER" ]; then
    [ $VERBOSE -eq 1 ] && echo "directory $XTREEMFS_HOME is not owned by $XTREEMFS_USER, executing chown"
    chown $XTREEMFS_USER $XTREEMFS_HOME
fi

if [ ! -e $XTREEMFS_LOG_DIR ]; then
    mkdir $XTREEMFS_LOG_DIR
    chown -R $XTREEMFS_USER $XTREEMFS_LOG_DIR
fi

if [ -e $XTREEMFS_ETC ]; then
    group=`stat -c %G $XTREEMFS_ETC 2>/dev/null`
    if [ $group != $XTREEMFS_GROUP ]; then
        [ $VERBOSE -eq 1 ] && echo "directory $XTREEMFS_ETC is owned by $group, should be owned by $XTREEMFS_GROUP, executing chgrp (may take some time)"
        chgrp -R $XTREEMFS_GROUP $XTREEMFS_ETC
    fi
    for file in `ls $XTREEMFS_ETC/*.properties 2>/dev/null`; do
      if [ -f $file -a "$(stat -c %a $file)" != "640" ]; then
          [ $VERBOSE -eq 1 ] && echo "setting $file 0640, executing chmod"
          chmod 0640 $file
      fi
    done
    if [ -d "$XTREEMFS_ETC/truststore/" ]
    then
        if [ "$(stat -c %a "$XTREEMFS_ETC/truststore/")" != "750" ]
        then
            [ $VERBOSE -eq 1 ] && echo "setting $XTREEMFS_ETC/truststore/ to 0750, executing chmod (may take some time)"
            chmod -R u=rwX,g=rX,o= $XTREEMFS_ETC/truststore/
        fi
    fi
fi

%files client
%_bindir/*.xtreemfs
%_bindir/xtfsutil
/sbin/*.xtreemfs
%_man1dir/*.xtreemfs*
%_man1dir/xtfsutil*
%doc LICENSE

%files backend
%_datadir/java/XtreemFS.jar
%_datadir/java/Foundation.jar
%_datadir/java/protobuf-java-2.5.0.jar
%_datadir/java/Flease.jar
%_datadir/java/BabuDB.jar
%_datadir/java/BabuDB_replication_plugin.jar
%_datadir/java/jdmkrt.jar
%_datadir/java/jdmktk.jar
%_datadir/java/commons-codec-1.3.jar
%doc LICENSE

%files server
%defattr(-,root,xtreemfs,-)
%attr(-,root,root) /etc/init.d/xtreemfs-*
%dir %attr(-,root,root) %_datadir/xtreemfs
%attr(-,root,root) %_datadir/xtreemfs/xtreemfs-osd-farm
%dir /etc/xos/
%dir %attr(0750,root,xtreemfs) /etc/xos/xtreemfs/
%dir %attr(0750,root,xtreemfs) /etc/xos/xtreemfs/truststore/
%dir %attr(0750,root,xtreemfs) /etc/xos/xtreemfs/truststore/certs/
%config(noreplace) %attr(0640,root,xtreemfs) /etc/xos/xtreemfs/*.properties
/etc/xos/xtreemfs/generate_uuid
# /etc/xos/xtreemfs/postinstall_setup.sh
%dir /etc/xos/xtreemfs/server-repl-plugin/
%config(noreplace) %attr(0640,root,xtreemfs) /etc/xos/xtreemfs/server-repl-plugin/dir.properties
%config(noreplace) %attr(0640,root,xtreemfs) /etc/xos/xtreemfs/server-repl-plugin/mrc.properties
%dir %attr(0750,xtreemfs,xtreemfs) /var/log/xtreemfs
%doc LICENSE

%files tools
%config(noreplace) /etc/xos/xtreemfs/default_dir
%_bindir/xtfs_*
%_man1dir/xtfs_*
%doc LICENSE

%changelog
* Tue Jun 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- initial build for ALT Linux Sisyphus

