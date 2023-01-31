Name: pom1
Version: 1.0.0
Release: alt1
Summary: Apple 1 emulator
License: GPL-2.0
Group: Emulators
Url: http://pom1.sourceforge.net
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://sourceforge.net/projects/pom1/files/pom1/%version/%name-%version.tar.gz
BuildRequires: libSDL-devel ImageMagick-tools

%description
Pom1 is an Apple 1 emulator ported to C and Android from the original Java version.
The port to C uses Simple DirectMedia Layer library and works on most platforms.

%prep
%setup

%build
# build section
%configure --docdir=%_docdir/packages
%make_build

%install
%make_build DESTDIR=%buildroot install

rm %buildroot%_iconsdir/%name.png
rm -rf %buildroot%_docdir

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Pom1
Comment=Apple I emulator
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert src/%name.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

install -d -m 755 %buildroot%_pixmapsdir
install -m 644 src/%name.png -t %buildroot%_pixmapsdir

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/%name
%_bindir/%name-%version
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/%name.png
%_datadir/%name

%changelog
* Tue Jan 31 2023 Artyom Bystrov <arbars@altlinux.org> 1.0.0-alt1
- initial build for ALT Sisyphus

* Fri Nov 25 2016 aloisio@gmx.com
- Update to version 1.0.0
- Dropped pom1-0.0.3.dif (changes included upstream)
- Spec cleanup
