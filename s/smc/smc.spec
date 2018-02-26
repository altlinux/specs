Name: smc
Version: 2.0.0
Release: alt2.git20110510
Summary: 2D platform game that uses OpenGL in a style similar to Super Mario
Group: Games/Arcade
License: GPLv3
Url: http://www.secretmaryo.org
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://downloads.sourceforge.net/smclone/%name-%version.tar.bz2
Source1: smc.sh
Source2: dochelper.pl

# Automatically added by buildreq on Thu Aug 20 2009
BuildRequires: boost-filesystem-devel cegui-devel gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libX11-devel libpng-devel

BuildRequires: desktop-file-utils
Requires: %name-data = %version-%release

%description
Secret Maryo Chronicles is a 2D platform game that makes use of OpenGL and is
built upon SDL. It is similar to the classic game Super Mario.

%package data
Summary: data files for game in a style similar to Super Mario
Group: Games/Arcade
BuildArch: noarch

%description data
Data files for Secret Maryo Chronicles game

%prep
%setup -q

#Fix EOL chars
sed -i 's/\r//' docs/style.css docs/*.html docs/*.txt

sed -i 's,/usr/share/gettext/config.rpath,/usr/share/gettext/intl/config.rpath,g' ./autogen.sh

./autogen.sh

%build
%configure
%make

# Generate the credit list from lots of little text files scattered around the
# installation. Very messy! A helper script is used to avoid over-complicating
# the spec. Additional processing is done on the credits to fix character
# encoding and to strip 'data/' from the paths because the installation
# location is now different and it's far simpler that altering dochelper.pl
cp %SOURCE2 . && perl dochelper.pl
sed -i 's/\r//' credits.txt
sed -i 's|data/||g' credits.txt
iconv -f iso8859-1 credits.txt -t utf8 > credits.conv && /bin/mv -f credits.conv credits.txt

# Build desktop file
cat >%name.desktop <<EOF
[Desktop Entry]
Name=Secret Maryo Chronicles
GenericName=Platform game
Comment=%summary
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ActionGame;
EOF

%install

%makeinstall_std
mkdir -p %buildroot%_iconsdir/hicolor/32x32/apps
install -pm0644 data/icon/window_32.png %buildroot%_iconsdir/hicolor/32x32/apps/smc.png
mv %buildroot%_bindir/%name %buildroot%_bindir/%name.bin
install -pm0755 %SOURCE1 %buildroot%_bindir/%name

desktop-file-install --vendor dribble \
                     --dir %buildroot%_desktopdir \
%name.desktop

%files
%_desktopdir/dribble-%name.desktop
%_bindir/%name
%_bindir/%name.bin

%files data
%_datadir/smc
%_iconsdir/hicolor/32x32/apps/smc.png
%doc credits.txt docs/*.html docs/license.txt docs/style.css

%changelog
* Fri Apr 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt2.git20110510
- rebuild with boost-1.49

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt1.git20110510
- rebuild with boost-1.47

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt0.git20110510
- git snapshot with cegui-0.7 support

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9-alt5
- rebuild with cegui-0.7.5

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9-alt4
- repair build with boost-1.46

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9-alt3
- rebuild with boost-1.45

* Sun Nov 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9-alt2
- rebuild with boost-1.42

* Thu Aug 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9-alt1
- 1.9

* Tue Jun 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2
- rebuild with new libpng

* Fri Apr 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt1
- 1.8

* Fri Dec 26 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7-alt1
- 1.7

* Fri Dec 19 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt2
- rebuild

* Wed Oct 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1
- 1.6

* Wed Jun 04 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1
- Initial for ALT

* Tue Jan 08 2008 Ian Chapman <packages[AT]amiga-hardware.com> 1.4.1-1
- Upgrade to 1.4.1

* Sat Dec 02 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.3-1
- Upgrade to 1.3
- Minor update to .desktop file due to new validation rules

* Sat Oct 20 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-1
- Upgrade to 1.2

* Fri Sep 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-1
- Upgrade to 1.1
- SPEC cleanups as latest version allows us to streamline the install a bit

* Wed Aug 08 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-1
- Upgrade to 1.0
- Changed license field to match new guidelines

* Sat Jun 23 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.7-1
- Upgrade to 0.99.7

* Sat Jun 02 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.6.1-1
- Upgrade to 0.99.6.1
- Dropped all patches as they are no longer needed.
- Changed .desktop category to Action Games
- Changed .desktop icon as it's now supplied with one.

* Tue Oct 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.2-1
- Upgrade to 0.99.2
- Dropped fonts patch in favour of using sed
- Updated fiximageset patch
- Added patch to fix the globals header

* Mon Oct 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.1-2
- Rebuild against latest libraries, seems to fix segfault on some machines

* Thu Sep 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.1-1
- Upgrade to 0.99.1
- Dropped smc-0.99-fixuint.patch, fixed upstream

* Wed Aug 02 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99-1
- Upgraded to 0.99
- Fixpaths patch reduced, fewer files need to be fixed
- Added patch to fix location of headers
- Added patch to convert uint to CEGUI::uint to avoid conflict
- Split imageset and fonts into separate patches for easier maintenance

* Sun Jul 16 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-3
- Added libpng-devel buildrequire for building under mock for fc5

* Sat Jul 08 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-2
- Corrected EOL chars in additional-licenses.txt
- Removed redundant params from %%setup
- Added automake buildrequire
- Removed pkgconfig buildrequire (required by cegui-devel)
- Moved icon installation to make it freedesktop compliant
- Added %%post and %%postun sections to update icon cache at installation
- Minor cleanups to smc.sh wrapper script
- Moved smc binary installation from /usr/games to %_bindir/smc.bin
- Enhanced the description

* Sat Jun 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-1
- Initial Release
