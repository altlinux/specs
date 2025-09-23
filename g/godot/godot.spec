%define _unpackaged_files_terminate_build 1
%def_with server
%define arch_alias %_arch
%ifarch aarch64
%define arch_alias arm64
%endif

%def_without builtin_bullet
%def_without builtin_certs
# embree 3
%def_with builtin_embree
%def_without builtin_enet
%def_without builtin_freetype
%def_without builtin_libogg
%def_without builtin_libpng
%def_without builtin_libtheora
%def_without builtin_libvorbis
%def_without builtin_libvpx
%def_without builtin_libwebp
# not packaged
%def_with builtin_wslay
%def_without builtin_mbedtls
%def_without builtin_miniupnpc
%def_without builtin_opus
%def_without builtin_pcre2
# not packaged
%def_with builtin_recast
%def_without builtin_squish
%def_without builtin_xatlas
%def_without builtin_zlib
%def_without builtin_zstd

Name: godot
Version: 3.6.1
Release: alt1

Summary: Libre game engine
License: %mit
Group: Development/Tools
Url: https://godotengine.org/
VCS: https://github.com/godotengine/godot.git

Source0: godot-%version.tar
Patch: godot-3.6.1-alt-unbundle-xatlas.patch
Patch1: godot-3.6.1-fedora-miniupnp228.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ ccache scons
BuildRequires: libX11-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: libudev-devel
# A copy of the imp module that was removed in Python 3.12.
# It shouldn't be used, should use `importlib.metadata` instead.
BuildRequires: python3-module-zombie-imp python3-module-distutils-extra

%{!?_with_builtin_bullet:BuildRequires: libbullet3-devel}
%{!?_with_builtin_enet:BuildRequires: libenet-devel}
%{!?_with_builtin_freetype:BuildRequires: libfreetype-devel}
%{!?_with_builtin_libogg:BuildRequires: libogg-devel}
%{!?_with_builtin_libpng:BuildRequires: libpng-devel}
%{!?_with_builtin_libtheora:BuildRequires: libtheora-devel}
%{!?_with_builtin_libvorbis:BuildRequires: libvorbis-devel}
%{!?_with_builtin_libvpx:BuildRequires: libvpx-devel}
%{!?_with_builtin_libwebp:BuildRequires: libwebp-devel}
%{!?_with_builtin_mbedtls:BuildRequires: libmbedtls13-devel}
%{!?_with_builtin_miniupnpc:BuildRequires: libminiupnpc-devel}
%{!?_with_builtin_opus:BuildRequires: libopus-devel libopusfile-devel}
%{!?_with_builtin_pcre2:BuildRequires: libpcre2-devel}
%{!?_with_builtin_recast:BuildRequires: librecast-devel}
%{!?_with_builtin_squish:BuildRequires: libsquish-devel}
%{!?_with_builtin_xatlas:BuildRequires: libxatlas-devel}
%{!?_with_builtin_zlib:BuildRequires: zlib-devel}
%{!?_with_builtin_zstd:BuildRequires: libzstd-devel}

%description
Godot Engine is a feature-packed, cross-platform game engine to create 2D and 3D
games from a unified interface. It provides a comprehensive set of common tools,
so that users can focus on making games without having to reinvent the wheel.
Games can be exported in one click to a number of platforms, including the major
desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and
web-based (HTML5) platforms.

#----------------------------------------------------------------------

%if_with server
%package server
Summary: Godot headless binary for servers
Group: Games/Other

%description server
This package contains the headless binary for the Godot game engine,
particularly suited for running dedicated servers.
%endif

#----------------------------------------------------------------------

%package runner
Summary: Shared binary to play games developed with the Godot engine
Group: Games/Other

%description runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

#----------------------------------------------------------------------

%prep
%setup
%autopatch -p1
%ifarch %e2k
# unsupported as of lcc 1.25.17 (mcst#6261)
sed -i  -e 's,-fno-tree-copy-prop,,' -e 's,-fno-tree-ccp,,' \
	-e 's,-fno-code-hoisting,,' modules/gdnative/SCsub
sed -i "s/'-Werror=return-type'/&, '-fno-error-always-inline'/" SConstruct
%endif
sed -i version.py \
  -e '/short_name/ s/godot/godot3/' \
  -e '/name/ s/Godot Engine/Godot Engine 3/' \
  #
pushd thirdparty
rm -rf \
  bullet \
  enet \
  freetype \
  libogg \
  libpng \
  libtheora \
  libvorbis \
  libvpx \
  libwebp \
  mbedtls \
  miniupnpc \
  opus \
  pcre2 \
  squish \
  xatlas \
  zlib \
  zstd \
  #
popd

%build
%define subst_builtin() %{expand:%1=%%{?_with_%1:yes}}%{expand:%%{?_without_%1:no}}

%define godot_common_builtin_options \\\
	%{subst_builtin builtin_certs} \\\
	%{subst_builtin builtin_bullet} \\\
	%{subst_builtin builtin_enet} \\\
	%{subst_builtin builtin_freetype} \\\
	%{subst_builtin builtin_libogg} \\\
	%{subst_builtin builtin_libpng} \\\
	%{subst_builtin builtin_libtheora} \\\
	%{subst_builtin builtin_libvorbis} \\\
	%{subst_builtin builtin_libvpx} \\\
	%{subst_builtin builtin_libwebp} \\\
	%{subst_builtin builtin_mbedtls} \\\
	%{subst_builtin builtin_miniupnpc} \\\
	%{subst_builtin builtin_opus} \\\
	%{subst_builtin builtin_pcre2} \\\
	%{subst_builtin builtin_recast} \\\
	%{subst_builtin builtin_squish} \\\
	%{subst_builtin builtin_xatlas} \\\
	%{subst_builtin builtin_zlib} \\\
	%{subst_builtin builtin_zstd} \\\
%nil

export GCC_USE_CCACHE=1
export BUILD_NAME="%release"
# Verbose build to see what exactly breaks next time
scons \
	%godot_common_builtin_options \
	platform=x11 \
	tools=yes \
	verbose=yes \
	target=release_debug \
	use_static_cpp=no \
	arch=%arch_alias \
	system_certs_path=%_datadir/ca-certificates/ca-bundle.crt \
    -j %__nprocs

# Build game runner (without tools)
scons \
	%godot_common_builtin_options \
	platform=x11 \
	tools=no \
	verbose=yes \
	target=release \
	use_static_cpp=no \
	arch=%arch_alias \
	system_certs_path=%_datadir/ca-certificates/ca-bundle.crt \
    -j %__nprocs

%if_with server
# Build headless version of the editor
scons \
	%godot_common_builtin_options \
	platform=server \
	tools=yes \
	verbose=yes \
	target=release_debug \
	use_static_cpp=no \
	arch=%arch_alias \
	system_certs_path=%_datadir/ca-certificates/ca-bundle.crt \
    -j %__nprocs
%endif

%install
install -Dm 0755 bin/godot.x11.opt.tools.* %buildroot%_bindir/godot
install -m755 bin/godot.x11.opt.%arch_alias %buildroot%_bindir/godot-runner
%if_with server
install -m755 bin/godot_server.x11.opt.tools.%arch_alias \
  %buildroot%_bindir/godot-server
%endif

mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
install -m 644 -D logo.svg %buildroot%_iconsdir/hicolor/scalable/apps/godot.svg
mkdir -p %buildroot%_desktopdir/
install -m 644 -D misc/dist/linux/org.godotengine.Godot.desktop \
  -t %buildroot%_desktopdir

%files
%_bindir/godot
%_desktopdir/org.godotengine.Godot.desktop
%_iconsdir/hicolor/scalable/apps/godot.svg

%files runner
%doc AUTHORS.md COPYRIGHT.txt LICENSE.txt
%_bindir/godot-runner

%if_with server
%files server
%doc AUTHORS.md COPYRIGHT.txt LICENSE.txt
%_bindir/godot-server
%endif

%changelog
* Tue Sep 23 2025 Constantin Sunzow <protvin@altlinux.org> 3.6.1-alt1
- Enable build on aarch64 architecture.
- New version.

* Fri Apr 25 2025 Constantin Sunzow <protvin@altlinux.org> 3.6-alt1
- Security fix: CVE-2021-26826.
- Security fix: CVE-2021-26825.
- NMU: new version (ALT 49110).

* Wed Sep 25 2024 Artyom Bystrov <arbars@altlinux.ru> 3.1-alt4.2
- NMU: Added distutils-extra to BuildRequires.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 3.1-alt4.1
- NMU: Added zombie-imp to BuildRequires.

* Thu Aug 12 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt4
- NMU: drop all python2 BR, drop openssl BR, cleanup all BR
- NMU: enable build with system opus

* Fri Jul 23 2021 Michael Shigorin <mike@altlinux.org> 3.1-alt3
- E2K: avoid lcc-unsupported options
- minor spec cleanup (incl. bogus changelog date fixup)

* Sun Jul 11 2021 Nazarov Denis <nenderus@altlinux.org> 3.1-alt2.1
- Fixed FTBFS (build with mbedTLS 2.27.0)

* Mon Mar 29 2021 Grigory Ustinov <grenka@altlinux.org> 3.1-alt2
- Fixed FTBFS (removed python-module-pyxdg from BR's)

* Mon Mar 18 2019 Sergey Bubnov <omg@altlinux.org> 3.1-alt1
- 3.1-stable

* Wed Jan 02 2019 Sergey Bubnov <omg@altlinux.org> 3.0.6-alt3
- fix for zstd-1.3.8

* Sat Oct 06 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt2
- NMU: merged features from autoimports build:
  * added runner binary and subpackage
  * added server binary and subpackage
  * added patch for armv7hl
- removed ExclusiveArch:

* Wed Sep 19 2018 Sergey Bubnov <omg@altlinux.org> 3.0.6-alt1
- 3.0.6-stable

* Sun Jun 10 2018 Sergey Bubnov <omg@altlinux.org> 3.0.2-alt2
- restrict arch as x86 and x86_64

* Sat Jun 9 2018 Sergey Bubnov <omg@altlinux.org> 3.0.2-alt1
- 3.0.2-stable
