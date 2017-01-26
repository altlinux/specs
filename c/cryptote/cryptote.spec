# Spec file for CryptoTE editor

Name: cryptote
Version: 0.6.0
Release: alt1

Summary: encrypting text editor

License: %gpl2only
Group: Editors
URL: https://github.com/bingmann/cryptote
#URL: http://idlebox.net/2009/cryptote/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name-16.png
Source2: %name-32.png

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Aug 28 2009
BuildRequires: bzlib-devel gcc-c++ wxGTK-devel zlib-devel

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
* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.390-alt2
- Fix build with GCC 4.7

* Fri Aug 28 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.390-alt1
- Initial build for ALT Linux Sisyphus

