Name: maim
Version: 3.3.41
Release: alt1

Summary: Flexible screenshotting utility

License: GPL-3.0+
Group: Graphics
Url: https://github.com/naelstrof/maim

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/naelstrof/%name/archive/v%version.tar.gz#/%name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gengetopt
BuildRequires: pkgconfig(imlib2)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)

Requires: imlib2
# Recommended
#Requires: slop

%description
maim (Make Image) is a utility that takes screenshots of your desktop
using imlib2. It's meant to overcome shortcomings of scrot and performs
better in several ways.

%prep
%setup

%build
%cmake_insource
%make_build

%install
# install executable
mkdir -p %buildroot%_bindir
install -Dm 0755 %name %buildroot%_bindir/

# install man
install -Dm 0644 man-src/%name.1 %buildroot%_man1dir/%name.1

%files
%doc COPYING README.md
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Jun 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.41-alt1
- initial build for ALT Linux Sisyphus

* Fri Jun 26 2015 nemysis@gmx.ch
- Update to 3.3.41, no changelog entry
- Change Source0 Web URL, to have right maim-3.3.41.tar.gz
- Add BuildRequires for cmake and gengetopt
- Add BuildRoot
- Use %%{name} instead of maim
- Switch to manual installation, because in Source isn't install command
- Add Documentation
- Add %%changelog
* Mon Oct 20 2014 rneuhauser@suse.cz
- maim-2.3.17
* Fri Oct 17 2014 rneuhauser@suse.cz
- maim-2.2.13
