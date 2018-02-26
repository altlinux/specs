%define nvIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define nvIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define nvIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define nvIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define module_name	nvidia
%define module_version	295.59
%define module_release	alt1
%define module_srcver	%(echo %module_version | tr -d .)
%define xorg_ver %{get_version xorg-server}
%if "%xorg_ver" == ""
%define xorg_ver %{get_version xorg-x11-server}
%endif
%nvIF_ver_lt %xorg_ver 1.6
%define legacy1 71.86.13
%else
%define legacy1 %nil
%endif
%define legacy1_src %(echo %legacy1 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.11
%define legacy2 96.43.20
%else
%define legacy2 %nil
%endif
%define legacy2_src %(echo %legacy2 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.13
%define legacy3 173.14.35
%else
%define legacy3 %nil
%endif
%define legacy3_src %(echo %legacy3 | tr -d .)
%define mod_ver_list %version %legacy1 %legacy2 %legacy3

%define upstream_module_name	NVIDIA_kernel

%define kversion	3.4.4
%define krelease	alt1
%define flavour		un-def

%define module_dir /lib/modules/%kversion-%flavour-%krelease/nVidia
%define module_local_dir /lib/modules/nvidia
%define module_version_dir /lib/modules/%kversion-%flavour-%krelease/.versions
%define nvidia_workdir %_localstatedir/nvidia
%define module_ext .ko
%nvIF_ver_lt "%kversion" "2.5.0"
%define module_ext .o
%endif

Summary:	nVidia video card drivers
Name:		kernel-modules-%module_name-%flavour
Version:	%module_version
Release:	%module_release.197636.1
License:	Proprietary
Group:		System/Kernel and hardware
URL:		http://www.nvidia.com

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS:	Linux
%if "%flavour" == "std-pae"
ExclusiveArch:	%ix86
%else
ExclusiveArch:	%ix86 x86_64
%endif

BuildRequires(pre): rpm-build-kernel xorg-x11-server
BuildRequires: rpm-utils
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_srcver
%if "%legacy1" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy1_src
%endif
%if "%legacy2" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy2_src
%endif
%if "%legacy3" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy3_src
%endif

Provides:  	kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: 	kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: 	kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Conflicts: modutils < 2.4.27-alt4

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
#Requires:       NVIDIA_GLX = %version
Requires:       nvidia_glx_%version
%if "%legacy1" != "%nil"
Requires:       nvidia_glx_%legacy1
%endif
%if "%legacy2" != "%nil"
Requires:       nvidia_glx_%legacy2
%endif
%if "%legacy3" != "%nil"
Requires:       nvidia_glx_%legacy3
%endif
Provides:       NVIDIA_kernel = %version

%description
nVidia video card drivers that provide 3d and 2d graphics support for XFree86
Xserver.


%prep
%setup -cT
for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    %__rm -rf kernel-source-%module_name-$sffx
    tar -jxvf %_usrsrc/kernel/sources/kernel-source-%module_name-$sffx.tar.bz2

    pushd kernel-source-%module_name-$sffx
    %__rm -f makefile Makefile
    %__ln_s Makefile.kbuild Makefile
    popd
done


%build
for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    pushd kernel-source-%module_name-$sffx
    %make_build -C %_usrsrc/linux-%kversion-%flavour modules \
	SUBDIRS=$PWD TEMP_DIR=$PWD/ \
	ARCH=%base_arch \
	SYSSRC=%_usrsrc/linux-%kversion-%flavour
    popd
done

%install
%__mkdir_p %buildroot/%module_dir
%__mkdir_p %buildroot/%module_local_dir
%__mkdir_p %buildroot/%module_version_dir
%__mkdir_p %buildroot/%nvidia_workdir

for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    pushd kernel-source-%module_name-$sffx
    %__install -p -m644 %module_name%module_ext %buildroot/%module_local_dir/%kversion-%flavour-%krelease-$ver
popd
done

echo -n "%version" >%buildroot/%nvidia_workdir/%kversion-%flavour-%krelease
ln -s %nvidia_workdir/%kversion-%flavour-%krelease %buildroot/%module_version_dir/%module_name
ln -s %module_local_dir/%kversion-%flavour-%krelease-%version %buildroot/%module_dir/%module_name%module_ext


%post
# switch nvidia driver and libraries
if [ -z "$DURING_INSTALL" ]; then
    if [ "`uname -r`" == "%kversion-%flavour-%krelease" ] ; then
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
fi
%post_kernel_modules %kversion-%flavour-%krelease

%postun
if [ -z "$DURING_INSTALL" ]; then
    if [ "`uname -r`" == "%kversion-%flavour-%krelease" ] ; then
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
fi
%post_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir
%module_version_dir/%module_name
%module_local_dir/%kversion-%flavour-%krelease-*
%config(noreplace) %nvidia_workdir/%kversion-%flavour-%krelease

%changelog
* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 295.59-alt1.197636.1
- Build for kernel-image-un-def-3.4.4-alt1.

* Thu Jun 14 2012 Sergey V Turchin <zerg at altlinux dot org> 295.59-alt1
- new release (295.59)

* Fri Jun 08 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt3
- fix requires

* Thu Jun 07 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt2
- new release (173.14.35 with xorg-server-1.12 support)

* Thu May 17 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt1
- new release (295.53)

* Thu May 03 2012 Sergey V Turchin <zerg at altlinux dot org> 295.49-alt1
- new release (295.49)

* Wed Apr 11 2012 Sergey V Turchin <zerg at altlinux dot org> 295.40-alt1
- new release (295.40)
- fixed CVE-2012-0946

* Mon Mar 26 2012 Sergey V Turchin <zerg at altlinux dot org> 295.33-alt1
- new release (295.33)

* Wed Feb 15 2012 Sergey V Turchin <zerg at altlinux dot org> 295.20-alt1
- new release (295.20)

* Wed Nov 23 2011 Sergey V Turchin <zerg at altlinux dot org> 290.10-alt1
- new release (290.10)

* Tue Oct 04 2011 Sergey V Turchin <zerg at altlinux dot org> 285.05.09-alt1
- new pre-release (285.05.09)

* Wed Aug 03 2011 Sergey V Turchin <zerg at altlinux dot org> 280.13-alt1
- new release (280.13)
- add ExclusiveArch workaround for std-pae

* Tue Aug 02 2011 Sergey V Turchin <zerg at altlinux dot org> 275.21-alt1
- new releases (275.21, 173.14.31, 96.43.20)

* Fri Jul 01 2011 Anton Protopopov <aspsk@altlinux.org> 275.09.07-alt2
- Use @ kernelarch @ macro in ExclusiveArch

* Wed Jun 15 2011 Sergey V Turchin <zerg at altlinux dot org> 275.09.07-alt1
- new release (275.09.07)

* Sat May 28 2011 Anton Protopopov <aspsk@altlinux.org> 270.41.19-alt2
- Use %ix86 x86_64

* Mon May 23 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.19-alt1
- new release (270.41.19)

* Mon Apr 25 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.06-alt1
- new releases (270.41.06, 173.14.30)

* Wed Apr 13 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.03-alt1
- new release (270.41.03)

* Mon Mar 14 2011 Sergey V Turchin <zerg at altlinux dot org> 260.19.44-alt1
- new release (260.19.44)

* Tue Jan 25 2011 Sergey V Turchin <zerg at altlinux dot org> 260.19.36-alt1
- new release (260.19.36)

* Fri Dec 24 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.29-alt1
- new release (260.19.29)

* Wed Nov 10 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.21-alt1
- new release (260.19.21)

* Wed Nov 03 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.12-alt2
- new release (96.43.19) with xorg-1.9 support

* Mon Oct 25 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.12-alt1
- new release (260.19.12)

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt4
- fix to build

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt3
- new release (173.14.28)

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt2
- don't build xorg incompatible modules

* Wed Sep 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt1
- new release (256.53)

* Tue Aug 31 2010 Sergey V Turchin <zerg at altlinux dot org> 256.52-alt1
- new release (256.52)

* Thu Aug 12 2010 Sergey V Turchin <zerg at altlinux dot org> 256.44-alt1
- new release (256.44)

* Mon Jul 19 2010 Sergey V Turchin <zerg at altlinux dot org> 256.35-alt2
- new releases (173.14.27, 96.43.18)

* Wed Jul 14 2010 Sergey V Turchin <zerg at altlinux dot org> 256.35-alt1
- new release (256.35)

* Tue Jun 14 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.31-alt1
- new release (195.36.31)

* Mon Apr 26 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.24-alt1
- new releases (195.36.24, 96.43.17)

* Thu Mar 18 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.15-alt1
- new release (195.36.15)

* Tue Mar 02 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.08-alt1
- new release (195.36.08)

* Thu Feb 18 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.03-alt1
- new beta release (195.36.03)
- new releases (173.14.25, 96.43.16)

* Thu Dec 17 2009 Sergey V Turchin <zerg at altlinux dot org> 190.53-alt1
- new releases (190.53, 173.14.22, 96.43.14)

* Thu Dec 17 2009 Sergey V Turchin <zerg at altlinux dot org> 190.42-alt2
- remove ldconfig from %%post

* Wed Oct 28 2009 Sergey V Turchin <zerg at altlinux dot org> 190.42-alt1
- new release (190.42)

* Tue Sep 08 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.36-alt2
- don't package legacy 71.86.11 because incompatible with current XOrg

* Mon Aug 24 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.36-alt1
- new release (185.18.36)

* Tue Aug 04 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.31-alt1
- new release (185.18.31)

* Thu Jul 02 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt3
- new legacy pre-releases (71.86.11, 96.43.13, 173.14.20)

* Tue Jun 23 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt2
- new legacy release candidates (71.86.10, 96.43.12, 173.14.19)

* Mon Jun 08 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt1
- new release (185.18.14)

* Mon Jun 08 2009 Sergey V Turchin <zerg at altlinux dot org> 180.60-alt1
- new release (180.60)

* Fri Apr 24 2009 Sergey V Turchin <zerg at altlinux dot org> 180.51-alt1
- new release (180.51)

* Thu Apr 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.44-alt1
- new release (180.44)

* Fri Mar 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt2
- new legacy release (173.14.18)

* Thu Mar 12 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt1
- revert to stable 180.29

* Wed Mar 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.37-alt1
- new beta (180.37)

* Tue Mar 10 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt2
- new legacy release (71.86.09)

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt1
- new beta (180.35)

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt1
- new release (180.29)
- new legacy betas (173.14.17, 96.43.11, 71.86.08)
- don't warn if x11setupdrv not found
- don't use deprecated macroses
- always execute %%post_kernel_modules macros

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt1
- new release (180.22)

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt1
- new release (177.82)
- new legacy betas (173.14.15, 96.43.09, 71.86.07)

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 177.80-alt1
- new release (177.80)
- 3 legacy (173.14.12, 96.43.07, 71.86.06)

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt1
- new release (173.14.12)

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.09-alt1
- new release (173.14.09)
- new legacy releases(96.43.07, 71.86.06)

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.05-alt1
- new release (173.14.05)

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt1
- new release (169.12)

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt2
- new legacy releases(96.43.05, 71.86.04)

* Fri Jan 25 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt1
- new release (169.09)

* Wed Dec 26 2007 Sergey Vlasov <vsu@altlinux.ru> 169.07-alt2
- Restructure the spec file to avoid %%if around the "Version:" line (required
  to work properly with gear, which does not support RPM conditionals).

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt1
- new release (169.07)

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt3
- new legacy releases(96.43.01, 71.86.01)

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt2
- bump release to rebuild

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt1
- new release (100.14.19)

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt3
- fix kernel modile filename

* Tue Sep 18 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt2
- use new nvidia drivers packaging scheme
- include legacy kernel modules

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt1
- new release (100.14.11)

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.09-alt1
- new release (100.14.09)

* Thu Mar 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9755-alt1
- new release (9755)

* Wed Feb 21 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt1
- new release (9746)

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1.0.9631-alt2
- Updated dependencies: replaced "Prereq: modutils >= 2.4.27-alt4" with
  "Conflicts: modutils < 2.4.27-alt4" (the dependency on modutils or
  module-init-tools already comes indirectly through kernel-image-%%flavour).

* Thu Dec 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9631-alt1
- new release (9631)

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9629-alt1
- new release (9629)

* Fri Nov 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9626-alt1
- new release (9626)

* Wed Oct 25 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt1
- new release (8776)

* Wed Sep 06 2006 L.A. Kostis <lakostis@altlinux.org> 1.0.8774-alt2
- make build independed from host-arch.

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt1
- new release (8774)

* Wed May 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8762-alt1
- new release (8762)

* Wed Apr 12 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8756-alt1
- new release (8756)
- remove NVIDIA_kernel-1.0-8178-U012206.diff (merged by upstream)

* Sat Mar 18 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.8178-alt2
- Added NVIDIA_kernel-1.0-8178-U012206.diff update patch from the nvnews.net
  forum (fixes several problems with newer kernels, including compilation
  failure with 2.6.16).

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt1
- new release (8178)

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt1
- new release (7676)

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7667-alt1
- new release (7667)

* Tue Jun 21 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.7174-alt3
- Require modutils >= 2.4.27-alt4 because of .versions/nvidia (#7151).

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt2
- add file with module version

* Thu Apr 07 2005 Anton Farygin <rider@altlinux.ru> 1.0.7174-alt1
- new release (7174)

* Mon Mar 14 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.7167-alt1
- New release (7167).
- Removed obsolete compatibility patches.

* Wed Dec 29 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6629-alt2
- Added patches for compatibility with kernel 2.6.10 (Patch2, Patch3).

* Sun Dec 26 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6629-alt1
- New release (6629).

* Wed Oct 20 2004 Anton Farygin <rider@altlinux.ru> 1.0.6111-alt4
- fixed unreslved symbols with kernel 2.6.9

* Sun Oct 17 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6111-alt3
- Rebuild for kernel 2.4.27.

* Mon Sep 06 2004 Anton Farygin <rider@altlinux.ru> 1.0.6111-alt2
- License fixed

* Tue Aug 17 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6111-alt1
- New release (6111).

* Tue Aug 03 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6106-alt2
- Use %%post_kernel_modules and %%postun_kernel_modules macros in scripts.

* Fri Jul 02 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6106-alt1
- New release (6106).

* Thu May 13 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5336-alt2
- Rebuild for kernel 2.4.26.

* Mon Mar 22 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5336-alt1
- New release (5336).
- Removed AGP fix patch (not needed for 5336).
- Modified build for new makefiles.

* Fri Feb 27 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt5
- Updated for the new compiler version selection scheme (GCC_VERSION).

* Wed Feb 18 2004 Anton Farygin <rider@altlinux.ru> 1.0.5328-alt4
- rebuild for 2.6.3 (increment release without changes)

* Mon Feb 16 2004 Anton Farygin <rider@altlinux.ru> 1.0.5328-alt3
- added build scripts for kernel 2.6 

* Thu Jan 15 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt2
- Added patch to work around problems with AGP support (part of the Linux-2.6
  adaptation patch from www.minion.de).

* Mon Dec 22 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt1
- New release (5328).

* Tue Dec 16 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt12
- Fixed compiler selection.

* Fri Nov 28 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt11
- Added Provides/Conflicts to make sure that only one version of the package
  can be installed for each kernel version.

* Tue Nov 18 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt10
- Fixed spec file name.
- Avoid %%postun failure when this package is removed after
  kernel-image-%%flavour (currently rpm cannot prevent this).

* Sat Sep 06 2003 Anton Farygin <rider@altlinux.ru> 1.0.4496-alt9
- /usr/include replaces to macros _includedir
- build requires fix

* Tue Aug 26 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt8
- rebuilt with 2.4.21rel-alt14

* Fri Aug 15 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt7
- rebuilt with 2.4.21rel-alt13

* Wed Aug 13 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt6
- rebuilt with 2.4.21rel-alt12

* Tue Aug 12 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt5
- rebuilt with 2.4.21rel-alt11

* Mon Aug 11 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt4
- rebuilt with 2.4.21rel-alt10

* Thu Aug 07 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt3
- rebuilt with 2.4.21rel-alt9

* Wed Aug 06 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt2
- rebuilt with 2.4.21rel-alt8

* Wed Jul 30 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt1
- new release (4496)
- rebuilt with 2.4.21rel-alt7

* Thu Jul 17 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt5
- rebuilt with 2.4.21rel-alt6

* Wed Jul 16 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt4
- rebuilt with 2.4.21rel-alt5

* Mon Jul 07 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt3
- rebuilt with 2.4.21rel alt3 kernel

* Wed Jul 02 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt2
- add provides NVIDIA_kernel = %version

* Sat Jun 21 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt1
- rebuilt with 2.4.21rel kernel

* Thu Apr 10 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt2
- Provides NVIDIA_kernel for now.

* Sun Mar 23 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt1
- Initial release


