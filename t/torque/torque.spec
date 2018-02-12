Summary: Tera-scale Open-source Resource and QUEue manager

Name: torque
Version: 4.2.1
Release: alt1.qa2

License: OpenPBS (Portable Batch System) v2.3 Software License (Redistribution in any form is only permitted for non-commercial, non-profit purposes)
Group: Sciences/Computer science
URL: http://www.clusterresources.com/products/torque/

Packager: Denis Pynkin <dans@altlinux.ru>

Source: %name-%version.tar
Source100: pbs_server.init
Source101: pbs_sched.init
Source102: pbs_mom.init

Source200: xpbs.desktop
Source201: xpbsmon.desktop

Patch: %name-%version-%release.patch

#set_verify_elf_method unresolved=relaxed

%define torquehomedir %_spooldir/%name

BuildRequires: flex gcc-c++ groff-base libncurses-devel libpam-devel 
BuildRequires: libreadline-devel sendmail-common tk-devel openssh
BuildRequires: openssl-devel libxml2-devel
BuildRequires: check hwloc libhwloc-devel

%description
TORQUE (Tera-scale Open-source Resource and QUEue manager) is a resource 
manager providing control over batch jobs and distributed compute nodes. 

TORQUE is based on OpenPBS version 2.3.12 and incorporates scalability, 
fault tolerance, and feature extension patches provided by USC, NCSA, OSC, 
the U.S. Dept of Energy, Sandia, PNNL, U of Buffalo, TeraGrid, and many 
other leading edge HPC organizations.

This package holds just a few shared files and directories.

%package docs
Group: Documentation
Summary: Documentation files for TORQUE
Requires: %name = %version-%release

%description docs
Documentation files for TORQUE

%package scheduler
Group: System/Servers
Summary: Simple fifo scheduler for TORQUE
Requires: %name = %version-%release

%description scheduler
This package holds fifo C scheduler for TORQUE

%package server
Group: System/Servers
Summary: The main part of TORQUE
Requires: %name = %version-%release

%description server
This package holds the TORQUE server.

%package mom
Group: System/Servers
Summary: Node execution daemon for TORQUE
Requires: %name = %version-%release

%description mom
This package holds the execute daemon required on every node.

%package client
Group: Sciences/Computer science
Summary: Client part of TORQUE
Requires: %name = %version-%release
Conflicts: qstat

%description client
This package holds the command-line client programs for TORQUE

%package gui
Group: Sciences/Computer science
Summary: Graphical clients for TORQUE
Requires: %name-client = %version-%release

%description gui
This package holds the graphical clients for TORQUE

%package -n lib%name
Summary: Run-time libs for programs which will use the %{name} library
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
This package includes the shared libraries
necessary for running TORQUE programs.

%package -n lib%{name}-devel
Summary: Development tools for programs which will use the %{name} library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%{name}-devel
This package includes the header files and static libraries
necessary for developing programs which will use TORQUE.

%package pam
Summary: PAM module for TORQUE MOM nodes
Group: System/Base

%description pam
A simple PAM module to authorize users on PBS MOM nodes with a running job.

%prep
%setup -q -n %name-%version
%patch -p1

%build
%add_optflags -DUSE_INTERP_RESULT
%add_optflags -DUSE_INTERP_ERRORLINE
#CFLAGS="%optflags -std=gnu99"

%configure \
	--with-rcp=scp \
	--with-gnu-ld \
	--enable-gui \
	--enable-cpuset \
	--disable-blcr \
	--enable-nvidia-gpus \
	--enable-force-nodefile \
	--enable-maintainer-mode \
	--disable-static \
	--with-default-server=localhost

#	--disable-gcc-warnings \
#	--enable-drmaa \
#	--with-pam \

%make_build

%install

%__make DESTDIR=$RPM_BUILD_ROOT install

echo "localhost" > %buildroot/%torquehomedir/server_name

%__install -Dpm755 %SOURCE100 %buildroot/%_initdir/pbs_server
%__install -Dpm755 %SOURCE101 %buildroot/%_initdir/pbs_sched
%__install -Dpm755 %SOURCE102 %buildroot/%_initdir/pbs_mom

%__install -Dpm644 %SOURCE200 %buildroot/%_desktopdir/xpbs.desktop
%__install -Dpm644 %SOURCE201 %buildroot/%_desktopdir/xpbsmon.desktop

%files
%doc README.* PBS_License.txt Release_Notes CHANGELOG
%config(noreplace) %torquehomedir/pbs_environment
%config(noreplace) %torquehomedir/server_name
%dir %torquehomedir
%torquehomedir/aux
%attr(1777,root,root) %torquehomedir/spool
%_man1dir/pbs.*

%files docs
%doc doc/admin_guide.ps
#%{_mandir}/man*/*


%files scheduler
%_initdir/pbs_sched
%_sbindir/pbs_sched
%_sbindir/qschedd
%dir %torquehomedir/sched_priv
%config(noreplace) %torquehomedir/sched_priv/*
%attr(700,root,root) %torquehomedir/sched_logs
%_man7dir/pbs_queue_attributes*
%_man8dir/pbs_sched*

%post scheduler
%post_service pbs_sched

%preun scheduler
%preun_service pbs_sched

%files server
%_initdir/pbs_server
%_sbindir/pbs_server
%_sbindir/qserverd
%_sbindir/momctl
%attr(700,root,root) %torquehomedir/server_logs
%torquehomedir/server_priv
%_man7dir/pbs_server*
%_man8dir/pbs_server*

%post server
%post_service pbs_server

%preun server
%preun_service pbs_server


%files mom
#if {use_rcp}
#attr(4755 root root) %{_sbindir}/pbs_rcp
#endif
%_initdir/pbs_mom
%_sbindir/pbs_mom
%_sbindir/qnoded
%_bindir/pbs_track
%torquehomedir/mom_priv
%attr(700,root,root) %torquehomedir/mom_logs
%torquehomedir/checkpoint
%attr(1777,root,root) %torquehomedir/undelivered
%_man8dir/pbs_mom*

%post mom
%post_service pbs_mom

%preun mom
%preun_service pbs_mom

%files client
%attr(4711 root root) %_sbindir/trqauthd
%_bindir/q*
%_bindir/chk_tree
%_bindir/hostn
%_bindir/nqs2pbs
%_bindir/pbsdsh
%_bindir/pbsnodes
%_bindir/printjob
%_bindir/printserverdb
%_bindir/printtracking
%_bindir/tracejob
%_sbindir/pbs_demux
%_bindir/pbs_tclsh
%_man1dir/q*
%_man1dir/basl2c.*
%_man1dir/nqs2pbs.*
%_man1dir/pbsdsh.*
%_man7dir/pbs_job_attributes*
%_man7dir/pbs_resources*
%_man8dir/q*
%_man8dir/pbsnodes*

%files gui
%_bindir/pbs_wish
%_bindir/xpbs
%_bindir/xpbsmon
%_libdir/xpbs
%_libdir/xpbsmon
%_man1dir/xpbs*
%_desktopdir/*.desktop

%files -n lib%name
%_libdir/*.so.*

%files -n lib%{name}-devel
%_libdir/*.so
%_includedir/*
%_bindir/pbs-config
%_man3dir/*

%changelog
* Fri Feb 09 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2.1-alt1.qa2
- Rebuilt without blcr.

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.2.1-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Sat Mar 09 2013 Denis Pynkin <dans@altlinux.org> 4.2.1-alt1
- New version

* Thu Sep 27 2012 Denis Pynkin <dans@altlinux.org> 4.1.2-alt1
- New version

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 3.0.1-alt1
- New version
- Added lsb header to init scripts

* Sun Dec 05 2010 Denis Pynkin <dans@altlinux.ru> 2.5.3-alt1
- New version from upstream

* Mon Oct 11 2010 Denis Pynkin <dans@altlinux.ru> 2.5.2-alt1
- New version from upstream

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 2.4.5-alt1
- New version from upstream

* Tue Dec 15 2009 Denis Pynkin <dans@altlinux.ru> 2.4.3-alt2
- Changed group name length to 32. request by rider@

* Sat Dec 12 2009 Denis Pynkin <dans@altlinux.ru> 2.4.3-alt1
- New version from upstream

* Mon Aug 24 2009 Denis Pynkin <dans@altlinux.ru> 2.3.7-alt1
- New version from upstream

* Tue Apr 07 2009 Denis Pynkin <dans@altlinux.ru> 2.3.6-alt2
- git repository restructurization

* Sun Feb 08 2009 Denis Pynkin <dans@altlinux.ru> 2.3.6-alt1
- New version from upstream
- removed obsoleted macroses
- added conflict with qstat package

* Mon Oct 20 2008 Denis Pynkin <dans@altlinux.ru> 2.3.3-alt1
- New version from upstream
- pbs_track - experimental version introduced

* Sat Apr 12 2008 Denis Pynkin <dans@altlinux.ru> 2.3.0-alt1
- New version from upstream

* Wed Sep 12 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.9-alt1
- 2.1.9
- fix permisions to shared spool directory, undelivered directory and *_logs directories

* Thu Aug 09 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.8-alt1.1
- add notes about redistribution to License

* Wed Aug 08 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.8-alt1
- Initial release
