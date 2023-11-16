Name:		fontmatrix
Version:	0.9.100
Release:	alt2
Summary:	Is a font manager for Linux users
Summary(ru_RU.UTF8): Менеджер шрифтов для пользователей Linux
Url:		https://github.com/fontmatrix/fontmatrix
Source0:	%name-%version.tar.gz
Group:		Publishing
License:	GPLv2
Patch0:		%name-0.6.0-desktopmenu.diff
Patch1:		bug_564904_fix-missing-DSO-icuuc.diff
Patch2:		%name-0.9.99-arm.diff
Patch3:     %name-g++8.patch

BuildRequires: cmake fontconfig-devel qt5-base-devel qt5-tools-devel qt5-svg-devel qt5-webkit-devel
BuildRequires: ImageMagick-tools

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
%setup -q
%patch0 -p1
%patch1 -p0
#patch2 -p0
#patch3 -p2

%build
cmake . \
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
* Thu Nov 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.9.100-alt2
- NMU: trimmed build dependencies according to CMakeLists.txt. Note that
  the dependencies of binary packages have not changed.
  Fixes FTBFS on LoongArch.

* Thu Jun 24 2021 Fr. Br. George <george@altlinux.ru> 0.9.100-alt1
- Switch upstream
- Update to 0.9.100

* Wed Feb 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.99-alt2
- no return statement in the non-void function fixed (according g++8)

* Mon Dec 09 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.99-alt1
- 0.9.99
- add patches NN 1 & 2 from FC

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
