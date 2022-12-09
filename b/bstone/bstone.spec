Name:     bstone
Version:  1.2.12
Release:  alt1

Summary:  Unofficial source port for Blake Stone series
License:  GPL2
Group:    Other
Url:      https://github.com/bibendovsky/bstone

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar
Patch0: bstone-1.2.12-fix-header.patch

BuildRequires(Pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake libSDL2-devel-static 

%description
BStone is unofficial source port for "Blake Stone" game series: "Aliens Of Gold" and "Planet Strike".

Features:

* High resolution vanilla rendering
* 3D-rendering
* Upscale texture filter
* Support for external textures
* Allows to customize control bindings
* 3D-audio
* Separate volume control of sound effects and music

Supported games:

* Aliens Of Gold (v1.0/v2.0/v2.1/v3.0) full or shareware
* Planet Strike (v1.0/v1.1)
    
Since all titles except shareware are not free you have
to own a copy of the game in order to play (see README.md for
more information about data assets wtat needed to play).

%prep
%setup

%patch0 -p1

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX='/usr/bin' \
    -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
    -DBSTONE_USE_STATIC_LINKING=0

%make_build -C %_cmake__builddir

%install
install -Dm0755 %_cmake__builddir/src/bstone %buildroot%_bindir/bstone

%files
%doc CHANGELOG.md README.md TODO.md  LICENSE
%_bindir/%name

%changelog
* Fri Dec 09 2022 Artyom Bystrov <arbars@altlinux.org> 1.2.12-alt1
- Initial build for Sisyphus
