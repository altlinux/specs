Name: vacuumvideoscript 
Version: 0.19
Release: alt1

Summary: Download videos from RuTube, vkontakte, and lots of other sites.
License: GPL2+
Group: Networking/File transfer
Url: http://saahriktu.org/utils.php

Source0: %{name}-%{version}.tar.xz
Source1: %name.watch

Packager: Igor Vlasenko <viy@altlinux.org>

BuildArch: noarch

%description
Vacuumvideoscript is a small command-line program to download videos
from various video sites. Usage: vacuumvideoscript url_of_webpage_with_video

supported video sites:
* blip.tv
* www.clipjunkie.com
* www.funnyhub.com
* www.liveleak.com
* www.metacafe.com
* www.nothingtoxic.com
* stupidvideos.us
* vbox7.com
* video.bigmir.net
* video.online.ua
* video.privet.ru
* video.proext.com
* video.sibnet.ru
* play.ukr.net
* youtube.com
* clips.rofl.to
* www.dukaramba.com
* akilli.tv
* www.mastitube.com
* vkontakte.ru
* spikedhumor.com
* www.220.ro
* snotr.ru
* www.myvideo.ge
* www.tubeit.se
* www.zkouknito.cz
* filmiki.jeden.com
* kontraband.com
* theync.com
* vidmax.com
* dailymotion.com
* liveinternet.ru
* rutube.ru

Usage for vkontakte.ru:
vacuumvideoscript http://vkontakte.ru/... login password

%prep
%setup

%install
install -D -pm 755 %name %buildroot%_bindir/%name

%files
%doc Changelog Readme
%_bindir/%name

%changelog
* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- new version (watch file uupdate)

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.2-alt1
- new version

* Wed Jul 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- first release for Sisyphus

