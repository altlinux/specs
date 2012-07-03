Name:		SheepShaver
Version:	2.3.20120410
Release:	alt1
Group:		Emulators
Summary:	PowerMac emulator
License:	GPL
URL:		http://sheepshaver.cebix.net
ExclusiveArch:	%ix86
# Synthetic CVS, see SheepShaver/get
Source:		%name-%version.tar

# Automatically added by buildreq on Tue Apr 10 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libICE-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config xorg-xextproto-devel xorg-xf86dgaproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libSDL-devel libSM-devel libXext-devel libXxf86dga-devel libXxf86vm-devel libgtk+2-devel xorg-cf-files

%description
SheepShaver is a MacOS run-time environment for BeOS and Linux that
allows you to run classic MacOS applications inside the BeOS/Linux
multitasking environment. This means that both BeOS/Linux and MacOS
applications can run at the same time (usually in a window on the
BeOS/Linux desktop) and data can be exchanged between them. If you are
using a PowerPC-based system, applications will run at native speed
(i.e. with no emulation involved). There is also a built-in PowerPC
emulator for non-PowerPC systems.

SheepShaver is distributed under the terms of the GNU General Public
License (GPL). However, you still need a copy of MacOS and a PowerMac
ROM image to use SheepShaver. If you're planning to run SheepShaver on
a PowerMac, you probably already have these two items.

%package -n BasiliskII
Group:		Emulators
License:	GPL
Summary:	Open Source 68k Macintosh emulator

%description -n BasiliskII
Basilisk II is an Open Source 68k Macintosh emulator. That is, it allows
you to run 68k MacOS software on your computer, even if you are using
a different operating system. However, you still need a copy of MacOS
and a Macintosh ROM image to use Basilisk II. Basilisk II is distributed
under the terms of the GNU General Public License (GPL).

For more information, see the README file. If you are interested in
learning how Basilisk II works internally, there is a Technical Manual
available (knowledge about programming and computer architecture is
required).

%prep
%setup -n %name
sed -i 's@linux/\.\./@@' BasiliskII/src/Unix/Linux/scsi_linux.cpp

%build
cd BasiliskII/src/Unix
NO_CONFIGURE=yes ./autogen.sh
%configure --enable-sdl-video --enable-sdl-audio --with-bincue --enable-jit-compiler 
%make

cd ../../../SheepShaver
make links
cd src/Unix
NO_CONFIGURE=yes ./autogen.sh
# TODO make SDL video work here (now it crushes SheepShaver every time)
%configure --enable-sdl-audio --with-bincue
%make

%install
%makeinstall -C BasiliskII/src/Unix
%makeinstall -C SheepShaver/src/Unix

%files
%doc %name/doc
%_bindir/S*
%_datadir/S*
%_man1dir/S*

%files -n BasiliskII
%doc BasiliskII/README BasiliskII/TECH BasiliskII/TODO
%_bindir/B*
%_datadir/B*
%_man1dir/B*

%changelog
* Tue Apr 10 2012 Fr. Br. George <george@altlinux.ru> 2.3.20120410-alt1
- Version up
- Fix dependencies

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.3.20110213-alt2
- Accurate arch handling

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 2.3.20110213-alt1
- Initial build from scratch

