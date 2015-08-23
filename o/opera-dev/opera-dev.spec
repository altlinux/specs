%define		softver 33.0
%define		buildver 1963.0

Name:		opera-dev
Version:	%softver.%buildver
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	A fast and secure web browser and Internet suite
Group:		Networking/WWW
License:	Distributable
Vendor:		Opera Software ASA
Url:		http://www.opera.com/
Source0:	opera-%softver.%buildver.i386.linux.tar.bz2
Source10:	opera-%softver.%buildver.x86_64.linux.tar.bz2

ExclusiveArch:	%ix86 x86_64

%ifarch %ix86
BuildArch:	i586
%else
BuildArch:	x86_64
%endif

%add_verify_elf_skiplist %_libdir/*-linux-gnu/opera-developer/*.so
%set_verify_elf_method textrel=relaxed

# Automatically added by buildreq on Thu Jun 11 2015 (-bi)
# optimized out: elfutils fontconfig libdbus-glib libgdk-pixbuf libwayland-client libwayland-server python-base
BuildRequires: libGConf libXScrnSaver libXtst libalsa libcurl libgtk+2 libnotify libnss

%description
Opera is a small, fast, customizable, powerful and user-friendly web
browser, as well as an Internet suite, including an email client, an IRC
client, web developer tools (Opera Dragonfly), and a personal web server
(Opera Unite).

%prep
%setup -q -n opera-%softver.%buildver.i386.linux
%ifarch x86_64
tar -xf %SOURCE10
%endif

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_datadir}
%ifarch x86_64
cd opera-%softver.%buildver.x86_64.linux
%endif
cp -a ./lib/* %buildroot%_libdir/
cp -a ./share/* %buildroot%_datadir
%ifarch %ix86
ln -s %_libdir/i386-linux-gnu/opera-developer/opera-developer %buildroot%_bindir/opera-developer
%else
ln -s %_libdir/x86_64-linux-gnu/opera-developer/opera-developer %buildroot%_bindir/opera-developer
subst 's|usr/lib/|%_libdir/|g' %buildroot%_datadir/lintian/overrides/opera-developer
%endif
subst 's|PepperFlash/libpepflashplayer.so|pepper-plugins/libpepflashplayer.so|g' %buildroot%_libdir/*-linux-gnu/opera-developer/resources/pepper_flash_config.json

%files
%_docdir/opera-developer
%_bindir/*
%_libdir/*-linux-gnu
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_datadir/lintian

%changelog
* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1963.0-alt1
- packed 33.0.1963.0 snapshot

* Thu Jul 23 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1933.0-alt1
- packed 32.0.1933.0 snapshot

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1.1
- change git folders

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1
- packed 32.0.1926.0 snapshot

* Thu Jul 02 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1910.0-alt1
- packed 32.0.1910.0 snapshot

* Thu Jun 18 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1899.0-alt1
- packed 32.0.1899.0 snapshot

* Thu Jun 11 2015 Motsyo Gennadi <drool@altlinux.ru> 31.0.1876.0-alt1
- packed for ALT Linux
