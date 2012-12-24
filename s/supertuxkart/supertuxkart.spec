%define status rc2

Name: supertuxkart
Version: 0.8
Release: alt1

License: GPL
Url: http://supertuxkart.sourceforge.net
Summary: SuperTuxKart is a kart racing game
Group: Games/Arcade
Packager: Alex Karpov <karpov@altlinux.ru>

Source: %name-%version-src.tar


## Automatically added by buildreq on Wed Jul 01 2009
#BuildRequires: gcc-c++ libGL-devel libSDL-devel libfreeglut-devel libopenal-devel libvorbis-devel plib-devel subversion

# Automatically added by buildreq on Tue Dec 25 2012
# optimized out: cmake cmake-modules libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libogg-devel libstdc++-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: cmake cmake-modules libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libogg-devel libstdc++-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel ctest gcc-c++ libXxf86misc-devel libXxf86vm-devel libcurl-devel libfribidi-devel libopenal-devel libvorbis-devel libxkbfile-devel ruby ruby-stdlibs
#ccmake ctest gcc-c++ glibc-devel-static libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcurl-devel libfribidi-devel libopenal-devel libvorbis-devel libxkbfile-devel ruby ruby-stdlibs

%description
SuperTuxCart is a kart racing game

%prep
%setup -qn %name-%version

%build
cd lib/irrlicht/source/Irrlicht
NDEBUG=1 make
cd ../../../../
mkdir cmake_build
cd cmake_build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd cmake_build
%makeinstall DESTDIR=%buildroot

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
#doc README TODO ChangeLog
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/*

%changelog
* Mon Dec 24 2012 Alex Karpov <karpov@altlinux.ru> 0.8-alt1
- at last - new version
    + libirrlicht dependency removed (there's included one)
    + build requirements revisited

* Thu Apr 05 2012 Alex Karpov <karpov@altlinux.ru> 0.7-alt2.2
- rebuild with new blender

* Sun Dec 26 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt2
- new release

* Mon Dec 20 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt1.rc2
- new release candidate

* Fri Dec 03 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt1.rc1
- mostly playable release candidate
    + updated build requirements

* Thu May 20 2010 Alex Karpov <karpov@altlinux.ru> 0.6.2-alt2
- fixed path for main executable in desktop-file (#23511)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for supertuxkart
  * postclean-05-filetriggers for spec file

* Thu Aug 20 2009 Alex Karpov <karpov@altlinux.ru> 0.6.2-alt1
- new version

* Fri Aug 07 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1.2
- fixed buffer overflow error

* Wed Jul 01 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1.1
- fixed libs

* Fri May 08 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1
- 0.6.1 bugfix release

* Sun Jan 25 2009 Alex Karpov <karpov@altlinux.ru> 0.6-alt1
- 0.6 release

* Sun Jan 18 2009 Alex Karpov <karpov@altlinux.ru> 0.6-alt0.rc1
- new version
    + minor spec cleanup

* Tue Jun 10 2008 Alex Karpov <karpov@altlinux.ru> 0.5-alt0.1
- new version

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 0.4-alt0.1
- new version
    + updated build requirements
    + added menu macros

* Thu Nov 08 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt1
- rebuild for keyboard problem fix

* Mon Jul 30 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt0.5
- buildreq update

* Wed Jul 25 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt0.1
- initial build for Sisyphus

* Wed Jul 25 2007 Alexey Novikov <shader@yandex.ru> 0.3-alt0.M40.1
- first build

