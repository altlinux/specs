Name: roadfighter
Version: 1.0.1269
Release: alt1
Summary: Death race between you and a group of crazy drivers
# http://www.braingames.getput.com/forum/forum_posts.asp?TID=678&PN=1
License:	Distributable
Group: Games/Arcade
Url: http://www.braingames.getput.com/roadf/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.bz2
# PATCH-FIX-OPENSUSE roadfighter-1.0.1269-Makefile.patch adam@mizerski.pl -- Use more pkg-config. Use RPM_OPT_FLAGS. Don't strip.
Patch0: %name-1.0.1269-Makefile.patch
# PATCH-FIX-UPSTREAM fix-bool-to-ptr.patch -- Fix invalid boolean to pointer conversion
Patch1: fix-bool-to-ptr.patch
BuildRequires: gcc-c++
BuildRequires: libSDL-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libSDL_ttf-devel

%description
In 2003 the people from Retro Remakes (http://www.remakes.org/) organized a remake competition for the first time.
The idea was to create a remake from scratch in a short amount of time. We decided to participate with a remake
of the MSX game Road Fighter (http://www.generation-msx.nl/msxdb/softwareinfo/684):
a simple racing game that would be doable before the deadline and still be fun to play (oh the nostalgia!).

In the end we met the deadline (barely!) and sent in our entry. When finally the results came in,
we finished 7th out the 83 entries. Not too bad for a 2 month project :)

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
export CXXFLAGS="%optflags"
%make_build

%install
install -D roadfighter %buildroot%_libexecdir/%name/roadfighter
install -d -D %buildroot%_datadir/%name
cp -r fonts graphics maps sound %buildroot%_datadir/%name

# Install game wrapper
install -d -D %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
#!/bin/bash
cd %_datadir/%name
%_libexecdir/%name/roadfighter
EOF
chmod 755 %buildroot%_bindir/%name

# Install Icon and .desktop file
install -D build/linux/roadfighter.png %buildroot%_pixmapsdir/roadfighter.png
install -D build/linux/roadfighter.desktop %buildroot%_desktopdir/roadfighter.desktop

%files
%_bindir/%name
%_libexecdir/%name
%_datadir/%name
%_pixmapsdir/roadfighter.png
%_desktopdir/roadfighter.desktop
%doc readme.txt

%changelog
* Fri May 05 2023 Artyom Bystrov <arbars@altlinux.org> 1.0.1269-alt1
- initial build for ALT Sisyphus

* Mon Jan 30 2023 Carsten Ziepke <kieltux@gmail.com>
- Add BuildRequires pkgconfig and use pkgconfig for sdl, fix
  building for openSUSE Leap
- Run spec-cleaner
* Mon Aug  8 2016 rpm@fthiessen.de
- Added fix-bool-to-ptr.patch to fix build with gcc >= 6.0
- Some cleanup
* Mon Feb 10 2014 dap.darkness@gmail.com
- "error: Not a directory: "usr/lib64/roadfighter/roadfighter"
  was fixed via dir macro removing from files list.
* Wed Mar 27 2013 joop.boonen@opensuse.org
- Adapted the License according to the spdx standard
* Mon Jun 14 2010 adam@mizerski.pl
- new package
