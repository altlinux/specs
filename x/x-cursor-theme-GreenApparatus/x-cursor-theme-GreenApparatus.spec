%define		themename GreenApparatus

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	Green Apparatus cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/Green+Apparatus?content=72698
Source:		%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains %themename cursors for Xorg.
Original author: (2007) - J. Aroche
Homepage: http://users.wincustomize.com/1925806/
Source: http://www.wincustomize.com/skins.aspx?skinid=2315&libid=25

All rights reserved by respective owners.

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
