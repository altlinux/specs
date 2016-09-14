Name: slim
Version: 1.3.6
Release: alt2

Summary: SLiM is a graphical, desktop-independent login manager for X11.

License: GPLv2
Group: System/X11
Url: http://sourceforge.net/projects/slim.berlios/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name-%version.tar.gz
Source1: %name.init
Source2: %name.pam
Patch1: CMakeLists.txt.patch
Patch2: slim-add-sessiondir.patch
Patch3: slim_conf.patch

BuildPreReq: cmake rpm-macros-cmake gcc-c++
# Automatically added by buildreq on Tue Feb 02 2016
# optimized out: cmake-modules fontconfig fontconfig-devel libICE-devel libSM-devel libX11-devel libXau-devel libXrender-devel libXt-devel libfreetype-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake gcc-c++ libXext-devel libXft-devel libXmu-devel libXrandr-devel libjpeg-devel libpam-devel libpng-devel libsystemd-devel

%description
SLiM (Simple Login Manager) is a graphical, desktop-independent login
manager for X11.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p2

%build
%cmake_insource -DUSE_PAM=yes \
	-DBUILD_SHARED_LIBS=no
%make_build

%install
%makeinstall_std
mkdir -p -- %buildroot%_initdir
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name
install -D -m 0755 -- %SOURCE2 %buildroot%_sysconfdir/pam.d/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%dir %_datadir/%name/
%_datadir/%name/*
%_man1dir/*
%_unitdir/*
%config %_sysconfdir/%name.conf
%config %_sysconfdir/pam.d/%name
%config %_initdir/%name

%changelog
* Wed Sep 14 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt2
- add slim-add-sessiondir.patch (Debian #740394)
- fix slim.conf (closes: #32389)

* Mon Apr 18 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt1
- initial build
