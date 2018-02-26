%define		appsnum 83194
%define		themename Vienna3

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/Vienna+3?content=%appsnum
Source:		%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains %themename cursors for Xorg.
J. Aroche's Vienna3 for CursorXP, converted to an X11 cursor.
Javier has agreed on providing me with a ubuntu logo animation
for the 'AppStarting' animation, previously had a Windows logo.
Some animations have been changed to ones that don't cause
glitches on the desktop when compiz-fusion is enabled, and the
"hand" image has been replaced with a much more interesting
animation from J.Aroche.

Link to Original for CursorXP: 
http://www.wincustomize.com/skins.aspx?skinid=2412&libid=25

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
