%def_with sdl2
#TODO: fix cmake SDLmain
%def_without cmake
Name: fheroes2
Epoch: 2
Version: 1.0.1
#define rev 20210604
#Release: alt1.%rev
Release: alt1
Summary: Free implementation of Heroes of the Might and Magic II engine
License: GPLv2+
Group: Games/Strategy
Url: https://github.com/ihhub/fheroes2
VCS: https://github.com/ihhub/fheroes2

%add_findreq_skiplist %_docdir/%name

Source: %name-%version.tar
Source2: %name.sh
Source3: %name.png
Source4: fheroes2-data.spec
Source5: README.ALT
Patch0: fheroes2-1.0.1-random-skills.patch

# Automatically added by buildreq on Wed Oct 03 2012
# optimized out: libSDL-devel libstdc++-devel zlib-devel
BuildRequires: gcc-c++ libfreetype-devel gettext-tools

# with image
BuildRequires: libpng-devel
# for future use:
#BuildRequires: libjpeg-devel libwebp-devel libogg-devel
%if_with sdl2
BuildRequires: libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel libSDL2_ttf-devel
%else
BuildRequires: libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel
%endif
%if_with cmake
BuildRequires: cmake
%endif

%description
Free implementation of Heroes of the Might and Magic II engine.
You need to copy files from data and maps directories from original game
into your /usr/share/games/fheroes2/{maps,data} directories respectively

%prep
%setup -q
%patch0 -p1

%build
export LANG=en_US.UTF-8
%if_with cmake
# see docs/README_cmake.md
%cmake \
    -DFHEROES2_DATA="%_gamesdatadir/%name/" \
%if_with sdl2
    -DUSE_SDL_VERSION=SDL2 \
%else
    -DUSE_SDL_VERSION=SDL \
%endif
    -DENABLE_IMAGE=ON
#    -DENABLE_TOOLS=ON

%cmake_build
%else
CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CCFLAGS="${CCFLAGS:-%optflags}"; export CCFLAGS;
%make_build \
%if_without sdl2
    FHEROES2_WITH_SDL1=1 \
%endif
    FHEROES2_DATA=%_gamesdatadir/%name/ \
    FHEROES2_WITH_IMAGE=1 \
    FHEROES2_WITH_TOOLS=

make -C files/lang
%endif

%install
%if_with cmake
%cmake_install
%else
# let's create directory structure...
mkdir -p %buildroot%_gamesdatadir/%name/{data,maps,files/lang}

# and install what we need where we need it to be...
install -pD -m 755 %name %buildroot%_bindir/%name
cp -a files/{data,images} %buildroot%_gamesdatadir/%name/files/
cp -a files/lang/*.mo %buildroot%_gamesdatadir/%name/files/lang/

install -pD -m 644 script/packaging/common/fheroes2.desktop %buildroot%_desktopdir/%name.desktop
%endif

# bin wrapper
mv %buildroot%_bindir/%name{,.bin}
install -pD -m 755 %SOURCE2 %buildroot%_bindir/%name

# install resources
install -pD -m 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pD -m 644 src/resources/fheroes2.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

# docs
mkdir -p %buildroot%_docdir/%name
install -pm 644 {CONTRIBUTING.md,changelog.txt,LICENSE,README.md,docs/INSTALL.md,docs/DEVELOPMENT.md} %buildroot%_docdir/%name/
install -pm 644 script/demo/download_demo_version.sh script/homm2/extract_homm2_resources.sh %buildroot%_docdir/%name/
install -pD -m 644 %SOURCE4 %SOURCE5 %buildroot%_docdir/%name/

%files
%_bindir/*
%_niconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_desktopdir/%name.desktop
%doc %_docdir/%name
%_gamesdatadir/%name

%changelog
* Fri Feb 10 2023 Igor Vlasenko <viy@altlinux.org> 2:1.0.1-alt1
- new version

* Thu Dec 22 2022 Igor Vlasenko <viy@altlinux.org> 2:1.0.0-alt1
- new version

* Sun Nov 27 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.21-alt1
- new version

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.20-alt1
- new version

* Sun Sep 11 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.19-alt1
- new version

* Mon Aug 15 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.18-alt1
- new version

* Fri Jul 15 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.17-alt1
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.16-alt1
- new version

* Tue May 10 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.15-alt2
- bugfix: switch to new format of defines

* Sun May 08 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.15-alt1
- new version

* Fri May 06 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.14-alt1
- new version

* Wed Mar 16 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.13-alt1
- new version

* Thu Feb 24 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.12-alt3
- support for data in lowercase
- fheroes2-0.9.12-fix-4997.patch

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.12-alt2
- properly set CONFIGURE_FHEROES2_DATA

* Fri Feb 11 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.12-alt1
- new version
- added translations (closes: #42001)
- python3 support (closes: #42002)

* Sun Jan 09 2022 Igor Vlasenko <viy@altlinux.org> 2:0.9.11-alt2
- XDG_DATA_DIR migration
- random-skills.patch
- added example fheroes2-data.spec

* Fri Dec 24 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.11-alt1
- new version

* Tue Dec 07 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.10-alt1
- new version

* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.9-alt1
- new version

* Fri Oct 08 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.8-alt1
- new version

* Fri Aug 13 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.6-alt1
- new version

* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.5-alt1
- new version

* Sat Jun 26 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.4-alt1
- new version

* Tue May 04 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.3-alt1
- new version

* Sat Apr 03 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.2-alt1
- new version

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 2:0.9.1-alt1
- new version

* Thu Feb 04 2021 Igor Vlasenko <viy@altlinux.ru> 2:0.9-alt1
- new version

* Wed Dec 23 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.8.4-alt1.20201223
- new version

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.8.3-alt1.20201104
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.8.2-alt1.20201004
- new version

* Thu Sep 24 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.8.1-alt1.20200904
- upstream re-released as 0.8.1

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.8.5-alt1.20200902
- new version

* Wed Aug 05 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.8-alt2.20200726
- added check of screen size
- sound=off by default

* Tue Aug 04 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.8-alt1.20200726
- new version

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 20161219-alt1.svn3279
- picked up from orphaned
- updated to the latest commit (closes: #32906)

* Wed Dec 24 2014 Andrew Clark <andyc@altlinux.org> 20131009-alt1.svn3269
- version update to 20131009-alt1.svn3269

* Sun Aug 31 2014 Andrew Clark <andyc@altlinux.org> 20131009-alt1.svn3225
- version update 20131009-alt1.svn3225

* Sun Apr 6 2014 Andrew Clark <andyc@altlinux.org> 20130303-alt1.svn3194
- version update 20130303-alt1.svn3194

* Sun Dec 22 2013 Andrew Clark <andyc@altlinux.org> 20130303-alt1.svn3190
- version update 20130303-alt1.svn3190

* Wed Jul 24 2013 Andrew Clark <andyc@altlinux.org> 20130303-alt1.svn3112
- version update 20130303-alt1.svn3112

* Sun May 26 2013 Andrew Clark <andyc@altlinux.org> 20130303-alt1.svn3097
- version update 20130303-alt1.svn3097

* Sat Apr 13 2013 Andrew Clark <andyc@altlinux.org> 20130303-alt1.svn3061
- version update 20130303-alt1.svn3061

* Wed Mar 13 2013 Andrew Clark <andyc@altlinux.ru> 20130303-alt1.svn3036
- version update 20130303-alt1.svn3036

* Fri Feb 22 2013 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2982
- version update 20120301-alt1.svn2982

* Sat Jan 26 2013 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2967
- version update 20120301-alt1.svn2967

* Tue Dec 18 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2964
- version update 20120301-alt1.svn2964

* Thu Nov 1 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2951
- version update 20120301-alt1.svn2951

* Wed Oct 3 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2886
- version update 20120301-alt1.svn2886

* Thu Aug 30 2012 Michael Shigorin <mike@altlinux.org> 20120301-alt1.svn2867.1
- actually use WITH_AI=simple (closes: #27151; see also SF#3467445)

* Wed Aug 29 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2867
- version update 20120301-alt1.svn2867

* Sat Jun 30 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2865
- version update 20120301-alt1.svn2865

* Sun Jun 10 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2862
- version update 20120301-alt1.svn2862

* Mon Apr 30 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2857
- version update 20120301-alt1.svn2857

* Sat Feb 18 2012 Andrew Clark <andyc@altlinux.ru> 20120301-alt1.svn2788
- version update 20120301-alt1.svn2788

* Sat Feb 18 2012 Andrew Clark <andyc@altlinux.ru> 20110313-alt1.svn2739
- version update 20110313-alt1.svn2739

* Sat Dec 31 2011 Andrew Clark <andyc@altlinux.ru> 20110313-alt1.svn2732
- version update 20110313-alt1.svn2732

* Sun Nov 20 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2713
- version update to 20110313-alt1.svn2713

* Sun Nov 13 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2699
- version update to 20110313-alt1.svn2699

* Sun Sep 25 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2593
- version update to 20110313-alt1.svn2593

* Thu Sep 1 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2504
- version update to 20110313-alt1.svn2504

* Sun Aug 7 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2438
- version update to 20110313-alt1.svn2438

* Sun Jul 10 2011  Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2399
- version update to 20110313-alt1.svn2399

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2363
- version update to 20110313-alt1.svn2363

* Sat Apr 9 2011 Andrew Clark <andyc@altlinux.org> 20110313-alt1.svn2350
- initial build for ALT.

