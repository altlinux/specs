%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: satdump
Version: 1.2.2
Release: alt1.git20250923.b79af48

Summary: Generic satellite data processing software
License: GPL-3.0-only
Group: Engineering
Url: https://github.com/SatDump/SatDump

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(OpenCL)
BuildRequires: pkgconfig(armadillo)
BuildRequires: pkgconfig(volk)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: libnng-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(hdf5)
BuildRequires: pkgconfig(jemalloc)
BuildRequires: libgomp-devel
BuildRequires: libstdc++-devel-static

# Hardware
BuildRequires: pkgconfig(libairspy)
# BuildRequires: pkgconfig(libhydrasdr) # TODO
# BuildRequires: pkgconfig(libairspyhf) # TODO
BuildRequires: pkgconfig(libhackrf)
BuildRequires: limesuite
BuildRequires: pkgconfig(libiio)
# BuildRequires: pkgconfig(libad9361) # TODO
BuildRequires: pkgconfig(libbladeRF)
BuildRequires: pkgconfig(librtlsdr)
BuildRequires: pkgconfig(uhd)

BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: zenity

BuildRequires: /usr/bin/magick

# no UHD on i586
ExcludeArch: %ix86

Requires: satdump-data = %{version}-%{release}
Requires: zenity

%description
%summary.

This package provides satdump GUI, CLI and server.

%package data
Summary: Data files for satdump
Group: Engineering
BuildArch: noarch

%description data
%summary.

This package provides data files of satdump.

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=Audio;HamRadio;AudioVideo;|' satdump.desktop

%build
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%ifarch x86_64 aarch64
       -DUSE_SIMD_OPTIMIZATIONS=ON
%else
       -DUSE_SIMD_OPTIMIZATIONS=OFF
%endif
%cmake_build

%install
%cmake_install

install -D -p -m644 resources/icon.png \
        %buildroot%_iconsdir/hicolor/512x512/apps/satdump.png

for size in 16 24 32 48 64 128 256; do
  mkdir -p %buildroot%_iconsdir/hicolor/${size}x${size}/apps ;
  magick resources/icon.png -filter Lanczos -resize ${size}x${size} %buildroot%_iconsdir/hicolor/${size}x${size}/apps/satdump.png ;
done

%files
%doc README.md cli_example.png gui_*.png
%_bindir/satdump
%_bindir/satdump-ui
%_bindir/satdump_sdr_server
%_desktopdir/satdump.desktop
%_iconsdir/hicolor/*/apps/satdump.png
%_libdir/libsatdump_core.so
%_libdir/libsatdump_interface.so
%dir %_libdir/satdump
%dir %_libdir/satdump/plugins
%_libdir/satdump/plugins/*.so

%files data
%dir %_includedir/satdump
%_includedir/satdump/*
%dir %_datadir/satdump
%_datadir/satdump/*

%changelog
* Fri Jun 19 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.2-alt1.git20250923.b79af48
- Initial build for Sisyphus
