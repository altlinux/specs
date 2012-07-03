%define		appsnum 117799
%define		themename X-Alien2

Name:		x-cursor-theme-%themename
Version:	0.0.1
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://kde-look.org/content/show.php/X-Alien2?content=%appsnum
Source0:	117799-%themename.tar.gz
Source1:	%themename-DARK.tar.gz
Source2:	%themename-GREY.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
%themename X11 Mouse Theme
Original theme By JJ Ying http://users.wincustomize.com/691873/

%package -n x-cursor-theme-%themename-DARK
Summary: %themename-DARK cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-DARK
%themename-DARK X11 Mouse Theme
Original theme By JJ Ying http://users.wincustomize.com/691873/

%package -n x-cursor-theme-%themename-GREY
Summary: %themename-GREY cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-GREY
%themename-GREY X11 Mouse Theme
Original theme By JJ Ying http://users.wincustomize.com/691873/

%prep
%setup -q -n %themename
tar -xf %SOURCE1
tar -xf %SOURCE2


%install
%__install -d %buildroot%_iconsdir/%themename
mv %themename-DARK %buildroot%_iconsdir/
mv %themename-GREY %buildroot%_iconsdir/
%__cp -a ./* %buildroot%_iconsdir/%themename/

%files
%dir %_iconsdir/%themename
%dir %_iconsdir/%themename/cursors
%_iconsdir/%themename/index.theme
%_iconsdir/%themename/cursors/*

%files -n x-cursor-theme-%themename-DARK
%dir %_iconsdir/%themename-DARK
%dir %_iconsdir/%themename-DARK/cursors
%_iconsdir/%themename-DARK/index.theme
%_iconsdir/%themename-DARK/cursors/*

%files -n x-cursor-theme-%themename-GREY
%dir %_iconsdir/%themename-GREY
%dir %_iconsdir/%themename-GREY/cursors
%_iconsdir/%themename-GREY/index.theme
%_iconsdir/%themename-GREY/cursors/*

%changelog
* Sun Jan 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux
