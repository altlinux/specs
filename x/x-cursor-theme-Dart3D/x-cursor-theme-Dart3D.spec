%define		appsnum 88322
%define		themename Dart3D

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/%themename?content=%appsnum
Source:		%appsnum-%{themename}_LHPPL.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
This package contains %themename cursors for Xorg.
Original work of lihu1267

%prep
%setup -q -n %{themename}_LHPPL

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
