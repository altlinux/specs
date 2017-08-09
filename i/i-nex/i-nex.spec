%define oname I-Nex

Summary: System information tool
Name: i-nex
Version: 7.6.0
Release: alt1
License: LGPLv3+
Group: System/Configuration/Hardware
Url: https://github.com/i-nex/I-Nex
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Just to make sure we have all these in repositories
BuildRequires: gambas3-devel
BuildRequires: gambas3-gb-desktop
BuildRequires: gambas3-gb-form-dialog
BuildRequires: gambas3-gb-form
BuildRequires: gambas3-gb-gui
BuildRequires: gambas3-gb-gtk
BuildRequires: gambas3-gb-image
BuildRequires: gambas3-gb-qt5
BuildRequires: gambas3-gb-settings
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libcpuid)
BuildRequires: pkgconfig(libprocps)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
Requires: gambas3-gb-desktop
Requires: gambas3-gb-form-dialog
Requires: gambas3-gb-form
Requires: gambas3-gb-gui
Requires: gambas3-gb-gtk
Requires: gambas3-gb-image
Requires: gambas3-gb-qt5
Requires: gambas3-gb-settings
Requires: gambas3-runtime
Requires: %_bindir/beesu

%description
An application that gathers information for hardware components available
on your system and displays it using an user interface similar to the popular
Windows tool CPU-Z.

%prep
%setup

# fix png rgb
pushd %oname/%name/logo
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd

%build
pushd %oname
%autoreconf
%configure
popd
%make_build STATIC=false

%install
#fix make install
for i in `find -name Makefile`; do
    sed -i 's/ 0755/ -m 0755/g' $i
    sed -i 's/ 0644/ -m 0644/g' $i
    sed -i 's/ 644/ -m 644/g' $i
done
%makeinstall_std

# install menu entries
mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Name=I-Nex
Comment=I-Nex, a system information tool
Exec=beesu %name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Utility;
EOF

cat > %buildroot%_desktopdir/%name-library.desktop << EOF
[Desktop Entry]
Version=1.0
Name=I-Nex Library
Comment=I-Nex System Library Information
Exec=%name --library
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Utility;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %oname/%name/logo/i-nex.0.4.x.png -resize ${N}x${N} $N.png;
install -D -m 0644 16.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

# not needed
rm -rf %buildroot%_docdir/%name

%files
%doc README.md
%_bindir/%{name}*
%_desktopdir/%name.desktop
%_desktopdir/%name-library.desktop
%_datadir/%name
%_pixmapsdir/%{name}*.png
%_iconsdir/hicolor/*/apps/%name.png
/lib/udev/rules.d/i2c_smbus.rules
%_man1dir/%{name}*.1*

%changelog
* Wed Aug 09 2017 Anton Midyukov <antohami@altlinux.org> 7.6.0-alt1
- Initial build for ALT Sisyphus (Thanks Rosa Team)
