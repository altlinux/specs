Name: xnp21kai
Version: rev.22
Release: alt1
Summary: PC-9801 series emulator	
Group: Emulators
License: BSD3
Url: http://domisan.sakura.ne.jp/article/np2kai/np2kai.html

Source: %name-%version.tar
Patch0: delete-git-CMakefiles.patch

BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libopenal-devel
BuildRequires: libalsa-devel
BuildRequires: cmake rpm-macros-cmake
BuildRequires: libusb-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libpcre-devel bzlib-devel libpng-devel libbrotli-devel libuuid-devel libX11-devel libexpat-devel libgtk+2-devel libssl-devel

ExcludeArch: armh

%description
PC-9801 series emulator


%prep
%setup -n %name-%version
%patch0 -p1

%build
%cmake
%cmake_build

%install

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Type=Application
Name=NP2kai
GenericName=PC-9801 Emulator
GenericName[ja]=PC-9801エミュレータ
Comment=PC-9801 Emulator
Comment[ja]=PC-9801エミュレータ
Exec=%name
Icon=%name
Categories=Game;Emulator;
Name[ja]=NP2kai
EOF

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
mkdir -p %buildroot%_datadir/%name

install -D -m0755 %_arch-alt-linux/xnp21kai %buildroot%_bindir/%name
install -D -m0755 misc/np2.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -D -m0755 %_arch-alt-linux/xnp21kai.1 %buildroot%_man1dir/%name.1
install -D -m0755 %_arch-alt-linux/xnp21kai.1j %buildroot%_man1dir/%name.1.j
cp x/resources/* %buildroot%_datadir/%name

%files
%doc README.md LICENSE
%dir %_datadir/%name
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man1dir/%name.1.*

%changelog
* Thu Aug 4 2022 Artyom Bystrov <arbars@altlinux.org> rev.22-alt1
 - initial release
