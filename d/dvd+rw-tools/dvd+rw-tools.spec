%define binaries growisofs dvd+rw-format dvd+rw-booktype dvd+rw-mediainfo dvd-ram-control

Name: dvd+rw-tools
Version: 7.1
Release: alt2

Summary: Toolchain for mastering recordable DVD media
License: %gpl2plus
Group: Archiving/Cd burning
Url: http://fy.chalmers.se/~appro/linux/DVD+RW

Source: %url/tools/%name-%version.tar
Patch1: %name-5.17.4.8.6-alt-setmntent.patch
Patch2: %name-5.17.4.8.6-alt-subfs.patch
Patch3: %name-6.0-alt-umount.patch
Patch4: %name-7.0-gentoo-limitschange.patch
# FC
Patch11: dvd+rw-tools-7.0.manpatch
Patch12: dvd+rw-tools-7.0-wexit.patch
Patch13: dvd+rw-tools-7.0-glibc2.6.90.patch
Patch14: dvd+rw-tools-7.0-reload.patch
Patch15: dvd+rw-tools-7.0-wctomb.patch
Patch16: dvd+rw-tools-7.0-dvddl.patch
Patch17: dvd+rw-tools-7.1-noevent.patch
Patch18: dvd+rw-tools-7.1-lastshort.patch
Patch19: dvd+rw-tools-7.1-format.patch
Patch20: dvd+rw-tools-7.1-bluray_srm+pow.patch
Patch21: dvd+rw-tools-7.1-bluray_pow_freespace.patch

Requires(pre): dvdrwtools-control >= 1.2-alt2
Requires: mkisofs >= 1.10

# Automatically added by buildreq on Sun May 18 2008
BuildRequires: gcc-c++
BuildRequires: rpm-build-licenses

%description
Collection of tools to master DVD+RW/+R/-R/-RW media.

%description -l ru_RU.UTF-8
Набор утилит для подготовки и записи на DVD+RW/+R/-R/-RW носители.


%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# fc
%patch11 -p1 -b .manpatch
%patch12 -p1 -b .wexit
%patch13 -p1 -b .glibc2.6.90
%patch14 -p1 -b .reload
%patch15 -p0 -b .wctomb
%patch16 -p0 -b .dvddl
%patch17 -p1 -b .noevent
%patch18 -p1 -b .lastshort
%patch19 -p1 -b .format
%patch20 -p1 -b .pow
%patch21 -p1 -b .freespace

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
install -d -m 0755 %buildroot{%_bindir,%_man1dir}
install -p -m700 %binaries %buildroot%_bindir/
install -p -m644 growisofs.1 %buildroot%_man1dir/

%pre
%pre_control %binaries

%post
%post_control %binaries

%files
%_bindir/*
%_man1dir/*
%doc index.html


%changelog
* Sun Feb 04 2018 Yuri N. Sedunov <aris@altlinux.org> 7.1-alt2
- synced fc patchset with 7.1-24

* Tue Apr 16 2013 Sergey V Turchin <zerg@altlinux.org> 7.1-alt1.qa1.1
- NMU: sync patches with FC (ALT#28851)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 7.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 16 2008 Led <led@altlinux.ru> 7.1-alt1
- cleaned up spec

* Sun May 18 2008 Led <led@altlinux.ru> 7.1-alt0.1
- 7.1
- cleaned up BuildRequires
- fixed License

* Tue Apr 08 2008 Michael Shigorin <mike@altlinux.org> 7.0-alt2
- NMU: fix build (apply a patch from Gentoo bug #195912)
- removed Requires(pre): modutils
- spec macro abuse cleanup

* Tue Oct 31 2006 L.A. Kostis <lakostis@altlinux.ru> 7.0-alt1
- NMU:
- updated to 7.0;
- remove legacy control (due missing 2.4 kernels).

* Wed Aug 16 2006 L.A. Kostis <lakostis@altlinux.ru> 6.1-alt2
- Add a trick for proper control set on 2.4 kernels.
- Fix requires for -control version.

* Fri Feb 24 2006 LAKostis <lakostis at altlinux.ru> 6.1-alt1
- NMU:
- updated to 6.1.

* Sat Jan 21 2006 LAKostis <lakostis at altlinux.ru> 6.0-alt1
- NMU:
- updated to 6.0.
- update unmount patch.
- s,kenel-headers,linux-libc-headers.

* Sat Apr 23 2005 Andrey Rahmatullin <wrar@altlinux.ru> 5.21.4.10.8-alt2
- NMU:
  + fix Group (#5246)
  + fix description charset (#5598)
  + package all binaries and manpage (#5829)
  + spec cleanup

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.21.4.10.8-alt1.1
- Rebuilt with libstdc++.so.6.

* Sat Oct 23 2004 Alexey Gladkov <legion@altlinux.ru> 5.21.4.10.8-alt1
- new version

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 5.17.4.8.6-alt5
- Fixed setmntent and supermount patches.
- Fixed umount(8) handling.
- Corrected build dependencies.
- Moved control files to separate package.
- Keep tools at mode "restricted" in the package, but default it
  to "public" in %%post when the package is first installed.
  This avoids a race and fail-open behaviour.

* Tue Aug 10 2004 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.17.4.8.6-alt4
- rebuild with patches - big thanks Sergey V Turchin

* Tue Aug 10 2004 Sergey V Turchin <zerg at altlinux dot org> 5.17.4.8.6-alt3.1
- add patch to read /etc/mtab instead /proc/mounts
- add patch to success umount when subfs or supermount
- remove requires to gcc-2.95
- cleanup spec

* Tue Jun 15 2004 Maxim Tyurin <mrkooll@altlinux.ru> 5.17.4.8.6-alt3
- rebuild with glibc 2.3.3

* Fri Jan 23 2004 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.17.4.8.6-alt2
- new program version
- Pioneer and LG devices fixes

* Fri Dec 19 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.14.4.7.4-alt2
- Spec fixing

* Mon Dec 08 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.14.4.7.4-alt1
- new program version

* Thu Oct 30 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.13.4.7.4-alt2
- add control support

* Thu Sep 25 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.13.4.7.4-alt1
- New programm version;
- Panasonic/MATSUSHITA DVD-RAM LF-D310 now supported;

* Tue Sep 02 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.12.4.7.4-alt3
- Spec editing

* Tue Sep 02 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.12.4.7.4-alt2
- New version

* Tue Aug 19 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.11.4.6.4-alt2
- Spec editing

* Mon Aug 18 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.11.4.6.4-alt1
- New version
- Spec editing
- Added original changelog in the %%doc folder

* Tue Jul 15 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.10.4.5.4-alt1
- New version

* Thu Jun 26 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 5.9.4.4.4-alt2.1
 - Updated %%BuildRequires, added %%Packager tag.

* Wed Jun 25 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.9.4.4.4-alt2
- spec editing

* Tue Jun 24 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.9.4.4.4-alt1
- New version

* Fri Jun 13 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 5.7.4.4.4-alt1
- New version

* Sat May 31 2003 Andy Polyakov <appro@fy.chalmers.se>
- Solaris support is merged;
* Mon May 26 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.6: unconditional exit in set-root-uid assistant, mostly
  for aesthetic reasons;
- support for DVD-RW DAO recordings (whenever Pioneer-ish Quick
  Format is not an option, DAO should fill in for it, as it's the
  only recording strategy applicable after *minimal* blanking
  procedure);
- support for SG_IO pass-through interface, or in other words
  support for Linux 2>=5;
- 'growisofs -M /dev/cdrom=/dev/zero', this is basically a counter-
  intuitive kludge assigned to fill up multi-session write-once
  media for better compatibility with DVD-ROM/-Video units, to keep
  it mountable [in the burner unit] volume descriptors from previous
  session are copied to the new session;
- disable -dvd-compat with -M option and DVD+R, advice to fill up
  the media as above instead;
- postpone Write Page setup all the way till after dry_run check;
- if recording to write-once media is terminated by external event,
  leave the session opened, so that the recording can be resumed
  (though no promises about final results are made, it's just that
  leaving it open makes more sense than to close the session);
- ask unit to perform OPC if READ DISC INFORMATION doesn't return
  any OPC descriptors;
- get rid of redundant Quick Grow in Restricted Overwrite;
- dvd+rw-formwat 4.4: support for -force=full in DVD-RW context;
- ask unit to perform OPC if READ DISC INFORMATION doesn't return
  any OPC descriptors;
- new dvd+rw-mediainfo utility for debugging purposes;
* Thu May 1 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.5: fix for ENOENT at unmount, I should have called myself
  with execlp, not execl;
- security: chdir to / in set-root-uid assistant;
- use /proc/mounts instead of MOUNTED (a.k.a. /etc/mtab) in Linux
  umount code;
- changed to 'all' target in Makefile to keep NetBSD people happy;
* Sun Apr 20 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.4: setup_fds is introduced to assist ports to another
  platforms;
- set-root-uid assistant code directly at entry point (see main());
- OpenBSD/NetBSD port added;
* Thu Mar 27 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.4: split first write to avoid "empty DMA table?" in
  kernel log;
- dvd+rw-format 4.3: natural command-line restrictions;
* Thu Mar 20 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.3: refuse to burn if session starts close to or beyond
  the 4GB limit (due to limitation of Linux isofs implementation).
- media reload is moved to growisofs from dvd+rw-format.
- dry_run check is postponed all the way till the first write.
* Sat Mar 15 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.3/dvd+rw-format 4.2: support for DVD-RW Quick Format,
  upon release tested with Pioneer DVR-x05.
- bug in DVD+RW overburn protection code fixed.
* Thu Feb 27 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.2: brown-bag bug in "LONG WRITE IN PROGRESS" handling
  code fixed.
* Sat Feb 1 2003 Andy Polyakov <appro@fy.chalmers.se>
- code to protect against overburns.
- progress indicator to display recording velocity.
- re-make it work under Linux 2.2 kernel.
* Tue Jan 14 2003 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.1: support for DVD-R[W] writing speed control.
- dvd+rw-booktype 4: see the source.
* Tue Nov 26 2002 Andy Polyakov <appro@fy.chalmers.se>
- growisofs 5.0: support for DVD-R[W].
- dvd+rw-format 4.0: support for DVD-RW.
- growisofs 4.2: workaround for broken DVD+R firmwares (didn't make
  public by itself).
* Mon Nov 4 2002 Andy Polyakov <appro@fy.chalmers.se>
- Minor growisofs update. Uninitialized errno at exit when
  -Z /dev/scd0=image.iso is used.
* Sun Nov 3 2002 Andy Polyakov <appro@fy.chalmers.se>
- Initial packaging. Package version is derived from growisofs,
  dvd+rw-format and dvd+rw-booktype version. 4.0.3.0.3 means
  growisofs 4.0, dvd+rw-format 3.0 dvd+rw-booktype 3.
