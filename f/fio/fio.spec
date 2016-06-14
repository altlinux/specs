%def_enable gfio
%def_enable numa
%def_enable rbd
%def_enable gfapi
%def_enable rdmacm

Name: fio
Version: 2.12
Release: alt1

Summary: IO testing tool
License: GPLv2
Group: System/Kernel and hardware

Url: http://git.kernel.dk/?p=fio.git;a=summary
Source0: %name-%version.tar

BuildRequires: libaio-devel zlib-devel

%{?_enable_gfio:BuildRequires: libgtk+2-devel}
%{?_enable_numa:BuildRequires: libnuma-devel }
%{?_enable_rbd:BuildRequires: ceph-devel}
%{?_enable_gfapi:BuildRequires: libglusterfs3-devel}
%{?_enable_rdmacm:BuildRequires: librdmacm-devel}

%description
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.


%package tools
Summary: Analyze tools for %name
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description tools
fio2gnuplot - analyze a set of fio's log files to turn them into a set of graphical traces using gnuplot tool.
fio_generate_plots - Generate plots for Flexible I/O Tester

%package -n gfio
Summary: Gtk frontend for %name
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description -n gfio
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

This package conteon gtk frontend for %name


%prep
%setup

%build
./configure \
	--prefix=%_prefix \
	--disable-optimizations \
	%{subst_enable gfio} \
	--extra-cflags="%optflags"

%make_build V=1 EXTFLAGS="%optflags"

%install
%make_install DESTDIR=%buildroot install prefix=%_prefix mandir=%_mandir

%files
%doc HOWTO README REPORTING-BUGS examples
%_bindir/genfio
%_bindir/%name
%_man1dir/%name.1.*

%files tools
%_bindir/*
%_datadir/%name
%_man1dir/*
%exclude %_bindir/gfio
%exclude %_bindir/fio
%exclude %_bindir/genfio
%exclude %_man1dir/%name.1.*

%files -n gfio
%_bindir/gfio

%changelog
* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12-alt1
- 2.12
- build with support numa, ceph, gluster, rdmacm

* Sun Jan 19 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.4-alt1
- 2.1.4
- add packages fio-tools and gfio

* Thu Dec 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.11-alt1
- 2.0.11

* Fri Nov 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.10-alt1
- 2.0.10

* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.59-alt1
- 1.59

* Fri Jul 22 2011 Victor Forsiuk <force@altlinux.org> 1.57-alt1
- 1.57

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 1.55-alt1
- 1.55

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 1.37-alt1
- 1.36 -> 1.37

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 1.36-alt1
- 1.34 -> 1.36

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.34-alt1
- 1.24 -> 1.34

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.24-alt1
- 1.23 -> 1.24

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.21 -> 1.23

* Sat Jul 19 2008 Igor Zubkov <icesik@altlinux.org> 1.21-alt1
- 1.17.2 -> 1.21

* Thu Nov 01 2007 Igor Zubkov <icesik@altlinux.org> 1.17.2-alt1
- build for Sisyphus

