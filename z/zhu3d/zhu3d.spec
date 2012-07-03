Name: zhu3d
Version: 4.2.2
Release: alt1.1

Summary: OpenGL-based equation viewer and solver

License: GPLv2+
Group: Sciences/Mathematics
Url: http://kde-apps.org/content/show.php?content=43071

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/sourceforge/zhu3d/%name-%version.tar.bz2
Source1: %name.desktop
Patch0: %name-3.3.0-path.patch
Patch1: %name-debug-and-link.patch

%define zdir %buildroot%_datadir/%name/

# Automatically added by buildreq on Mon Jun 23 2008
BuildRequires: gcc-c++ libqt4-devel

Requires: desktop-file-utils
BuildPreReq: desktop-file-utils

%description
With Zhu3D you interactively can view and animate functions,
isosurfaces and a further independent parametric system.
Numerical solutions of equation systems can be found with
a precise and reliable adaptive random search. The
OpenGL-viewer supports zooming, scaling, rotating and
translating as well as filed lightning or surface properties.
Special effects are transparency, textures, fog and motion blur.

%prep
%setup -q
#%patch0 -p1
%patch1 -p2

%build
export PATH=%_qt4dir/bin:$PATH
export QTDIR=%_qt4dir/
qmake
%make_build

%install
mkdir -p %zdir/{work/textures,system/languages}
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps

install -D %name %buildroot%_bindir/%name
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install work/*.zhu %zdir/work
install work/textures/* %zdir/work/textures
install system/*.zhu %zdir/system
install system/languages/*.qm %zdir/system/languages
install system/icons/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

#useless file
rm -f %zdir/work/.directory

%files
%doc doc/ readme.txt
%_bindir/%name
%dir %_datadir/%name/
%dir %_datadir/%name/work/
%dir %_datadir/%name/work/textures/
%dir %_datadir/%name/system/
%dir %_datadir/%name/system/languages/
%_datadir/%name/work/*.zhu
%_datadir/%name/work/textures/*.jpg
%_datadir/%name/work/textures/*.txt
%_datadir/%name/system/*.zhu
%_iconsdir/hicolor/64x64/apps/*.png
%_desktopdir/%name.desktop
%lang(de) %_datadir/%name/system/languages/%{name}_de.qm
%lang(es) %_datadir/%name/system/languages/%{name}_es.qm
%lang(fr) %_datadir/%name/system/languages/%{name}_fr.qm
%lang(zh) %_datadir/%name/system/languages/%{name}_zh.qm

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.1
- Fixed build

* Fri Jul 10 2009 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- new version 4.2.2 (with rpmrb script)

* Sat Nov 01 2008 Vitaly Lipatov <lav@altlinux.ru> 4.1.4-alt1
- new version 4.1.4 (with rpmrb script)

* Tue Jun 24 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0.4-alt2
- fix datadir

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0.4-alt1
- initial build for ALT Linux Sisyphus

* Tue Mar 11 2008 Funda Wang <fundawang@mandriva.org> 4.0.0-1mdv2008.1
+ Revision: 185931
- Updated to new version 4.0.0

* Sun Mar 09 2008 Funda Wang <fundawang@mandriva.org> 3.4.8-1mdv2008.1
+ Revision: 182805
- New version 3.4.8

* Sat Mar 08 2008 Funda Wang <fundawang@mandriva.org> 3.4.6-1mdv2008.1
+ Revision: 182052
- update to new version 3.4.6

* Sun Feb 24 2008 Funda Wang <fundawang@mandriva.org> 3.4.4-1mdv2008.1
+ Revision: 174227
- New version 3.4.4

* Sun Jan 27 2008 Funda Wang <fundawang@mandriva.org> 3.4.2-1mdv2008.1
+ Revision: 158672
- New version 3.4.2

* Tue Jan 08 2008 Funda Wang <fundawang@mandriva.org> 3.4.0-1mdv2008.1
+ Revision: 146569
- update to new version 3.4.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3.6-1mdv2008.1
+ Revision: 133092
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Funda Wang <fundawang@mandriva.org> 3.3.4-1mdv2008.1
+ Revision: 119081
- New version 3.3.4

* Fri Dec 07 2007 Funda Wang <fundawang@mandriva.org> 3.3.2-1mdv2008.1
+ Revision: 116309
- update to new version 3.3.2

* Mon Dec 03 2007 Funda Wang <fundawang@mandriva.org> 3.3.0-1mdv2008.1
+ Revision: 114556
- New version 3.3.0
- rediff patch0

* Sat Dec 01 2007 Funda Wang <fundawang@mandriva.org> 3.2.9-3mdv2008.1
+ Revision: 114248
- remove quotes in desktop file

* Fri Nov 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.9-2mdv2008.1
+ Revision: 114035
- fix patch 0 :|

* Fri Nov 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.9-1mdv2008.1
+ Revision: 113997
- rewrite patch 0
- new version

* Mon Nov 26 2007 Funda Wang <fundawang@mandriva.org> 3.2.0-1mdv2008.1
+ Revision: 112079
- New version 3.2.0

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.8-1mdv2008.1
+ Revision: 111372
- new version

* Mon Nov 19 2007 Funda Wang <fundawang@mandriva.org> 3.1.6-1mdv2008.1
+ Revision: 110399
- drop kdelibs BR
- New version 3.1.6

* Thu Nov 15 2007 Funda Wang <fundawang@mandriva.org> 3.1.4-1mdv2008.1
+ Revision: 108889
- New version 3.1.4

* Mon Nov 05 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.2-2mdv2008.1
+ Revision: 106221
- fix typo in desktop file

* Sun Nov 04 2007 Funda Wang <fundawang@mandriva.org> 3.1.2-1mdv2008.1
+ Revision: 105741
- New version 3.1.2

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.0-2mdv2008.1
+ Revision: 102410
- better desktop file
- new license policy

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.0-1mdv2008.1
+ Revision: 102326
- new version

* Tue Oct 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.9-1mdv2008.1
+ Revision: 101371
- new version

* Tue Oct 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.6-1mdv2008.1
+ Revision: 98767
- new version

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.4-1mdv2008.0
+ Revision: 93933
- new version
- new version

* Fri Aug 10 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.0-1mdv2008.0
+ Revision: 61051
- new version

* Thu Jul 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.8-1mdv2008.0
+ Revision: 53663
- new version
- drop X-MandrivaLinux from desktop file

* Mon May 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.6-2mdv2008.0
+ Revision: 32015
- rebuild

* Tue Feb 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.6-1mdv2007.0
+ Revision: 123170
- new version
- some cleans in spec file

* Tue Jan 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.4-1mdv2007.1
+ Revision: 112454
- provide desktop file
- add patch 0
- complete spec file
- Import zhu3d

