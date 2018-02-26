Name: xtrkcad
Version: 4.0.3a
Release: alt1.1
Group: Games/Educational
License: GPL
Summary: XTrkCad Model Railroad CAD
Source: %name-source-%version.tar.gz
Patch0: xtrkcad-4.0.3a-alt-DSO.patch
URL:	http://www.xtrkcad.org

# Automatically added by buildreq on Wed Jul 27 2011
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstdc++-devel libxml2-devel pkg-config xorg-xproto-devel
BuildRequires: cmake gcc-c++ libgtkhtml2-devel

%description
XTrkCad is a CAD program for designing Model Railroad layouts.
XTrkCad supports any scale, has libraries of popular brands of x
turnouts and sectional track (plus you add your own easily), can
automatically use spiral transition curves when joining track
and has extensive on-line help and demonstrations.
XTrkCad lets you manipulate track much like you would with actual
flex-track to modify, extend and join tracks and turnouts.
Additional features include tunnels, 'post-it' notes, on-screen
ruler, parts list, 99 drawing layers, undo/redo commands,
benchwork, 'Print to BitMap', elevations, train simulation and
car inventory.

%prep
%setup -n %name-source-%version
%patch0 -p2

%build
%cmake
cd BUILD
%make_build
cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=XTrackCAD
GenericName=Railroad CAD
Comment=%summary
Icon=%name
Exec=%name
Terminal=false
Categories=Game;Simulation;
@@@

%install
install -D app/doc/png.d/bnewcar.png %buildroot%_niconsdir/%name.png
cd BUILD
%makeinstall DESTDIR=%buildroot
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README app/lib/*.txt
%dir %_datadir/%name
%_datadir/%name/*
%_bindir/%{name}*
%_niconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3a-alt1.1
- Fixed build

* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 4.0.3a-alt1
- Autobuild version bump to 4.0.3a
- Desktop file added

* Tue Oct 07 2008 Fr. Br. George <george@altlinux.ru> 4.0.2-alt1
- Initial build from scratch

