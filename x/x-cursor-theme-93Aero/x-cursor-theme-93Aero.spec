%define		appsnum 73200
%define		themename 93Aero

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/9+3+Aero?content=%appsnum
Source:		%appsnum-%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains %themename cursors for Xorg.
Original author: Night Train on Tuesday, September 04, 2007
Homepage: http://users.wincustomize.com/686510/
Source: http://www.wincustomize.com/skins.aspx?skinid=2244&libid=25
Comment from the author: " A simple Cursor XP theme to match my 9 3 Aero
windowblinds skin. Best used at 75% if you like em tiny."

All rights reserved by the respective owners

%prep
%setup -q -c -n %themename

%install
%__install -d %buildroot%_iconsdir/
%__cp -a %themename/ %buildroot%_iconsdir/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%changelog
* Fri Oct 10 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
