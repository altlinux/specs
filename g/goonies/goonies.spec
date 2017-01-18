Name:		goonies
Version:	1.4.1528
Release:	alt2
Summary:	20th anniversary edition of The Goonies remake
Group:		Games/Arcade
URL:		http://goonies.jorito.net/
License:	GPL
# goonies.src_1.4.1528.tgz
Source:		%name.src_%{version}.tgz
Patch:		goonies-1.4.1528-DSO.patch
Requires: %name-data = %version-%release

# Automatically added by buildreq on Mon Mar 04 2013
# optimized out: libGL-devel libGLU-devel libSDL-devel libstdc++-devel
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel

%description
The 20th anniversary edition of The Goonies is available for Windows,
Mac OS X and Linux computers. We provide binary versions for Windows,
OSX and Ubuntu. For other Linux distributions or other computers you can
download the source code.

%package data
Summary: Data files for %name, %summary
BuildArch: noarch
Group: Games/Arcade
%description data
Data files for %name

%prep
%setup
%patch -p1

cat > %name.sh <<@@@
#!/bin/sh
cd %_gamesdatadir/%name
exec ./%name "$@"
@@@

%build
%make_build BINDIR=%_gamesdatadir/%name

%install
mkdir -p %buildroot%_gamesdatadir/%name
%makeinstall PREFIX=%buildroot%_prefix BINDIR=%buildroot%_gamesdatadir/%name
mv %buildroot%_gamesdatadir/%name/%name %buildroot%_gamesbindir/%name.bin
install %name.sh %buildroot%_gamesbindir/%name
ln -s %_gamesbindir/%name.bin %buildroot%_gamesdatadir/%name/%name

%files
%_gamesbindir/*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_gamesdatadir/%name/%name

%files data
%_gamesdatadir/%name/*
%exclude %_gamesdatadir/%name/%name

%changelog
* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 1.4.1528-alt2
- GCC6 fix

* Mon Mar 04 2013 Fr. Br. George <george@altlinux.ru> 1.4.1528-alt1
- Initial build from scratch

