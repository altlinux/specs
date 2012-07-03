%define		git 20120505

Name:		screengrab
Version:	0.9.92
Release:	alt1.%git
Summary:	ScreenGrab is a tool for geting screenshots
License:	GPLv2
Source0:	%name-%version.tar.gz
Url:		http://code.google.com/p/screengrab-qt/
Group:		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildRequires: /usr/bin/convert cmake gcc-c++ libqt4-devel

%description
ScreenGrab is a crossplatform tool for geting screenshots
working in Linux and Windows. The program uses Qt and is
independent of any desktop environment.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
%make DESTDIR=%buildroot install
rm -rf %buildroot%_docdir/%name
ln -s %_docdir/%name-%version %buildroot%_docdir/%name

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 img/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 img/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 img/%name.png %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/%name
%dir %_datadir/%name/localize
%dir %_docdir/%name
%doc docs/*
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png

%changelog
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
