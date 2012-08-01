%define		themename BW3D

Name:		x-cursor-theme-%themename
Version:	0.1
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	%themename cursors for Xorg
License:	GPLv2+
Group:		System/X11
Url:		http://xfce-look.org/content/show.php/BW3D?content=105097
Source:		bw3d_by_grynays-d2y80i8.zip

BuildArch:	noarch

BuildRequires:	unzip

%description
%themename X11 Mouse Theme
BW3D X11 Mouse theme converted from original theme
By lihu1266 http://lihu1266.wincustomize.com/

%prep
%setup -q -c
%__install -d %buildroot%_iconsdir
tar xvfz %themename.tar.gz -C %buildroot%_iconsdir/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%changelog
* Wed Aug 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
