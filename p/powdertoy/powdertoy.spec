Name: powdertoy
Version: 91.5.330
Release: alt1
Summary: Classic 'falling sand' physics sandbox game
Group: Games/Educational
Epoch: 1
License: GPL
Url: http://powdertoy.co.uk/
# GitHub https://github.com/FacialTurd/The-Powder-Toy/tags
Source: v%version.tar.gz
Obsoletes: powder

# Automatically added by buildreq on Wed Apr 03 2013
# optimized out: fontconfig libX11-devel libstdc++-devel pkg-config python-base python-modules python-modules-compiler xorg-xproto-devel
BuildRequires: ImageMagick-tools bzlib-devel flex gcc-c++ ghostscript-classic libSDL-devel libfftw3-devel liblua5-devel python-modules-email scons zlib-devel

%description
The Powder Toy is a desktop version of the classic 'falling sand'
physics sandbox game, it simulates air pressure and velocity as well as
heat!

%prep
%setup -n The-Powder-Toy-%version
# Hack out version update messge
sed -i 's/gameModel->AddNotification.*\("A new.*available.*update"\).*;/fprintf(stderr, "%%s\\n", \1);/g' src/gui/game/GameController.cpp

cat > %name.sh <<@@@
#!/bin/sh
test -d "\$HOME/.powdertoy" ||
{ rm -f "\$HOME/.powdertoy"; mkdir -p "\$HOME/.powdertoy/Brushes"; }
cd "\$HOME/.powdertoy" && \$0.bin
@@@

sed -i.lua51 's/lua5.1/lua/g' SConscript

cat > %name.desktop <<@@@
[Desktop Entry]
Name=The Powder Toy
Type=Application
Exec=%name
Icon=%name
Terminal=false
GenericName=Sandbox game
Categories=Game;Simulation;
Comment=%summary
@@@

%build
convert -set filename:area '%%wx%%h' resources/powder.ico 'powder-%%[filename:area].png'
%ifarch x86_64
scons -j %__nprocs --lin --64bit
%else
scons -j %__nprocs --lin
%endif

# TODO this doesn't compile for build263
# --opengl

%install
# TODO MIME (it can install mime locally!)
install -D build/powder* %buildroot%_gamesbindir/%name.bin
install -m755 %name.sh %buildroot%_gamesbindir/%name
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for N in powder-*.png; do
	install -D $N %buildroot%_iconsdir/hicolor/$(basename ${$##*-} .png)/apps/%name.png
done

%files
%doc README* TODO
%_gamesbindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1:91.5.330-alt1
- Autobuild version bump to 91.5.330

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1:91.4.329-alt1
- Autobuild version bump to 91.4.329

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 1:90.2.322-alt1
- Autobuild version bump to 90.2.322

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 1:90.1.320-alt1
- Autobuild version bump to 90.1.320
- Fix build

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1:89.2.283-alt1
- Autobuild version bump to 89.2.283

* Thu Feb 27 2014 Fr. Br. George <george@altlinux.ru> 1:89.2.281-alt1
- Autobuild version bump to 89.2.281
- Remove new version ad again

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 1:89.0.273-alt1
- Autobuild version bump to 89.0.273

* Mon Aug 26 2013 Fr. Br. George <george@altlinux.ru> 1:88.1.272-alt1
- Autobuild version bump to 88.1.272
- Switch to versioning scheme (introducing Epoch)
- Fix install typo

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 271-alt1
- Autobuild version bump to 271

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 270-alt1
- Autobuild version bump to 270

* Wed Apr 03 2013 Fr. Br. George <george@altlinux.ru> 263-alt1
- Switch versioning from version to build number
- Autobuild version bump to 263
- Patch C++ flaws
- Provide a wrapper for ~/.powdertoy cwd

* Wed Feb 06 2013 Fr. Br. George <george@altlinux.ru> 82.0-alt1
- Newer version build

* Tue Feb 05 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 81.3-alt2
- drop native optimization
- do not strip main binary before debuginfo

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 81.3-alt1
- Autobuild version bump to 81.3

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 80.3-alt1
- Autobuild version bump to 80.3

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 77.0-alt1
- Autobuild version bump to 77.0

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 74.2-alt1
- Autobuild version bump to 74.2

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 71.3-alt1
- Autobuild version bump to 71.3

* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 70.1-alt1
- Autobuild version bump to 70.1
- Fix docs

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 57.0-alt1
- Autobuild version bump to 57.0
- Remove new version ad again

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 55.9-alt1
- Autobuild version bump to 55.9

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 51.0-alt1
- Autobuild version bump to 51.0
- Remove new version ad

* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 50.6-alt2
- Added some native optimization

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 50.6-alt1
- Initial build from scratch

