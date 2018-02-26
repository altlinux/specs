Name:		xmms-skin-winamp5
Version:	20040802
Release:	alt2
Summary:	Winamp 5 skin for XMMS
License:	GPL
Group:		Sound

BuildPreReq:	rpm-build-wlskins
Requires:	winamplike-skins
BuildArch:	noarch

Url:		http://www.gnome-look.org/content/show.php?content=14870
Source0:	14870-Winamp5-XMMS.tar.bz2

Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
Skin for XMMS based on default Winamp 5 ("Modern") skin.

%description -l ru_RU.CP1251
Скин для XMMS, основанный на стандартном "Modern" скине Winamp 5.

%install
%__install -pD -m644 %SOURCE0 %buildroot%_wlskindir/Winamp5.tar.bz2

%files
%_wlskindir/*

%changelog
* Mon Dec 08 2008 Motsyo Gennadi <drool@altlinux.ru> 20040802-alt2
- rebuild with winamplike-skins

* Mon Aug 09 2004 Andrey Rahmatullin <wrar@altlinux.ru> 20040802-alt1
- initial build
