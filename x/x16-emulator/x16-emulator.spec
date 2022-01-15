Name: x16-emulator
Version: r38
Release: alt3

Summary: Emulator for the Commander X16 computer system
License: BSD-2-Clause License
Group: Emulators

Url: https://www.commanderx16.com
Source0: %name-%version.tar
Source1: commanderx16-logo.png
Patch0: fix-rom-path.patch
# https://github.com/commanderx16/x16-emulator/pull/362/commits/fa963e7dc20c4782f29c390ef9d028180f6ae5da
Patch1: gcc11_workaround.patch

BuildRequires(pre): ImageMagick-tools
BuildRequires: libSDL2-devel
%ifnarch %e2k
BuildRequires: pandoc
%endif
Requires: x16-rom

%description
This is an emulator for the Commander X16 computer system.
It only depends on SDL2 and should compile on all modern
operating systems.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%ifnarch %e2k
pandoc --from gfm --to html -c github-pandoc.css --standalone --metadata pagetitle="X16 Emulator" README.md --output README.html
%endif

%make_build

%install
mkdir -p %buildroot%_docdir/%name/

install -Dm0644 %SOURCE1 %buildroot%_liconsdir/%name.png
install -Dm0755 x16emu %buildroot%_bindir/%name

%ifnarch %e2k
install -Dm644 README.html %buildroot%_docdir/%name/README.html
install -Dm644 github-pandoc.css %buildroot%_docdir/%name/github-pandoc.css
%endif

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=x16-emulator
Comment=Emulator for the Commander X16 computer system
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Emulator;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%doc README.md LICENSE
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%ifnarch %e2k
%_docdir/%name/README.html
%_docdir/%name/github-pandoc.css
%endif

%changelog
* Sat Jan 15 2022 Michael Shigorin <mike@altlinux.org> r38-alt3
- E2K: build without pandoc (unavailable for now)
- minor spec cleanup

* Fri Sep 24 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt2
- fixing build on gcc11

* Thu Jan 07 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt1
- initial build for ALT Sisyphus
