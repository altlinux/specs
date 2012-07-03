%add_findreq_skiplist %_bindir/nvidia-bug-report.sh

%define tbname         NVIDIA-Linux-x86
%ifarch x86_64
%define tbname         NVIDIA-Linux-x86_64
%endif
%define virtual_pkg_name NVIDIA_GLX
%define bin_pkg_name     nvidia_glx
%define module_name    nvidia
%define tbsuffix pkg0

# version-release
%define nv_version 173
%define nv_release 14
%define nv_minor 35
%define pkg_rel alt63
%define set_gl_nvidia_ver 0.6.5
%def_enable kernelsource

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
%define nv_lib_dir_prefix %_libdir/nvidia_
%define nv_lib_dir_prefix_old /usr/X11R6/%_lib/nvidia_
%define nv_lib_dir %nv_lib_dir_prefix%tbver
%add_findprov_lib_path %nv_lib_dir/*
%add_findreq_skiplist %_libdir/*
%add_findreq_skiplist %x11_lib_dir/*
%add_findreq_skiplist %x11_lib_old/*

%if "%nv_minor" == "%nil"
Version: %nv_version.%nv_release
%else
Version: %nv_version.%nv_release.%nv_minor
%endif
Name: %{bin_pkg_name}_src_%{nv_version}.%{nv_release}.%{nv_minor}
Release: %pkg_rel

Source0: null
Source201: ftp://download.nvidia.com/XFree86/Linux-x86/%tbver/NVIDIA-Linux-x86-%tbver-%tbsuffix.run
Source202: ftp://download.nvidia.com/XFree86/Linux-x86_64/%tbver/NVIDIA-Linux-x86_64-%tbver-%tbsuffix.run

Source1: set_gl_nvidia-%set_gl_nvidia_ver.tar.bz2
Source2: nvidia.xinf
Source100: nvidia_create_xinf

BuildRequires: kernel-build-tools libsysfs-devel
ExclusiveArch: %ix86 x86_64
#ExcludeArch: ppc64 x86_64 ppc s390 s390x ia64



Group: %myGroup
Summary: %mySummary
Summary(ru_RU.UTF-8): %mySummaryRu
Url: %myUrl
License: %myLicense
%description
Sources for %{bin_pkg_name}_%{version} package



%package -n %{bin_pkg_name}_common
Conflicts: xorg-x11-mesagl <= 6.8.2-alt7
Requires(post): x11presetdrv
#
Group: %myGroup
Summary: This is common package for usability NVIDIA drivers.
Summary(ru_RU.UTF-8): Пакет для совместимости драйверов NVIDIA.
Url: %myUrl
License: %myLicense
# old
Conflicts: nvidia_glx_100.14.19-100.14.19 <= alt40
Conflicts: nvidia_glx_169.07-169.07 <= alt40
Conflicts: nvidia_glx_169.09-169.09 <= alt41
Conflicts: nvidia_glx_71.86.01-71.86.01 <= alt36
Conflicts: nvidia_glx_96.43.01-96.43.01 <= alt36
#
Conflicts: nvidia_glx_71.86.04-71.86.04 <= alt37
Conflicts: nvidia_glx_71.86.06-71.86.06 <= alt38
Conflicts: nvidia_glx_96.43.05-96.43.05 <= alt37
Conflicts: nvidia_glx_96.43.07-96.43.07 <= alt38
Conflicts: nvidia_glx_169.12-169.12 <= alt44
Conflicts: nvidia_glx_173.14.12-173.14.12 <= alt47
#
%description -n %{bin_pkg_name}_common
This is common package for NVIDIA drivers.
#
%description -n %{bin_pkg_name}_common -l ru_RU.UTF-8
Этот пакет нужен для совместимости при отсутствии
одной из компонент драйверов для NVIDIA.



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

%prep
%setup -T -c -n %tbname-%tbver-%tbsuffix
rm -rf %_builddir/%tbname-%tbver-%tbsuffix
cd %_builddir
%ifarch x86_64
sh %SOURCE202 -x
%else
sh %SOURCE201 -x
%endif
cd %tbname-%tbver-%tbsuffix
tar xvfj %SOURCE1
pushd set_gl_nvidia*
cp settings.h.in settings.h
subst "s|@DEFAULT_VERSION@|%version|" settings.h
subst "s|@LIB_SYML_DIR@|%lib_sym_dir|" settings.h
subst "s|@NV_LIB_SYML_DIR@|%nv_lib_sym_dir|" settings.h
subst "s|@TLS_LIB_DIR@|%tls_lib_dir|" settings.h

subst "s|@XLIB_DIR@|%x11_lib_dir|" settings.h
subst "s|@XLIB_DIR_OLD@|%x11_lib_old|" settings.h

subst "s|@XMOD_DIR@|%x11_mod_dir|" settings.h
subst "s|@XMOD_DIR_OLD@|%x11_mod_old|" settings.h

subst "s|@XDRV_DIR@|%x11_drv_dir|" settings.h
subst "s|@XDRV_DIR_OLD@|%x11_drv_old|" settings.h

subst "s|@XEXT_DIR@|%x11_ext_dir|" settings.h
subst "s|@XEXT_DIR_OLD@|%x11_ext_old|" settings.h

subst "s|@NV_DRV_DIR_PREFIX@|%nv_lib_dir_prefix|" settings.h
subst "s|@NV_DRV_DIR_PREFIX_OLD@|%nv_lib_dir_prefix_old|" settings.h

subst "s|@XINF_DIR@|%xinf_dir|" settings.h
popd

pushd usr/src/nv/
rm -rf precompiled
popd


%build
#make OPTFLAGS="%optflags -Wl,--hash-style=sysv" -C set_gl_nvidia*
make OPTFLAGS="%optflags" -C set_gl_nvidia*
strip set_gl_nvidia*/nvidia
strip set_gl_nvidia*/nvidia_preset
>nvidianull.c
gcc %optflags -c nvidianull.c -o nvidianull.o
#ld --hash-style=sysv --shared nvidianull.o -o libnvidianull.so
ld --shared nvidianull.o -o libnvidianull.so
strip libnvidianull.so


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


%__install -m 0755 set_gl_nvidia*/nvidia %buildroot/%xdrv_d/nvidia
#%__ln_s ../../../..%xdrv_d/nvidia %buildroot/%xdrv_d_old/nvidia

%__install -m 0755 set_gl_nvidia*/nvidia_preset %buildroot/%xdrv_pre_d/nvidia

%__install -m 0755 libnvidianull.so %buildroot/%x11_lib_dir/

%__ln_s %nv_lib_dir/nvidia.xinf %buildroot/%nv_lib_sym_dir/nvidia.xinf
%__ln_s %nv_lib_dir/nvidia.xinf %buildroot/%xinf_dir/nvidia-%version.xinf
%__install -m 0644 %SOURCE2 %buildroot/%nv_lib_dir/nvidia.xinf

[ -f usr/X11R6/lib/%drvs/nvidia_drv.o ] && \
%__install -m 0644 usr/X11R6/lib/%drvs/nvidia_drv.o      %buildroot/%nv_lib_dir/
[ -f usr/X11R6/lib/%drvs/nvidia_drv.so ] && \
%__install -m 0644 usr/X11R6/lib/%drvs/nvidia_drv.so      %buildroot/%nv_lib_dir/

[ -f usr/X11R6/lib/%mods/libnvidia-wfb.so.%tbver ] && \
%__install -m 0644 usr/X11R6/lib/%mods/libnvidia-wfb.so.%tbver %buildroot/%nv_lib_dir/libwfb.so

%__install -m 0644 usr/X11R6/lib/%exts/libglx.so.%tbver %buildroot/%nv_lib_dir/libglx.so
%__ln_s libglx.so %buildroot/%nv_lib_dir/libglx.a

%__install -m 0644 usr/lib/libGL.so.%tbver  %buildroot/%nv_lib_dir/libGL.so

%__install -m 0644 usr/lib/libGLcore.so.%tbver %buildroot/%nv_lib_dir/libGLcore.so

%__install -m 0644 usr/X11R6/lib/libXvMCNVIDIA.so.%tbver %buildroot/%nv_lib_dir/libXvMCNVIDIA.so
%__ln_s libXvMCNVIDIA.so %buildroot/%nv_lib_dir/libNVIDIAXvMC.so

%__install -m 0644 usr/lib/libnvidia-cfg.so.%tbver %buildroot/%nv_lib_dir/libnvidia-cfg.so
%__install -m 0644 usr/lib/libnvidia-tls.so.%tbver %buildroot/%nv_lib_dir/libnvidia-tls.so
%__install -m 0644 usr/bin/tls_test %buildroot/%nv_lib_dir/tls_test
%__install -m 0644 usr/bin/tls_test_dso.so %buildroot/%nv_lib_dir/tls_test_dso.so
/sbin/ldconfig -n %buildroot/%nv_lib_dir
%__install -m 0644 usr/lib/tls/libnvidia-tls.so.%tbver %buildroot/%nv_lib_dir/libnvidia-tls-tls.so
%__ln_s libnvidia-tls-tls.so %buildroot/%nv_lib_dir/libnvidia-tls-tls.so.1

[ -f usr/X11R6/lib/%drvs/nvidia_drv.o ] && \
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/nvidia_drv.o
[ -f usr/X11R6/lib/%drvs/nvidia_drv.so ] && \
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/nvidia_drv.so
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libGLcore.so`
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libNVIDIAXvMC.so`
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/libNVIDIAXvMC.so
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libnvidia-tls.so`
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libnvidia-cfg.so`
%if "%_lib" == "lib64"
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib32_sym_dir/`soname %buildroot/%nv_lib_dir/libGLcore.so`
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib32_sym_dir/`soname %buildroot/%nv_lib_dir/libNVIDIAXvMC.so`
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib32_sym_dir/libNVIDIAXvMC.so
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_lib32_sym_dir/`soname %buildroot/%nv_lib_dir/libnvidia-tls.so`
%endif

if [ -f usr/X11R6/lib/%drvs/nvidia_drv.o ] ; then
%__ln_s ../../../../..%nv_lib_sym_dir/nvidia_drv.o %buildroot/%x11_drv_dir/nvidia_drv.o
#%__ln_s ../../../../..%nv_lib_sym_dir/nvidia_drv.o %buildroot/%x11_drv_old/nvidia_drv.o
fi
if [ -f usr/X11R6/lib/%drvs/nvidia_drv.so ] ; then
%__ln_s ../../../../..%nv_lib_sym_dir/nvidia_drv.so %buildroot/%x11_drv_dir/nvidia_drv.so
#%__ln_s ../../../../..%nv_lib_sym_dir/nvidia_drv.so %buildroot/%x11_drv_old/nvidia_drv.so
fi
%__ln_s ../..%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libGLcore.so` \
    %buildroot/%x11_lib_dir/`soname %buildroot/%nv_lib_dir/libGLcore.so`
%__ln_s ../..%nv_lib_sym_dir/`soname %buildroot/%nv_lib_dir/libNVIDIAXvMC.so` \
    %buildroot/%x11_lib_dir/`soname %buildroot/%nv_lib_dir/libNVIDIAXvMC.so`
%__ln_s ../..%nv_lib_sym_dir/libNVIDIAXvMC.so \
    %buildroot/%x11_lib_dir/libNVIDIAXvMC.so
SONAME=`soname %buildroot/%nv_lib_dir/libnvidia-cfg.so`
%__ln_s ../..%nv_lib_sym_dir/$SONAME %buildroot/%x11_lib_dir/$SONAME
SONAME=`soname %buildroot/%nv_lib_dir/libnvidia-tls.so`
%__ln_s ../..%nv_lib_sym_dir/$SONAME %buildroot/%tls_lib_dir/$SONAME

# kernel-source install
%__rm -rf kernel-source-%module_name-%module_version/
%__mkdir_p %buildroot/%_usrsrc/kernel/sources/ kernel-source-%module_name-%module_version/
%__cp -ar usr/src/nv/* kernel-source-%module_name-%module_version/
%__cp LICENSE kernel-source-%module_name-%module_version/
tar -c kernel-source-%module_name-%module_version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

# install headers
%__mkdir_p %buildroot/%_includedir/nvidia
%__cp -ar usr/include/GL %buildroot/%_includedir/nvidia

# install scripts
mkdir -p %buildroot/%_bindir
install -m 0755 usr/bin/nvidia-bug-report.sh %buildroot/%_bindir/


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

%post -n %{bin_pkg_name}_common
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

%files -n %{bin_pkg_name}_%{version}
%doc LICENSE
%doc usr/share/doc/*
#
%defattr (0555, root, root)
#
%dir %nv_lib_dir
%nv_lib_dir/nvidia_drv.*
%nv_lib_dir/libglx.*
%nv_lib_dir/libGL.so*
%nv_lib_dir/libGLcore.so*
%nv_lib_dir/lib*XvMC*.so*
%nv_lib_dir/libnvidia-tls.so*
%nv_lib_dir/libnvidia-tls-tls.so*
%nv_lib_dir/libnvidia-cfg.so*
%attr(0755,root,root) %nv_lib_dir/tls_test
%nv_lib_dir/tls_test*.so
%nv_lib_dir/libwfb.so
%nv_lib_dir/libnvidia-wfb.so*
%nv_lib_dir/nvidia.xinf
%xinf_dir/nvidia-%version.xinf

%if 0
%files -n %{bin_pkg_name}_common
%_bindir/nvidia-bug-report.sh
%xdrv_pre_d/nvidia
%xdrv_d/nvidia
#%xdrv_d_old/nvidia
%x11_lib_dir/libnvidianull.so
%dir %nv_lib_sym_dir/
#
%nv_lib_sym_dir/nvidia_drv.*
%x11_drv_dir/nvidia_drv.*
#%ghost %x11_drv_old/nvidia_drv.*
#
%nv_workdirdir
%nv_lib_sym_dir/libGLcore.so.?
%nv_lib_sym_dir/libXvMCNVIDIA_dynamic.so.?
%nv_lib_sym_dir/libNVIDIAXvMC.so
%nv_lib_sym_dir/libnvidia-tls.so.?
%nv_lib_sym_dir/libnvidia-cfg.so.?
#%nv_lib_sym_dir/nvidia.xinf
%if "%_lib" == "lib64"
%dir %nv_lib32_sym_dir/
%nv_lib32_sym_dir/libGLcore.so.?
%nv_lib32_sym_dir/libXvMCNVIDIA_dynamic.so.?
%nv_lib32_sym_dir/libNVIDIAXvMC.so
%nv_lib32_sym_dir/libnvidia-tls.so.?
%endif
#
%x11_lib_dir/libGLcore.so.?
%x11_lib_dir/libXvMCNVIDIA_dynamic.so.?
%x11_lib_dir/libNVIDIAXvMC.so
%tls_lib_dir/libnvidia-tls.so.?
%x11_lib_dir/libnvidia-cfg.so.?

%files -n %{bin_pkg_name}-devel
%_includedir/nvidia
%endif

%if_enabled kernelsource
%files -n kernel-source-%module_name-%module_version
%_usrsrc/*
%endif

%changelog
* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 173.14.35-alt63
- new release 173.14.35

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 173.14.34-alt62
- new release 173.14.34

* Tue Aug 02 2011 Sergey V Turchin <zerg@altlinux.org> 173.14.31-alt61
- new release 173.14.31

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 173.14.30-alt60
- new release 173.14.30

* Fri Oct 01 2010 Sergey V Turchin <zerg@altlinux.org> 173.14.28-alt59
- new release 173.14.28

* Mon Jul 19 2010 Sergey V Turchin <zerg@altlinux.org> 173.14.27-alt58
- new release 173.14.27

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 173.14.25-alt57
- new release 173.14.25

* Thu Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 173.14.22-alt56
- release 173.14.22
- remove ldconfig from %post
- fix file permissions

* Thu Jul 02 2009 Sergey V Turchin <zerg@altlinux.org> 173.14.20-alt54
- release 173.14.20

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 173.14.19-alt53
- release 173.14.19

* Thu Mar 12 2009 Sergey V Turchin <zerg at altlinux dot org> 173.14.18-alt52
- release 173.14.18

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 173.14.17-alt51
- beta 173.14.17
- remove x11setupdrv requires
- don't use deprecated macroses

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.15-alt50
- new beta 173.14.15

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
