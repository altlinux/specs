Name:		screengrab
Version:	1.99
Release:	alt1
Summary:	ScreenGrab is a tool for geting screenshots
License:	GPLv2
Source0:	%name-%version.tar.xz
Source1:	%name.sh
Url:		https://github.com/lxqt/screengrab/releases
Group:		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildRequires: /usr/bin/convert cmake kf5-kwindowsystem-devel libqtxdg-devel qt5-tools qt5-x11extras-devel

Patch0:		%name-1.99-check_ling_tools_off.patch

Requires:	libkf5windowsystem

%add_findprov_lib_path %_libdir/%name
%brp_strip_none %_libdir/%name/%name
%add_verify_elf_skiplist %_libdir/%name/%name
%set_verify_elf_method textrel=relaxed

%description
ScreenGrab is a crossplatform tool for geting screenshots
working in Linux and Windows. The program uses Qt and is
independent of any desktop environment.

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
lrelease-qt5 ./translations/*.ts
cd BUILD
%make_build

%install
cd BUILD
%make DESTDIR=%buildroot install
mv %buildroot%_bindir/%name %buildroot%_libdir/%name/%name
install -m 0775 %SOURCE1 %buildroot%_bindir/%name
subst 's|/lib|/%_lib|g' %buildroot%_bindir/%name

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_liconsdir}
convert -resize 48x48 ../img/%name.png %buildroot%_liconsdir/%name.png
convert -resize 16x16 ../img/%name.png %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/%name
%dir %_docdir/%name
%dir %_libdir/%name
%_bindir/*
%_libdir/%name/*

%_desktopdir/%name.desktop
%_docdir/%name
%_datadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sun Jul 22 2018 Motsyo Gennadi <drool@altlinux.ru> 1.99-alt1
- 1.99 (#altbug 35169)

* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- 1.0

* Thu Jun 14 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.92-alt1.20120505
- git snapshot 20120505

* Tue Jul 05 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.81-alt1
- 0.9.81

* Sun Jan 23 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Nov 15 2010 Motsyo Gennadi <drool@altlinux.ru> 0.9-alt1
- 0.9

* Fri May 14 2010 Motsyo Gennadi <drool@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sat Mar 27 2010 Motsyo Gennadi <drool@altlinux.ru> 0.8-alt1
- 0.8

* Thu Mar 25 2010 Motsyo Gennadi <drool@altlinux.ru> 0.6.2-alt1
- initial build for ALT Linux
