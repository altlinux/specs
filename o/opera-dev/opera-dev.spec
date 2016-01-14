%define		softver 36.0
%define		buildver 2106.0

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
%_datadir/mime/packages/*.xml

%changelog
* Thu Jan 14 2016 Motsyo Gennadi <drool@altlinux.ru> 36.0.2106.0-alt1
- packaged 36.0.2106.0 snapshot

* Tue Dec 22 2015 Motsyo Gennadi <drool@altlinux.ru> 36.0.2079.0-alt1
- packaged 36.0.2079.0 snapshot

* Mon Dec 14 2015 Motsyo Gennadi <drool@altlinux.ru> 36.0.2072.0-alt1
- packaged 36.0.2072.0 snapshot

* Sun Dec 06 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2064.0-alt1
- packaged 35.0.2064.0 snapshot

* Fri Nov 27 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2060.0-alt1
- packaged 35.0.2060.0 snapshot

* Wed Nov 18 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2052.0-alt1
- packaged 35.0.2052.0 snapshot

* Fri Nov 13 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2044.0-alt1
- packaged 34.0.2044.0 snapshot

* Sat Nov 07 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2036.2-alt1
- packaged 34.0.2036.2 snapshot

* Sun Oct 25 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2026.0-alt1
- packaged 34.0.2026.0 snapshot

* Tue Oct 20 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2023.0-alt1
- packaged 34.0.2023.0 snapshot

* Fri Oct 09 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2011.0-alt1
- packaged 34.0.2011.0 snapshot

* Sat Sep 26 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.1996.0-alt1
- packaged 34.0.1996.0 snapshot

* Fri Sep 11 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1982.0-alt1
- packaged 33.0.1982.0 snapshot

* Wed Sep 02 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1967.0-alt1
- packaged 33.0.1967.0 snapshot

* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1963.0-alt1
- packaged 33.0.1963.0 snapshot

* Thu Jul 23 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1933.0-alt1
- packaged 32.0.1933.0 snapshot

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1.1
- change git folders

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1
- packaged 32.0.1926.0 snapshot

* Thu Jul 02 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1910.0-alt1
- packaged 32.0.1910.0 snapshot

* Thu Jun 18 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1899.0-alt1
- packaged 32.0.1899.0 snapshot

* Thu Jun 11 2015 Motsyo Gennadi <drool@altlinux.ru> 31.0.1876.0-alt1
- packaged for ALT Linux
