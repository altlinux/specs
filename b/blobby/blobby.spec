Name: blobby
Version: 1.1.1
Release: alt2

Summary: Volley-ball game
Group: Games/Other
License: GPLv2+

Url: http://blobbyvolley.de
VCS: https://github.com/danielknobe/blobbyvolley2

Source0: %name-%version.tar
Patch: LinkedList-1.1.1.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel libGLU-devel libglvnd-devel unzip
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel, libphysfs-devel, zlib-devel ctest cmake, boost-complete, zip
BuildRequires: ImageMagick-tools, desktop-file-utils, icon-theme-hicolor
BuildRequires: libGL-devel

%description
Blobby Volley is one of the most popular freeware games.
Blobby Volley 2 is the continuation of this lovely game.

%prep
%setup
%patch -p1

%build
%cmake -DOpenGL_GL_PREFERENCE=GLVND .
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README* ChangeLog COPYING
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/blobby
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml

%changelog
* Sat May 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.1-alt2
- fixed FTBFS

* Sun Jul 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.1.1-alt1
- 1.0 -> 1.1.1
- removed patchs
- added VCS

* Mon Jun 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0-alt4_19.svn1681
- NMU: fixed FTBFS

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_19.svn1681
- update to new release by fcimport

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_17.svn1681
- use boost-complete

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17.svn1681
- update to new release by fcimport

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11.svn1541
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.11.rc4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.rc4
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.8.rc4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.6.rc3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.5.rc3
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.4.rc3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.rc1
- update to new release by fcimport

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.1.rc1
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.1.rc1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9b-alt1_2
- converted from Fedora by srpmconvert script

