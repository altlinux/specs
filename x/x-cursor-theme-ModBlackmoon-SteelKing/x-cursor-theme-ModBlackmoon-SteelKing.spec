%define		themename ModBlackmoon-SteelKing

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	%themename cursors for Xorg
License:	GPLv2+
Group:		System/X11
Url:		http://xfce-look.org/content/show.php/ModBlackmoon-SteelKing?content=106338
Source:		106338-ModBlackmoon-SteelKing.tar.gz

BuildArch:	noarch

%description
%themename X11 Mouse Theme
MB-SteelKing X11 Mouse theme converted from original theme
By ModBlackmoon http://users.wincustomize.com/2501323/

%prep
%setup -q -n %themename

%install
%__install -d %buildroot%_iconsdir/%themename
cp -a ./* %buildroot%_iconsdir/%themename/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%changelog
* Wed Aug 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
