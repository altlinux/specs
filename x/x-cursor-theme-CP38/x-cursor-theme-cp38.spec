%define		appsnum 88325
%define		themename CP38

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	CP38 cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/%{themename}?content=%appsnum
Source:		%appsnum-%themename.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains CP38 cursors for Xorg.
Original work of pinchecl

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
