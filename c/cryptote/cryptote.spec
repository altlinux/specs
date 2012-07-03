# Spec file for CryptoTE editor

Name: cryptote
Version: 0.5.390
Release: alt1

Summary: encrypting text editor
#Summary(ru_RU.UTF-8): 

License: %gpl2only
Group: Editors
URL: http://idlebox.net/2009/cryptote/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
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

#%%description -l ru_RU.UTF-8

%prep
%setup
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
* Fri Aug 28 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.390-alt1
- Initial build for ALT Linux Sisyphus

