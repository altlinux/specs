Version:	0.3
Name:		qmmp-skins
Release:	alt3
Summary:	Collection skins for QMMP
License: 	Distributable
Group: 		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>

Source0:	73.wsz
Source1:	Almond_alu_rounded.wsz
Source2:	Almond_alu.wsz
Source3:	Almond_copper_rounded.wsz
Source4:	Almond_copper.wsz
Source5:	Almond_darkblue_rounded.zip
Source6:	Almond-dark-blue.zip
Source7:	Almond-dark-orange.wsz
Source8:	Almond_steel_rounded.wsz
Source9:	Almond_steel.wsz
Source10:	Antares_1a.wsz
Source11:	AntiMatter_UD.wsz
Source12:	Atlantida_2.wsz
Source13:	bunjee_blue.wsz
Source14:	bunjee_grey.wsz
Source15:	bunjee_orange.wsz
Source16:	BWD_MediaTower-V2.wsz
Source17:	ColderXMMS.tar.gz
Source18:	Cramers_Sony_Discman.wsz
Source19:	detone_blue.zip
Source20:	detone_green.zip
Source21:	Digitanium3.wsz
Source22:	Kore.zip
Source23:	mmii-2002.wsz
Source24:	Vortigo-Clear-final-green.zip
Source25:	Vortigo-Clear.wsz
Source26:	Vortigo.wsz
Source27:	WinAmp_Longhorn_Inspiriat.wsz
Source28:	wmp11.zip
Source29:	wmp.zip


BuildArch:	noarch
Requires:	winamplike-skins

BuildRequires:	rpm-build-wlskins

Conflicts:	qmmp < 0.2.3-alt1.M40.1

%description
Collection skins for QMMP audio-player:

73
Almond_alu_rounded
Almond_alu
Almond_copper_rounded
Almond_copper
Almond_darkblue_rounded
Almond-dark-blue
Almond-dark-orange
Almond_steel_rounded
Almond_steel
Antares_1a
AntiMatter_UD
Atlantida_2
bunjee_blue
bunjee_grey
bunjee_orange
BWD_MediaTower-V2
ColderXMMS
Cramers_Sony_Discman
detone_blue
detone_green
Digitanium3
Kore
mmii-2002
Vortigo-Clear-final-green
Vortigo-Clear
Vortigo
WinAmp_Longhorn_Inspiriat
wmp11
wmp

%install
%__mkdir -p %buildroot%_wlskindir
cp %SOURCE0 %buildroot%_wlskindir/
cp %SOURCE1 %buildroot%_wlskindir/
cp %SOURCE2 %buildroot%_wlskindir/
cp %SOURCE3 %buildroot%_wlskindir/
cp %SOURCE4 %buildroot%_wlskindir/
cp %SOURCE5 %buildroot%_wlskindir/
cp %SOURCE6 %buildroot%_wlskindir/
cp %SOURCE7 %buildroot%_wlskindir/
cp %SOURCE8 %buildroot%_wlskindir/
cp %SOURCE9 %buildroot%_wlskindir/
cp %SOURCE10 %buildroot%_wlskindir/
cp %SOURCE11 %buildroot%_wlskindir/
cp %SOURCE12 %buildroot%_wlskindir/
cp %SOURCE13 %buildroot%_wlskindir/
cp %SOURCE14 %buildroot%_wlskindir/
cp %SOURCE15 %buildroot%_wlskindir/
cp %SOURCE16 %buildroot%_wlskindir/
cp %SOURCE17 %buildroot%_wlskindir/
cp %SOURCE18 %buildroot%_wlskindir/
cp %SOURCE19 %buildroot%_wlskindir/
cp %SOURCE20 %buildroot%_wlskindir/
cp %SOURCE21 %buildroot%_wlskindir/
cp %SOURCE22 %buildroot%_wlskindir/
cp %SOURCE23 %buildroot%_wlskindir/
cp %SOURCE24 %buildroot%_wlskindir/
cp %SOURCE25 %buildroot%_wlskindir/
cp %SOURCE26 %buildroot%_wlskindir/
cp %SOURCE27 %buildroot%_wlskindir/
cp %SOURCE28 %buildroot%_wlskindir/
cp %SOURCE29 %buildroot%_wlskindir/

%files
%_wlskindir/*

%changelog
* Wed Dec 10 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt3
- remove Winamp5 skin (provides in xmms-skin-winamp5)
- remove qmmp from Requires (for winamp like skins players)
- add conflict with qmmp < 0.2.3-alt1.M40.1

* Sun Dec 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt2
- rebuild with winamplike-skins

* Sun May 04 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1
- change license from GPL to Distributable
- add 73 skin
- add AntiMatter_UD skin
- add BWD_MediaTower-V2 skin
- add Cramers_Sony_Discman skin
- add detone_blue skin
- add detone_green skin
- add mmii-2002 skin
- add Antares_1a skin
- add Atlantida_2 skin
- add ColderXMMS skin
- add Digitanium3 skin
- add wmp skin

* Sun Mar 09 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt2
- fix Summary 's/skisn/skins/' (thanks to Slava Semushin for report)

* Sat Mar 08 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1
- add Winamp5 skin
- add Vortigo skin
- add Vortigo-Clear skin
- add Vortigo-Clear-final-green skin
- add bunjee_blue skin
- add bunjee_grey skin
- add bunjee_orange skin
- add WinAmp_Longhorn_Inspiriat skin
- add wmp11 skin

* Fri Jan 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial packing
