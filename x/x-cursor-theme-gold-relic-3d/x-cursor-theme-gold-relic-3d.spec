%define		appsnum 109777
%define		themename gold-relic

Name:		x-cursor-theme-%themename-3d
Version:	0.0.1
Release:	alt1
Summary:	%themename-3d cursors for Xorg
License:	X11
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/Gold_Relic_3D?content=%appsnum
Source:		xcursor-theme-%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
Gold_Relic_3D X11 Mouse Theme

%prep
%setup -q -n Gold_relic

%install
%__install -d %buildroot%_iconsdir/%themename
%__cp -a ./* %buildroot%_iconsdir/%themename/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%changelog
* Sun Jan 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux
