%define origname openmotif

Name: libopenmotif3
Version: 2.2.4
Release: alt3

Summary: The Open Motif
License: Open Group Public License
Group: System/Libraries

Url: http://www.motifzone.org
Source: %origname-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

# RH
Patch1: openMotif-2.2.3-rh-acinclude.patch
Patch2: openMotif-2.2.3-rh-char_not_supported.patch
Patch3: openMotif-2.2.3-rh-libdir.patch
Patch4: openMotif-2.2.3-rh-long64.patch
Patch5: openMotif-2.2.3-rh-multiscreen.patch
Patch6: openMotif-2.2.3-rh-pixel_length.patch
Patch7: openMotif-2.2.3-rh-popup_timeout.patch
Patch8: openMotif-2.2.3-rh-uil_lib.patch
Patch9: openmotif-2.2.3-rh-utf8.patch
Patch10: openMotif-2.2.3-rh-vizcount.patch
# CAN, CVE
Patch21: openMotif-2.2.3-CAN-2004-0687-0688.patch
Patch22: openMotif-2.2.3-CAN-2004-0914.patch
Patch23: openmotif-2.2.3-CAN-2004-0914_sec8.patch
Patch24: openmotif-CVE-2005-3964.patch
#
Patch31: openMotif-2.2.3-motifzone_1193.patch
Patch32: openMotif-2.2.3-motifzone_1202.patch
Patch33: openMotif-2.2.3-rgbtxt.patch
Patch34: openmotif-2.2.3-gentoo-buffer.patch
# ALT
Patch41: openmotif-2.2.2-alt-DefaultUserPath.patch
Patch42: openmotif-2.2.2-alt-VARDIR.patch
Patch43: openmotif-2.2.2-alt-bison.patch
Patch44: openmotif-2.2.3-alt-VERSION.patch
Patch45: openMotif-2.2.4-alt-compatonly.patch
Patch46: openmotif-2.2.x-alt-types.patch

Provides: motif = %version-%release
Provides: openmotif = %version-%release

# Automatically added by buildreq on Sat Mar 24 2012
# optimized out: libICE-devel libSM-devel libX11-devel libXau-devel libXmu-devel libXt-devel libstdc++-devel xorg-printproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: chrpath flex gcc-c++ imake libXaw-devel libXext-devel libXp-devel xorg-bitmaps xorg-cf-files
BuildRequires: libjpeg-devel libpng-devel

%description
This package contains shared Open Motif 2.2 libraries
required to run legacy Motif 2.2 applications.

%prep
%setup -n %origname-%version
# RH
#patch1 -p1
#patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#patch9 -p1
%patch10 -p1
# CAN
#patch21 -p1
#patch22 -p1
#patch23 -p1
%patch24 -p1
#
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
# ALT
%patch41 -p1
%patch42 -p1
#patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1

#patch4 -p1

find -type f -name \*.orig -print -delete

%build
%set_autoconf_version 2.5
%set_automake_version 1.7
%set_libtool_version 1.5

for i in config.guess config.sub; do ln -sf %_datadir/libtool/config/$i; done
for i in depcomp install-sh missing; do ln -sf %_datadir/automake/$i; done

%add_optflags -D_FILE_OFFSET_BITS=64
export lt_cv_prog_cc_static_works=no
libtoolize --copy --force

CFLAGS="%optflags" \
%configure --enable-shared --disable-static

make clean
%make_build

%install
%makeinstall_std
chrpath -d %buildroot%_libdir/*.so.*

%files
%_libdir/*.so.*
%doc COPYRIGHT.MOTIF RELNOTES

%changelog
* Mon Mar 26 2012 Michael Shigorin <mike@altlinux.org> 2.2.4-alt3
- added patch by vx8400@ (see #27115)
- enabled JPEG and PNG support (thx at@, see 2.3.3-alt2)

* Sat Mar 24 2012 Michael Shigorin <mike@altlinux.org> 2.2.4-alt2
- fixed build in recent environments with gentoo patch (closes: #27115)

* Tue Jan 25 2011 Michael Shigorin <mike@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu May 21 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt4
- renamed to libopenmotif3 due to SharedLibsPolicy and #20114
- removed all extra subpackages leaving just the library
- buildreq

* Tue Mar 31 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt3.3
- added libXt-devel, libXext-devel deps to devel subpackage (#17155)

* Mon Mar 23 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt3.2
- added xorg-printproto-devel dependency to devel subpackage (#19285)
- removed obsolete macros

* Wed Jun 21 2006 Anton Farygin <rider@altlinux.ru> 2.2.3-alt3.1
- fixed build for x86_64

* Tue Feb 07 2006 Victor Forsyuk <force@altlinux.ru> 2.2.3-alt3
- Migration from /usr/X11R6 to /usr.
- Security fix for CVE-2005-3964 (buffer overflows in libUil).
- Patch for new rgb.txt location.
- Add buildreq'ed deps.

* Sat Mar 26 2005 Anton D. Kachalov <mouse@altlinux.org> 2.2.3-alt2
- Syncing with RH patches
- x86_64 support

* Wed May 05 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3.
- Reviewed patches.

* Sun Nov 30 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt4
- Do not package .la files.
- Do not build static libraries by default.

* Wed Oct 01 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt3
- Merged RH patches:
  libdir, utf8 (rh #80271), Xmu (rh #80777).
- Fixed multiply build problems.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt2
- Merged two RH patches: rh-config, rh-maxlinelen.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.2-alt1
- 2.2.2

* Sun Mar 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.30-ipl7mdk
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.30-ipl6mdk
- Added bunch of provides.

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.30-ipl5mdk
- Relocated config files according to FHS.
- Use new group: Graphical desktop/Motif.

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.30-ipl4mdk
- Updated groups, summaries and descriptions.
- More compatibility with lesstif.

* Tue Jun 20 2000 Dmitry V. Levin <ldv@fandra.org>
- More RE adaptions.

* Wed May 17 2000 AEN <aen@logic.ru>
- build with -O2

* Wed May 17 2000 AEN <aen@logic.ru>
- first build for RE
