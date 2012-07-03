
%define tbname         NVIDIA-Linux-x86
%ifarch x86_64
%define tbname         NVIDIA-Linux-x86_64
%endif
%define virtual_pkg_name NVIDIA_GLX
%define bin_pkg_name     nvidia_glx
%define module_name    nvidia
%define dirsuffix %nil
%ifarch x86_64
%define dirsuffix -no-compat32
%endif

# version-release
%define nv_version 295
%define nv_release 20
%define nv_minor %nil
%define pkg_rel alt98
%def_disable common
%def_disable kernelsource

%define tbver %{nv_version}.%{nv_release}.%{nv_minor}
%if "%nv_minor" == "%nil"
%define tbver %{nv_version}.%{nv_release}
%endif
%define module_version	%nv_version%nv_release%nv_minor
%define module_release	%pkg_rel

%define myGroup System/Kernel and hardware
%define mySummary NVIDIA drivers and OpenGL libraries for XOrg X-server
%define mySummaryRu Драйверы NVIDIA и библиотеки OpenGL для Х-сервера XOrg
%define myUrl http://www.nvidia.com
%define myVendor NVIDIA Corp.
%define myLicense NVIDIA

%define mods /modules
%define exts /modules/extensions
%define drvs /modules/drivers
%define lib_sym_dir %_sysconfdir/X11/%_lib
%define nv_lib_sym_dir %{lib_sym_dir}_nvidia
%define nv_lib32_sym_dir %_sysconfdir/X11/lib_nvidia
%define xdrv_d /usr/libexec/X11/drv.d
%define xdrv_d_old /usr/X11R6/lib/drv.d
%define xdrv_pre_d /usr/libexec/X11/drvpre.d
%define xdrv_pre_d_old /usr/X11R6/lib/drvpre.d

%define xinf_dir %_datadir/hwdatabase/videoaliases/
%define nv_workdirdir %_localstatedir/nvidia
%define tls_lib_dir %_libdir
%define x11_lib_dir %_libdir
%define x11_lib_old /usr/X11R6/lib
%define x11_mod_dir /usr/%_lib/X11%mods
%define x11_mod_old /usr/X11R6/%_lib%mods
%define x11_drv_dir /usr/%_lib/X11%drvs
%define x11_drv_old /usr/%_lib/X11%drvs
%define x11_ext_dir /usr/%_lib/X11%exts
%define x11_ext_old /usr/X11R6/%_lib%exts
%define x11driver_dir %_libdir/X11
%define nv_lib_dir_prefix %_libdir/nvidia_
%define nv_lib_dir_prefix_old /usr/X11R6/%_lib/nvidia_
%define nv_lib_dir %nv_lib_dir_prefix%tbver

%add_findprov_lib_path %nv_lib_dir/*
%add_findreq_skiplist %_libdir/*
%add_findreq_skiplist %x11_lib_dir/*
%add_findreq_skiplist %x11_lib_old/*
%add_findreq_skiplist %_bindir/nvidia-bug-report*.sh

%if "%nv_minor" == "%nil"
Name: nvidia_glx_src_%nv_version.%nv_release
Version: %nv_version.%nv_release
%else
Name: nvidia_glx_src_%nv_version.%nv_release.%nv_minor
Version: %nv_version.%nv_release.%nv_minor
%endif
Release: %pkg_rel

Source0: null
Source201: ftp://download.nvidia.com/XFree86/Linux-x86/%tbver/NVIDIA-Linux-x86-%tbver.run
Source202: ftp://download.nvidia.com/XFree86/Linux-x86_64/%tbver/NVIDIA-Linux-x86_64-%tbver-no-compat32.run

Source2: nvidia.xinf
Source100: nvidia_create_xinf

BuildRequires: kernel-build-tools rpm-macros-alternatives
ExclusiveArch: %ix86 x86_64
#ExcludeArch: ppc64 x86_64 ppc s390 s390x ia64



Group: %myGroup
Summary: %mySummary
Summary(ru_RU.UTF-8): %mySummaryRu
Url: %myUrl
License: %myLicense
%description
Sources for %{bin_pkg_name}_%{version} package


%package -n %{bin_pkg_name}_%{version}
PreReq: %{bin_pkg_name}_common >= %version
Requires(post): x11presetdrv
Provides: %virtual_pkg_name = %version-%release
Obsoletes: %virtual_pkg_name < %version-%release
#
Group: %myGroup
Summary: %mySummary
Summary(ru_RU.UTF-8): %mySummaryRu
Url: %myUrl
License: %myLicense
#
%description -n %{bin_pkg_name}_%{version}
NVIDIA XFree86 4.x server drivers and OpenGL libraries for GeForce/Quadro
based video cards. Older RIVA 128 and RIVA TNT/TNT2 based video cards are
supported by the server module shipping with XOrg, nv_drv.so. You
should install this package if you have one of the newer cards.

You must also install the NVIDIA_kernel package for your current kernel
if you want NVIDIA module and OpenGL libraries for XOrg X server.
#
%description -n %{bin_pkg_name}_%{version} -l ru_RU.UTF-8
Драйверы и OpenGL-библиотеки для Х-сервера X11 и видеокарт NVIDIA на базе
GeForce/Quadro. Более ранние версии видеокарт на базе RIVA 128 и RIVA TNT/TNT2
поддерживаются модулем nv_drv.so, входящим в состав сервера XOrg.
Если вы имеете одну из этих новых видеокарт, то вам желательно установить данный
пакет.

Если вы желаете использовать модули NVIDIA и библиотеки OpenGL для Х-сервера XOrg,
то вы должны также установить пакет NVIDIA_kernel для текущего ядра.

%package -n kernel-source-%module_name-%module_version
Group: Development/Kernel
Summary: Linux %module_name modules sources
License: %myLicense
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
#
%description -n kernel-source-%module_name-%module_version
%module_name modules sources for Linux kernel

%package -n %{bin_pkg_name}-devel
Group: Development/C
Summary: Development files for NVIDIA OpenGL
License: %myLicense
#
%description -n %{bin_pkg_name}-devel
Development files for NVIDIA OpenGL

%package -n libcuda
Group: Development/C
Summary: CUDA library
License: %myLicense
%description -n libcuda
NVIDIA CUDA library

%package -n libcuda-devel
Group: Development/C
Summary: Development files for NVIDIA CUDA
License: %myLicense
Requires: libcuda = %version-%release
%description -n libcuda-devel
Development files for NVIDIA CUDA

%package -n libvdpau
Group: Development/C
Summary: VDPAU library
License: %myLicense
%description -n libvdpau
NVIDIA VDPAU library

%package -n libvdpau-devel
Group: Development/C
Summary: Development files for NVIDIA VDPAU
License: %myLicense
Requires: libvdpau = %version-%release libX11-devel
%description -n libvdpau-devel
Development files for NVIDIA VDPAU

%prep
%setup -T -c -n %tbname-%tbver%dirsuffix
rm -rf %_builddir/%tbname-%tbver%dirsuffix
cd %_builddir
%ifarch x86_64
sh %SOURCE202 -x
%else
sh %SOURCE201 -x
%endif
cd %tbname-%tbver%dirsuffix

pushd kernel/
rm -rf precompiled
popd


%build


%install
%set_verify_elf_method textrel=relaxed
%brp_strip_none %_libdir/*
%brp_strip_none %nv_lib_dir/*

soname()
{
    readelf -a $1| grep SONAME| sed 's/.*\[//'| sed 's/\].*//'
}

%__mkdir_p %buildroot/%_sbindir
%__mkdir_p %buildroot/%tls_lib_dir
%__mkdir_p %buildroot/%nv_lib_dir
%__mkdir_p %buildroot/%x11_mod_dir
#%__mkdir_p %buildroot/%x11_mod_old
%__mkdir_p %buildroot/%x11_drv_dir
#%__mkdir_p %buildroot/%x11_drv_old
%__mkdir_p %buildroot/%x11_ext_dir
#%__mkdir_p %buildroot/%x11_ext_old
%__mkdir_p %buildroot/%lib_sym_dir
%__mkdir_p %buildroot/%nv_lib_sym_dir
%__mkdir_p %buildroot/%nv_lib32_sym_dir
%__mkdir_p %buildroot/%xdrv_d
#%__mkdir_p %buildroot/%xdrv_d_old
%__mkdir_p %buildroot/%xdrv_pre_d
%__mkdir_p %buildroot/%xinf_dir
%__mkdir_p %buildroot/%nv_workdirdir


# install libraries
for n in cuda vdpau; do
    if [ -f lib${n}.so.%tbver ]; then
	libsoname=`soname lib${n}.so.%tbver`
	install -m 0644 lib${n}.so.%tbver \
	    %buildroot/%_libdir/$libsoname
	[ -e %buildroot/%_libdir/lib${n}.so ] \
	    || ln -s $libsoname %buildroot/%_libdir/lib${n}.so
	#ln -s $libsoname %buildroot/%_libdir/lib${n}.so
    fi
done
%__install -m 0644 libnvidia-glcore.so.%tbver %buildroot/%_libdir/
%__install -m 0644 tls/libnvidia-tls.so.%tbver %buildroot/%_libdir/

%__ln_s %nv_lib_dir/nvidia.xinf %buildroot/%nv_lib_sym_dir/nvidia.xinf
%__ln_s %nv_lib_dir/nvidia.xinf %buildroot/%xinf_dir/nvidia-%version.xinf
%__install -m 0644 %SOURCE2 %buildroot/%nv_lib_dir/nvidia.xinf

if [ -f nvidia_drv.o ] ; then
    %__install -m 0644 nvidia_drv.o  %buildroot/%nv_lib_dir/
fi
if [ -f nvidia_drv.so ] ; then
    %__install -m 0644 nvidia_drv.so %buildroot/%nv_lib_dir/
fi

[ -f libnvidia-wfb.so.%tbver ] && \
%__install -m 0644 libnvidia-wfb.so.%tbver %buildroot/%nv_lib_dir/libwfb.so

%__install -m 0644 libglx.so.%tbver %buildroot/%nv_lib_dir/libglx.so
%__ln_s libglx.so %buildroot/%nv_lib_dir/libglx.a

%__install -m 0644 libGL.so.%tbver  %buildroot/%nv_lib_dir/libGL.so

%__install -m 0644 libXvMCNVIDIA.so.%tbver %buildroot/%nv_lib_dir/libXvMCNVIDIA.so
%__ln_s libXvMCNVIDIA.so %buildroot/%nv_lib_dir/libNVIDIAXvMC.so

%__install -m 0644 libvdpau_nvidia.so.%tbver %buildroot/%nv_lib_dir/libvdpau_nvidia.so
%__install -m 0644 libnvidia-cfg.so.%tbver %buildroot/%nv_lib_dir/libnvidia-cfg.so
/sbin/ldconfig -n %buildroot/%nv_lib_dir

# kernel-source install
%__rm -rf kernel-source-%module_name-%module_version/
%__mkdir_p %buildroot/%_usrsrc/kernel/sources/ kernel-source-%module_name-%module_version/
%__cp -ar kernel/* kernel-source-%module_name-%module_version/
%__cp LICENSE kernel-source-%module_name-%module_version/
tar -c kernel-source-%module_name-%module_version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

# install headers
%__mkdir_p %buildroot/%_includedir/nvidia/
for D in GL cuda vdpau; do
    d=`echo "$D"| tr A-Z a-z`
    if [ -n "`ls -1 ${d}*.h`" ]; then
	mkdir %buildroot/%_includedir/$D/
	%__cp -ar ${d}*.h %buildroot/%_includedir/$D/
    fi
done
mv %buildroot/%_includedir/GL %buildroot/%_includedir/nvidia/

# install scripts
mkdir -p %buildroot/%_bindir
install -m 0755 nvidia-bug-report.sh %buildroot/%_bindir/nvidia-bug-report-%version.sh
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/%name <<__EOF__
%_bindir/nvidia-bug-report.sh %_bindir/nvidia-bug-report-%version.sh %version
__EOF__


%post -n %{bin_pkg_name}_%{version}
# switch nvidia driver and libraries
if [ -z "$DURING_INSTALL" ]; then
    X11PRESETDRV=`which x11presetdrv 2>/dev/null`
    if [ -n "$X11PRESETDRV" ]; then
	$X11PRESETDRV ||:
    else
	echo "Warning! x11presetdrv program not found!" >&2
    fi
    X11SETUPDRV=`which x11setupdrv 2>/dev/null`
    if [ -n "$X11SETUPDRV" ]; then
	$X11SETUPDRV ||:
    fi
fi

%postun -n %{bin_pkg_name}_%{version}
X11SETUPDRV=`which x11setupdrv 2>/dev/null`
if [ -n "$X11SETUPDRV" ]; then
    $X11SETUPDRV ||:
fi


%files -n %{bin_pkg_name}_%{version}
%doc LICENSE
%doc html NVIDIA_Changelog README.txt
#
%_libdir/libnvidia-glcore.so.%version
%_libdir/libnvidia-tls.so.%version
%_altdir/%name
%_bindir/nvidia-bug-report-%version.sh
%dir %nv_lib_dir
%nv_lib_dir/nvidia_drv.*
%nv_lib_dir/libglx.*
%nv_lib_dir/libGL.so*
%nv_lib_dir/lib*XvMC*.so*
%nv_lib_dir/libnvidia-cfg.so*
%nv_lib_dir/libvdpau_nvidia.so
%nv_lib_dir/libwfb.so
%nv_lib_dir/libnvidia-wfb.so*
%nv_lib_dir/nvidia.xinf
%xinf_dir/nvidia-%version.xinf

%if_enabled common
%files -n %{bin_pkg_name}-devel
%dir %_includedir/nvidia
%_includedir/nvidia/GL

%if 0
%files -n libvdpau
%_libdir/libvdpau.so.*

%files -n libvdpau-devel
%_libdir/libvdpau.so
%_includedir/vdpau
%endif

#%files -n libcuda
#%_libdir/libcuda.so.*

#%files -n libcuda-devel
#%_libdir/libcuda.so
#%_includedir/cuda
%endif

%if_enabled kernelsource
%files -n kernel-source-%module_name-%module_version
%_usrsrc/*
%endif

%changelog
* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt98
- don't package kernel module sources

* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt97
- new release 295.20

* Tue Nov 22 2011 Sergey V Turchin <zerg@altlinux.org> 290.10-alt96
- new release 290.10

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 285.05.09-alt95
- new release 285.05.09

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 280.13-alt94
- new release 280.13

* Tue Aug 02 2011 Sergey V Turchin <zerg@altlinux.org> 275.21-alt93
- new release 275.21

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 275.09.07-alt92
- new release 275.09.07

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.19-alt91
- new release 270.41.19

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.06-alt90
- new release 270.41.06

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt89
- new release 270.41.03

* Tue Mar 15 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.44-alt87.M51.1
- built for M51

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.44-alt88
- new release 260.19.44

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.36-alt87
- new release 260.19.36

* Fri Dec 24 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.29-alt86
- new release 260.19.29

* Wed Nov 10 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.21-alt85
- new version

* Thu Oct 21 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.12-alt84
- new release 260.19.12
- don't package devel files

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt83
- new release 256.53
- split common subpackage to separate src.rpm

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 256.52-alt82
- new release 256.52

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 256.44-alt81
- new release 256.44

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt79.M51.1
- built for M51

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt80
- new release 256.35
- make nvidia-bug-report.sh as alternative

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt79
- new release 195.36.31

* Mon Apr 26 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.24-alt78
- new release 195.36.24

* Tue Mar 16 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt77
- new release 195.36.15

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.08-alt76
- new release 195.36.08

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.03-alt75
- new release 195.36.03

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73.M40.1
- built for M40

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73.M41.1
- built for M41

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt74
- remove ldconfig from %%post

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73
- new version

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt71.M41.1
- built for M41

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt71.M40.1
- built for M40

* Wed Oct 28 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt72
- new version

* Thu Oct 15 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt71
- don't package libvdpau
- fix file perissions

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt70
- add 0x087D to .xinf (ALT#21688)

* Wed Sep 09 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt69
- don't restore %_libdir/X11/modules/libwfb.so

* Mon Aug 24 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt68
- new version

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.31-alt67
- new version

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt66
- add libdri.so switching

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt65
- check kernel module symlink when x11presetdrv

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt64
- new version

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 180.60-alt63
- new version

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 180.51-alt62
- new version

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 180.44-alt61
- new version

* Wed Mar 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.37-alt60
- new beta

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt59
- new version

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt59
- update xinf-file

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt58
- remove x11setupdrv requires
- don't use deprecated macroses in post-scripts

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt57
- new version

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt56
- move vdpau includes upper

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt55
- reduce debug messages when update symlinks during x11setupdrv

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt54
- libvdpau and vdpau nvidia module

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt53
- new version

* Fri Dec 26 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt52
- don't touch proper symlinks during x11setupdrv
- remove *_ldconfig macroses frpm post* scripts

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt51
- new release

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 177.80-alt50
- new version

* Fri Oct 03 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt49
- remove 10DE:0242(GF 6100) from .xinf

* Fri Aug 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt48
- add support for /etc/X11/lib64
- add support for 32-bit libs switching on x86_64
  (requies to install proper i586-nvidia_glx_XXXX package
  or copy /usr/lib/nvidia_XXXX from proper i586 package)

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt47
- new version

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.09-alt46
- new version

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.05-alt45
- new version

* Mon Mar 17 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt44
- use libsysfs instead of libpci in drvpre.d/nvidia

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt43
- update xinf-file

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt42
- new version

* Wed Jan 23 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt41
- new version

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt40
- new version

* Fri Dec 14 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt40
- clean xinf-file

* Thu Sep 27 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt39
- fix selecting best driver in drvpre.d/nvidia

* Wed Sep 26 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt38
- add more versbosity to drvpre.d/nvidia

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt37
- reduce executed code in drvpre.d if no nvidia cards found

* Mon Sep 24 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt36
- more check the loaded kernel version

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt35
- new version

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt34
- fix crush of drvpre.d/nvidia

* Thu Sep 20 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt33
- check loaded kernel module version before try to unload

* Wed Sep 19 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt32
- add autoswitching of kernel module

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt31
- new version

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.09-alt30
- new version

* Thu Mar 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9755-alt29
- new version
- megre x86_64 and ix86 into one src.rpm
- update package description

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt28
- fix modules path in %%post

* Wed Jan 24 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt27
- add info file for alterator-x11

* Wed Jan 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt26
- new version

* Tue Dec 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9631-alt25
- new version

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9629-alt24
- new version

* Tue Nov 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt23
- add nvidia-bug-report.sh

* Tue Oct 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt22
- new version

* Mon Oct 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt21
- remove requires to rtld(GNU_HASH)

* Thu Oct 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt20
- turn on tls checking in x11setupdrv module
- turn off verbosity for /usr/X11R6 support by default

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt19
- new version
- add libnvidia-cfg.so to package

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8762-alt18
- new version

* Mon Apr 10 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8756-alt17
- new version

* Tue Jan 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt16
- fix to work with old and new xorg

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt15
- new version

* Thu Aug 25 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt14
- dont restore libglx.so for Compact-3.0

* Thu Aug 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt13
- symlink /etc/X11/lib_nvidia/nvidia_drv.* to existing file again

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt12
- new version

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7667-alt11
- new version

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt10
- add libglx.so
- turn off verbosity of /usr/X11R6/lib/drv.d/nvidia by default
  (added command line options)

* Wed Jul 06 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt9
- fix path to .versions/nvidia in %%post

* Thu Jun 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt8
- change setgl to x11setupdrv in %%post
- symlink /etc/X11/lib_nvidia/nvidia_drv.* to unexisting file by default

* Tue Jun 14 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt7
- add symlink libnvidia-tls.so.1 to /usr/lib
- do not check for tls in /usr/X11R6/lib/nvidia
- restore symlinks for libglx.a and libGL.so.1 in /usr/X11R6/lib if absent

* Fri Jun 10 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt6
- move writable symlinks to %nv_lib_sym_dir
- add check for tls to link libnvidia-tls.so correctly

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt5
- new x11 driver switch system; %xdrv_d/nvidia adjust the driver

* Fri Apr 29 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt4
- fix provides for X configurator

* Thu Apr 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt3
- add kernel-source-nvidia subpackage

* Wed Apr 06 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt2
- fix nvidia_set_glx

* Mon Apr 04 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt1
- new version

* Tue Mar 15 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7167-alt1
- new version
- service start after network by default

* Mon Nov 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6629-alt1
- new version

* Fri Oct 08 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6111-alt2
- try to fix link to libGL.so.1 when service nvidia_glx starts

* Fri Aug 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6111-alt1
- new version

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt4
- ignore non-NVIDIA videocards via pciscan in initscript

* Tue Jul 13 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt3
- add %%ghost files to -common package

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt2
- fix libnvidia-tls.so.1 link placement

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt1
- new version

* Tue Feb 03 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.5336-alt1
- new version

* Mon Jan 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.5328-alt2
- initscript compatible with 2.6.x kernels
- add start on 3,4 runlevels

* Tue Dec 23 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.5328-alt1
- new version

* Tue Dec 23 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt7
- fix initscript status message

* Thu Oct 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt6
- fix initscript fail message

* Fri Sep 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt5
- fix %%post

* Fri Sep 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt4
- force install service nvidia_lgx when variable DURING_INSTALL=1

* Mon Sep 15 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt3
- fix initscript

* Mon Sep 15 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4363-alt2
- make possible to install different versions together

* Wed Jul 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt1
- new version

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4363-alt1
- new version

* Tue May 06 2003 Sergey V Turchin <zerg at altlinux dot ru> 1.0.4349-alt2
- remove requires to XFree86-server libGLwrapper
- remove very old versions from %%versions

* Wed Apr 02 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt1
- New upstream version

* Sun Feb 16 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.4191-alt3
- Fixed file permissions on %%doc
- Added Summary and %%description in Russian

* Fri Dec 20 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.4191-alt2
- fix link to libglx.so

* Thu Dec 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.4191-alt1
- new version

* Fri Sep 13 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.3123-alt1
- new version

* Thu Jun 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.2960-alt1
- new version

* Fri Mar 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.2802-alt1
- new version

* Fri Feb 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.2313-alt1
- prepare for Sisyphus

* Thu Jan 31 2002 Sergey V Turchin <zerg@altlinux.ru> ALL-alt2
- fix requires
- cleanup spec

* Tue Jan 29 2002 Sergey V Turchin <zerg@altlinux.ru> ALL-alt1
- add interactive build

* Sat Dec 29 2001 Ivan Zakharyaschev <imz@altlinux.ru> 1.0.2313-alt3
- fix requires version (add 1.0 prefix)

* Tue Dec 18 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.2313-alt2
- Fixed requires as kernel_version of this driver is 2314

* Wed Dec 05 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.2313-alt1
- new version

* Thu Jun 14 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.1251-alt5
- changed pakage name to nvidiaGL

* Fri Jun 08 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.1251-alt4
- fix requires

* Wed May 23 2001 Sergey V Turchin <zerg@altlinux.ru>
- first build
