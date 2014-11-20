Name: darkplaces
Version: rev20141016
Release: alt1

Summary: Quake engine
License: GPL
Group: Games/Arcade
Url: http://icculus.org/twilight/darkplaces

Packager: %packager
Source: %name-%version.tar
Source1: README.maintainer

# Automatically added by buildreq on Thu Nov 20 2014
BuildRequires: libSDL-devel libXext-devel libXpm-devel libXxf86vm-devel libalsa-devel libjpeg-devel zlib-devel

%description
An engine for iD software's Quake.

%description -l ru_RU.UTF-8
darkplaces - современный движок для игры Quake.

%prep
%setup -q

%build
%make release

%install
mkdir -p %buildroot/%_bindir/
install -pm755 darkplaces-glx %buildroot/%_bindir/
install -pm755 darkplaces-sdl %buildroot/%_bindir/
install -pm755 darkplaces-dedicated %buildroot/%_bindir/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

install -pm644 COPYING %buildroot%docdir/
install -pm644 darkplaces.txt %buildroot%docdir/

install -pm644 %SOURCE1 %buildroot%docdir/

%files
%_bindir/darkplaces-glx
%_bindir/darkplaces-sdl
%_bindir/darkplaces-dedicated
%dir %docdir
%docdir/COPYING
%docdir/darkplaces.txt
%docdir/README.maintainer

%changelog
* Thu Nov 20 2014 Andrey Bergman <vkni@altlinux.org> rev20141016-alt1
- Initial release for Sisyphus.

