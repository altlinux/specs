Name:		fontmatrix
Version:	0.6.0
Release:	alt1.1.2.1
Summary:	Is a font manager for Linux users
Summary(ru_RU.UTF8): Менеджер шрифтов для пользователей Linux
Url:		http://www.fontmatrix.net/
Source0:	http://www.fontmatrix.net/archives/%name-%version-Source.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Publishing
License:	GPLv2
Patch0:		%name-0.6.0-desktopmenu.diff

# Automatically added by buildreq on Sun Jan 13 2008 (-bi)
BuildRequires: cmake gcc-c++ ImageMagick libqt4-devel libSM-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel

%description
Fontmatrix  is  a  font  manager  for  Linux users. I repeat, for
users. It aims to be more features rich than well  designed.  I.d
say  it.s  much  more  an open minded than an open source or free
software project . also it.s GPL.d . in the way it is,  and  will
be, led by its users.

%description -l ru_RU.UTF8
Fontmatrix - это менеджер шрифтов (программа для управления шрифтами)
для пользователей Linux. Да, именно для пользователей. В менеджере шрифтов
Fontmatrix упор сделан на функциональность, а не на детальную проработанность.
Правильнее будет сказать, что Fontmatrix гораздо более восприимчив к новшествам,
чем просто проект с открытым исходным кодом или свободный проект. Кроме того,
Fontmatrix выпускается под лицензией GPL. В некотором смысле, развитие Fontmatrix
происходит и будет происходить далее под влиянием его пользователей.

%prep
%setup -q -n %name-%version-Source
%patch0 -p1

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_SKIP_RPATH=YES \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags"
%make_build VERBOSE=1

%install
%make DESTDIR=%buildroot install

# icons
rm -rf %buildroot%_liconsdir/%name.png
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir}
convert -resize 48x48 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/%name
%doc INSTALL TODO
%_bindir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop
%_man1dir/%name.*
%_datadir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1.1.2.1
- Rebuild with Python-2.7

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1.2
- Rebult for debuginfo

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1.1
- Rebuilt with python 2.6

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1.1
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1
- 0.6.0 version
- added russian description and summary (fixed #22073). Thanks to Phantom.

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.4.2-alt2
- delete post/postun scripts (new rpm)

* Sat Jun 21 2008 Motsyo Gennadi <drool@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Tue Feb 12 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Sun Jan 13 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt1
- 0.3.0 release
- use cmake
- exclude COPYING from packaging
- refresh buildrequires with buildreq -bi

* Wed Nov 28 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1.svn
- initial build for ALT Linux (thanks to Mike Shigorin for URL)
