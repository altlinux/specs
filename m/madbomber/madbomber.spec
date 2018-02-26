Name: madbomber
Version: 0.2.5
Release: alt1.qa2

Summary: Catch the bombs
License: GPL
Url: http://newbreedsoftware.com/madbomber
Group: Games/Arcade
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: ftp://ftp.sonic.net/pub/users/nbs/unix/x/madbomber/madbomber-%version.tar.bz2
Patch: %name-0.1.8-fix-CFLAGS.patch.bz2
Patch1: %name-0.2.4-add-keypad-keys.patch.bz2

# Automatically added by buildreq on Втр Мар 25 2003
BuildRequires: aalib esound libSDL-devel libSDL_image-devel libSDL_mixer-devel libalsa2 libaudiofile libjpeg libogg libslang libsmpeg libtiff libvorbis

%description
The Mad Bomber is loose in the city and he's dropping bombs everywhere! It's
your job to catch them before they hit the ground and explode. Luckily, you have
a set of trusty buckets to extinguish them with.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%define _optlevel 3
%add_optflags %optflags_kernel %optflags_notraceback %optflags_fastmath
%make_build CFLAGS="%optflags" BIN_PREFIX=%_bindir DATA_PREFIX=%_datadir/%name/

%install
install -D %name $RPM_BUILD_ROOT%_bindir/%name
install -d $RPM_BUILD_ROOT%_datadir/%name
cp -a data/* $RPM_BUILD_ROOT%_datadir/%name

install -D -m644 data/images/icon.png $RPM_BUILD_ROOT%_liconsdir/madbomber.png
#mkdir -p $RPM_BUILD_ROOT%_miconsdir/ $RPM_BUILD_ROOT%_niconsdir/
#convert -resize 16x16 data/images/icon.png $RPM_BUILD_ROOT%_miconsdir/madbomber.png
#convert -resize 32x32 data/images/icon.png $RPM_BUILD_ROOT%_niconsdir/madbomber.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Mad Bomber
Comment=%summary
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc AUTHORS.txt CHANGES.txt README.txt
%_bindir/*
%_datadir/%name
#%_miconsdir/*.png
#%_niconsdir/*.png
%_liconsdir/*.png
%_desktopdir/%{name}.desktop

%changelog
* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1.qa2
- NMU: converted debian menu to freedesktop

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.5-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for madbomber
  * pixmap-in-deprecated-location for madbomber
  * postclean-05-filetriggers for spec file

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.2.5-alt1.1
- rebuild
- update requires

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt1
- 0.2.4
- cleanup spec

* Fri Aug 17 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.8-ipl8mdk
- Rebuilt with new SDL.

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.1.8-ipl7mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.1.8-ipl6mdk
- fix BuildPreReq

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 0.1.8-ipl5mdk
- Build for RE
- adding menu

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-5mdk
- rebuild with new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-4mdk
- rebuild, build req

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-1mdk
- initial spec

# end of file
