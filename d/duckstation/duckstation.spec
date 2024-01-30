Name:           duckstation
Version:        git.20240126.e9a21c4
Release:        alt1
Summary:        Sony PlayStation(TM) Emulator
License:        GPL-3.0-or-later
URL:            https://github.com/stenzek/duckstation
Source:         %{name}-%{version}.tar.xz
Group:          Emulators
Patch0:         fix-build-error-va_list-has-not-been-declared.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(Pre): rpm-macros-ninja-build rpm-build-ninja 
BuildRequires:  cmake clang-devel clang-tools libstdc++-devel llvm17.0-devel lld17.0-devel
BuildRequires:  git
BuildRequires:  libSDL2-devel
BuildRequires:  libgtk+3-devel
BuildRequires:  qt6-base-devel qt6-tools-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libgbm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libalsa-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  xorg-proto-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libdbus-devel

%description
DuckStation is an simulator/emulator of the Sony PlayStation(TM) console, focusing on playability, speed, and long-term maintainability.
The goal is to be as accurate as possible while maintaining performance suitable for low-end devices.
"Hack" options are discouraged, the default configuration should support all playable games with only
some of the enhancements having compatibility issues.

A "BIOS" ROM image is required to to start the emulator and to play games.

%prep
%setup  -n %{name}-%{version}
#patch0 -p1

%build
%cmake .. \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DCMAKE_C_FLAGS="$CFLAGS -Wno-error=format-security" \
        -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-error=format-security" \
        -DCMAKE_EXE_LINKER_FLAGS_INIT="-fuse-ld=lld" \
        -DCMAKE_MODULE_LINKER_FLAGS_INIT="-fuse-ld=lld" \
        -DCMAKE_SHARED_LINKER_FLAGS_INIT="-fuse-ld=lld" \
        -DENABLE_DISCORD_PRESENCE=OFF \
        -DUSE_FBDEV=ON \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{_builddir}/%{name}-%{version}/%_cmake__builddir/bin/* %{buildroot}%{_libexecdir}/%{name}/

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/%{name}-qt %{buildroot}%{_bindir}/

install -d -m 0755 %{buildroot}%{_datadir}/pixmaps
ln -s %{_libexecdir}/%{name}/resources/images/duck.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Duckstation
Comment=%{summary}
Exec=%{_bindir}/%{name}-qt
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

%files

%doc LICENSE README.md
%{_bindir}/%{name}-qt
%{_libexecdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jan 30 2024 Artyom Bystrov <arbars@altlinux.org> git.20240126.e9a21c4-alt1
- update to new version

* Sat Jul 22 2023 Artyom Bystrov <arbars@altlinux.org> git.20230414.5fee6f5-alt1
- Initial build for Sisyphus