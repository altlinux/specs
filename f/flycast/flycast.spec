Name: flycast
Version: 2.0
Release: alt1
Summary: multi-platform Sega Dreamcast, Naomi, Naomi 2, and Atomiswave emulator
License: GPL-2.0
Group: Emulators
Url: https://github.com/flyinghead/flycast
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.xz

EXclusiveArch: x86_64

BuildRequires(Pre): cmake rpm-macros-cmake
BuildRequires: cmake gcc-c++ libzip-devel zlib-devel libGL-devel libxxhash-devel python3-dev git libSDL2-devel libcurl-devel liblua5.3-devel libpulseaudio-devel libao-devel libminiupnpc-devel glslang-devel libspirv-cross-devel libchdr-devel libvulkan-devel vulkan-tools 

%description
Flycast is a multi-platform Sega Dreamcast, Naomi, Naomi 2,
and Atomiswave emulator derived from reicast.

%prep
%setup
# Ensure unneeded deps are not bundled
	for dep in chdr dirent libretro-common libzip miniupnpc patches SDL vixl xxHash; do
		rm -rf core/deps/${dep}
	done

	# Skip alsa if flag not enabled
	use !alsa && sed -i -e '/find_package(ALSA)/d' CMakeLists.txt

	# Skip ao if flag not enabled
	use !ao && sed -i -e '/pkg_check_modules(AO/d' CMakeLists.txt

	# Skip lua if flag not enabled
	use !lua && sed -i -e '/find_package(Lua)/d' CMakeLists.txt

	# Skip pulseaudio if flag not enabled
	use !pulseaudio && sed -i -e '/pkg_check_modules(LIBPULSE/d' CMakeLists.txt

	# Unbundle glslang
	sed -i -e '/add_subdirectory(core\/deps\/glslang/{N;s/.*/find_library(GLSLANG libglslang.so)\nfind_library(SPIRV libSPIRV.so)\ntarget_link_libraries(${PROJECT_NAME} PRIVATE ${GLSLANG} ${SPIRV})/}' CMakeLists.txt || die
	sed -i -e '/include.*SPIRV/{s:":<glslang/:;s/"/>/}' core/rend/vulkan/shaders.h \
		core/rend/vulkan/compiler.cpp || die
##	sed -i -e '/maxMeshViewCountNV/a1,' core/rend/vulkan/compiler.cpp || die

	# Unbundle xxHash
	sed -i -e '/XXHASH_BUILD_XXHSUM/{N;N;s/.*/target_link_libraries(${PROJECT_NAME} PRIVATE xxhash)/}' CMakeLists.txt || die

	# Unbundle chdr
	sed -i -e '/add_subdirectory.*chdr/d' -e 's/chdr-static/chdr/' -e 's:core/deps/chdr/include:/usr/include/chdr:' CMakeLists.txt || die

	# Do not use ccache
	sed -i -e '/find_program(CCACHE_FOUND/d' CMakeLists.txt

	# Ensure static libs are not built
	sed -i -e '/BUILD_SHARED_LIBS/d' CMakeLists.txt

	# Vulkan-header
	sed -i -e '/add_subdirectory(core.*Vulkan-Headers)$/,/Vulkan::Headers/d' \
		-e '/core\/deps\/Vulkan-Headers\/include)/d' CMakeLists.txt
	# local fix for < 1.3.224
	sed -i -e '/^1,$/d' core/rend/vulkan/compiler.cpp
	sed -i -e '/swapchainExtent = /{s/= /&static_cast<VkExtent2D>(/;s/;/);/}' core/rend/vulkan/vulkan_context.cpp

	# Do not use ccache
	sed -i -e '/find_program(CCACHE_PROGRAM ccache)/d' CMakeLists.txt

%build
cmake -B build 	-DUSE_OPENGL=ON \
		-DUSE_VULKAN=OFF \
		-DUSE_HOST_LIBZIP=ON \
		-DWITH_SYSTEM_ZLIB=ON 

%make -C build

%install
install -d %buildroot%_bindir
install -d %buildroot%_man1dir
install -d %buildroot%_datadir/%name/mappings
mkdir -p %buildroot%_desktopdir

install -pDm755 build/%name %buildroot%_bindir
cp -r shell/linux/mappings/controller_*.cfg %buildroot%_datadir/%name/mappings

for N in 16 32 48 64 128;
do
install -D -m 0644 shell/linux/%name.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

install -D -m 0644 shell/linux/%name.desktop %buildroot%_desktopdir
install -D -m 0644 shell/linux/man/%name.1 %buildroot%_man1dir/

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Jan 19 2023 Artyom Bystrov <arbars@altlinux.org> 2.0-alt1
- initial build for ALT Sisyphus
