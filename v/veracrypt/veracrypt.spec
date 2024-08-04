%define _unpackaged_files_terminate_build 1

Name: veracrypt
Version: 1.26.7
Release: alt1

Summary: Disk encryption software

License: Apache-2.0
Group: File tools
Url: https://www.veracrypt.fr

# Source-url: https://github.com/veracrypt/VeraCrypt/archive/VeraCrypt_%version.tar.gz?/VeraCrypt_%version.tar.gz
Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: pkgconfig(fuse)
BuildRequires: /usr/bin/convert
BuildRequires: libpcsclite-devel
#BuildRequires: makeself
BuildRequires: libwxGTK3.0-devel
BuildRequires: gcc-c++
BuildRequires: yasm
BuildRequires: nasm

%description
Free disk encryption software based on TrueCrypt.

%prep
%setup

%build
%make_build NOSTRIP=1 DEBUGGER=1 -C src

pushd src/Resources/Icons
magick VeraCrypt-16x16.xpm VeraCrypt-16x16.png
magick VeraCrypt-48x48.xpm VeraCrypt-48x48.png
magick VeraCrypt-128x128.xpm VeraCrypt-128x128.png
popd

%install
%makeinstall_std -C src

for png in 128x128 48x48 16x16; do
	mkdir -p %buildroot%_iconsdir/hicolor/${png}/apps/
	install -m 0644 src/Resources/Icons/VeraCrypt-${png}.png %buildroot%_iconsdir/hicolor/${png}/apps/%name.png
done

rm -rv %buildroot%_bindir/%name-uninstall.sh

%files
%doc %_docdir/veracrypt/
%_bindir/veracrypt
%_sbindir/mount.veracrypt
%_desktopdir/veracrypt.desktop
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/packages/veracrypt.xml
%dir %_datadir/veracrypt/
%_datadir/veracrypt/languages/


%changelog
* Sun Aug 04 2024 Egor Ignatov <egori@altlinux.org> 1.26.7-alt1
- 1.26.7

* Thu Nov 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.25.9-alt1
- initial build for ALT Sisyphus (thanks, ROSA!)
