%define		appsnum 105586
%define		themename Protozoa

Name:		x-cursor-theme-%themename
Version:	20120114
Release:	alt1
Summary:	%themename cursors for Xorg
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPL
Group:		System/X11
BuildArch:	noarch
Url:		http://xfce-look.org/content/show.php/Protozoa?content=%appsnum
Source0:	%themename.tar.gz
Source1:	%themename-Blu.tar.gz
Source2:	%themename-grey.tar.gz
Source3:	%themename-red.tar.gz

Patch0:		Protozoa_alt_names.diff

%description
%themename X11 Mouse Theme
Original theme By Chuckeye http://users.wincustomize.com/2811415/

Bacterial jellyfish, infectious ectoplasmic and all animated.

%package -n x-cursor-theme-%themename-Green
Summary: %themename-Green cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-Green
%themename-Green X11 Mouse Theme
Original theme By Chuckeye http://users.wincustomize.com/2811415/

Bacterial jellyfish, infectious ectoplasmic and all animated.

%package -n x-cursor-theme-%themename-Blue
Summary: %themename-Blue cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-Blue
%themename-Blue X11 Mouse Theme
Original theme By Chuckeye http://users.wincustomize.com/2811415/

Bacterial jellyfish, infectious ectoplasmic and all animated.

%package -n x-cursor-theme-%themename-Red
Summary: %themename-Red cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-Red
%themename-Red X11 Mouse Theme
Original theme By Chuckeye http://users.wincustomize.com/2811415/

Bacterial jellyfish, infectious ectoplasmic and all animated.

%package -n x-cursor-theme-%themename-Grey
Summary: %themename-Grey cursors for Xorg
Group:		System/X11

%description -n x-cursor-theme-%themename-Grey
%themename-Grey X11 Mouse Theme
Original theme By Chuckeye http://users.wincustomize.com/2811415/

Bacterial jellyfish, infectious ectoplasmic and all animated.

%prep
%setup -c -n %themename
tar -xf %SOURCE1
tar -xf %SOURCE2
tar -xf %SOURCE3
%patch0 -p1


%install
mkdir -p %buildroot%_iconsdir
cp -a ./%themename %buildroot%_iconsdir/%themename-Green
cp -a ./%themename-Blu %buildroot%_iconsdir/%themename-Blue
cp -a ./%themename-grey %buildroot%_iconsdir/%themename-Grey
cp -a ./%themename-red %buildroot%_iconsdir/%themename-Red

%files -n x-cursor-theme-%themename-Green
%dir %_iconsdir/%themename-Green
%dir %_iconsdir/%themename-Green/cursors
%_iconsdir/%themename-Green/*.*
%_iconsdir/%themename-Green/cursors/*

%files -n x-cursor-theme-%themename-Red
%dir %_iconsdir/%themename-Red
%dir %_iconsdir/%themename-Red/cursors
%_iconsdir/%themename-Red/*.*
%_iconsdir/%themename-Red/cursors/*

%files -n x-cursor-theme-%themename-Blue
%dir %_iconsdir/%themename-Blue
%dir %_iconsdir/%themename-Blue/cursors
%_iconsdir/%themename-Blue/*.*
%_iconsdir/%themename-Blue/cursors/*

%files -n x-cursor-theme-%themename-Grey
%dir %_iconsdir/%themename-Grey
%dir %_iconsdir/%themename-Grey/cursors
%_iconsdir/%themename-Grey/*.*
%_iconsdir/%themename-Grey/cursors/*

%changelog
* Mon Dec 23 2013 Motsyo Gennadi <drool@altlinux.ru> 20120114-alt1
- initial build for ALT Linux
