Name: gargoyle
Version: 0
%define rel_date 2009-08-25
%define rel      2009.08.25
Release: alt1.%rel

Summary: a typography-aware Glk-based interactive fiction interpreter suite
License: Distributable (see documentation)
Group: Games/Other
Url: http://ccxvii.net/gargoyle/

Packager: Alexander Myltsev <avm@altlinux.ru>

Source: %name-%version.tar
Source2: garglk.ini
Patch1: %name-2006-04-28-alt-launcher.patch

BuildPreReq: libgtk+2-devel libpng-devel libjpeg-devel libfreetype-devel
BuildPreReq: libogg-devel libvorbis-devel libsmpeg-devel
BuildPreReq: jam gcc-c++
BuildRequires: libSDL-devel libSDL_mixer-devel

%description
Gargoyle is a suite of interpreters presenting a uniform interface
for playing all the major interactive fiction formats. It is based on
Glk, an interface standard for IF.

Gargoyle is, just like Glk, free software.

Gargoyle cares about typography, featuring unhinted anti-aliased fonts,
kerning, ligatures, smart quotes (and other punctuation formatting),
and plenty of spacing.

%prep
%setup
%patch1 -p1

%build
ln -s tads/tads2 tads2
ln -s tads/tads3 tads3

jam -q

%install
jam install

mkdir -p %buildroot%_sysconfdir
cp %SOURCE2 %buildroot%_sysconfdir/

mkdir -p %buildroot%_libdir/%name
mv build/dist/libgarglk.so %buildroot%_libdir/
mkdir -p %buildroot%_bindir

install -m755 build/dist/%name %buildroot%_bindir/
subst 's,@TERPS_PATH@,%_libdir/%name,' %buildroot%_bindir/%name

mv build/dist/* %buildroot%_libdir/%name/

%files
%config %_sysconfdir/garglk.ini
%_bindir/%name
%_libdir/%name
%_libdir/libgarglk.so

%changelog
* Sun Jan 03 2010 Alexander Myltsev <avm@altlinux.ru> 0-alt1.2009.08.25
- New version.

* Mon Oct 20 2008 Alexander Myltsev <avm@altlinux.ru> 0-alt1.2006.09.17
- Fix build, update version.

* Wed May 17 2006 Alex V. Myltsev <avm@altlinux.ru> 0-alt1.2006.04.28
- Initial build for Sisyphus.

