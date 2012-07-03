Version:	1.4.8
Name:		qosmic
Release:	alt1
Summary:	Qosmic Fractal Flame Editor
License: 	GPLv2
Group: 		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://code.google.com/p/qosmic/
Source0:	http://qosmic.googlecode.com/files/%name-%version.tar.bz2
Source1:	%name.desktop
Source2:	%name
Patch0:		%name-1.4.8-alt_dirs.diff
Requires:	flam3-palettes

BuildRequires: ImageMagick flam3-palettes flam3-devel-static >= 2.7.18 gcc-c++ libjpeg-devel liblua5-devel libqt4-devel libxml2-devel

%description
Qosmic is a nifty toy with which you can
edit and render flam3 fractal images.

%prep
%setup -n %name
%patch0 -p1

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%__install -Dp -m 0755 %name %buildroot%_bindir/%name.bin
%__install -Dp -m 0755 %SOURCE2 %buildroot%_bindir/%name

# Menu
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 icons/%name.xpm %buildroot%_miconsdir/%name.png
convert -resize 32x32 icons/%name.xpm %buildroot%_niconsdir/%name.png
convert -resize 48x48 icons/%name.xpm %buildroot%_liconsdir/%name.png

%files
%doc README* changes.txt
%_bindir/%{name}*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sat Jan 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.8-alt1
- 1.4.8
- change URL

* Sat Aug 15 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Thu Jul 23 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Sun Nov 23 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt2.1
- really delete post/postun scripts

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt2
- delete post/postun scripts (new rpm)

* Tue Apr 15 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Feb 25 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3

* Fri Jan 04 2008 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- 1.2

* Wed Oct 31 2007 Motsyo Gennadi <drool@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Oct 23 2007 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- initial build for ALT Linux
