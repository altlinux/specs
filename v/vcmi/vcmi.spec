%set_verify_elf_method unresolved=relaxed

Name: vcmi
Version: 0.93
Release: alt1

Summary: Open-source project aiming to reimplement HMM3:WoG game engine
License: GPLv2+
Group: Games/Strategy
URL: http://wiki.vcmi.eu/index.php?title=Main_Page

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

# Automatically added by buildreq on Sat Jun 22 2013
# optimized out: boost-devel boost-intrusive-devel cmake cmake-modules libSDL-devel libavcodec-devel libavutil-devel libopencore-amrnb0 libopencore-amrwb0 libstdc++-devel pkg-config
BuildRequires:  boost-asio-devel boost-devel-headers boost-filesystem-devel boost-interprocess-devel boost-program_options-devel ctest gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libavdevice-devel libavformat-devel libfreetype-devel libpostproc-devel libswscale-devel zlib-devel

%description
The purpose of VCMI project is to rewrite entire HOMM 3: WoG engine from
scratch, giving it new and extended possibilities. We hope to support mods and
new towns already made by fans but abandoned because of game code limitations.

VCMI is fan-made open-source project in progress. We already allow support for
maps of any sizes, higher resolutions and extended engine limits. However,
although working, the game is not finished. There are still many features and
functionalities to add, both old and brand new.

As yet VCMI is not standalone program, it uses Wake of Gods files and graphics.
You need to install WoG before running VCMI.

%prep
%setup -q

%build
%cmake_insource -DCMAKE_SKIP_RPATH=OFF
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README README.linux
%_bindir/*
%_libdir/%name/*
%_datadir/%name/*
%_desktopdir/*
%_datadir/icons/*/*/apps/vcmiclient.png

%changelog
* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.93-alt1
- build for Sisyphus (closes #28586)

* Sun Oct 21 2012 VCMI - 0.9-2
- Second release of 0.9, Fixed battles crash

* Sat Oct 06 2012 VCMI - 0.9-1
- New upstream release

* Sun Jun 08 2012 VCMI - 0.89-1
- Initial version
