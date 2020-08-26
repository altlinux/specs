%define name    stella
%define version 6.2.1
%define rel     1

%define enable_gl 1
%define enable_sound 1
%define enable_debugger 1
%define enable_joystick 1
%define enable_cheats 1
%define enable_static 0

%define release %rel

Name: stella
Summary: An Atari 2600 Video Computer System emulator
Version: 6.2.1
Release: alt3
Group: Emulators
License: GPL2
Url: https://stella-emu.github.io
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ libSDL2-devel libGLU-devel zlib-devel libpng-devel libpng-devel

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was the most
popular home video game system of the early 1980's.  This emulator will run
most Atari ROM images, so that you can play your favorite old Atari 2600 games
on your PC.

%prep
%setup

%build
export CXXFLAGS=$RPM_OPT_FLAGS
touch configure.in
./configure \
%if %enable_gl
	--enable-gl \
%else
	--disable-gl \
%endif
%if %enable_sound
	--enable-sound \
%else
	--disable-sound \
%endif
%if %enable_debugger
	--enable-debugger \
%else
	--disable-debugger \
%endif
%if %enable_joystick
	--enable-joystick \
%else
	--disable-joystick \
%endif
%if %enable_cheats
	--enable-cheats \
%else
	--disable-cheats \
%endif
%if %enable_static
	--enable-static \
%else
	--enable-shared \
%endif
	--docdir=%_docdir/stella \
	--prefix=%prefix \
	--x-libraries=%prefix/X11R6/%_lib
%make

%install
%make_install install-strip DESTDIR=%buildroot
# Mandriva menu entries
install -d -m0755 %buildroot%_menudir
cat > %buildroot%_menudir/%name << EOF
?package(%name): command="stella" \
icon="stella.png" \
needs="x11" \
title="Stella" \
longtitle="A multi-platform Atari 2600 emulator" \
section="More Applications/Emulators" \
xdg="true"
EOF

rm -rf $RPM_BUILD_DIR/%name-%version

%files
%dir %_docdir/%name
%dir %_iconsdir/hicolor/22x22
%dir %_iconsdir/hicolor/22x22/apps
%dir %_iconsdir/hicolor/24x24
%dir %_iconsdir/hicolor/24x24/apps
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%_bindir/*
%_menudir/%name
%_desktopdir/%name.desktop
%_docdir/%name/*
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Wed Aug 26 2020 Artyom Bystrov <arbars@altlinux.org> 6.2.1-alt3
- removing non-working macros

* Sat Jun 20 2020 Artyom Bystrov <arbars@altlinux.org> 6.2.1-alt2
- Fix up missing directories

* Sat Jun 20 2020 Artyom Bystrov <arbars@altlinux.org> 6.2.1-alt1
- initial build for ALT Sisyphus
