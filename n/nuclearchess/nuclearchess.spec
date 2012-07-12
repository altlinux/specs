Name:		nuclearchess
Version:	1.0.0
Release:	alt2.1
Summary:	NuclearChess is a chess variant
License:	GPLv2
Group:		Games/Boards
Url:		http://user.cs.tu-berlin.de/~karlb/nuclearchess
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://user.cs.tu-berlin.de/~karlb/nuclearchess/%name-%version.tar.gz
Source1:	%name.desktop
Patch0: nuclearchess-1.0.0-alt-DSO.patch

# Automatically added by buildreq on Thu Jun 19 2008 (-bi)
BuildRequires: ImageMagick libSDL-devel libSDL_image-devel

%description
NuclearChess is a chess variant. Whenever a piece is captured,
both pieces and all pieces on neighbour fields die. Games are
short and fun even for people who usually don't play chess.

%prep
%setup
%patch -p2

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
%makeinstall bindir=$RPM_BUILD_ROOT%_gamesbindir \
	     datadir=$RPM_BUILD_ROOT%_gamesdatadir
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_desktopdir}
convert -resize 16x16 gfx/atom.png %buildroot%_miconsdir/%name.png
convert -resize 32x32 gfx/atom.png %buildroot%_niconsdir/%name.png
convert -resize 48x48 gfx/atom.png %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS ChangeLog
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/gfx
%_gamesbindir/%name
%_gamesdatadir/%name/gfx
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.1
- Fixed build

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt2
- delete post/postun scripts (new rpm)

* Thu Jun 19 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux
