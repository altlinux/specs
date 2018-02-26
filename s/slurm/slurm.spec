%def_enable shared
%def_enable static
%def_disable debug
%def_disable bgl_emulation
%def_disable bgp_emulation
%def_disable cray_xt
%def_disable sun_const
%def_enable largefile
%def_enable iso8601
%def_enable load_env_no_login
%def_disable multiple_slurmd
%def_disable front_end
%def_enable pam
%def_with readline
%def_with blcr
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define Name SLURM
Name: slurm
%define lname lib%name
Version: 2.3.0
%define pre %nil
Release: alt2
Summary: Simple Linux Utility for Resource Management
License: %gpl2plus
Group: System/Base
Url: https://computing.llnl.gov/linux/%name
Source0: %name-%version%pre.tar
Source1: %name.init
Source2: %{name}ctl.init
Source3: %{name}db.init
Source11: %name.conf.in
Source12: %{name}dbd.conf.in
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libmysqlclient-devel libgtk+2-devel libncurses-devel service
%{?_with_readline:BuildRequires: libreadline-devel}
%{?_with_blcr:BuildRequires: libblcr-devel}
%{?_enable_pam:BuildRequires: libpam-devel}

BuildPreReq: libssl-devel chrpath

%description
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.


%package common
Summary: %Name common files
Group: System/Base
BuildArch: noarch
Conflicts: %name < 2.0.1-alt2

%description common
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.

This package contains %Name common files.


%package utils
Summary: %Name utils
Group: System/Base
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-common = %version-%release
Conflicts: %name < 2.0.1-alt2

%description utils
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.

This package contains %Name utils.


%package master
Summary: The central management daemon of %Name
Group: System/Base
Provides: %{name}ctld = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-common = %version-%release
Requires: openssl
Conflicts: %name < 2.0.1-alt2

%description master
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.

This package contains the central management daemon of %Name.


%package slave
Summary: The compute node daemon for %Name
Group: System/Base
Provides: %{name}d = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-common = %version-%release
Conflicts: %name < 2.0.1-alt2

%description slave
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.

This package contains compute node daemon for %Name.


%package sview
Summary: GUI to view and modify %Name state
Group: System/Base
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-common = %version-%release
Conflicts: %name < 2.0.1-alt2

%description sview
%Name is an open source, fault-tolerant, and highly scalable cluster
management and job scheduling system for Linux clusters containing up
to 65,536 nodes. Components include machine status, partition
management, job management, scheduling and accounting modules.

This package contains graphical user interface to view and modify %Name
state.


%if_with blcr
%package blcr
Summary: BLCR support for %Name
Group: System/Base
Provides: %name-plugin-blcr = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-slave = %version-%release
Requires: blcr

%description blcr
BLCR support for %Name.
%endif


%package doc
Summary: Manuals for development with %Name
Group: Development/Documentation
BuildArch: noarch
Provides: %name-doc-html = %version-%release
Obsoletes: %name-doc-html
Conflicts: %name < 2.0.1-alt2

%description doc
This package contains manuals for development with %Name.


%if_enabled shared
%package -n %lname
Summary: Common libraries for %Name
Group: System/Libraries

%description -n %lname
This package contains Common libraries for %Name.
%endif


%package -n %lname-devel
Summary: Development files for %Name
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
This package contains development files for %Name.


%package -n %lname-devel-man
Summary: Manuals for development with %Name
Group: Development/Documentation
BuildArch: noarch

%description -n %lname-devel-man
This package contains manuals for development with %Name.


%if_enabled static
%package -n %lname-devel-static
Summary: Static %Name libraries
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
This package contains static %Name libraries.
%endif


%package %{name}dbd
Summary: %Name database daemon
Group: System/Base
Provides: %{name}dbd = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-plugins
Requires: %name-master = %version-%release

%description %{name}dbd
%Name database daemon.


%package plugins
Summary: %Name plugins (loadable shared objects)
Group: System/Base
%{?_enable_shared:Requires: %lname = %version-%release}
AutoReq: yes,noruby
Requires: %name-common = %version-%release

%description plugins
%Name plugins (loadable shared objects).


%prep
%setup -n %name-%version%pre
%patch -p1

%build
%set_automake_version 1.10
#autoreconf
%configure \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable debug} \
    %{subst_enable_to debug memory-leak-debug} \
    %{subst_enable_to bgl_emulation bgl-emulation} \
    %{subst_enable_to bgp_emulation bgp-emulation} \
    %{subst_enable_to cray_xt cray-xt} \
    %{subst_enable_to sun_const sun-const} \
    %{subst_enable largefile} \
    %{subst_enable iso8601} \
    %{subst_enable_to load_env_no_login load-env-no-login} \
    %{subst_enable_to multiple_slurmd multiple-slurmd} \
    %{subst_enable_to front_end front-end} \
    %{subst_enable pam} \
    %{subst_with readline} \
    %{subst_with blcr} \
    %{?ctl_port:--with-slurmctld-port=%ctl_port} \
    %{?port:--with-slurmctld-port=%port} \
    %{?bd_port:--with-slurmctld-port=%bd_port} \
    --with-gnu-ld

%make_build
bzip2 --best --force --keep NEWS


%install
touch AUTHORS NEWS.bz2 README.rst RELEASE_NOTES DISCLAIMER

%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot{%_sysconfdir/{sysconfig,%name},%_initdir}
install -m 0644 AUTHORS NEWS.* README.rst RELEASE_NOTES DISCLAIMER %buildroot%_docdir/%name-%version/
:> %buildroot%_sysconfdir/sysconfig/%name
:> %buildroot%_sysconfdir/%name/%name.key
:> %buildroot%_sysconfdir/%name/%name.cert
install -m 0755 %SOURCE1 %buildroot%_initdir/%name
install -m 0755 %SOURCE2 %buildroot%_initdir/%{name}ctl
install -m 0755 %SOURCE3 %buildroot%_initdir/%{name}db
install -m 0644 %SOURCE11 %buildroot%_sysconfdir/%name.conf
install -m 0644 %SOURCE12 %buildroot%_sysconfdir/%{name}dbd.conf
install -m 0644 etc/%name{*.conf.example,.epilog.clean} %buildroot%_docdir/%name-%version/
rm -rf %buildroot%_libdir/%name/src
rm -f %buildroot{%_libdir/%name/*a,%_man3dir/%{name}_*_trigger*}

cp doc/man/man1/srun_cr.1 %buildroot%_man1dir

chrpath -d %buildroot%_libdir/libpmi.so

%post
%post_service %name ||:

%preun
%preun_service %name ||:


%post master
[ -e %_sysconfdir/slurm/slurm.key ] ||
%_bindir/openssl genrsa -out %_sysconfdir/slurm/slurm.key 1024 &&
%_bindir/openssl rsa -in %_sysconfdir/slurm/slurm.key -pubout -out %_sysconfdir/slurm/slurm.cert
%post_service %{name}ctl ||:

%preun master
%preun_service %{name}ctl ||:


%post slave
%post_service %name ||:

%preun slave
%preun_service %name ||:


%post %{name}dbd
%post_service %{name}db ||:

%preun %{name}dbd
%preun_service %{name}db ||:


%files common
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/DISCLAIMER
%doc %_docdir/%name-%version/README.rst
%doc %_docdir/%name-%version/RELEASE_NOTES
%config %_sysconfdir/%name.*
%config %_sysconfdir/sysconfig/%name


%files master
%attr(700,root,root) %dir %_sysconfdir/%name
%attr(600,root,root) %ghost %config(noreplace) %_sysconfdir/%name/*
%_sbindir/%{name}ctld
%_man8dir/%{name}ctld.*
%_initdir/%{name}ctl


%files slave
%attr(700,root,root) %dir %_sysconfdir/%name
%attr(600,root,root) %ghost %config(noreplace) %_sysconfdir/%name/*
%_sbindir/%{name}d
%_sbindir/%{name}stepd
%_man8dir/%{name}d.*
%_man8dir/%{name}stepd.*
%_initdir/%name


%files utils
%_bindir/*
%exclude %_bindir/sview
%_man1dir/*
%exclude %_man1dir/sview.*
%exclude %_man1dir/srun_cr.1*
%if_with blcr
#exclude %_bindir/cr_*
%exclude %_bindir/*_cr
#exclude %_man1dir/*_cr.*
%endif
%_man5dir/%name.*
%_man5dir/wiki.*
%_libexecdir/%name
%{?_enable_blg_emulation:%_man5dir/bluegene.*}


%files sview
%_bindir/sview
%_man1dir/sview.*


%if_with blcr
%files blcr
#_bindir/cr_*
%_bindir/*_cr
#_man1dir/*_cr.*
%_man1dir/srun_cr.1*
%_libdir/%name/*_blcr.so
%endif


%files doc
%dir %_docdir/%name-%version
%_docdir/%name-%version/html
%_docdir/%name-%version/NEWS.*
%_docdir/%name-%version/%name.epilog.clean
%_docdir/%name-%version/*.conf.example


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/%name
%{?_enable_shared:%_libdir/*.so}


%files -n %lname-devel-man
%_man3dir/*
%_man5dir/cgroup.conf.5*
%_man5dir/cray.conf.5*
%_man5dir/gres.conf.5*
%_man5dir/topology.conf.5*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files %{name}dbd
%_initdir/%{name}db
%_sbindir/%{name}dbd
%_man5dir/%{name}dbd.*
%_man8dir/%{name}dbd.*
%config %_sysconfdir/%{name}dbd.*


%files plugins
%dir %_libdir/%name
%_libdir/%name/*.so
%_man8dir/spank*
%{?_with_blcr:%exclude %_libdir/%name/*_blcr.so}


%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt2
- Removed RPATH

* Thu Oct 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0 (ALT #26420)

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.5
- Added libssl-devel into BuildPreReq

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.4
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.3
- Rebuilt with openssl10

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.2
- Rebuilt with libmysqlclient.so.16

* Mon Jan 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.1
- Built version 2.0.9 for Sisyphus

* Tue Dec 15 2009 Led <led@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Mon Nov 16 2009 Led <led@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Wed Oct 21 2009 Led <led@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Mon Oct 12 2009 Led <led@altlinux.ru> 2.0.5-alt3
- slurmctld: added key -W for force refresh accounts

* Thu Oct 01 2009 Led <led@altlinux.ru> 2.0.5-alt2
- disabled:
  + multiple-slurmd
  + front-end

* Wed Sep 23 2009 Led <led@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Jul 13 2009 Led <led@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Tue Jun 30 2009 Led <led@altlinux.ru> 2.0.3-alt2
- fixed linking plugins

* Tue Jun 30 2009 Led <led@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Thu Jun 18 2009 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Jun 08 2009 Led <led@altlinux.ru> 2.0.1-alt3
- cleaned up %_sysconfdir/
- added post scripts
- added init scripts
- added default configs

* Mon Jun 08 2009 Led <led@altlinux.ru> 2.0.1-alt2
- split package %name to subpackages:
  %name-{common,master,slave,utils,sview}

* Thu Jun 04 2009 Led <led@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon May 25 2009 Led <led@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue May 19 2009 Led <led@altlinux.ru> 2.0.0-alt0.5
- 2.0.0-rc2b

* Mon May 18 2009 Led <led@altlinux.ru> 2.0.0-alt0.4
- 2.0.0-rc2

* Tue May 12 2009 Led <led@altlinux.ru> 2.0.0-alt0.3
- moved blcr support to %name-blcr subpackage

* Tue May 12 2009 Led <led@altlinux.ru> 2.0.0-alt0.2
- with blcr

* Wed May 06 2009 Led <led@altlinux.ru> 2.0.0-alt0.1
- 2.0.0-rc1

* Tue Apr 28 2009 Led <led@altlinux.ru> 1.4.0-alt0.2
- 1.4.0-pre13

* Wed Mar 25 2009 Led <led@altlinux.ru> 1.4.0-alt0.1
- 1.4.0-pre9
- cleaned up spec
- added post scripts

* Tue Mar 10 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.4.0-alt1
- First build for ALTLinux
