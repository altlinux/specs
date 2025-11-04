# Spec file for CryptoTE editor

Name: cryptote
Version: 0.6.0
Release: alt4

Summary: encrypting text editor

License: %gpl2only
Group: Editors
URL: https://github.com/bingmann/cryptote
#URL: http://idlebox.net/2009/cryptote/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1: %name-0.6.0-alt-gcc11.2_fix.patch
Patch2: %name-0.6.0-alt-wxGTK3.0_fix.patch
Patch3: %name-0.6.0-alt-wxGTK3.2_fix.patch

Source1: %name-16.png
Source2: %name-32.png

BuildRequires(pre): rpm-build-licenses rpm-build-xdg

# Automatically added by buildreq on Tue Nov 04 2025
# optimized out: at-spi2-atk glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libp11-kit libsasl2-3 libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwxGTK3.2-devel python-modules python2-base python3 python3-base sh5
BuildRequires: bzlib-devel gcc-c++ libwxBase3.2-devel zlib-devel

%description
CryptoTE is a text editor with integrated strong cryptography.
It automatically stores text data in secure encrypted container
files. Compared to other "password keeper" programs, CryptoTE
does not force any structure upon your data: it works with
plain ASCII text and does not require you to fill in grids,
key-value attributes, descriptions etc.
Encryption is transparently performed using the Serpent cipher.

%prep
%setup
%patch0 -p1

%patch1
%patch2
%patch3

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make

%install
%make install DESTDIR=%buildroot

# Fix file names
mv -- %buildroot%_desktopdir/CryptoTE.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p -- %buildroot%_liconsdir %buildroot%_miconsdir %buildroot%_niconsdir
/bin/install -m 0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
/bin/install -m 0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
mv -- %buildroot%_pixmapsdir/%{name}* %buildroot%_liconsdir/


%find_lang %name

%files -f %name.lang
%doc NEWS README
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%{name}*

%_desktopdir/%name.desktop
%_xdgmimedir/packages/%{name}*
%_datadir/mimelnk/application/*.desktop

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*

%changelog
* Tue Nov 04 2025 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt4
- Rebuild with wxGTK 3.2 (Closes: 55410)

* Fri Oct 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt3
- Fix build with GCC 11.2
- Rebuild with wxGTK 3.0

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt2
- Fix build: update BuildRequires

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.390-alt2
- Fix build with GCC 4.7

* Fri Aug 28 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.390-alt1
- Initial build for ALT Linux Sisyphus

