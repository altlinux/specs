%define _groupname	mfs
%define _username	mfs
%define _localstatedir	/var/lib
%define liz_datadir	%_localstatedir/mfs
%define liz_confdir	%_sysconfdir/mfs
%define liz_limits_conf %_sysconfdir/security/limits.d/10-lizardfs.conf
%define liz_pam_d %_sysconfdir/pam.d/lizardfs

%def_without ganesha

Summary: LizardFS - distributed, fault tolerant file system
Name: lizardfs
Version: 3.13.0
Release: alt0.rc1
License: GPLv3
Group: System/Servers
Url: https://www.lizardfs.org/
# git-vcs: https://github.com/lizardfs/lizardfs.git
Source: %name-%version.tar
Source1: pam-lizardfs
Source2: 10-lizardfs.conf
Source3: spdlog-0.14.0.zip
%if_with ganesha
Source4: nfs-ganesha-2.5-stable.zip
Source5: ntirpc-1.5.zip
%endif
# Patch: %name-%version.patch

Conflicts: moosefs
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): unzip
BuildRequires: asciidoc-a2x
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libfuse-devel
BuildRequires: libjudy-devel
BuildRequires: libpam-devel
BuildRequires: libdb4-devel
BuildRequires: libsystemd-devel
BuildRequires: thrift
BuildRequires: zlib-devel

%description
LizardFS is an Open Source, easy to deploy and maintain, distributed,
fault tolerant file system for POSIX compliant OSes.
LizardFS is a fork of MooseFS. For more information please visit
http://lizardfs.com

%package master
Summary: LizardFS master server
Group: System/Servers
#Requires: pam

%description master
LizardFS master (metadata) server together with metadata restore utility.
%summary.

%package metalogger
Summary: LizardFS metalogger server
Group: System/Servers

%description metalogger
LizardFS metalogger (metadata replication) server.

%package chunkserver
Summary: LizardFS data server
Group: System/Servers

%description chunkserver
LizardFS data server.

%package client
Summary: LizardFS client
Group: System/Servers
Requires: fuse
Requires: libfuse
Requires: bash-completion

%description client
LizardFS client: mfsmount and lizardfs.

%package lib-client
Summary: LizardFS client C/C++ library
Group: System/Libraries

%description lib-client
LizardFS client library for C/C++ bindings.

%if_with ganesha
%package nfs-ganesha
Summary: LizardFS plugin for nfs-ganesha
Group: System/Servers
Requires: %name-lib-client

%description nfs-ganesha
LizardFS fsal plugin for nfs-ganesha.
%endif

%package cgi
Summary: LizardFS CGI Monitor
Group: System/Servers
#Requires: python2

%description cgi
LizardFS CGI Monitor.

%package cgiserv
Summary: Simple CGI-capable HTTP server to run LizardFS CGI Monitor
Group: System/Servers
Requires: %name-cgi = %EVR

%description cgiserv
Simple CGI-capable HTTP server to run LizardFS CGI Monitor.

%package adm
Summary: LizardFS administration utility
Group: System/Servers

%description adm
LizardFS command line administration utility.

%package uraft
Summary: LizardFS cluster management tool
Group: System/Servers
Requires: %name-master
Requires: %name-adm

%description uraft
LizardFS cluster management tool.

%prep
%setup

unzip -q -d external %SOURCE3
%if_with ganesha
unzip -q -d external %SOURCE4
unzip -q -d external %SOURCE5
%endif

# Remove /usr/bin/env from bash scripts
for i in src/tools/mfstools.sh src/master/mfsrestoremaster.in \
	 src/common/serialization_macros_generate.sh src/data/postinst.in \
	 utils/coverage.sh utils/cpp-interpreter.sh utils/wireshark/plugins/lizardfs/generate.sh; do
	sed -i 's@#!/usr/bin/env bash@#!/bin/bash@' $i
done
# Remove /usr/bin/env from python2 scripts
for i in src/cgi/cgiserv.py.in src/cgi/chart.cgi.in src/cgi/lizardfs-cgiserver.py.in src/cgi/mfs.cgi.in; do
	sed -i "s@#!/usr/bin/env python2@#!/usr/bin/python2@" $i
done

%build
%cmake  \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_TESTS=NO \
	-DENABLE_DEBIAN_PATHS=YES \
	-DENABLE_CLIENT_LIB=YES \
%if_with ganesha
	-DENABLE_NFS_GANESHA=YES \
%endif
	-DENABLE_URAFT=YES \
	-DCMAKE_INSTALL_PREFIX=/ \
    -DENABLE_DOCS=YES

%cmake_build

%install
%cmakeinstall_std

# configs
for configs in %buildroot%liz_confdir/*.cfg.dist; do
    mv -n -v "$configs" "${configs%%.dist}"
done
mv -n -v \
    %buildroot%_localstatedir/mfs/metadata.mfs.empty \
    %buildroot%_localstatedir/mfs/metadata.mfs

install -d -m755 %buildroot%_unitdir
for f in rpm/service-files/*.service ; do
	install -m644 "$f" %buildroot%_unitdir/$(basename "$f")
done

install -D -p -m644 %SOURCE1 %buildroot%liz_pam_d
install -D -p -m644 %SOURCE2 %buildroot%liz_limits_conf

pushd alt
# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m644 lizardfs-chunkserver.udev %buildroot%_udevrulesdir/80-lizardfs-chunkserver.rules

# sysv init scripts
mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m644 lizardfs-cgiserv.sysconfig %buildroot%_sysconfdir/sysconfig/lizardfs-cgiserv
mkdir -p %buildroot%_initdir

for f in *.init ; do
    install -p -m755 $f %buildroot%_initdir/${f%%.init}
done
popd

%pre master
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:

%post master
%post_service %name-master
%preun master
%preun_service %name-master

%pre metalogger
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:

%post metalogger
%post_service %name-metalogger
%preun metalogger
%preun_service %name-metalogger

%pre chunkserver
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:
%post chunkserver
%post_service %name-chunkserver
%preun chunkserver
%preun_service %name-chunkserver

%post cgiserv
%post_service %name-cgiserv
%preun cgiserv
%preun_service %name-cgiserv

%files master
%doc NEWS README.md UPGRADE INSTALL COPYING
%_sbindir/mfsmaster
%_sbindir/mfsrestoremaster
%_sbindir/mfsmetadump
%_sbindir/mfsmetarestore
%_man5dir/mfsexports.cfg.5*
%_man5dir/mfstopology.cfg.5*
%_man5dir/mfsgoals.cfg.5*
%_man5dir/mfsmaster.cfg.5*
%_man5dir/globaliolimits.cfg.5*
%_man7dir/mfs.7*
%_man7dir/moosefs.7*
%_man7dir/lizardfs.7*
%_man8dir/mfsmaster.8*
%_man8dir/mfsmetadump.8*
%_man8dir/mfsmetarestore.8*
%_man8dir/mfsrestoremaster.8*
%_unitdir/lizardfs-master.service
%_initdir/lizardfs-master

%attr(0755,%_username,%_groupname) %dir %liz_datadir
%config(noreplace) %attr(644,%_username,%_groupname) %liz_datadir/metadata.mfs
# Upstream documentation expects default config files to be stored in /etc/mfs
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsexports.cfg
%config(noreplace) %liz_confdir/mfstopology.cfg
%config(noreplace) %liz_confdir/mfsgoals.cfg
%config(noreplace) %liz_confdir/mfsmaster.cfg
%config(noreplace) %liz_confdir/globaliolimits.cfg
%config(noreplace) %liz_pam_d
%config(noreplace) %liz_limits_conf

%files metalogger
%doc NEWS README.md UPGRADE
%_sbindir/mfsmetalogger
%_man5dir/mfsmetalogger.cfg.5*
%_man8dir/mfsmetalogger.8*
%_unitdir/lizardfs-metalogger.service
%_initdir/lizardfs-metalogger
%attr(0755,%_username,%_groupname) %dir %liz_datadir
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsmetalogger.cfg

%files chunkserver
%doc NEWS README.md UPGRADE
%_sbindir/mfschunkserver
%_man5dir/mfschunkserver.cfg.5*
%_man5dir/mfshdd.cfg.5*
%_man8dir/mfschunkserver.8*
%_udevrulesdir/80-lizardfs-chunkserver.rules
%_unitdir/lizardfs-chunkserver.service
%_initdir/lizardfs-chunkserver
%attr(0755,%_username,%_groupname) %dir %liz_datadir
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfschunkserver.cfg
%config(noreplace) %liz_confdir/mfshdd.cfg
%config(noreplace) %liz_pam_d
%config(noreplace) %liz_limits_conf

%files client
%doc NEWS README.md UPGRADE
%_bindir/lizardfs
%_bindir/mfstools.sh
%_bindir/mfsmount
%_bindir/mfsappendchunks
%_bindir/mfscheckfile
%_bindir/mfsdeleattr
%_bindir/mfsdirinfo
%_bindir/mfsfileinfo
%_bindir/mfsfilerepair
%_bindir/mfsgeteattr
%_bindir/mfsgetgoal
%_bindir/mfsgettrashtime
%_bindir/mfsmakesnapshot
%_bindir/mfsrepquota
%_bindir/mfsrgetgoal
%_bindir/mfsrgettrashtime
%_bindir/mfsrsetgoal
%_bindir/mfsrsettrashtime
%_bindir/mfsseteattr
%_bindir/mfssetgoal
%_bindir/mfssetquota
%_bindir/mfssettrashtime
%_man1dir/lizardfs-appendchunks.1*
%_man1dir/lizardfs-checkfile.1*
%_man1dir/lizardfs-deleattr.1*
%_man1dir/lizardfs-dirinfo.1*
%_man1dir/lizardfs-fileinfo.1*
%_man1dir/lizardfs-filerepair.1*
%_man1dir/lizardfs-geteattr.1*
%_man1dir/lizardfs-getgoal.1*
%_man1dir/lizardfs-gettrashtime.1*
%_man1dir/lizardfs-makesnapshot.1*
%_man1dir/lizardfs-repquota.1*
%_man1dir/lizardfs-rgetgoal.1*
%_man1dir/lizardfs-rgettrashtime.1*
%_man1dir/lizardfs-rremove.1*
%_man1dir/lizardfs-rsetgoal.1*
%_man1dir/lizardfs-rsettrashtime.1*
%_man1dir/lizardfs-seteattr.1*
%_man1dir/lizardfs-setgoal.1*
%_man1dir/lizardfs-setquota.1*
%_man1dir/lizardfs-settrashtime.1*
%_man1dir/lizardfs.1*
%_man5dir/iolimits.cfg.5*
%_man5dir/mfsmount.cfg.5*
%_man7dir/mfs.7*
%_man7dir/moosefs.7*
%_man7dir/lizardfs.7*
%_man1dir/mfsmount.1*
%_sysconfdir/bash_completion.d/lizardfs
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsmount.cfg
%config(noreplace) %liz_confdir/iolimits.cfg

%files lib-client
%_libdir/liblizardfsmount_shared.so
%_libdir/liblizardfs-client.so
%_libdir/liblizardfs-client-cpp.a
%_libdir/liblizardfs-client-cpp_pic.a
%_libdir/liblizardfs-client.a
%_libdir/liblizardfs-client_pic.a
%_includedir/lizardfs/
%_includedir/lizardfs/lizardfs_c_api.h
%_includedir/lizardfs/lizardfs_error_codes.h

%if_with ganesha
%files nfs-ganesha
%_libdir/ganesha/libfsallizardfs.so
#%_libdir/ganesha/libfsallizardfs.so.4
#%_libdir/ganesha/libfsallizardfs.so.4.2.0
%endif

%files cgi
%doc NEWS README.md UPGRADE
%dir %_datadir/mfscgi
%_datadir/mfscgi/err.gif
%_datadir/mfscgi/favicon.ico
%_datadir/mfscgi/index.html
%_datadir/mfscgi/logomini.png
%_datadir/mfscgi/mfs.css
%_datadir/mfscgi/mfs.cgi
%_datadir/mfscgi/chart.cgi

%files cgiserv
%doc NEWS README.md UPGRADE
%_sbindir/lizardfs-cgiserver
%_sbindir/mfscgiserv
%_man8dir/lizardfs-cgiserver.8*
%_man8dir/mfscgiserv.8*
%_unitdir/lizardfs-cgiserv.service
%_initdir/lizardfs-cgiserv
%_sysconfdir/sysconfig/lizardfs-cgiserv

%files adm
%doc NEWS README.md UPGRADE
%_bindir/lizardfs-admin
%_man8dir/lizardfs-admin.8*
%_bindir/lizardfs-probe
%_man8dir/lizardfs-probe.8*

%files uraft
%attr(755,root,root) %_sbindir/lizardfs-uraft
%attr(755,root,root) %_sbindir/lizardfs-uraft-helper
%doc NEWS README.md UPGRADE
%_man8dir/lizardfs-uraft.8*
%_man8dir/lizardfs-uraft-helper.8*
%_man5dir/lizardfs-uraft.cfg.5*
%config(noreplace) %liz_confdir/lizardfs-uraft.cfg
%attr(754,root,root) %_initdir/lizardfs-uraft
%attr(644,root,root) %_unitdir/lizardfs-uraft.service
%attr(644,root,root) %_unitdir/lizardfs-ha-master.service
%attr(644,root,root) %_unitdir/lizardfs-uraft.lizardfs-ha-master.service

%changelog
* Thu May 28 2019 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc1
- Import from upstream 3.13.0-rc1

