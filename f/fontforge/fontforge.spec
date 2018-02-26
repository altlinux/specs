# Patent related warning:
# it is possible to build with --with-freetype-bytecode
# but it is FORBIDDEN in some countries. See documentation
%def_with bytecode

Name: fontforge
Version: 20110222
Release: alt3
Summary: FontForge -- font editor
Summary(ru_RU.KOI8-R): Редактор шрифтов FontForge

License: BSD
Group: Publishing
Url: http://fontforge.sourceforge.net/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %{name}_full-%version.tar.bz2
Source2: %name.png
Patch0: %name-%version.patch

# manually removed: glibc-devel-static packages-info-i18n-common
# Automatically added by buildreq on Mon Oct 29 2007
BuildRequires: gcc-c++ imake libfreetype-devel libjpeg-devel
BuildRequires: libpng-devel libtiff-devel libungif-devel libXi-devel
BuildRequires: libxml2-devel  python-devel xorg-cf-files libX11-devel
BuildPreReq: libfreetype-devel

Obsoletes: pfaedit
Provides: pfaedit

%description
FontForge allows the user to create and modify 
Type 1 (postscript) and true type fonts.
User can save fonts in different postscript 
formats and generate bitmaps.

%description -l ru_RU.KOI8-R
FontForge позволяет пользователям создавать и изменять 
шрифты форматов Type1 (postscipt) и True Type. 
Возможно сохранять шрифты в различных
форматах postscript и генерировать 
растровые изображения шрифтов.

%package -n lib%name
Summary: FontForge shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: FontForge development files
Group: Development/C
Requires: lib%name = %version-%release

%package -n python-module-%name
Summary: FontForge python module
Group: Development/Python
Requires: python

%description -n lib%name
FontForge shared library

%description -n lib%name-devel
FontForge development files

%description -n python-module-%name
FontForge python module

%prep
%setup -q
%patch -p0

%build
%add_optflags -fno-strict-aliasing
%configure 	--disable-static \
			--with-freetype-src=%_includedir/freetype2/freetype/internal \
			--with-gdraw \
			--enable-pyextension \
%if_with bytecode
			--with-freetype-bytecode
%else

%endif

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make_build
pushd pyhook
%python_build
popd

%install
install -D -m644 %SOURCE2 %buildroot%_niconsdir/%name.png

%makeinstall_std

mkdir -p %buildroot%_desktopdir
cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=FontForge Font Editor
Comment=Edit and convert fonts
Exec=fontforge %U
Icon=icon-accessories
Terminal=false
Type=Application
Categories=Graphics;Publishing;
MimeType=application/x-font;application/x-font-bdf;application/x-font-ttf;application/x-font-truetype;application/x-truetype-font;application/font-tdpfr;application/x-font-afm;application/x-font-type1;
EOF

pushd pyhook
python setup.py install --root=%buildroot \
                          --optimize=2 \
                          --record=../python-module-%name
popd

%find_lang FontForge

%files -f FontForge.lang
%doc LICENSE
%_bindir/*
%_datadir/%name/
%_man1dir/*
%_desktopdir/%name.desktop
%_niconsdir/*

%files -n lib%name
%_libdir/libgunicode.so.*
%_libdir/libgdraw.so.*
%_libdir/libfontforge.so.*
%_libdir/libgutils.so.*
%_libdir/libgioftp.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name/
%_pkgconfigdir/*.pc

%files -n python-module-%name -f python-module-%name

%changelog
* Sat Dec 24 2011 Pavel Vainerman <pv@altlinux.ru> 20110222-alt3
- applied patch from fedora (fontforge-20100501-select-points-crash.patch)
  altbug #25979
- add require 'python' for python-module-fontforge

* Thu Dec 15 2011 Pavel Vainerman <pv@altlinux.ru> 20110222-alt2
- remove -rpath (new ALT Linux policy)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20110222-alt1.1
- Rebuild with Python-2.7

* Tue Feb 22 2011 Pavel Vainerman <pv@altlinux.ru> 20110222-alt1
- new version

* Tue Feb 22 2011 Pavel Vainerman <pv@altlinux.ru> 20100501-alt4
- remove 'application/x-font-bdf' double in desktop-file

* Mon Feb 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100501-alt3
- Fixed build

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100501-alt2
- Fixed desktop file

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100501-alt1
- Version 20100501

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090923-alt2
- Rebuilt with python 2.6

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090923-alt1
- Version 20090923

* Thu Sep 25 2008 Pavel Vainerman <pv@altlinux.ru> 20080828-alt1
- new version
- update patch
- and many thanks Boris Savelev <boris@altlinux.org> for
	- split into 4 package: lib, lib-devel, python-module, and binaries
	- add python-module
	- add devel

* Tue Aug 19 2008 Pavel Vainerman <pv@altlinux.ru> 20080720-alt1
- new version

* Fri May 30 2008 Pavel Vainerman <pv@altlinux.ru> 20080429-alt1
- new version

* Tue Mar 25 2008 Pavel Vainerman <pv@altlinux.ru> 20080309-alt1
- new version

* Fri Feb 29 2008 Pavel Vainerman <pv@altlinux.ru> 20080203-alt1
- new version

* Wed Dec 12 2007 Vitaly Lipatov <pv@altlinux.ru> 20071210-alt1
- new version

* Thu Nov 01 2007 Pavel Vainerman <pv@altlinux.ru> 20071002-alt2
(thank`s to Vitaly Lipatov)
- fix build requires
- add missed libfontforge dir
- no pack .so files
- replace menu with desktop file
- remove unresolved=relaxed
- enable SMP build

* Mon Oct 29 2007 Pavel Vainerman <pv@altlinux.ru> 20071002-alt1
- new version
- update patch
- update build requires

* Sat Sep 01 2007 Pavel Vainerman <pv@altlinux.ru> 20070831-alt1
- new version

* Sat Mar 17 2007 Pavel Vainerman <pv@altlinux.ru> 20070312-alt1
- new version

* Sat Nov 11 2006 Pavel Vainerman <pv@altlinux.ru> 20061025-alt1
- new version
- addpatch for --as-needed

* Sun Mar 05 2006 Pavel Vainerman <pv@altlinux.ru> 20060209-alt2
- spec cleanup (ttfmode removed)
- split doc to stand-alone package
- enable --with-freetype-bytecode
- add po files

* Wed Feb 22 2006 Pavel Vainerman <pv@altlinux.ru> 20060209-alt1
- new version

* Tue Oct 11 2005 Pavel Vainerman <pv@altlinux.ru> 20050912-alt2
- fix bug in previous build
- update BuildRequires in spec-file
- add '--with-gdraw' for build section (see configure --help)

* Mon Sep 12 2005 Pavel Vainerman <pv@altlinux.ru> 20050912-alt1
- build new version
- update BuildRequires in spec-file

* Mon Mar 14 2005 Pavel Vainerman <pv@altlinux.ru> 20050209-alt1
- build new version

* Wed Oct 27 2004 Pavel Vainerman <pv@altlinux.ru> 20040930-alt1
- build new version

* Mon Sep 06 2004 Pavel Vainerman <pv@altlinux.ru> 20040824-alt1
- build new version

* Wed Jun 23 2004 Pavel Vainerman <pv@altlinux.ru> 0.20040618-alt2
- fix ld_config
- remove cidmaps.tgz from doc

* Sun Jun 20 2004 Pavel Vainerman <pv@altlinux.ru> 0.20040618-alt1
- build new version with new name - fontforge
- add doc package
- spec cleanup
- fix menu
- add dummy icon for menu

* Tue Jun 03 2003 AEN <aen@altlinux.ru> 0.030518-alt1
- new snapshot
- cidmaps added

* Mon Feb 03 2003 AEN <aen@altlinux.ru> 0.030201-alt1
- new snapshot

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 0.021119-alt1
- new snapshot

* Wed Jun 26 2002 AEN <aen@logic.ru> 0.029623-alt3
- 2 packages, pfaedit docs in main package
- ttfmod docs added
- urlview required for ttfmod

* Wed Jun 26 2002 AEN <aen@logic.ru> 0.029623-alt2
- split to 3 packages
- license changed to BSD

* Wed Jun 26 2002 AEN <aen@logic.ru> 0.029623-alt1
- new snapshot
- new docs
- ttfmod added

* Tue Jun 17 2002 AEN <aen@logic.ru> 0.020611-alt1
- new snapshot

* Mon May 20 2002 AEN <aen@logic.ru> 0.020518-alt1
- new snapshot

* Thu Mar 28 2002 AEN <aen@logic.ru> 0.020312-alt1
- new snapshot

* Mon Mar 06 2002 AEN <aen@logic.ru> 0.020310-alt1
- new snapshot

* Wed Feb 06 2002 AEN <aen@logic.ru> 0.020205-alt1
- new snapshot

* Fri Jan 18 2002 AEN <aen@logic.ru> 0.020117-alt1
- new snapshot

* Thu Jan 10 2002 AEN <aen@logic.ru> 0.020109-alt1
- new snapshot

* Wed Jan 09 2002 AEN <aen@logic.ru> 0.020108-alt1
- new snapshot

* Thu Dec 20 2001 AEN <aen@logic.ru> 0.011219-alt1
- new snapshot

* Thu Dec 13 2001 AEN <aen@logic.ru> 0.011212-alt1
- new snapshot

* Tue Nov 20 2001 AEN <aen@logic.ru> 0.011115-alt1
- new snapshot

* Tue Nov 06 2001 AEN <aen@logic.ru> 0.011102-at1
- new snapshot

* Thu Oct 31 2001 AEN <aen@logic.ru> 0.011031-alt1
- new snapshot

* Tue Oct 1 2001 AEN <aen@logic.ru> 0.011001-alt1
- new snapshot

* Wed Sep 26 2001 AEN <aen@logic.ru> 0.010924-alt1
- new snapshot
* Tue Sep 18 2001 AEN <aen@logic.ru> 0.010915-alt1
- new snapshot
* Thu Sep 6 2001 AEN <aen@logic.ru> 0.010905-alt1
- new snapshot
* Mon Sep 1 2001 AEN <aen@logic.ru> 0.010901-alt1
- new snapshot
* Fri Aug 31 2001 AEN <aen@logic.ru> 0.010830-alt1
- new snapshot
* Wed Jul 25 2001 AEN <aen@logic.ru> 0.010724-alt1
- new snapshot
* Wed Jul 24 2001 AEN <aen@logic.ru> 0.010722-alt1
- new snapshot
* Mon Jul 22 2001 AEN <aen@logic.ru> 0.010715-alt1
- new snapshot
* Mon Jul 15 2001 AEN <aen@logic.ru> 0.010715-alt1
- new snapshot
* Thu Jul 12 2001 AEN <aen@logic.ru> 0.010711-alt1
- new snapshot
* Wed Jul 11 2001 AEN <aen@logic.ru> 0.010710-alt1
- new snapshot
* Mon Jul 9 2001 AEN <aen@logic.ru> 0.010707-alt1
- new snapshot
* Fri Jun 29 2001 AEN <aen@logic.ru> 0.010628-alt1
- new snapshot with Val patch
* Tue Jun 26 2001 AEN <aen@logic.ru> 0.010624-alt1
- new snapshot with patch from Val
* Thu Jun 21 2001 AEN <aen@logic.ru> 0.010619-alt1
- new snapshot
* Fri Jun 13 2001 AEN <aen@logic.ru> 0.010611-alt1
- new snapshot
* Mon Jun 6 2001 AEN <aen@logic.ru> 0.010607-alt1
- new snapshot again
* Mon May 14 2001 AEN <aen@logic.ru> 0.010511-alt1
- new snapshot
* Wed May 9 2001 AEN <aen@logic.ru> 0.010507-alt1
- new snapshot
* Fri Apr 6 2001 AEN <aen@logic.ru> 0.010402-alt1
- new snapshot
* Mon Apr 2 2001 AEN <aen@logic.ru>	0.010329-alt1
- first build for Sisyphus
