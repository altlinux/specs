Name: unvanquished
Version: 0.55.2
Release: alt1

Summary: An FPS/RTS hybrid game powered by the Daemon engine (a combination of ioq3 and XreaL)
License: BSD-3-Clause and CC-BY-SA-4.0 and Zlib and MIT and GPL-2.0-or-later and GPL-3.0-or-later and FTL and CC-BY-SA-2.5
Group: Games/Other

Url: https://unvanquished.net
Vcs: https://github.com/Unvanquished/Unvanquished

Source0: %name-%version.tar
Source1: daemon.tar
Source2: libs.tar

# https://dl.unvanquished.net/deps/
Source3: linux-amd64-default_10.tar
Source4: linux-arm64-default_10.tar
Source5: linux-i686-default_10.tar

ExclusiveArch: x86_64

BuildRequires(Pre): rpm-macros-cmake rpm-build-cmake
BuildRequires: cmake clang libstdc++-devel qt6-base-devel llvm-devel
BuildRequires: zlib-devel libncursesw-devel libnettle-devel
BuildRequires: libcurl-devel libSDL2-devel libogg-devel libvorbis-devel
BuildRequires: libopusfile-devel libwebp-devel libjpeg-devel libpng-devel 
BuildRequires: libGLEW-devel libopenal-devel liblua5.4-devel libfreetype-devel
BuildRequires: libharfbuzz-devel libcairo-devel python3-module-jinja2
BuildRequires: python3-module-yaml gzip

%description
Unvanquished is an arena game with RTS elements (you can build) in which two very different factions fight.

%prep
%setup
tar -xf %SOURCE1 -C %_builddir/%name-%version/
tar -xf %SOURCE2 -C %_builddir/%name-%version/

%ifarch x86_64
 tar -xf %SOURCE3 -C daemon/external_deps/
%endif
%ifarch aarch64
 tar -xf %SOURCE4 -C daemon/external_deps/
%endif
%ifarch i586
 tar -xf %SOURCE5 -C daemon/external_deps/
%endif

%build
export CC=clang
export CXX=clang++
mkdir %_arch-alt-linux
cd %_arch-alt-linux
cmake ..
make -j%__nprocs
%ifarch x86_64
 gzip -c irt_core-amd64.nexe > irt_core-amd64.nexe.gz
%endif
%ifarch aarch64
 gzip -c irt_core-armhf.nexe > irt_core-armhf.nexe.gz
%endif
%ifarch i586
 gzip -c irt_core-i686.nexe > irt_core-i686.nexe.gz
%endif
cd ..

%install
# In this block I took part of the specification of the unassembled project oficerovas@
install -D %_arch-alt-linux/daemon %buildroot%_libdir/%name/daemon
install -D %_arch-alt-linux/daemonded %buildroot%_libdir/%name/daemonded
install -D %_arch-alt-linux/daemon-tty %buildroot%_libdir/%name/daemon-tty
install -D %_arch-alt-linux/nacl_helper_bootstrap %buildroot%_libdir/%name/nacl_helper_bootstrap
install -D %_arch-alt-linux/nacl_loader %buildroot%_libdir/%name/nacl_loader

%ifarch x86_64
 cp -r %_arch-alt-linux/irt_core-amd64.nexe %buildroot%_libdir/%name/irt_core-amd64.nexe
 cp -r %_arch-alt-linux/irt_core-amd64.nexe.gz %buildroot%_libdir/%name/irt_core-amd64.nexe.gz
%endif
%ifarch aarch64
 cp -r %_arch-alt-linux/irt_core-armhf.nexe %buildroot%_libdir/%name/irt_core-armhf.nexe
 cp -r %_arch-alt-linux/irt_core-armhf.nexe.gz %buildroot%_libdir/%name/irt_core-armhf.nexe.gz
 cp -r %_arch-alt-linux/nacl_helper_bootstrap-armhf %buildroot%_libdir/%name/nacl_helper_bootstrap-armhf
 #mkdir -p %buildroot%_libdir/%name/lib-armhf/
 #install -D %_arch-alt-linux/lib-armhf/* %buildroot%_libdir/%name/lib-armhf/
%endif
%ifarch i586
 cp -r %_arch-alt-linux/irt_core-i686.nexe %buildroot%_libdir/%name/irt_core-i686.nexe
 cp -r %_arch-alt-linux/irt_core-i686.nexe.gz %buildroot%_libdir/%name/irt_core-i686.nexe.gz
%endif
for r in 32 64 128 256 512
do
 install -Dm 0644 dist/icons/${r}x${r}/%name.png %buildroot%_iconsdir/hicolor/${r}x${r}/apps/%name.png
done

cat >> %name <<EOF
#!/bin/sh
exec %_libdir/%name/daemon -pakpath %{_datadir}/%{name}/pkg
EOF
 
cat >> %name-server <<EOF
#!/bin/sh
exec %_libdir/%name/daemonded -pakpath %{_datadir}/%{name}/pkg
EOF

install -D %name %buildroot%_bindir/%name
install -D %name-server %buildroot%_bindir/%name-server

cat >> %name.desktop <<EOF
[Desktop Entry]
Categories=Game;ActionGame;
Name=Unvanquished
GenericName=An FPS/RTS hybrid game powered by the Daemon engine
Type=Application
Exec=%name
Icon=%name
EOF

install -Dm 644 %name.desktop %buildroot%_datadir/applications/%name.desktop

%post
%ifarch x86_64
 rm %_libdir/%name/irt_core-amd64.nexe
 gunzip -f %_libdir/%name/irt_core-amd64.nexe.gz
 gzip -c %_libdir/%name/irt_core-amd64.nexe > %_libdir/%name/irt_core-amd64.nexe.gz
%endif
%ifarch aarch64
 rm %_libdir/%name/irt_core-armhf.nexe
 gunzip -f %_libdir/%name/irt_core-armhf.nexe.gz
 gzip -c %_libdir/%name/irt_core-armhf.nexe > %_libdir/%name/irt_core-armhf.nexe.gz
%endif
%ifarch i586
 rm %_libdir/%name/irt_core-i686.nexe
 gunzip -f %_libdir/%name/irt_core-i686.nexe.gz
 gzip -c %_libdir/%name/irt_core-i686.nexe > %_libdir/%name/irt_core-i686.nexe.gz
%endif

%files
%_bindir/*
%_libdir/%name/*
%_iconsdir/hicolor/*/*/*.png
%_datadir/applications/%name.desktop
%doc *.md *.txt

%changelog
* Sun Feb 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.2-alt1
- Initial build for ALT Linux.

