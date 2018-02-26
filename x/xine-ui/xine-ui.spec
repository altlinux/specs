%def_disable static
%def_enable shared

%def_enable shm
%def_enable shm_default
%def_enable mbs
%def_enable xft
%def_enable lirc
%def_enable vdr_keys

%def_with readline
%def_with ncurses
%def_with curl
%def_with aa
%def_with caca
%def_with fb
%def_with X11

%define lirclib shared
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_test_to() %{expand:%%{?_with_%{1}:--enable-%{2}test}} %{expand:%%{?_without_%{1}:--disable-%{2}test}}
%define subst_test() %{expand:%%{?_with_%{1}:--enable-%{1}test}} %{expand:%%{?_without_%{1}:--disable-%{1}test}}

%{?_disable_shm:%set_disable shm}
%{?_disable_X11:%set_disable xft}
%{?_disable_mbs:%set_disable xft}
%{?_enable_aa:%set_enable ncurses}
%{?_enable_caca:%set_enable ncurses}
%{?_enable_fb:%set_enable ncurses}
%if_without X11
%if_with caca
%define xinebin caca
%else
%if_with aa
%define xinebin aa
%else
%if_with fb
%define xinebin fb
%else
%set_with aa
%define xinebin aa
%endif
%endif
%endif
%endif

%define Name Xine
Name: xine-ui
Version: 0.99.6
Release: alt1
Summary: Video Player
License: %gpl2plus
Group: Video
URL: http://xine.sourceforge.net
Source0: http://xine.sourceforge.net/files/%name-%version.tar
Source1: %name.desktop
%{?_without_X11:Requires: xine-%xinebin = %version-%release}
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ pkg-config
BuildRequires: libxine-devel >= 1.1.7-alt3
BuildRequires: libpng-devel >= 1.2.8
BuildRequires: libXinerama-devel libXtst-devel libXv-devel
BuildRequires: libXxf86vm-devel xorg-sdk imake

%{?_with_aa:BuildRequires: aalib-devel >= 1.2.0}
%{?_with_caca:BuildRequires: libcaca-devel >= 0.99}
%{?_with_curl:BuildRequires: libcurl-devel >= 7.10.2}
%{?_with_ncurses:BuildRequires: libncurses-devel libgpm-devel libslang-devel}
%{?_with_readline:BuildRequires: libreadline-devel}
%{?_enable_xft:BuildRequires: libXft-devel}
%{?_with_X11:BuildRequires: libXext-devel libXt-devel xorg-cf-files xorg-inputproto-devel desktop-file-utils}
%if_enabled lirc
%if %lirclib == shared
BuildRequires: liblirc-devel
%else
BuildRequires: liblirc-devel-static
%endif
%endif

%description
%Name is a free gpl-licensed video player for unix-like systems. It
support mpeg-2 and mpeg-1 system (audio + video multiplexed + DVD)
streams, eventually mpeg-4 and other formats might be added.


%package -n xine-utils
Summary: Utils for xine Video Player
Group: Video

%description -n xine-utils
%Name is a free gpl-licensed video player for unix-like systems. It
support mpeg-2 and mpeg-1 system (audio + video multiplexed + DVD)
streams, eventually mpeg-4 and other formats might be added.
This package provide utils for xine video player.


%if_with aa
%package -n xine-ui-aa
Summary: Console version of a Video Player
Group: Video
Provides: aaxine = %version-%release
Provides: xine-aa = %version-%release
Requires: aalib >= 1.2.0

%description -n xine-ui-aa
%Name is a free gpl-licensed video player for unix-like systems. It
support mpeg-2 and mpeg-1 system (audio + video multiplexed + DVD)
streams, eventually mpeg-4 and other formats might be added.
This package provide text version of the video player.
%endif

%if_with caca
%package -n xine-ui-caca
Summary: Color console version of a Video Player
Group: Video
Provides: cacaxine = %version-%release
Provides: xine-caca = %version-%release

%description -n xine-ui-caca
%Name is a free gpl-licensed video player for unix-like systems. It
support mpeg-2 and mpeg-1 system (audio + video multiplexed + DVD)
streams, eventually mpeg-4 and other formats might be added.
This package provide color text version of the video player.
%endif

%if_with fb
%package -n xine-ui-fb
Summary: Framebuffer version of a Video Player
Group: Video
Provides: fbxine = %version-%release
Provides: xine-fb = %version-%release

%description -n xine-ui-fb
%Name is a free gpl-licensed video player for unix-like systems. It
support mpeg-2 and mpeg-1 system (audio + video multiplexed + DVD)
streams, eventually mpeg-4 and other formats might be added.
This package provide framebuffer version of the video player.
%endif

%prep
%setup
subst 's/cbreak/delch/g' configure.ac
subst 's|/usr/lib|%_libdir|' m4/_xine.m4
%if %lirclib == shared
subst 's/\(liblirc_client\.\)a/\1so/g' m4/_xine.m4
%endif


%build
%add_optflags "-DHAVE_ICONV"
./autogen.sh noconfig
%configure --with-pic \
    %{subst_enable static} \
    %{subst_enable shared} \
    %{subst_enable shm} \
    %{subst_enable_to shm_default shm-default} \
    %{subst_enable mbs} \
    %{subst_enable xft} \
    %{subst_enable lirc} \
    %{subst_enable_to vdr_keys vdr-keys} \
    %{subst_with readline} \
    %{subst_with ncurses} \
    %{subst_with curl} %{subst_test curl} \
    %{subst_with_to aa aalib} %{subst_test_to aa aalib} \
    %{subst_with_to caca libcaca} %{subst_test caca} \
    %{subst_with_to X11 x} \
    --enable-xinetest

%make_build


%install
make DESTDIR=%buildroot docsdir=%_docdir/%name-%version desktopdir=%_desktopdir install
install -m 0644 %SOURCE1 %buildroot%_desktopdir/xine.desktop
echo -n "MimeType=" >> %buildroot%_desktopdir/xine.desktop
cat %_libdir/xine/plugins/*/mime.types | sed 's/;.*//'|tr '\n' ';' >> %buildroot%_desktopdir/xine.desktop
echo >> %buildroot%_desktopdir/xine.desktop
mv %buildroot%_docdir/%name-%version/README %buildroot%_docdir/%name-%version/README.xitk
bzip2 --best --force --stdout ChangeLog > %buildroot%_docdir/%name-%version/ChangeLog.bz2
ln -sf xine-check %buildroot%_bindir/xine-bugreport
%{?_without_X11:ln -s %{xinebin}xine %buildroot%_bindir/xine}
%{?_without_X11:find %buildroot%_mandir -type f -name 'xine.1' -delete}
%{?_without_aa:find %buildroot%_mandir -type f -name 'aaxine.1' -delete}
%{?_without_caca:find %buildroot%_mandir -type f -name 'cacaxine.1' -delete}
%{?_without_aa:find %buildroot%_mandir -type f -name 'fbxine.1' -delete}
find %buildroot%_mandir -type f -name 'xine-bugreport.1' -print0 -exec ln -sf xine-check.1 \{} \;
%{?_without_X11:rm -rf %buildroot{%_desktopdir,%_pixmapsdir}}

%find_lang --with-man --output=xine.lang %name xine xitk
grep -v 'aaxine' xine.lang > %name.lang
for i in aa caca fb dfb; do
    %find_lang --with-man --output=xine-ui-$i.lang ${i}xine
done
%find_lang --with-man --output=xine-utils.lang xine-bugreport xine-check xine-remote


%files -f %name.lang
%_docdir/%name-%version
%_bindir/xine
%_datadir/xine/*
%if_with X11
%_desktopdir/*
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*
%endif


%files -n xine-utils -f xine-utils.lang
%_bindir/xine-*


%if_with aa
%files -n xine-ui-aa -f xine-ui-aa.lang
%_bindir/aaxine
%endif


%if_with caca
%files -n xine-ui-caca -f xine-ui-caca.lang
%_bindir/cacaxine
%endif


%if_with fb
%files -n xine-ui-fb -f xine-ui-fb.lang
%_bindir/fbxine
%endif


%changelog
* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.99.6-alt1
- 0.99.6
- build fixed

* Tue Aug 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.99.5-alt8
- build fixed

* Tue Dec 02 2008 Led <led@altlinux.ru> 0.99.5-alt7
- updated BuildRequires

* Thu Aug 07 2008 Led <led@altlinux.ru> 0.99.5-alt6
- fixed %name.desktop

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.99.5-alt5
- fixed License
- fixes desktop-mime-entry

* Wed Feb 20 2008 Led <led@altlinux.ru> 0.99.5-alt4
- rebuild to fix xine.desktop (#13346)

* Thu Sep 20 2007 Led <led@altlinux.ru> 0.99.5-alt3
- fixed xine.desktop

* Sun Aug 26 2007 Led <led@altlinux.ru> 0.99.5-alt2
- fixed #12621, thanks to Victor Belyaevski)

* Fri Jun 01 2007 Led <led@altlinux.ru> 0.99.5-alt1
- 0.99.5
- removed %name-0.99.4-caca-1.patch (fixed in upstream)
- removed %name-0.99.4-errors.patch (fixed in upstream)
- removed %name-0.99.4-mkdir.patch
- cleaned up spec
- added -DHAVE_ICONV to %%optflags

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.99.4-alt6.0
- Rebuilt due to libcurl.so.3 -> libcurl.so.4 soname change.

* Thu Feb 01 2007 Led <led@altlinux.ru> 0.99.4-alt6
- cleaned up Requires in %name-* packages

* Wed Jan 31 2007 Led <led@altlinux.ru> 0.99.4-alt5
- fixed Requires in %name-* packages

* Fri Jan 26 2007 Led <led@altlinux.ru> 0.99.4-alt4
- added %name-0.99.4-mkdir.patch

* Mon Jan 15 2007 Led <led@altlinux.ru> 0.99.4-alt3
- fixed "errors_create_window()" format string vulnerability (SA23709):
  %name-0.99.4-errors.patch
- added %name-0.99.4-caca-1.patch

* Tue Aug 15 2006 Led <led@altlinux.ru> 0.99.4-alt2.2
- fixed names of packages

* Sun Aug 13 2006 Led <led@altlinux.ru> 0.99.4-alt2.1
- remade spec
- removed ru.po sources (mainstream ones are newer)
- replaced xine-ui-0.9.18-alt-shared-lirc.patch with subst (optional)
- fixed ncurses detection
- added packages xine-caca, xine-fb, xine-utils
- fixed xine.desktop

* Fri Mar 24 2006 Anton Farygin <rider@altlinux.ru> 0.99.4-alt2
- fixed build

* Thu Jan 12 2006 LAKostis <lakostis at altlinux.ru> 0.99.4-alt1.1
- NMU;
- x86_64 fix.
- remove old desktop menu.
- remove unparseable macros.

* Fri Aug 12 2005 Anton Farygin <rider@altlinux.ru> 0.99.4-alt1
- new version

* Mon Jun 27 2005 Anton Farygin <rider@altlinux.ru> 0.99.3-alt2
- changed %%f to %%F into desktop file (#5288)

* Mon Dec 27 2004 Anton Farygin <rider@altlinux.ru> 0.99.3-alt1
- new version

* Thu Jul 22 2004 Anton Farygin <rider@altlinux.ru> 0.99.2-alt3
- fixed gui.tips_timeout (patch from xine-ui CVS, #4731)

* Tue Jul 20 2004 Anton Farygin <rider@altlinux.ru> 0.99.2-alt2
- icon fixed
- russian translation updated

* Mon Jul 05 2004 Anton Farygin <rider@altlinux.ru> 0.99.2-alt1
- new version
- russian translation added (#3605)

* Fri May 14 2004 Anton Farygin <rider@altlinux.ru> 0.99.1-alt2
- menu fixes
- added english description to xine-ui-aa package

* Mon Apr 19 2004 Anton Farygin <rider@altlinux.ru> 0.99.1-alt1
- 0.99.1

* Sun Jan 04 2004 Anton Farygin <rider@altlinux.ru> 0.9.23-alt1
- 0.9.23

* Thu Oct 30 2003 Rider <rider@altlinux.ru> 0.9.22-alt1.cvs20031030
- update from CVS
- disabled show setup window after first start

* Tue Oct 07 2003 Rider <rider@altlinux.ru> 0.9.22-alt1.cvs20031007
- update from CVS

* Tue Sep 30 2003 Rider <rider@altlinux.ru> 0.9.22-alt0.1.cvs20030930
- update from CVS

* Wed Sep 24 2003 Rider <rider@altlinux.ru> 0.9.22-alt0.1.cvs20030924
- update from CVS

* Thu Aug 14 2003 Rider <rider@altlinux.ru> 0.9.22-alt0.1.cvs20030814
- update from CVS

* Mon Jul 14 2003 Rider <rider@altlinux.ru> 0.9.21-alt0.1.cvs20030714
- update from CVS

* Tue Apr 29 2003 Rider <rider@altlinux.ru> 0.9.20-alt0.1.cvs20030429
- update from CVS
- build requires fix

* Wed Apr 09 2003 Rider <rider@altlinux.ru> 0.9.20-alt0.1.cvs20030409
- update from CVS

* Mon Mar 31 2003 Rider <rider@altlinux.ru> 0.9.20-alt0.1.cvs20030331
- update from CVS

* Mon Mar 24 2003 Rider <rider@altlinux.ru> 0.9.20-alt0.1.cvs20030324
- update from CVS

* Mon Mar 10 2003 Rider <rider@altlinux.ru> 0.9.19-alt0.1.cvs20030310
- 0.9.19

* Mon Mar 03 2003 Rider <rider@altlinux.ru> 0.9.18-alt0.1.cvs20030305
- update from CVS

* Tue Feb 25 2003 Rider <rider@altlinux.ru> 0.9.18-alt0.1.cvs20030225
- update from CVS

* Sun Feb 17 2003 Rider <rider@altlinux.ru> 0.9.18-alt0.1.cvs20030217
- update from CVS

* Fri Feb 14 2003 Rider <rider@altlinux.ru> 0.9.18-alt0.1.cvs20030214
- update from CVS
- build with shared lirc libraries

* Thu Jan 30 2003 Rider <rider@altlinux.ru> 0.9.18-alt0.1.cvs20030130
- build 0.9.18 from xine CVS

* Sun Jan 05 2003 Rider <rider@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 0.9.13-alt2
- rebuild (gcc 3.2)

* Mon Aug 05 2002 Rider <rider@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Wed Jul 31 2002 Rider <rider@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Mon Jun 03 2002 Rider <rider@altlinux.ru> 0.9.10-alt3
- sync with Yuri N. Sedunov specfile (%%find_lang)

* Mon Jun 03 2002 Rider <rider@altlinux.ru> 0.9.10-alt2
- xine-aa requires fix
- specfile cleanup


* Fri May 31 2002 Rider <rider@altlinux.ru> 0.9.10-alt1
- 0.9.10
- removed xine dfb output 
- skins: only xinetic, cloudy and lcd

* Tue Apr 30 2002 Rider <rider@altlinux.ru> 0.9.9-alt1
- 0.9.9
- build aalib & DirectFB interfaces

* Fri Jan 25 2002 Rider <rider@altlinux.ru> 0.9.8-alt2
- BuildReq fix

* Wed Jan 16 2002 Rider <rider@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Mon Dec 17 2001 Rider <rider@altlinux.ru> 0.9.7-alt2
- bug #0000231 fix

* Fri Dec 14 2001 Rider <rider@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Sun Dec 02 2001 Rider <rider@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Nov 08 2001 Rider <rider@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Tue Oct 23 2001 Rider <rider@altlinux.ru> 0.9.2-alt2
- new icons
- requires fix

* Tue Oct 16 2001 Rider <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 0.9.1-alt2
- snapshot from CVS

* Tue Sep 18 2001 Rider <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Sep 17 2001 Rider <rider@altlinux.ru> 0.9.0-alt2
- update from CVS

* Sat Sep 15 2001 Rider <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0 from CVS

* Wed Sep 12 2001 Rider <rider@altlinux.ru> 0.5.3-alt5
- rebuild version from CVS  with new libxine package

* Mon Sep 10 2001 Rider <rider@altlinux.ru> 0.5.3-alt4
- menu fix

* Mon Sep 10 2001 Rider <rider@altlinux.ru> 0.5.3-alt3
- menu & icons added
- fixed CFLAGS
- fullscreen patch added

* Mon Sep 10 2001 Rider <rider@altlinux.ru> 0.5.3-alt2
- requires fix
- build from CVS

* Sat Sep 08 2001 Rider <rider@altlinux.ru> 
- first build for ALT Linux

* Thu Jul 26 2001 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- Made AA as separate package.
* Thu Jul 26 2001 Matthias Dahl <matthew2k@web.de>
- updated filelist.
* Tue Jul 03 2001 Matthias Dahl <matthew2k@web.de>
- fixed the "no-skins-in-final-RPM-package" problem (nice explanation *grin*)
* Sun Jun 10 2001 Matthias Dahl <matthew2k@web.de>
- updated filelist and the requirements field
- removed /sbin/ldconfig as post install script
* Thu Mar 28 2001 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- add korean summary, patch from Louis JANG <louis@ns.mizi.com>
* Thu Jan 11 2001 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- patch from Sung-Hyun Nam <namsh@lgic.co.kr> applied.
* Fri Oct 17 2000 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- first spec file.
