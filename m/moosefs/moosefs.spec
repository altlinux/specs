%define _groupname	mfs
%define _username	mfs
%define _localstatedir	/var/lib
%define mfsconfdir	%_sysconfdir/mfs

Summary: MooseFS - distributed, fault tolerant file system
Name: moosefs
Version: 4.59.0
Release: alt1
License: GPLv2
Group: System/Servers
Url: http://www.moosefs.com/
Vcs: https://github.com/moosefs/moosefs.git
Source: %name-%version.tar
Patch: %name-%version.patch

%filter_from_requires /python3(common\./d
%filter_from_requires /python3(views\./d

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libfuse3-devel
BuildRequires: zlib-devel
BuildRequires: libpcap-devel
BuildRequires: pkgconfig(systemd)

%description
MooseFS is an Open Source, easy to deploy and maintain, distributed,
fault tolerant file system for POSIX compliant OSes.

%package -n libmfsio
Summary: MooseFS IO library
Group: System/Libraries
%description -n libmfsio
%summary.

%package -n libmfsio-devel
Summary: Development files for MooseFS IO library
Group: Development/C
Requires: libmfsio = %EVR
%description -n libmfsio-devel
%summary.

%package common
Summary: MooseFS - common files
Group: System/Servers
BuildArch: noarch

%description common
MooseFS - distributed, fault tolerant file system

%package master
Summary: MooseFS master server
Group: System/Servers
Requires: %name-common = %EVR

%description master
MooseFS master (metadata) server together with mfssupervisor utility.

%package metalogger
Summary: MooseFS metalogger server
Group: System/Servers
Requires: %name-common = %EVR

%description metalogger
MooseFS metalogger (metadata replication) server.

%package chunkserver
Summary: MooseFS data server
Group: System/Servers
Requires: %name-common = %EVR

%description chunkserver
MooseFS data server.

%package client
Summary: MooseFS client
Group: File tools
Requires: %name-common = %EVR

%description client
MooseFS client: mfsmount and mfstools.

%package cli
Summary: MooseFS CLI Utility
Group: File tools
BuildArch: noarch

%description cli
MooseFS CLI utilities.

%package gui
Summary: MooseFS CGI Monitor
Group: System/Servers
Obsoletes: %name-cgiserv < %EVR
Obsoletes: %name-cgi < %EVR
Provides: %name-cgiserv = %EVR
Provides: %name-cgi = %EVR
Requires: %name-common = %EVR
Requires: %name-cli = %EVR

%description gui
MooseFS web-based GUI.

%package netdump
Summary: MooseFS network packet dump utility
Group: System/Servers

%description netdump
MooseFS network packet dump utility

%prep
%setup
%patch -p1

%build
export PYTHON=/usr/bin/python3
%autoreconf
%configure \
	--disable-static \
	--with-default-user=%_username \
	--with-default-group=%_groupname \
	--with-systemdsystemunitdir=%_unitdir

%make_build

%install
%makeinstall_std
# configs
for configs in %buildroot%mfsconfdir/*.cfg.sample; do
    mv -n -v "$configs" "${configs%%.sample}"
done
mv -n -v \
    %buildroot%_localstatedir/mfs/metadata.mfs.empty \
    %buildroot%_localstatedir/mfs/metadata.mfs

pushd alt
# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m644 moosefs-chunkserver.udev %buildroot%_udevrulesdir/80-moosefs-chunkserver.rules

# sysv init scripts
mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m644 moosefs-gui.sysconfig %buildroot%_sysconfdir/sysconfig/moosefs-gui
mkdir -p %buildroot%_initdir

for f in *.init ; do
    install -p -m755 $f %buildroot%_initdir/${f%%.init}
done
popd

%pre common
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "MooseFS" -g %_groupname %_username 2>/dev/null ||:

%post master
%post_service %name-master
%preun master
%preun_service %name-master

%post metalogger
%post_service %name-metalogger
%preun metalogger
%preun_service %name-metalogger

%post chunkserver
%post_service %name-chunkserver
%preun chunkserver
%preun_service %name-chunkserver

%post gui
%post_service %name-gui
%preun gui
%preun_service %name-gui

%files -n libmfsio
%_libdir/libmfsio.so.*

%files -n libmfsio-devel
%_includedir/mfsio.h
%_libdir/libmfsio.so

%files common
%doc NEWS README
%dir %attr(770,root,%_groupname) %_localstatedir/mfs
%dir %attr(770,root,%_groupname) %mfsconfdir

%files master
%_sbindir/mfsmaster
%_sbindir/mfsmetadump
%_sbindir/mfsmetadirinfo
%_sbindir/mfsmetarestore
%_sbindir/mfsstatsdump
%_sbindir/mfssupervisor
%_man5dir/mfsexports.cfg.5*
%_man5dir/mfstopology.cfg.5*
%_man5dir/mfsmaster.cfg.5*
%_man5dir/mfsipmap.cfg.5*
%_man7dir/moosefs.7*
%_man8dir/mfsmaster.8*
%_man8dir/mfsmetarestore.8*
%_man8dir/mfsmetadump.8*
%_man8dir/mfsmetadirinfo.8*
%_man8dir/mfsstatsdump.8*
%_man8dir/mfsmetasearch.8*
%_man8dir/mfssupervisor.8*
%config(noreplace) %mfsconfdir/mfsexports.cfg
%config(noreplace) %mfsconfdir/mfstopology.cfg
%config(noreplace) %mfsconfdir/mfsmaster.cfg
%config(noreplace) %mfsconfdir/mfsipmap.cfg
%config(noreplace) %attr(640,%_username,%_groupname) %_localstatedir/mfs/metadata.mfs
%_initdir/moosefs-master
%_unitdir/moosefs-master.service
%_unitdir/moosefs-master@.service

%files metalogger
%_sbindir/mfsmetalogger
%_man5dir/mfsmetalogger.cfg.5*
%_man8dir/mfsmetalogger.8*
%config(noreplace) %mfsconfdir/mfsmetalogger.cfg
%_initdir/moosefs-metalogger
%_unitdir/moosefs-metalogger.service
%_unitdir/moosefs-metalogger@.service

%files chunkserver
%_sbindir/mfschunkserver
%_sbindir/mfschunktool
%_sbindir/mfschunkdbdump
%_sbindir/mfscsstatsdump
%_sbindir/mfsmetasearch
%_man5dir/mfschunkserver.cfg.5*
%_man5dir/mfshdd.cfg.5*
%_man8dir/mfschunkserver.8*
%_man8dir/mfschunktool.8*
%_man8dir/mfscsstatsdump.8*
%_man8dir/mfschunkdbdump.8*
%config(noreplace) %mfsconfdir/mfschunkserver.cfg
%config(noreplace) %mfsconfdir/mfshdd.cfg
%_udevrulesdir/80-moosefs-chunkserver.rules
%_initdir/moosefs-chunkserver
%_unitdir/moosefs-chunkserver.service
%_unitdir/moosefs-chunkserver@.service

%files client
%_bindir/mfsappendchunks
%_bindir/mfsarchive
%_bindir/mfscheckfile
%_bindir/mfschkarchive
%_bindir/mfsclonesclass
%_bindir/mfsclrarchive
%_bindir/mfscopyeattr
%_bindir/mfscopygoal
%_bindir/mfscopyquota
%_bindir/mfscopysclass
%_bindir/mfscopytrashretention
%_bindir/mfscopytrashtime
%_bindir/mfscreatepattern
%_bindir/mfscreatesclass
%_bindir/mfsdeleattr
%_bindir/mfsdeletepattern
%_bindir/mfsdeletesclass
%_bindir/mfsdelquota
%_bindir/mfsdiagtools
%_bindir/mfsdirinfo
%_bindir/mfseattr
%_bindir/mfsfacl
%_bindir/mfsfileinfo
%_bindir/mfsfilepaths
%_bindir/mfsfilerepair
%_bindir/mfsgeteattr
%_bindir/mfsgetfacl
%_bindir/mfsgetgoal
%_bindir/mfsgetquota
%_bindir/mfsgetsclass
%_bindir/mfsgettrashretention
%_bindir/mfsgettrashtime
%_bindir/mfsimportsclass
%_bindir/mfslistpattern
%_bindir/mfslistsclass
%_bindir/mfsmakesnapshot
%_bindir/mfsmodifysclass
%_bindir/mfsmount
%_bindir/mfsmount
%_bindir/mfspatadmin
%_bindir/mfsquota
%_bindir/mfsrenamesclass
%_bindir/mfsrmsnapshot
%_bindir/mfsscadmin
%_bindir/mfssclass
%_bindir/mfssetarchive
%_bindir/mfsseteattr
%_bindir/mfssetfacl
%_bindir/mfssetgoal
%_bindir/mfssetquota
%_bindir/mfssetsclass
%_bindir/mfssettrashretention
%_bindir/mfssettrashtime
%_bindir/mfssnapshots
%_bindir/mfstrashretention
%_bindir/mfstrashtime
%_bindir/mfstrashtool
%_bindir/mfsxchgsclass
%_sbindir/mfsbdev
/sbin/mount.moosefs
%_man1dir/*
%exclude %_man1dir/mfscli.1*
%_man5dir/mfsbdev.cfg.5*
%_man5dir/mfsmount.cfg.5*
%_man8dir/mfsmount.8*
%_man8dir/mount.moosefs.8*
%_man8dir/mfsbdev.8*
%config(noreplace) %mfsconfdir/mfsmount.cfg

%files cli
%_bindir/mfscli
%_man1dir/mfscli.1*

%files gui
%config(noreplace) %_sysconfdir/sysconfig/moosefs-gui
%{_sbindir}/mfscgiserv
%{_sbindir}/mfsgui
%_man5dir/mfsgui.cfg.5*
%_man8dir/mfsgui.8*
%config(noreplace) %mfsconfdir/mfsgui.cfg
%_initdir/moosefs-gui
%_unitdir/moosefs-gui.service
%_unitdir/moosefs-gui@.service
%dir %_datadir/mfscgi
%attr(755,root,root) %_datadir/mfscgi/*.cgi
%_datadir/mfscgi/requests.cfg
%_datadir/mfscgi/assets/
%_datadir/mfscgi/common/
%_datadir/mfscgi/views/

%files netdump
%_sbindir/mfsnetdump
%_man8dir/mfsnetdump.8*

%changelog
* Thu Apr 30 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.59.0-alt1
- 4.59.0

* Wed Mar 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.58.4-alt1
- 4.58.4

* Tue Dec 16 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.58.3-alt1
- 4.58.3

* Wed Nov 05 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.58.2-alt1
- 4.58.2

* Wed Oct 01 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.58.1-alt1
- 4.58.1

* Tue Sep 16 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.58.0-alt1
- 4.58.0

* Wed Jun 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.57.7-alt1
- 4.57.7
- new package gui (replaces cgi and deprecates cgiserv), removed cgiserv

* Thu Apr 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.57.6-alt1
- 4.57.6

* Sat Mar 08 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.57.5-alt1
- 4.57.5

* Wed Sep 25 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.56.6-alt1
- 4.56.6

* Fri Sep 20 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.56.5-alt1
- 4.56.5

* Tue Aug 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.0.118-alt1
- 3.0.118

* Fri Feb 03 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.0.117-alt1
- 3.0.117

* Thu Aug 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.0.116-alt1
- 3.0.116

* Tue Nov 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.0.115-alt1
- 3.0.115

* Mon Jun 01 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.113-alt1
- 3.0.113

* Sun Mar 15 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.111-alt1
- 3.0.111
- build with libfuse3

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.109-alt1
- 3.0.109

* Wed May 29 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.105-alt1
- 3.0.105

* Wed May 08 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.104-alt1
- 3.0.104

* Sun Mar 03 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.103-alt1
- inital build for ALT (based on upstream spec)
