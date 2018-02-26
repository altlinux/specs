%define		appsnum 72514
%define		themename Gold2

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/Gold+2?content=%appsnum
Source:		%appsnum-%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains %themename cursors for Xorg.
Original author: Renzo Riccio
Homepage: http://users.wincustomize.com/165733/
Source: http://www.wincustomize.com/skins.aspx?skinid=3&libid=25

All rights reserverd by the respective owners.

%prep
%setup -q -n %themename

%install
%__install -d %buildroot%_iconsdir/%themename
%__cp -a ./* %buildroot%_iconsdir/%themename/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%changelog
* Fri Oct 10 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
