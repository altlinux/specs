BuildRequires: desktop-file-utils
Name:		qvkeyboard
Version:	1.0.0
Release:	alt2.qa2
Summary:	Virtual keyboard for X11
Source0:	http://qt-apps.org/CONTENT/content-files/77983-%name.tgz
Source1:	%name.png
Source2:	%name.desktop
Patch0: qvkeyboard-1.0.0-alt-DSO.patch
URL:		http://qt-apps.org/content/show.php/QVKeyboard?content=77983
Group:		Accessibility
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>

# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: gcc-c++ ImageMagick libqt4-devel libXtst-devel

%description
Virtual keyboard for X11. Has support for languages via xml file.

%prep
%setup -q -n %name
%patch0 -p2

%build
export PATH=$PATH:%_qt4dir/bin
%add_optflags -fpermissive
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
mkdir -p %buildroot%_datadir/%name
install -Dp -m 0755 %name %buildroot%_bindir/%name.bin
cp *.xml %buildroot%_datadir/%name/ && chmod 0644 %buildroot%_datadir/%name/*.xml
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

cat << EOF > %buildroot%_bindir/%name
#!/bin/sh
cd %_datadir/%name && %name.bin &
EOF
chmod +x %buildroot%_bindir/%name

# icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Accessibility \
	%buildroot%_desktopdir/qvkeyboard.desktop

%files
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.qa2
- Fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qvkeyboard
  * postclean-03-private-rpm-macros for the spec file

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt2
- delete post/postun scripts (new rpm)

* Thu Apr 03 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux
