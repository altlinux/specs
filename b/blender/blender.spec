Name: blender
Version: 2.62
Release: alt1

Summary: 3D modeling, animation, rendering and post-production
License: GPL
Group: Graphics
URL: http://www.blender.org/
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %name-%version.tar
Source1: %name-wrapper
Source2: %name.desktop
Source3: %name-win.desktop
Patch2: %name-2.47-alt-usertempdir.patch
Patch3: %name-2.49b-alt-ld.patch
Patch4: %name-2.49b-alt-qhull.patch
Patch5: %name-2.62-alt-libav.patch
Patch7: 0004-install_in_usr_lib.patch
Patch8: 0006-locales_directory_install.patch
Patch9: 0009-do_not_use_version_number_in_the_system_path.patch
Patch10: 0011-look_for_droid_ttf_with_fontconfig.patch

BuildRequires(pre): rpm-build-python3

%add_python3_path %_libexecdir/%name/scripts
%add_python3_req_skip _bpy
%add_python3_req_skip BPyWindow
%add_python3_req_skip mathutils
%add_python3_req_skip bge
%add_python3_req_skip bgl
%add_python3_req_skip blf

Provides: python%_python3_version(Blender)
Provides: python%_python3_version(bpy)
Provides: python%_python3_version(BPyMesh)

# Automatically added by buildreq on Fri Feb 17 2012
BuildRequires: cmake gcc-c++ libSDL-devel libXi-devel libavdevice-devel libavformat-devel libfftw3-devel libfreetype-devel libglew-devel libjpeg-devel libopenal-devel libpng-devel libswscale-devel libtiff-devel openexr-devel python3-dev boost-devel libjack-devel libsndfile-devel libopenjpeg-devel

%description
Fully integrated creation suite, offering a broad range of essential
tools for the creation of 3D content, including modeling, uv-mapping,
texturing, rigging, skinning, animation, particle and other simulation,
scripting, rendering, compositing, post-production and game creation

%description -l ru_RU.UTF-8
Полностью интегрированный пакет разработки, предлагающий широкий
выбор инструментов необходимых для создания 3D-графики. Включает
средства моделирования, анимации, рендеринга, постобработки видео,
а также создания интерактивных игр. Пакет имеет такие функции,
как динамика твердых тел, жидкостей и мягких тел, систему горячих
клавиш, большое количество легко доступных расширений, написанных
на языке Python.

%package i18n
Group: Graphics
Summary: Languages support for blender
Requires: %name = %version-%release
BuildArch: noarch

%description i18n
Languages support for blender

%prep
%setup -q -n %name-%version
#patch2 -p1
#patch3 -p2
#patch4 -p2
%patch5 -p2
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1


#sed -i 's|\(CFLAGS\=\"\)|\1 -g |' release/plugins/bmake
#sed -i '36a\#include <GL/gl.h>' \
#	source/blender/ftfont/intern/FTF_TTFont.h
#rm -fR extern/fftw extern/qhull

%build
mkdir cmake-make
cd cmake-make
export CFLAGS="$RPM_OPT_FLAGS -fPIC -funsigned-char -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%ifnarch %{ix86} x86_64
  -DWITH_RAYOPTIMIZATION=OFF \
%endif
 -DCMAKE_SKIP_RPATH=ON \
 -DBUILD_SHARED_LIBS=OFF \
 -DWITH_FFTW3=ON \
 -DWITH_JACK=ON \
 -DWITH_CODEC_SNDFILE=ON \
 -DWITH_IMAGE_OPENJPEG=ON \
 -DWITH_PYTHON=ON \
 -DWITH_PYTHON_INSTALL=OFF \
 -DWITH_CODEC_FFMPEG=ON \
 -DWITH_GAMEENGINE=ON \
 -DWITH_CXX_GUARDEDALLOC=OFF \
 -DWITH_BUILTIN_GLEW=OFF \
 -DWITH_INSTALL_PORTABLE=OFF \
 -DWITH_PYTHON_SAFETY=ON \
 -DWITH_PLAYER=ON \
 -DWITH_OPENMP=OFF \
#

%make
cd ..

install -d release/plugins/include
install -m 644 source/blender/blenpluginapi/*.h release/plugins/include

#chmod +x release/plugins/bmake
#make -C release/plugins/

%install
install -pD -m755 cmake-make/bin/%name %buildroot%_bindir/%name
install -pD -m755 cmake-make/bin/%{name}player %buildroot%_bindir/%{name}player

# icons and .desktop files
/bin/install -pD -m644 release/freedesktop/icons/16x16/apps/%name.png %buildroot%_miconsdir/%name.png
/bin/install -pD -m644 release/freedesktop/icons/32x32/apps/%name.png %buildroot%_niconsdir/%name.png
/bin/install -pD -m644 release/freedesktop/icons/scalable/apps/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
/bin/install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
/bin/install -pD -m644 %SOURCE3 %buildroot%_desktopdir/%name-win.desktop

#/bin/install -d %%buildroot%%_libdir/%%name/plugins/sequence
#/bin/install -d %%buildroot%%_libdir/%%name/plugins/texture
#/bin/install -pD -m644 release/plugins/sequence/*.so %%buildroot%%_libdir/%%name/plugins/sequence
#/bin/install -pD -m644 release/plugins/texture/*.so %%buildroot%%_libdir/%%name/plugins/texture

install -d %buildroot%_libexecdir/%name
cp -a release/scripts %buildroot%_libexecdir/%name
cp -a release/datafiles/locale %buildroot%_datadir

#/bin/install -m644 release/VERSION %%buildroot%%_datadir/%%name
#/bin/install -m644 bin/.blender/.Blanguages %%buildroot%%_datadir/%%name

%find_lang %name

%files
#doc README release/linux/*.pdf release/linux/release_*.txt release/linux/blender.html
%_bindir/*
%_desktopdir/*
#_libdir/%%name/

%_niconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%_libexecdir/%name/
#exclude %%_datadir/%%name/.Blanguages

%files i18n -f %name.lang
#_datadir/%%name/.Blanguages


%changelog
* Sat Mar 31 2012 Sergei Epiphanov <serpiph@altlinux.ru> 2.62-alt1
- Build with new rpm-build-python3
- Fix libav patch

* Sat Mar  3 2012 Sergey Kurakin <kurakin@altlinux.org> 2.62-alt0.2
- jack support
- sndfile codec support
- openjpeg support

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt9.3
- Rebuilt with qhull 2012.1

* Sat Feb 18 2012 Sergey Kurakin <kurakin@altlinux.org> 2.62-alt0.1
- 2.62 test build

* Fri Feb 17 2012 Sergey Kurakin <kurakin@altlinux.org> 2.61-alt0.2
- patches from Debian:
  + scripts in libexecdir
  + non-versioned scripts directory
  + use fontconfig to get interface font

* Tue Feb 14 2012 Sergey Kurakin <kurakin@altlinux.org> 2.61-alt0.1
- 2.61 test build

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt9.2
- Rebuilt with qhull 2011.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.49b-alt9.1
- Rebuild with Python-2.7

* Thu Aug 04 2011 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt9
- Build with libav fixed once again

* Wed Aug 03 2011 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt8
- Fixed build with libav

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt7
- Rebuilt with qhull 2011.1

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt6
- Rebuilt for debuginfo

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt5
- Added libalut-devel into BuildPreReq
- Built with system qhull instead of build-in

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt4
- Fixed build

* Sun Dec 19 2010 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt3
- added Provides: python(BPyMesh) (closes: #24769)
- removed useless python pseudo-modules, containing sources
  of the python API reference
- really linked with system libFTGL instead of bundled one
- built with system libGLEW instead of bundled one

* Tue Sep 28 2010 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt2
- added Provides: python(bpy) (closes: #24147)
- languages support moved to -i18n subpackage
- blender-wrapper refactoring
- spare font removed from package

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 2.49b-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt1
- 2.49b: bugfix release

* Thu Jul 23 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49a-alt2
- removed deprecated Requires: python = pyton_version
  (repocop warning)

* Fri Jun 26 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49a-alt1
- 2.49a
- warning: yafray support is completely removed in 2.49
- dropped openal_source patch (fixed in upstream)
- dropped alt-gimp patch (fixed in upstream)
- dropped alt-ffmpeg52 patch (fixed in upstream)
- removed spare BuildRequires

* Tue May  5 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt5
- blender-wrapper fixed on x86_64
- blender-wrapper improved to take care with blender scripts
  from other packages
- Provides: python(Blender) for other packages with blender scripts
- Requires: symlinks (needed for blender-wrapper)
- minor spec cleanup

* Mon Mar 16 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt4
- build fixed (BuldRequires)
- description corrected (russian)

* Thu Feb 12 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt3
- fixed build with libavcodec52

* Tue Dec  9 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt2
- libopenal support enabled again
  (see 2.48a-alt0.1 chengelog entry)

* Fri Nov 28 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt1
- post-scripts removed (update_menus & update_desktopdb)
- additional code in wrapper: move ~/.blender/.B.blend to ~/.B.blend
  (see .B.blend issue in 2.46-alt1 changelog)

* Tue Oct 28 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt0.1
- 2.48a (bugfix release)
- libopenal support temporary removed
  in order to build with gcc4.3

* Thu Oct 16 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48-alt0.1
- 2.48
- gimp used as external image editor

* Wed Oct 10 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.47-alt2
- summary and description updated
- libtiff4 patch restored and updated,
  fixing libtiff.so.4 loading on x86_64
- new usertempdir patch fixes tmp directory issues
- removed .menu files
- updated .desktop files:
  + fixed repocop warnings
  + #16829
  + run in terminal (for window mode only)
- unnecessary icons removed from sources (included in tarball)
- more spec cleanup

* Mon Aug 25 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.47-alt1
- 2.47

* Mon Jul 14 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.46-alt1
- 2.46
- removed verify_elf_skiplist, useless for now
- removed long list of add_python_req_skip, useless for now
- removed tiff4 patch
- removed fix-temp patch
- user configuration file .B.blend moved back to original
  location $HOME/.B.blend (see 2.45-alt1 changelog entry)
- spec cleanup

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.45-alt2.2.1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for blender

* Fri Feb 29 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.45-alt2.2.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Sun Feb 17 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt2.2
- Rebuild with libavformat.52

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.45-alt2.1
- Rebuilt with python-2.5.

* Mon Oct 22 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt2
- Fix owner/group of plugins

* Sat Oct 13 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt1
- New version
- Fix temp dir
- Move user defaults file from ~ to ~/.blender
- Fix plugin rights
- Fix execution script
- Fix verify_elf
- Set hard depend to python2.4

* Tue Sep 11 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt4
- Fix python dependencies

* Fri Jun 29 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt3
- Swap windowed and fullscreen mode

* Sat May 26 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt2
- Cleaning .spec
- Add russian description
- Fix build process

* Mon May 14 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt1
- New version
- Replace illegal Requires with right stuff
- Fix 'blender' script for x86_64

* Mon Mar 12 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.43-alt2
- Fix Provides/Requires section

* Sat Feb 24 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.43-alt1
- New version

* Thu Feb 15 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt4
- Add selection between desktop and menu files
- Add blender startup in window mode

* Thu Dec 14 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt3
- rebuild

* Wed Sep 20 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt2
- fixing error in build

* Sun Sep 10 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt1
- New version

* Fri Sep 08 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.41-alt2
- Fixing load of libtiff4.

* Sat Mar 04 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.41-alt1
- New version
- Cleanup spec for X.Org 7.0

* Fri Mar 03 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt3
- Correcting spec (correcting icons dir).

* Wed Dec 28 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt2
- Correction of blender.menu file

* Mon Dec 26 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt1
- New version

* Wed Mar 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.36-alt1.1
- Rebuilt with python-2.4.

* Sun Jan 30 2005 Andrey Astafiev <andrei@altlinux.ru> 2.36-alt1
- 2.36
- Some features incorporated from Debian package.

* Mon Mar 01 2004 Kachalov Anton <mouse@altlinux.ru> 2.32-alt1
- new version 2.32

* Sun Dec 28 2003 Kachalov Anton <mouse@altlinux.ru> 2.30-alt1
- new version 2.30

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 2.28a-alt1
- new version 2.28a

* Tue Jun 24 2003 Kachalov Anton <mouse@altlinux.ru> 2.27-alt1
- new version 2.27

* Mon Jan 20 2003 Kachalov Anton <mouse@altlinux.ru> 2.25b-alt2
- fixed buildrequires

* Tue Nov 12 2002 Kachalov Anton <mouse@altlinux.ru> 2.25b-alt1
- build for Sisyphus
