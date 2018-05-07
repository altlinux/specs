# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libGLU-devel unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global svn_rev 1681
Name:           blobby
Version:        1.0
Release:        alt2_17.svn%{svn_rev}
Summary:        Volley-ball game
Group:          Games/Other
License:        GPLv2+
URL:            http://blobby.sourceforge.net
# Version 1 is broken. Upstream suggested I use the svn checkout.
# svn export -r 1541  svn://svn.code.sf.net/p/blobby/code/trunk blobby-1.0svn1541
# tar -cvzf blobby-1.0svn1541.tar.gz blobby-1.0svn1541/
# Source0:        http://downloads.sourceforge.net/%%{name}/%%{name}2-linux-%%{version}.tar.gz
Source0:        %{name}-%{version}svn%{svn_rev}.tar.gz
Source1:        blobby.desktop
Source2:        blobby.appdata.xml
Patch0:         blobby-vector.patch
Patch1:         blobby-vector2.patch
Patch2:         blobby-vector3.patch
Patch3:         blobby-compile-flags.patch
Patch4:         blobby-vector4.patch

BuildRequires:  libSDL2-devel, libphysfs-devel, zlib-devel ctest cmake boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-headers boost-signals-devel boost-wave-devel, zip
BuildRequires:  ImageMagick-tools, desktop-file-utils, icon-theme-hicolor
BuildRequires:  tinyxml-devel lua-devel
BuildRequires:  libGL-devel
Source44: import.info

%description
Blobby Volley is one of the most popular freeware games.
Blobby Volley 2 is the continuation of this lovely game.

%prep
%setup -q -n %{name}-%{version}svn%{svn_rev}
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig2
%patch2 -p0 -b .orig3
%patch3 -p0 -b .orig4
%patch4 -p0 -b .orig5

# Remove lua and tinyxml
rm -rvf src/lua
rm -rvf src/tinyxml
sed -ibackup -e "/add_subdirectory(lua)/d" -e "/add_subdirectory(tinyxml)/d" src/CMakeLists.txt
sed -ibackup 's|tinyxml/||' src/UserConfig.cpp
sed -ibackup 's|tinyxml/||' src/TextManager.cpp
sed -ibackup 's|tinyxml/||' src/state/NetworkSearchState.cpp
sed -ibackup 's|tinyxml/||' src/replays/ReplayRecorder.cpp
sed -ibackup 's|tinyxml/||' src/replays/ReplayLoader.cpp
sed -ibackup 's|tinyxml/||' src/FileRead.cpp
sed -ibackup 's|lua/||' src/FileRead.cpp
sed -ibackup 's|lua/||' src/GameLogic.cpp
sed -ibackup 's|lua/||' src/IScriptableComponent.cpp
sed -ibackup 's|lua/||' src/ScriptedInputSource.cpp

# Updated to SDL2 but still looks for SDL also? Why!
sed -ibackup '/find_package(SDL REQUIRED)/d' src/CMakeLists.txt

%build
%{fedora_cmake} -DOpenGL_GL_PREFERENCE=GLVND .
%make_build

%install
%makeinstall_std

# Icon
# unzip -o -j data/gfx.zip gfx/ball01.bmp
convert -size 48x48 -transparent black data/Icon.bmp blobby.png
install -p -m 644 -D blobby.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/blobby.png

# Desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
install -p -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata/blobby.appdata.xml

%files
%doc AUTHORS README ChangeLog COPYING TODO
%{_bindir}/*
%{_datadir}/blobby
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
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

