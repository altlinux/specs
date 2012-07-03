%define		appsnum 109907
%define		themename TheCandyman02

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	Artistic v2.0
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/TheCandyman+with+changed+animations?content=%appsnum
Source:		%{themename}tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
%themename X11 Mouse Theme
The Candyman For CursorXP Javier Aroche

the original version of CurXPTheme, can you see here:
http://www.wincustomize.com/skins.aspx?skinid=2227&libid=25

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
* Sun Jan 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
