# TODO: it is better use wineg++ for compile, it more fresh

Name: pipelight
Version: 0.2.5.9
Release: alt1

Summary: A browser plugin which allows to use windows plugins inside Linux browsers

License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Networking/WWW
Url: https://launchpad.net/pipelight

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-git: git://fds-team.de/pipelight.git
Source: %name-%version.tar

# wine binary exe.so with exe extension placed in /usr/share
%set_verify_elf_method fhs=relaxed

BuildPreReq: rpm-build-browser-plugins

# manually removed: mariadb-server 
# Automatically added by buildreq on Sat Apr 05 2014
# optimized out: libstdc++-devel mariadb-client mariadb-common mingw32-binutils mingw32-gcc mingw32-runtime mingw32-w32api xorg-xproto-devel
BuildRequires: gcc-c++ libX11-devel mingw32-gcc-c++

%description
Pipelight is a special browser plugin which allows one to use windows only plugins inside Linux browsers.
We are currently focusing on Silverlight, Flash, Shockwave and the Unity Webplayer.
The project needs a patched version of Wine to execute the Silverlight DLL.

%prep
%setup

%build
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--wine-path=%_bindir/wine \
	--moz-plugin-path=%browser_plugins_path
%make_build

%install
%makeinstall_std

%files
%_bindir/pipelight-plugin
%dir %_datadir/%name/
%_datadir/%name/sig-install-dependency.gpg
%_datadir/%name/pluginloader*.exe
%_datadir/%name/install-dependency
%_datadir/%name/hw-accel-default
%_datadir/%name/scripts/
%_datadir/%name/configs/
%_datadir/%name/licenses/
%_libdir/%name/libpipelight.so
%_man1dir/*

%changelog
* Sat Apr 05 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2.5.9-alt1
- initial build for ALT Linux Sisyphus
