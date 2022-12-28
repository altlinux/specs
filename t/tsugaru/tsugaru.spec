Name: tsugaru
Version: 20220702
Release: alt3
Summary: It is an emulator of legendary Fujitsu FM TOWNS computer including Marty
Group: Emulators
License: BSD3
Url: https://github.com/captainys/TOWNSEMU

Source: %name-%version.tar
Source1: marty.png
Patch0: fix_build_wav2snd.patch
Patch1: fix_build_gui.patch

BuildRequires: gcc-c++
BuildRequires: zlib-devel ImageMagick-tools
BuildRequires: libstdc++-devel-static
BuildRequires: libopenal-devel
BuildRequires: libGLU-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: libalsa-devel 
BuildRequires: cmake rpm-macros-cmake

%description
It is an emulator of legendary Fujitsu FM TOWNS computer including Marty

%package utils
Group: Emulators
Summary: Utils for Tsugaru emulator
Requires: %name = %version-%release

%description utils
Utils for Tsugaru emulator

%package tests
Group: Emulators
Summary: Set of test data and programs for Tsugaru Emulator
Requires: %name = %version-%release

%description tests
Set of test data and programs for Tsugaru Emulator


%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1

%build
mkdir build
cd ./build
cmake ../src
%make_build
cd ../gui
mkdir build
cd ./build
cmake ../src
cmake --build main_gui

%install

mkdir -p %buildroot%_bindir/
install -D -m0755 gui/build/main_gui/Tsugaru_GUI %buildroot%_bindir/%name
install -D -m0755 build/main_cui/Tsugaru_CUI %buildroot%_bindir
install -D -m0755 build/cmdutil/chopbincue %buildroot%_bindir
install -D -m0755 build/cmdutil/flattenbincue %buildroot%_bindir
install -D -m0755 build/cmdutil/padbincue %buildroot%_bindir
install -D -m0755 build/cmdutil/wav2snd %buildroot%_bindir
install -D -m0755 build/cpputil/pathtest %buildroot%_bindir
install -D -m0755 build/discimg/bincue2wav %buildroot%_bindir
install -D -m0755 build/discimg/testcue %buildroot%_bindir
install -D -m0755 build/discimg/testiso %buildroot%_bindir
install -D -m0755 build/discimg/testmds %buildroot%_bindir
install -D -m0755 build/discimg/testmsf %buildroot%_bindir
install -D -m0755 build/resources/png2cpp %buildroot%_bindir
install -D -m0755 build/tests/disasm %buildroot%_bindir
install -D -m0755 build/tests/disasm_addr %buildroot%_bindir
install -D -m0755 build/tests/relpath %buildroot%_bindir
install -D -m0755 build/tests/truename %buildroot%_bindir
install -D -m0755 build/tests/vram_mapping %buildroot%_bindir
install -D -m0755 build/tests/wildcard %buildroot%_bindir
install -D -m0755 build/ym2612tests/maketonewav/maketonewav %buildroot%_bindir
install -D -m0755 build/ym2612tests/tonetest/tonetest %buildroot%_bindir
install -D -m0755 build/ym2612tests/vgmplayer/vgmplayer %buildroot%_bindir
install -D -m0755 build/lineparser/lineParserTest %buildroot%_bindir
mkdir -p %buildroot/%_datadir/%name
cp -R townsapp  %buildroot/%_datadir/%name
cp -R testdata  %buildroot/%_datadir/%name
cp -R symtables  %buildroot/%_datadir/%name

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Tsugaru
Comment=FM Towns emulator
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc readme.md LICENSE
%dir %_datadir/%name
%_bindir/%name
%_bindir/Tsugaru_CUI
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files utils
%_bindir/chopbincue
%_bindir/flattenbincue
%_bindir/padbincue
%_bindir/wav2snd
%_bindir/bincue2wav

%files tests
%_bindir/pathtest
%_bindir/testcue
%_bindir/testiso
%_bindir/testmds
%_bindir/testmsf
%_bindir/lineParserTest
%_bindir/disasm
%_bindir/disasm_addr
%_bindir/relpath
%_bindir/truename
%_bindir/vram_mapping
%_bindir/wildcard
%_bindir/maketonewav
%_bindir/tonetest
%_bindir/vgmplayer
%_bindir/png2cpp
%_datadir/%name

%changelog
* Thu Dec 29 2022 Artyom Bystrov <arbars@altlinux.org> 20220702-alt3
 - Add logo and desktop files

* Thu Sep 22 2022 Artyom Bystrov <arbars@altlinux.org> 20220702-alt2
 - change libwxGTK3.1-devel to libwxGTK3.2-devel

* Sat Jul 24 2022 Artyom Bystrov <arbars@altlinux.org> 20220702-alt1
 - initial release
