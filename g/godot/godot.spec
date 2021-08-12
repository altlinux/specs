%def_with server

%def_with builtin_bullet # need version >=2.88 to build against system library
%def_without builtin_enet
%def_without builtin_freetype
%def_without builtin_libogg
%def_without builtin_libpng
%def_without builtin_libtheora
%def_without builtin_libvorbis
%def_without builtin_libvpx
%def_without builtin_libwebp
%def_without builtin_mbedtls
%def_without builtin_opus
%def_without builtin_pcre2
%def_with builtin_recast
%def_with builtin_squish
%def_with builtin_thekla_atlas
%def_without builtin_zlib
%def_without builtin_zstd

Name: godot
Version: 3.1
Release: alt4

Summary: Godot Engine - Multi-platform 2D and 3D game engine
License: %mit
Group: Development/Tools
Url: https://godotengine.org/

Source0: godot-%version.tar
Source1: %name.desktop
Source2: %name-icon-48.png
Source3: %name.svg
# Workaround for GCC < 8.1 ICE on armv7hl
# https://github.com/godotengine/godot/issues/16100
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=79085
Patch0: godot-3.0.2-workaround-gcc-ice-armv7hl.patch
Patch1: fix-zstd-linking.patch
Patch2: fix-zstd-1.3.8.patch
#ExclusiveArch: x86_64 %ix86

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ ccache scons
BuildRequires: libX11-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: libudev-devel

%{!?_with_builtin_bullet:BuildRequires: libbullet-devel}
%{!?_with_builtin_enet:BuildRequires: libenet-devel}
%{!?_with_builtin_freetype:BuildRequires: libfreetype-devel}
%{!?_with_builtin_libogg:BuildRequires: libogg-devel}
%{!?_with_builtin_libpng:BuildRequires: libpng-devel}
%{!?_with_builtin_libtheora:BuildRequires: libtheora-devel}
%{!?_with_builtin_libvorbis:BuildRequires: libvorbis-devel}
%{!?_with_builtin_libvpx:BuildRequires: libvpx-devel}
%{!?_with_builtin_libwebp:BuildRequires: libwebp-devel}
%{!?_with_builtin_mbedtls:BuildRequires: libmbedtls13-devel}
%{!?_with_builtin_opus:BuildRequires: libopus-devel libopusfile-devel}
%{!?_with_builtin_pcre2:BuildRequires: libpcre2-devel}
%{!?_with_builtin_recast:BuildRequires: librecast-devel}
%{!?_with_builtin_squish:BuildRequires: libsquish-devel}
%{!?_with_builtin_thekla_atlas:BuildRequires: libtheklaatlas-devel}
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
%package        server
Summary:        Godot headless binary for servers
Group:          Games/Other

%description    server
This package contains the headless binary for the Godot game engine,
particularly suited for running dedicated servers.
%endif

#----------------------------------------------------------------------

%package        runner
Summary:        Shared binary to play games developed with the Godot engine
Group:          Games/Other

%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

#----------------------------------------------------------------------

%prep
%setup
%patch0 -p1
%{!?_with_builtin_zstd:%patch1 -p2}
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
%ifarch %e2k
# unsupported as of lcc 1.25.17 (mcst#6261)
sed -i  -e 's,-fno-tree-copy-prop,,' -e 's,-fno-tree-ccp,,' \
	-e 's,-fno-code-hoisting,,' modules/gdnative/SCsub
sed -i "s/'-Werror=return-type'/&, '-fno-error-always-inline'/" SConstruct
%endif

%build
%define subst_builtin() %{expand:%{1}=%%{?_with_%{1}:yes}}%{expand:%%{?_without_%{1}:no}}

%define godot_common_builtin_options \\\
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
	%{subst_builtin builtin_opus} \\\
	%{subst_builtin builtin_pcre2} \\\
	%{subst_builtin builtin_recast} \\\
	%{subst_builtin builtin_squish} \\\
	%{subst_builtin builtin_thekla_atlas} \\\
	%{subst_builtin builtin_zlib} \\\
	%{subst_builtin builtin_zstd} \\\
%nil

export GCC_USE_CCACHE=1
# Verbose build to see what exactly breaks next time
scons \
	%godot_common_builtin_options \
	platform=x11 \
	tools=yes \
	verbose=yes \
	target=release_debug \
    -j %__nprocs

# Build game runner (without tools)
scons \
	%godot_common_builtin_options \
	platform=x11 \
	tools=no \
	verbose=yes \
	target=release \
    -j %__nprocs

%if_with server
# Build headless version of the editor
scons \
	%godot_common_builtin_options \
	platform=server \
	tools=yes \
	verbose=yes \
	target=release_debug \
    -j %__nprocs
%endif

%install
install -Dm 0755 bin/godot.x11.opt.tools.* %buildroot%_bindir/%{name}
install -m755 bin/%{name}.x11.opt.[0-9]* %buildroot%_bindir/%{name}-runner
%if_with server
install -m755 bin/%{name}_server.x11.opt.tools.[0-9]* %buildroot%_bindir/%{name}-server
%endif

install -m 644 -D %name-icon-48.png %buildroot%_liconsdir/%name.png
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
install -m 644 -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/
mkdir -p %buildroot%_desktopdir/
install -m 644 -D %name.desktop %buildroot%_desktopdir/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%files runner
%doc AUTHORS.md COPYRIGHT.txt LICENSE.txt
%_bindir/%{name}-runner

%if_with server
%files server
%doc AUTHORS.md COPYRIGHT.txt LICENSE.txt
%_bindir/%{name}-server
%endif

%changelog
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
