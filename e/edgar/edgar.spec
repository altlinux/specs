%define rel 1
Summary: 2D Platform Game
Name: edgar
Version: 1.26
Release: alt1
Source: %version.tar.gz
Url: http://www.parallelrealities.co.uk/p/legend-of-edgar.html
Group: Games/Arcade
License: GPL
Patch: %name-1.26-icons.patch
Requires: %name-data = %version

# Automatically added by buildreq on Sun Feb 28 2010
BuildRequires: libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel zlib-devel
BuildRequires: desktop-file-utils

%description
The Legend of Edgar. When his father fails to return home after venturing out
one stormy night, Edgar sets off on a quest to rescue him.

%package data
Group: Games/Arcade
License: GPL
BuildArch: noarch
Summary: The Legend of Edgar level set
Requires: %name = %version

%description data
The Legend of Edgar. When his father fails to return home after venturing
out one stormy night, Edgar sets off on a quest to rescue him.

This package contains official level set for Edgar.

%prep
%setup
%patch

%build
%make_build VERSION=%version RELEASE=%rel DATA_DIR=%_gamesdatadir/%name/ BIN_DIR=%_gamesbindir/ DOC_DIR=%_defaultdocdir/%name-%version ICON_DIR=%_iconsdir/hicolor/ DESKTOP_DIR=%_desktopdir LOCALE_DIR=%_datadir/locale/

%install
%makeinstall VERSION=%version RELEASE=%rel DATA_DIR=%buildroot%_gamesdatadir/%name/ BIN_DIR=%buildroot%_gamesbindir/ DOC_DIR=`pwd`/localdoc ICON_DIR=%buildroot%_iconsdir/hicolor/ DESKTOP_DIR=%buildroot%_desktopdir/ LOCALE_DIR=%buildroot%_datadir/locale/ PREFIX=%buildroot%prefix

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RolePlaying \
	%buildroot%_desktopdir/edgar.desktop

%find_lang %name

%files -f %name.lang
%doc localdoc
%_gamesbindir/*
%dir %_gamesdatadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_man6dir/*
%_datadir/appdata/edgar.appdata.xml

%files data
%_gamesdatadir/%name/*

%changelog
* Wed Mar 15 2017 Fr. Br. George <george@altlinux.ru> 1.26-alt1
- Autobuild version bump to 1.26

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 1.24-alt1
- Autobuild version bump to 1.24

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.20-alt1
- Autobuild version bump to 1.20

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 1.19-alt1
- Autobuild version bump to 1.19
- Fix patch

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 1.18-alt1
- Autobuild version bump to 1.18
- Desktop modification fixed

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.17-alt1
- Autobuild version bump to 1.17

* Tue May 27 2014 Fr. Br. George <george@altlinux.ru> 1.16-alt1
- Autobuild version bump to 1.16

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.15-alt1
- Autobuild version bump to 1.15

* Sun Jan 12 2014 Fr. Br. George <george@altlinux.ru> 1.14-alt1
- Autobuild version bump to 1.14

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 1.12-alt1
- Autobuild version bump to 1.12

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.11-alt1
- Autobuild version bump to 1.11

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 1.08-alt1
- Autobuild version bump to 1.08

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.07-alt1
- Autobuild version bump to 1.07

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.06-alt1
- Autobuild version bump to 1.06

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.05-alt1
- Autobuild version bump to 1.05

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 1.04-alt1
- Autobuild version bump to 1.04
- Fix patch

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 1.02-alt1
- Autobuild version bump to 1.02

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.01-alt1
- Autobuild version bump to 1.01

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 1.00-alt1
- Autobuild version bump to 1.00

* Mon Mar 26 2012 Fr. Br. George <george@altlinux.ru> 0.98-alt1
- Autobuild version bump to 0.98

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 0.97-alt1
- Autobuild version bump to 0.97

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 0.96-alt1
- Autobuild version bump to 0.96

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 0.92-alt1
- Autobuild version bump to 0.92

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 0.90-alt1
- Autobuild version bump to 0.90

* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 0.87-alt1
- Autobuild version bump to 0.87

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.82-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for edgar

* Mon Apr 11 2011 Fr. Br. George <george@altlinux.ru> 0.82-alt1
- Autobuild version bump to 0.82

* Thu Mar 31 2011 Fr. Br. George <george@altlinux.ru> 0.81-alt1
- Autobuild version bump to 0.81

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 0.77-alt1
- Autobuild version bump to 0.77

* Mon Jan 31 2011 Fr. Br. George <george@altlinux.ru> 0.76-alt1
- Autobuild version bump to 0.76

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 0.73-alt1
- Autobuild version bump to 0.73

* Wed Oct 06 2010 Fr. Br. George <george@altlinux.ru> 0.72-alt1
- Autobuild version bump to 0.72

* Sat Oct 02 2010 Fr. Br. George <george@altlinux.ru> 0.71-alt1
- Autobuild version bump to 0.71

* Fri Sep 17 2010 Fr. Br. George <george@altlinux.ru> 0.70-alt1
- Version up

* Thu Aug 19 2010 Fr. Br. George <george@altlinux.ru> 0.67-alt1
- Version up

* Thu Jul 29 2010 Fr. Br. George <george@altlinux.ru> 0.65-alt1
- Version up

* Thu Jun 24 2010 Fr. Br. George <george@altlinux.ru> 0.61-alt1
- Version up

* Sun Jun 13 2010 Fr. Br. George <george@altlinux.ru> 0.60-alt1
- Version up

* Mon May 24 2010 Fr. Br. George <george@altlinux.ru> 0.56-alt1
- Version up

* Wed May 12 2010 Fr. Br. George <george@altlinux.ru> 0.55-alt1
- Version up

* Sun Feb 28 2010 Fr. Br. George <george@altlinux.ru> 0.50-alt1
- Version up

* Thu Feb 04 2010 Fr. Br. George <george@altlinux.ru> 0.46-alt1
- Version up

* Mon Jan 04 2010 Fr. Br. George <george@altlinux.ru> 0.45-alt1
- Version up

* Thu Dec 31 2009 Fr. Br. George <george@altlinux.ru> 0.41-alt1
- Version up

* Thu Nov 26 2009 Fr. Br. George <george@altlinux.ru> 0.40-alt1
- Version up

* Thu Oct 08 2009 Fr. Br. George <george@altlinux.ru> 0.33-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 0.30-alt1
- Version up

* Sat Aug 22 2009 Fr. Br. George <george@altlinux.ru> 0.25-alt1
- Version up

* Sun Aug 02 2009 Fr. Br. George <george@altlinux.ru> 0.22-alt1
- Version up
- Strict -Werror handling patch

* Sun Jun 28 2009 Fr. Br. George <george@altlinux.ru> 0.11-alt1
- Version up

* Mon Jun 15 2009 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build from scratch

