Name:		gravit
Version:	0.5.0
Release:	alt1.1
Group:		Games/Educational
Summary:	Visually stunning gravity simulator
URL:		http://gravit.slowchop.com
Source:		%name-%version.tgz
License:	GPLv2+

# Automatically added by buildreq on Wed Sep 25 2013
# optimized out: libGL-devel libGLU-devel libICE-devel libSDL-devel libX11-devel pkg-config xorg-xproto-devel
BuildRequires: libSDL_image-devel libSDL_ttf-devel libSM-devel lua-devel libpng-devel

BuildRequires:	autoconf-archive rpm-macros-fonts

%description
Gravit is a free, visually stunning gravity simulator, where you can
spend endless time experimenting with various configurations of
simulated universes.

%prep
%setup
touch NEWS AUTHORS
sed -i '/AX_EXT_SSE/d' configure.in

%build
%autoreconf
%configure --disable-silent-rules
%ifarch x86_64
%make_build CPPFLAGS+=-DHAVE_SSE
%else
%make_build
%endif

%install
%makeinstall_std
ln -sf %_ttffontsdir/TrueType-vera/Vera.ttf %buildroot%_datadir/%name/data/Vera.ttf

%files
%doc README
%_bindir/*
%_sysconfdir/%name
%_datadir/%name

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1.1
- rebuild with new lua 5.3

* Mon Sep 23 2013 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Initial build for ALT

