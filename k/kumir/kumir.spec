Name: kumir
Version: 1.8.0
Release: alt6

Summary: Kumir is a simple programming language and IDE for teaching programming
Summary(ru_RU.UTF-8): Кумир это простой язык программирования и среда разработки, применяемый при обучении

License: GPL
Group: Education
Url: http://lpm.org.ru/kumir
Packager: Denis Kirienko <dk@altlinux.ru>

BuildPreReq: libqt4-devel gcc-c++ python-modules
Requires: libqt4-core

Source: kumir-1.8.0.2780.tar.bz2
Source1: %name-alt-icons.tar.bz2
Source2: test.vod

Patch0: %name-1.7.1-desktop.patch
Patch1: %name-1.7.90-x-kumir-program.desktop.patch
Patch2: %name-1.7.1-x-kumir-program.xml.patch
Patch3: %name-1.8.0-build.patch

%description
Implementation of Kumir programming language, designed by academician
Ershov. It has very simple syntax, also known as "Russian algorithmical
language". Includes compiler, runtime, IDE and  modules "Robot", "Draw",
"Turtle" and some others.

%description -l ru_RU.UTF-8
Кумир - это учебный язык программирования, описанный в учебнике
А.Г.Кушниренко, и среда разработки. Он имеет простой синтаксис,
известный также как "русский алгоритмический язык". В состав среды также
входят канонические исполнители Робот, Чертежник, Черепаха и другие,
что делает Кумир очень удобным для начального обучения программированию.

%prep
%setup -n kumir -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
cp %SOURCE2 .
find . -type f -name \*.pro |xargs sed -i 's,QMAKE_CXXFLAGS_RELEASE += -O2,QMAKE_CXXFLAGS_RELEASE += %optflags,'

%build
chmod a+x configure.py
%configure --prefix=%buildroot/usr --target-dir=%buildroot%_libdir/%name --qmake=qmake-qt4 --lrelease=lrelease-qt4
qmake-qt4 Addons/Robotor3D/robotor3D.pro PREFIX=%buildroot/usr KUMIR_DIR=%buildroot%_libdir/%name
%make_build

%install
mkdir -p %buildroot/usr/bin
%make_install install

# Install desktop and mime-info files
install -m 644 -D Kumir/X-Desktop/%name.desktop %buildroot%_desktopdir/%name.desktop
install -m 644 -D Kumir/X-Desktop/x-kumir-program.xml %buildroot/%_datadir/mime/packages/x-kumir-program.xml
install -m 644 -D Kumir/X-Desktop/x-kumir-program.desktop  %buildroot/%_datadir/mimelnk/application/x-kumir-program.desktop

# Install icons
mkdir -p %buildroot%_miconsdir/ %buildroot%_niconsdir/ %buildroot%_liconsdir/ %buildroot%_iconsdir/hicolor/64x64/apps/ %buildroot%_iconsdir/hicolor/128x128/apps/
install -m 644 app_icons/png/16x16/*.png %buildroot%_miconsdir/
install -m 644 app_icons/png/32x32/*.png %buildroot%_niconsdir/
install -m 644 app_icons/png/48x48/*.png %buildroot%_liconsdir/
install -m 644 app_icons/png/64x64/*.png %buildroot%_iconsdir/hicolor/64x64/apps/
install -m 644 app_icons/png/128x128/*.png %buildroot%_iconsdir/hicolor/128x128/apps/
rm %buildroot%_iconsdir/hicolor/128x128/apps/kumir.png
rm %buildroot%_iconsdir/hicolor/*/apps/pictomir.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/16x16/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/16x16/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/22x22/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/22x22/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/32x32/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/32x32/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/48x48/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/48x48/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/64x64/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/64x64/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/scalable/application-x-kumir-program.svg %buildroot%_iconsdir/crystalsvg/scalable/mimetypes/application-x-kumir-program.svg
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/16x16/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/16x16/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/22x22/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/22x22/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/32x32/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/32x32/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/48x48/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/48x48/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/64x64/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/64x64/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/scalable/application-x-kumir-program.svg %buildroot%_iconsdir/oxygen/scalable/mimetypes/application-x-kumir-program.svg

# Install TaskControl plugin and taskEdit
install -m 644 -D TaskControl/libtaskControl.so  %buildroot%_libdir/%name/TaskControl/libtaskControl.so
install -m 755 taskEdit %buildroot%_libdir/%name/

# Install Painter module
install -m 644 Addons/libpainter.so  %buildroot%_libdir/%name/Addons/
mkdir -p %buildroot%_libdir/%name/Addons/painter/resources/
install -m 644 Addons/painter/resources/* %buildroot%_libdir/%name/Addons/painter/resources/

# Install robot25d module
install -m 644 Addons/librobot25d.so  %buildroot%_libdir/%name/Addons/
mkdir -p %buildroot%_libdir/%name/Addons/robot25d/resources/
install -m 644 Addons/robot25d/resources/* %buildroot%_libdir/%name/Addons/robot25d/resources/

# Install Vodoley default environment
install -m 644 -D test.vod  %buildroot%_libdir/%name/Addons/vodoley/resources/test.vod

# Install turtle.ini file
install -m 644 -D Addons/turtle.ini %buildroot%_libdir/%name/Addons/turtle.ini

# Fix paths to help files
cd %buildroot%_libdir/%name/Kumir
ln -s Help help

# Rename kumir.png to correct name
cd %buildroot/%_datadir/pixmaps
mv kumir.png application-x-kumir-program.png

# make link in /usr/bin/kumir
cd %buildroot%_bindir
rm kumir kumpluginstarter
ln -s ../..%_libdir/kumir/kumir kumir
ln -s ../..%_libdir/kumir/pluginstarter kumpluginstarter

%files
%_bindir/*
%_libdir/%name
%_desktopdir/*
%_iconsdir/*/*/*/*
%_datadir/pixmaps/*
%_datadir/mime/packages/x-kumir-program.xml
%_datadir/mimelnk/application/x-kumir-program.desktop

%changelog
* Sat Jun 02 2012 Denis Kirienko <dk@altlinux.org> 1.8.0-alt6
- SVN snapshot 2780

* Tue Mar 20 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.0-alt5
- rebuilt with optflags

* Fri Aug 05 2011 Denis Kirienko <dk@altlinux.ru> 1.8.0-alt4
- SVN snapshot 2596

* Thu Jun 30 2011 Denis Kirienko <dk@altlinux.ru> 1.8.0-alt3
- SVN snapshot 2590

* Tue Apr 26 2011 Denis Kirienko <dk@altlinux.ru> 1.8.0-alt2
- BuildPreReq: python-modules

* Fri Apr 08 2011 Denis Kirienko <dk@altlinux.ru> 1.8.0-alt1
- Version 1.8.0 (SVN 2565)

* Wed Mar 30 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2560-alt1
- SVN snapshot 2560

* Wed Mar 16 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2527-alt1
- SVN snapshot 2527

* Fri Mar 11 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2522-alt1
- SVN snapshot 2522

* Wed Feb 23 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2486-alt1
- SVN snapshot 2486

* Fri Feb 18 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2475-alt1
- SVN snapshot 2475
- Added module "Painter"

* Wed Feb 09 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2461-alt1
- SVN snapshot 2461

* Wed Feb 02 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2438-alt1
- SVN snapshot 2438

* Wed Jan 26 2011 Denis Kirienko <dk@altlinux.ru> 1.7.90.2419-alt1
- SVN snapshot 2419

* Fri Dec 17 2010 Denis Kirienko <dk@altlinux.ru> 1.7.90.2369-alt1
- SVN snapshot 2369 (1.7.3 final release)

* Mon Dec 13 2010 Denis Kirienko <dk@altlinux.ru> 1.7.90.2366-alt1
- SVN snapshot 2366

* Sun Dec 12 2010 Denis Kirienko <dk@altlinux.ru> 1.7.90.2364-alt1
- SVN snapshot 2364

* Fri Dec 10 2010 Denis Kirienko <dk@altlinux.ru> 1.7.90.2358-alt1
- SVN snapshot 2358

* Thu Nov 04 2010 Denis Kirienko <dk@altlinux.ru> 1.7.90.2247-alt1
- Development version 1.7.90, SVN snapshot 2247

* Fri Sep 17 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt8
- 1.7.1 final release

* Fri Aug 27 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt7
- SVN snapshot 2027

* Fri Jul 02 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt6
- 1.7.1-rc6 (SVN snapshot 1998)

* Mon Jun 21 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt5
- 1.7.1-rc5 (SVN snapshot 1994)

* Thu Jun 10 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt4
- 1.7.1-rc4 (SVN snapshot 1980)

* Mon May 10 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt3
- 1.7.1-rc2

* Wed May 05 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt2
- 1.7.1-rc1

* Fri Apr 30 2010 Denis Kirienko <dk@altlinux.ru> 1.7.1-alt1
- 1.7.1-pre3
- Removed Pictomir application because of license restrictions

* Fri Feb 19 2010 Denis Kirienko <dk@altlinux.ru> 1.7-alt11
- SVN snapshot 1694

* Thu Feb 11 2010 Denis Kirienko <dk@altlinux.ru> 1.7-alt10
- SVN snapshot 1690

* Sat Jan 09 2010 Denis Kirienko <dk@altlinux.ru> 1.7-alt9
- SVN snapshot 1579

* Thu Dec 17 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt8
- SVN snapshot 1546

* Wed Dec 16 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt7
- SVN snapshot 1541

* Mon Dec 07 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt6
- SVN snapshot 1523

* Wed Nov 18 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt5
- SVN snapshot 1435
- Included module "vodoley"

* Thu Nov 12 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt4
- SVN snapshot 1414
- Added "pictomir" application
- Modules "turtle", "kuznechik" and "isometricRobot" are
  integrated to the main menu
- Excluded module "vodoley" (upstream bugreport #591)

* Fri Oct 23 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt3
- SVN snapshot 1342
- Initial experimental support for external modules:
  "turtle", "vodoley", "Kuznechik"

* Fri Oct 09 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt2
- SVN snapshot 1323

* Sun Oct 04 2009 Denis Kirienko <dk@altlinux.ru> 1.7-alt1
- Development version 1.7 (SVN 1291)

* Fri Aug 28 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt19
- Fixed searching for available PDF viewer under KDE4

* Sat Feb 28 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt18
- Version 1.6 final release (SVN 988)

* Sat Feb 21 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt17
- SVN snapshot 978

* Mon Feb 09 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt16
- SVN snapshot 965

* Sat Feb 07 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt15
- SVN snapshot 960

* Fri Jan 23 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt14
- SVN snapshot 945
- Removed recursion patch

* Wed Jan 21 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt13
- SVN snapshot 935

* Thu Jan 15 2009 Denis Kirienko <dk@altlinux.ru> 1.6-alt12
- SVN snapshot 930

* Sun Dec 28 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt11
- SVN snapshot 913
- Max recursion depth decreased to 200

* Mon Dec 22 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt10
- SVN snapshot 904
- Fixed build for x86_64

* Sun Dec 21 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt9
- SVN snapshot 898
- Added mime info and mime icons
- Added patch to increase maximum recursion depth from 128 to 4096

* Sat Nov 29 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt8
- SVN snapshot 719
- Spec cleanup

* Tue Sep 30 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt7
- SVN snapshot 562
- Fixed kumir.desktop

* Fri Sep 19 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt6
- SVN snapshot 530

* Sun Sep 07 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt5.svn512
- SVN snapshot 512
- Fixed kumir.desktop

* Fri Aug 01 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt4.svn440
- SVN snapshot 440

* Thu Jul 03 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt3.svn377
- SVN snapshot 377

* Sun Jun 08 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt2.svn307
- SVN snapshot 307

* Sun Jun 01 2008 Denis Kirienko <dk@altlinux.ru> 1.6-alt1.svn273
- First build for ALT Linux Sisyphus
- SVN snapshot 273
