Name: qmotion
Version: 3.0
Release: alt1

Summary: Detect motion with your webcam.
Group: Development/Tools
License: GPLv2+
Url: http://slist.lilotux.net/linux/%{name}/index_en.html

Source0: %{name}-%{version}.tgz
Source1: %name.watch

BuildRequires: gcc-c++ libqt4-devel >= 4.3 pkgconfig(opencv)
# for convert
BuildRequires: ImageMagick-tools

%description
%summary

%prep
%setup
#sed -i 's,debug_and_release,release,' qgit.pro
#sed -i '/QMAKE_CXXFLAGS_RELEASE/s,-O2 ,%optflags ,g' src/src.pro

%build
sed -i -e s,lrelease,lrelease-qt4, %name.pro
qmake-qt4 %name.pro
%make_build

%install
install -pD -m755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Name=%name
Comment=Detect motion with your webcam.
TryExec=%name
Exec=%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Video;AudioVideo;Recorder;
StartupNotify=true
EOF

convert hibou.ico %name.png
install -Dm644 %name-0.png %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -Dm644 %name-1.png %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -Dm644 %name-2.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -Dm644 %name-3.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

mkdir -p examples
cat > examples/%{name}2avi.sh << EOF
#!/bin/sh
# example: encode captured motion frames into a movie
mencoder "mf://*.jpg" -mf fps=5 -o qmotion.avi -ovc lavc -lavcopts vcodec=mpeg4
EOF

%files
#doc README
%doc examples
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/??x??/apps/%name.png

%changelog
* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- new version (watch file uupdate)

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt3
- rebuild with new libopencv

* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2
- added %name.desktop and examples

* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- Built for Sisyphus
