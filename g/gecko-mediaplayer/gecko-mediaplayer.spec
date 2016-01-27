%define plugdir  %_libdir/browser-plugins

Summary:	Gecko Media Player browser plugin
Summary(ru_RU.UTF-8): Дополнение для браузера - Gecko Media Player
Name:		gecko-mediaplayer
Version:	1.0.9
Release:	alt3
License:	GPLv2+
Group:		Networking/WWW
URL:		http://kdekorte.googlepages.com/gecko-mediaplayer
Packager:	Radik Usupov <radik@altlinux.org>

Source0:	http://gecko-mediaplayer.googlecode.com/files/%{name}-%{version}.tar.gz
Patch: 		Add-ru-and-tt-translations.patch
Patch1: 	0001-nomozalloc.patch
Patch2:		np_loadds.patch

BuildPreReq:    GConf rpm-build-gnome rpm-build-firefox libdbus-devel
BuildRequires: 	gcc-c++ libGConf-devel libX11-devel libdbus-glib-devel libgio-devel xulrunner-devel libgmlib-devel
Requires:      	gnome-mplayer >= 0.9.6 browser-plugins-npapi

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to play media in a browser.
It should work with all browsers on Unix-ish systems(Linux, BSD, Solaris) 
and use the NS4 API (Mozilla, Firefox, Opera, etc.).

%description -l ru_RU.UTF-8
Дополнение для браузера 'Gecko Media Player' позволяет с помощью видеопроигрывателя
GNOME Mplayer показывать видео прямо в окне интернет проводников. Дополнение должно работать в Opera, SeaMonkey и других интернет проводниках.

%prep
%setup
%patch -p2
%patch1 -p1
%patch2 -p1

%build
%add_optflags -std=c++11
%autoreconf
%configure
%make

%install
%makeinstall_std
mkdir %buildroot%plugdir
mv %buildroot%_libdir/mozilla/plugins/* %buildroot%plugdir

%find_lang %name

# Removed files
rm -rf %buildroot%_docdir/%name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README DOCS/tech/javascript.txt
%plugdir/*

%changelog
* Wed Jan 27 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt3
- Remove watch file

* Sun Apr 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt2
- Fix build in Sisyphus (thanks Debian for patches)

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt1
- New version

* Thu Mar 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.8-alt1
- New version

* Wed Nov 07 2012 Radik Usupov <radik@altlinux.org> 1.0.7-alt1
- New version (1.0.7) (Closes: 27926)
- Added russian and tatar translation (tnx Ainur Shakirov)
- Small cleaned spec

* Mon Nov 28 2011 Radik Usupov <radik@altlinux.org> 1.0.4-alt2
- Fixed build with ff8

* Tue Aug 09 2011 Radik Usupov <radik@altlinux.org> 1.0.4-alt1
- New version (1.0.4)
- Fixed build 

* Wed Apr 27 2011 Radik Usupov <radik@altlinux.org> 1.0.3-alt1
- New version (1.0.3)
- Fixed build

* Sat Feb 19 2011 Radik Usupov <radik@altlinux.org> 1.0.0-alt1
- New version (1.0.0) (Closes: 25120)
    + Fix problem with javascript seek function where value was coming in as an int where unexpected
    + Change libxul 2.0 check from 2.0b5 to just 2.0
    + Fix incorrect variable
    + Apply patch from Onur Kucuk to allow gecko-mediaplayer to compile against 
    + xulrunner 2.0beta5 and higher
    + Fully qualify streaming URLs loaded from the embed tag
    + Obtain the plugin caller page and use that to resolve streaming urls
    + Fix problem where first item on list is not playable
    + Support qtsrcdontusebrowser option
    + Updated Spanish translation
    + Add WEBM types to plugin
    + Handle nocache=1 better
    + Mark asx files with ENTRY in them as non-playable
    + Allow separate cache sizes for audio or video data, depends on mimetype identification
    + Protect against NULL console
    + Added German translation
    + Move "stream" test to streaming function, change from int to boolean
    + If url has "stream" in it, mark the url as streaming
    + Give each item in the RAM playlist a unique id
- Drop gecko-mediaplayer-as-needed.patch
- Changed packager
- Changed license
- Changed summary(ru) and description(ru)

* Thu Oct 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.8-alt2
- Changes for browsers-plugins-npapi package were taken into account.

* Sun Sep 27 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.8-alt1
- First build for Sisyphus.

