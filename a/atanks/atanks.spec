Name: atanks
Version: 5.4
Release: alt1

Summary: Atomic Tanks - multi-player game similar to worms
License: GPL
Group: Games/Arcade

Url: http://atanks.sourceforge.net

Packager: Ilya Mashkin <oddity@altlinux.ru>


Source: %name-%version.tar.gz
Source1: atanks.desktop
Source2: %name.png
Patch: %name-gcc34-fix.patch

# Automatically added by buildreq on Mon Jan 17 2005 (-bi)
BuildRequires: gcc-c++ liballegro-devel libstdc++-devel desktop-file-utils

%description
This is Atomic Tanks, a multi-player game similar to worms which involves firing enormous
weapons to try and destroy the other tanks.

%prep
%setup -q -n %name-%version
#patch0 -p1
%__subst 's,-DDATA_DIR=\\\".\\\",-DDATA_DIR=\\\"%_gamesdatadir/%name\\\",' src/Makefile

%build
%__make

%install
%__mkdir_p %buildroot{%_gamesbindir,%_gamesdatadir/%name,%_gamesdatadir/%name/sound,%_gamesdatadir/%name/button,%_gamesdatadir/%name/missile,%_gamesdatadir/%name/title,%_gamesdatadir/%name/text,%_gamesdatadir/%name/tank,%_gamesdatadir/%name/misc,%_gamesdatadir/%name/stock,%_gamesdatadir/%name/tankgun}



%__install -p -m 755 atanks %buildroot%_gamesbindir/%name
%__install -p -m 644 *.dat %buildroot%_gamesdatadir/%name/
%__install -p -m 644 *.txt %buildroot%_gamesdatadir/%name/

%__install -p -m 644 button/*.bmp %buildroot%_gamesdatadir/%name/button/
%__install -p -m 644 sound/*.wav %buildroot%_gamesdatadir/%name/sound/

%__install -p -m 644 missile/*.bmp %buildroot%_gamesdatadir/%name/missile/
%__install -p -m 644 title/*.bmp %buildroot%_gamesdatadir/%name/title/
%__install -p -m 644 text/*.txt %buildroot%_gamesdatadir/%name/text/
%__install -p -m 644 tank/*.bmp %buildroot%_gamesdatadir/%name/tank/


%__install -p -m 644 misc/*.bmp %buildroot%_gamesdatadir/%name/misc/
%__install -p -m 644 stock/*.bmp %buildroot%_gamesdatadir/%name/stock/
%__install -p -m 644 tankgun/*.bmp %buildroot%_gamesdatadir/%name/tankgun/

%__mkdir -p %buildroot%_niconsdir
%__install -m 644 %SOURCE2 %buildroot%_niconsdir/

desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    %SOURCE1



%files
%doc README TODO Changelog
%_gamesbindir/*
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_gamesdatadir/%name/*/*
#_menudir/%name
%_niconsdir/%name.png
%_datadir/applications/*

%changelog
* Tue Apr 24 2012 Ilya Mashkin <oddity@altlinux.ru> 5.4-alt1
- 5.4

* Sat Feb 25 2012 Ilya Mashkin <oddity@altlinux.ru> 5.3-alt1
- 5.3

* Thu Oct 06 2011 Ilya Mashkin <oddity@altlinux.ru> 5.2-alt1
- 5.2

* Fri Aug 12 2011 Ilya Mashkin <oddity@altlinux.ru> 5.1-alt1
- 5.1

* Sat Jun 18 2011 Ilya Mashkin <oddity@altlinux.ru> 5.0-alt1
- 5.0

* Thu May 05 2011 Ilya Mashkin <oddity@altlinux.ru> 4.9-alt1
- 4.9

* Fri Mar 11 2011 Ilya Mashkin <oddity@altlinux.ru> 4.8-alt1
- 4.8

* Thu Sep 09 2010 Ilya Mashkin <oddity@altlinux.ru> 4.7-alt1
- 4.7

* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 4.6-alt1
- 4.6

* Fri Apr 16 2010 Ilya Mashkin <oddity@altlinux.ru> 4.5-alt1
- 4.5

* Sat Mar 06 2010 Ilya Mashkin <oddity@altlinux.ru> 4.4-alt1
- 4.4

* Sun Jan 24 2010 Ilya Mashkin <oddity@altlinux.ru> 4.3-alt1
- 4.3

* Thu Dec 17 2009 Ilya Mashkin <oddity@altlinux.ru> 4.2-alt1
- 4.2
- Packed games/%%name/* dirs (Closes: #22520)

* Fri Oct 30 2009 Ilya Mashkin <oddity@altlinux.ru> 4.1-alt1
- 4.1

* Wed Oct 07 2009 Ilya Mashkin <oddity@altlinux.ru> 4.0-alt1
- 4.0

* Wed Jul 29 2009 Ilya Mashkin <oddity@altlinux.ru> 3.8-alt1
- 3.8

* Tue Jun 16 2009 Ilya Mashkin <oddity@altlinux.ru> 3.6-alt1
- 3.6

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 3.2-alt2
- add desktop file
- remove unneeded post scripts

* Thu Oct 09 2008 Ilya Mashkin <oddity@altlinux.ru> 3.2-alt1
- 3.2

* Sat Sep 06 2008 Ilya Mashkin <oddity@altlinux.ru> 3.1-alt1
- 3.1

* Thu Jul 03 2008 Ilya Mashkin <oddity@altlinux.ru> 3.0-alt1
- 3.0

* Mon May 26 2008 Ilya Mashkin <oddity@altlinux.ru> 2.9-alt1
- 2.9

* Wed Mar 05 2008 Ilya Mashkin <oddity@altlinux.ru> 2.8-alt1
- 2.8

* Sat Dec 22 2007 Ilya Mashkin <oddity@altlinux.ru> 2.7-alt1
- New version 2.7

* Sun Sep 09 2007 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- New version 2.5

* Sat Apr 21 2007 Ilya Mashkin <oddity@altlinux.ru> 2.3-alt1
- New version 2.3

* Sun Mar 11 2007 Ilya Mashkin <oddity@altlinux.ru> 2.2-alt1
- New version 2.2

* Fri Feb 09 2007 Ilya Mashkin <oddity@altlinux.ru> 2.0-alt1
- Release 2.0 

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 2.0-alt0.1beta1
- New version 2.0 beta

* Mon Jan 17 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.0-alt2
- Fix build with gcc-3.4

* Mon Jul 12 2004 Vladimir Lettiev <crux@altlinux.ru> 1.1.0-alt1
- Initial release for Sisyphus

