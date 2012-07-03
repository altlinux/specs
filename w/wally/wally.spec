Name:		wally
Summary:	Qt4 wallpaper changer
Version:	2.3.2
Release:	alt0.2.qa2
License:	GPLv2+
Group:		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://code.google.com/p/wally/
Source0:	http://wally.googlecode.com/files/%name-%version.tar.gz
Patch0:		%name-2.3.2-fix_build.diff
Patch1:   %name-2.3.2-alt-DSO.diff

# Automatically added by buildreq on Mon May 03 2010 (-bi)
BuildRequires: ImageMagick-tools cmake gcc-c++ glib2-devel libSM-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libqt4-devel

Requires: libqt4-core
BuildRequires: desktop-file-utils

%description
Wally is a Qt4 wallpaper changer, using multiple sources like files, folders,
FTP remote folders, Flickr, Yahoo!, Panoramio, Pikeo, Ipernity, Photobucket,
Buzznet, Picasa, Smugmug and Bing images. It runs under Linux, Win32, and MacOSX,
and it's available in many languages.

Supported Window Managers: - Win32 - MacOSX (using OSA scripts) - KDE3 - KDE4
(using WallyPlugin) - Gnome - XFCE4 - Fluxbox - Blackbox - FVWM (unstable) - WindowMaker

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 res/images/%name.xpm %buildroot%_miconsdir/%name.png
convert -resize 32x32 res/images/%name.xpm %buildroot%_niconsdir/%name.png
convert -resize 48x48 res/images/%name.xpm %buildroot%_liconsdir/%name.png

# menu-entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Terminal=false
Name=Wally
Comment=A Qt4 wallpaper changer using multiple sources
Exec=%name
Icon=%name
Categories=Qt;DesktopSettings;Graphics;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Graphics \
	--add-category=DesktopSettings \
	--add-category=Settings \
	%buildroot%_desktopdir/wally.desktop

%files
%doc DISCLAIMER README.shortcuts README.XFCE4 LICENSE
%_bindir/%name
# #%exclude %{_datadir}/kde4/services/plasma-wallpaper-wallyplugin.desktop
# #%exclude %{_libdir}/kde4/plasma_wallpaper_wallyplugin.so
# #%exclude %{_datadir}/icons/oxygen/16x16/apps/wallyplugin.png
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt0.2.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.2-alt0.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for wally
  * freedesktop-desktop-file-proposed-patch for wally
  * postclean-03-private-rpm-macros for the spec file

* Fri May 14 2010 Motsyo Gennadi <drool@altlinux.ru> 2.3.2-alt0.2
- fix build

* Mon May 03 2010 Motsyo Gennadi <drool@altlinux.ru> 2.3.2-alt0.1
- test build for ALT Linux
