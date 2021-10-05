%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_enable debug

Name: springrts
Version: 105.0
Release: alt2
Summary: Real time strategy game engine with many mods
License: GPL-2.0+ and BSD-3-Clause
Group: Games/Strategy
Url: https://springrts.com/

ExclusiveArch: %ix86 x86_64

# https://github.com/spring/spring.git
Source: %name-%version.tar

# submodules
Source1: %name-%version-AI-Interfaces-Python.tar
Source2: %name-%version-AI-Skirmish-AAI.tar
Source3: %name-%version-AI-Skirmish-CircuitAI.tar
Source4: %name-%version-AI-Skirmish-HughAI.tar
Source5: %name-%version-AI-Skirmish-KAIK.tar
Source6: %name-%version-AI-Skirmish-Shard.tar
Source7: %name-%version-tools-mapcompile.tar
Source8: %name-%version-tools-pr-downloader.tar
Source9: %name-%version-tools-pr-downloader-src-lib-libgit2.tar
Source10: %name-%version-tools-unitsync-python.tar

Patch1: %name-alt-linking.patch
Patch2: %name-alt-unbundle-libs.patch
Patch3: %name-alt-unbundle-libs-pr-downloader.patch
Patch4: %name-alt-gcc11-compat.patch

BuildRequires(pre): rpm-build-xdg rpm-macros-cmake
BuildRequires: cmake cmake-modules java-devel /proc libGL-devel libGLU-devel gcc-c++
BuildRequires: boost-devel boost-program_options-devel boost-asio-devel boost-signals-devel boost-filesystem-devel
BuildRequires: libICE-devel libSM-devel libX11-devel libXdamage-devel libXfixes-devel libXrender-devel 
BuildRequires: libXt-devel libfreetype-devel libogg-devel libstdc++-devel 
BuildRequires: xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel 
BuildRequires: xorg-xineramaproto-devel xorg-xproto-devel zlib-devel p7zip libXcursor-devel
BuildRequires: libdevil-devel libfreeglut-devel libglew-devel libopenal1-devel 
BuildRequires: libvorbis-devel  python-devel libSDL2-devel
BuildRequires: docbook5-style-xsl asciidoc libminizip-devel
BuildRequires: libXres-devel libXtst-devel libXau-devel libXcomposite-devel
BuildRequires: libXdmcp-devel libXext-devel libXft-devel libXi-devel
BuildRequires: libXinerama-devel libxkbfile-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXScrnSaver-devel libXv-devel
BuildRequires: libXxf86misc-devel libXxf86vm-devel
BuildRequires: libcurl-devel jsoncpp-devel libunwind-devel
BuildRequires: /usr/bin/xsltproc
BuildRequires: asio-devel libassimp-devel

Requires: %name-data = %EVR
Conflicts: %name-dedicated < %EVR
Provides: %name-dedicated = %EVR
Obsoletes: %name-dedicated

%description
Spring is an open source RTS (Real time Strategy) engine originally
designed to recreate the experience of Total Annihilation.  Spring now
supports many different games ("mods"), including both remakes of the
original Total Annihilation and completely new games.

This package contains the game engine and default AI, but no maps, mods,
or user interface.

%package data
Summary: data files for Spring RTS engine
Group: Games/Strategy
BuildArch: noarch

%description data
data files for Spring RTS engine

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10
%patch1 -p1
%patch2 -p1

pushd tools/pr-downloader
%patch3 -p1
popd

%patch4 -p1

# TODO: remove remaining bundled libraries. They're either missing or patched.
rm -rf tools/pr-downloader/src/lib/{jsoncpp,minizip}
rm -rf rts/lib/{asio,assimp,minizip}

# provide version information
echo %version > VERSION

%build
%add_optflags -fPIC -DPIC -D_FILE_OFFSET_BITS=64
%cmake \
%if_enabled debug
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%else
	-DCMAKE_BUILD_TYPE=Release \
%endif
	-DLIBDIR=%_libdir \
	-DBINDIR=%_gamesbindir \
	-DAI_LIBS_DIR=%_libdir/spring \
	-DAI_DATA_DIR=%_gamesdatadir/spring \
	-DDOCDIR=share/doc/%name-%version \
	-DDOCBOOK_XSL=%_datadir/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl \
	-DAI_TYPES=NATIVE \
	%nil

%cmake_build

%install
%cmake_install

# Move icons into proper Freedesktop hicolor theme
mkdir -p %buildroot%_liconsdir

mv %buildroot%_pixmapsdir/spring.png \
    %buildroot%_liconsdir/

mkdir -p %buildroot%_iconsdir/hicolor/48x48/mimetypes/

mv %buildroot%_pixmapsdir/application-x-spring-demo.png \
    %buildroot%_iconsdir/hicolor/48x48/mimetypes/

# Make it visible
sed -i -e '/NoDisplay=true/d' \
    %buildroot%_desktopdir/spring.desktop

%files
%doc LICENSE LICENSE.html
%doc AUTHORS FAQ THANKS
%_gamesbindir/pr-downloader
%_gamesbindir/spring
%_gamesbindir/spring-headless
%_gamesbindir/spring-dedicated
%_gamesbindir/mapcompile
%_gamesbindir/mapdecompile
%_libdir/spring
%_libdir/*.so

%files data
%_gamesdatadir/*
%_xdgmimedir/packages/*
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/*/mimetypes/*.png
%_man6dir/*

%changelog
* Tue Oct 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 105.0-alt2
- Fixed build with gcc-11 and new jsoncpp.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 105.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Apr 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 105.0-alt1
- Updated to upstream version 105.0.
- Updated packaging scheme and license.

* Mon Jan 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 104.0-alt3
- Fixed build with gcc-10.

* Wed Dec 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 104.0-alt2
- Fixed build with new toolchain.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 104.0-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon Apr 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 104.0-alt1
- Updated to upstream version 104.0.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 103.0-alt1
- Updated to upstream release 103.0.
- Moved dedicated server back to main package.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 91.0-alt1.git20120830.qa1.1
- rebuild with boost 1.57.0
- fix build

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 91.0-alt1.git20120830.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 91.0-alt1.git20120830
- Version 91.0

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.5
- Fixed build

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.4
- Rebuilt with Boost 1.49.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.81.2.1-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Apr 15 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.2.1-alt1
- Bump to 0.81.2.1
- NTAI removed as it is broken
- Fix AI load crash

* Thu Apr 15 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.1.3-alt2
- Fix build with current Boost
- Fix AI libs search by unitsync library

* Mon Feb 01 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.1.3-alt1
- Bump to 0.81.1.3

* Sun Jan 24 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.0-alt1
- Bump to 0.81.0

* Sat Jan 09 2010 Maxim Ivanov <redbaron at altlinux.org> 0.80.5.2-alt1
- Updated to 0.80.5.2
- Corrected buildreq
- Better arch vs noarch files destribution

* Sat Oct 31 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.5.1-alt1
- Updated to 0.80.5.1
- Dedicated server packed separately

* Sat Sep 05 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.4.1-alt1
- Update to 0.80.4.1

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.2-alt1
- Update to 0.80.2

* Sun Jun 07 2009 Maxim Ivanov <redbaron at altlinux.org> 0.79.1-alt1
- Initial build for ALTLinux
