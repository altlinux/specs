%define rev svn2865
Name: fheroes2
Version: 20120301
Release: alt1.%rev
Summary: Free implementation of Heroes of the Might and Magic II engine
License: GPL
Group: Games/Strategy
Url: http://sourceforge.net/projects/fheroes2/
Packager: Andrew Clark <andyc@altlinux.org>

Source: http://sourceforge.net/projects/fheroes2/files/fheroes2/%name-%version.tar.gz
Source2: %name.sh
Source3: %name.png
Source4: %name.desktop
Source5: %name.cfg

# Automatically added by buildreq on Sun Aug 07 2011
# optimized out: libSDL-devel libstdc++-devel pkg-config zlib-devel
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libfreetype-devel libpng-devel

%description
Free implementation of Heroes of the Might and Magic II engine.
You need to copy files from data and maps directories from original game
into your /usr/share/games/fheroes2/{maps,data} directories respectively

%prep
%setup -n %name

%build
%make_build WITH_AI=simple CONFIGURE_FHEROES2_DATA="%_gamesdatadir/%name/" 

%install
# let's create directory structure...
mkdir -p %buildroot{%_bindir,%_niconsdir,%_desktopdir,%_docdir/%name,%_gamesdatadir/%name/{data,maps}}

# and install what we need where we need it to be...
install -pm755 %name %buildroot%_bindir/%name.bin
install -pm755 %SOURCE2 %buildroot%_bindir/%name
mv files/ %buildroot%_gamesdatadir/%name/
install -pm 644 %name.cfg %buildroot%_gamesdatadir/%name/
install -pm 644 %name.key %buildroot%_gamesdatadir/%name/
install -pm 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pm 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -pm 644 %SOURCE5 %buildroot%_gamesdatadir/%name/
install -pm 644 {AUTHORS,changelog.txt,COPYING,LICENSE,README} %buildroot%_docdir/%name/

%files
%_bindir/*
%_niconsdir/%name.png
%_desktopdir/%name.desktop
%_docdir/%name
%_gamesdatadir/%name


%changelog
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

