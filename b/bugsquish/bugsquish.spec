Name: bugsquish
Version: 0.0.6
Release: alt2.qa1

Summary: Kill bugs with mouse
License: GPL
Url: http://newbreedsoftware.com/bugsquish
Group: Games/Arcade

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: ftp://ftp.sonic.net/pub/users/nbs/unix/x/bugsquish/bugsquish-%version.tar.bz2
Patch: bugsquish-0.0.2-fix-CFLAGS.patch

# Automatically added by buildreq on Wed Sep 25 2010
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel

%description
Bugs are trying to suck blood out of your arm! Squish them with with your fly
swatter before you run out of blood.

%prep
%setup -q
%patch0 -p1

%define _optlevel 3
%add_optflags %optflags_kernel %optflags_notraceback %optflags_fastmath

%build
%make_build CFLAGS="%optflags" DATA_PREFIX=%_datadir/%name/

%install
install -D %name $RPM_BUILD_ROOT%_bindir/%name
install -d $RPM_BUILD_ROOT%_datadir/%name
cp -a data/* $RPM_BUILD_ROOT%_datadir/%name

install -D -pm644 data/images/bugsquish-icon.xpm $RPM_BUILD_ROOT%_miconsdir/bugsquish.xpm
install -D -pm644 data/images/bugsquish-icon.xpm $RPM_BUILD_ROOT%_niconsdir/bugsquish.xpm
install -D -pm644 data/images/bugsquish-icon.xpm $RPM_BUILD_ROOT%_liconsdir/bugsquish.xpm

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Bugsquish
Comment=Kill bugs with mouse
Icon=%name
Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc AUTHORS.txt CHANGES.txt README.txt
%_bindir/%name
%_datadir/%name/*
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_desktopdir/%name.desktop

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2.qa1
- NMU: converted menu to desktop file

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.6-alt2
- remove deprecated macros
- fix icons locations

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.0.6-alt1.1
- rebuild

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.0.6-alt1
- 0.0.6
- spec cleanup

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.0.2-ipl7mdk
- Rebuild with new SDL
- Fixed optflags

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.0.2-ipl6mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.0.2-ipl5mdk
- fix BuildPreReq

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 0.0.2-ipl4mdk
- Build for RE
- adding menu

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-4mdk
- rebuild with new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-3mdk
- build req, rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-2mdk
- rebuild with uptodate SDL
- fix summary-not-capitalized

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-1mdk
- initial spec

# end of file
