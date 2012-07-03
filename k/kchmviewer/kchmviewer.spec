Name: kchmviewer
Version: 5.2
Release: alt1

Summary: A chm (MS HTML help file format) viewer (with KDE4 support)
License: %gpl3plus
Group: Office
Url: http://kchmviewer.net

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-5.2-alt-remove-update-check.patch
Patch1: %name-5.2-alt-fix-cmake-build.patch

BuildRequires(pre): rpm-build-licenses kde-common-devel
BuildPreReq: gcc-c++ kde4libs-devel libchm-devel

Conflicts: kde4graphics-okular < 4.2.3-alt1
Obsoletes: kchmviewer4 <= 4.0-alt3
Provides: kchmviewer4 = %version-%release

%define _unpackaged_files_terminate_build 1
%define __kde4_alternate_placement 1

%package nokde
Summary: A chm (MS HTML help file format) viewer
Group: Office
Conflicts: kchmviewer


%description
KchmViewer is a chm (MS HTML help file format) viewer, written in C++.
The main advantage of KchmViewer is extended support for non-English
languages. Unlike others, KchmViewer in most cases correctly detects chm
file encoding, correctly shows tables of context of Russian, Korean,
Chinese and Japanese help files. It also correctly searches text in
non-English help files, including Korean, Chinese and Japanese.

This version is built with KDE4 support and uses KHTML engine.


%description nokde
KchmViewer is a chm (MS HTML help file format) viewer, written in C++.
The main advantage of KchmViewer is extended support for non-English
languages. Unlike others, KchmViewer in most cases correctly detects chm
file encoding, correctly shows tables of context of Russian, Korean,
Chinese and Japanese help files. It also correctly searches text in
non-English help files, including Korean, Chinese and Japanese.

This version is built without KDE4 support and uses Qt Webkit engine.


%prep
%setup
%patch0 -p2
%patch1 -p2

%build
%K4cmake -DKDE4_ENABLE_FINAL:BOOL=1
%K4make
%K4make

mkdir build-nokde
pushd build-nokde
qmake-qt4 ../kchmviewer.pro %{!?_enable_debug:-after "CONFIG -= debug"}
%make lib/Makefile src/Makefile
%make -C lib libchmfile/Makefile
sed -i 's|-pipe |%optflags |g' lib/libchmfile/Makefile src/Makefile
%make_build

%install
%K4install VERBOSE=1
install -pD -m755 build-nokde/bin/kchmviewer %buildroot%_bindir/%name
install -pD -m644 packages/kchmviewer.png %buildroot%_K4datadir/icons/hicolor/128x128/apps/%name.png

%K4find_lang --with-kde %name


%files -f %name.lang
%doc ChangeLog DBUS-bindings FAQ README
%__kde4_bindir/*
%_K4lib/*.so
%_K4datadir/icons/hicolor/*/apps/*.png
%_K4datadir/applications/kde4/*.desktop
%_K4srv/*.protocol


%files nokde
%_bindir/%name
%doc ChangeLog DBUS-bindings FAQ README


%changelog
* Sat Feb 05 2011 Ivan A. Melnikov <iv@altlinux.org> 5.2-alt1
- 5.2
- patch updated
- added patch 1 to fix cmake build
- rebuild with new Qt to fix crash with QWebKit

* Sun Dec 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 5.1-alt1
- 5.1

* Tue Dec 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 5.0-alt1
- 5.0

* Sun Oct 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.2-alt1
- 4.2

* Thu Sep 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.1-alt2
- move icons from crystalsvg/ to hicolor/

* Tue Jul 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.1-alt1
- 4.1

* Sat May 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt5
- don't conflict with ocular >= 4.2.3-alt1

* Sun Mar 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt4
- rename back to kchmviewer
- update description
- build a version without KDE support (closes: #12407)

* Tue Dec 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt3
- 4.0 release

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt2.beta3
- enable KDE4_ENABLE_FINAL

* Tue Jun 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt1.beta3
- 4.0beta3
- Sisyphus build

* Thu Mar 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt1.beta2
- add update_desktopdb/clean_desktopdb calls (found by repocop)
- fix desktop file according to desktop-file-validate

* Tue Feb 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.beta2
- 4.0 beta2

* Sat Sep 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.beta1
- 4.0 beta1

* Sun Jun 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.1-alt1
- 3.1-2

* Sun Apr 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt1
- 3.0

* Thu Dec 07 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.7-alt1
- 2.7

* Thu Oct 05 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt1
- 2.6
- take from orphaned
- build with KDE
- spec fixes and cleanup
- enable installing of translation files
- enable _unpackaged_files_terminate_build

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 2.5-alt1
- 2.5

* Tue Feb 07 2006 Andrey Semenov <mitrofan@altlinux.ru> 2.0-alt1
- new version

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- new version

* Wed Nov 02 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.1-alt1
- new version

* Mon Sep 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt2
- add file menu

* Fri Jul 29 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- 1.0

* Thu Jun 30 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.92-alt1
- 0.92

* Mon Jun 20 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.91-alt1
- 0.91

* Wed Jun 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.9-alt1
- 0.9

* Thu May 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3-alt1
- 0.3

* Mon Apr 25 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt1
- 0.2

* Thu Apr 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.1-alt1
- First version
