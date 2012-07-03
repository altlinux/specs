Name: svg-cleaner
Version: 0.2
Release: alt1

Summary: Batch, tunable, crossplatform SVG cleaning program 

License: GPLv3
Group: Graphics
Url: https://launchpad.net/svg-cleaner

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sat Jan 14 2012
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-svg libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ glibc-devel phonon-devel

BuildPreReq: perl-XML-Twig

%description
Batch, tunable, crossplatform SVG cleaning program 

%prep
%setup
chmod 755 svgcleaner

%build
qmake-qt4 -config release
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc TODO
%_bindir/svgcleaner
%_bindir/svgcleaner-gui
%_datadir/svgcleaner
%_desktopdir/svgcleaner.desktop
%_iconsdir/hicolor/scalable/apps/svgcleaner.svg

%changelog
* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
