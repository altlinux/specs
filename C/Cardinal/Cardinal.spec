
%define _unpackaged_files_terminate_build 1

Name:     Cardinal
Version:  22.12
Release:  alt1

Summary:  Virtual modular synthesizer plugin
License:  GPL-3.0-or-later
Group:    Sound
Url:      https://github.com/DISTRHO/Cardinal

ExclusiveArch: x86_64 aarch64

Source:   %name-%version.tar

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)

Patch1:   Cardinal-22.07-alt-lv2-in-lib64.patch
Patch2:   Cardinal-22.11-rebeltech-fix-compilation.patch
Patch3:   Cardinal-22.12-alt-more-system-libs.patch

BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrandr)

Requires: %name-common = %EVR

%description
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package provides Cardinal as standalone jack client.


%package -n lv2-Cardinal-plugins
Group:    Sound
Summary:  Virtual modular synthesizer -- LV2 plugin
Requires: %name-common = %EVR

%description -n lv2-Cardinal-plugins
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package provides Cardinal as LV2 plugin.


%package common
Group:    Sound
Summary:  Virtual modular synthesizer -- resources
BuildArch: noarch

%description common
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package contains common resources for Cardinal.


%prep
%setup

# unpack sub-merged sources
sh "%SOURCE2"

# don't build VST plugin variants
sed -i '/^TARGETS/ s/vst[23]\|clap//g' src/Makefile.cardinal.mk

%autopatch -p0

%build
%make_build \
    NOOPT=true \
    SKIP_STRIPPING=true \
    PREFIX=/usr \
    SYSDEPS=true \
    WITH_LTO=true \
    AR=gcc-ar \
    VERBOSE=1

%install
# standalone
install -Dm755 bin/Cardinal %buildroot%_bindir/Cardinal

# resources
install -d %buildroot%_datadir/cardinal/
cp -rL bin/Cardinal.lv2/resources/* %buildroot%_datadir/cardinal/

# lv2
for plugin in Cardinal CardinalFX CardinalSynth; do
    src="bin/$plugin.lv2"
    dst="%buildroot%_libdir/lv2/$plugin.lv2"

    install -d "$dst"
    install -m644 "$src"/*.so "$dst"
    install -m644 "$src"/*.ttl "$dst"
    ln -sr %buildroot%_datadir/cardinal/ "$dst"/resources
done

# docs
install -d %buildroot%_datadir/doc/cardinal/docs
install -m 644 README.md %buildroot%_datadir/doc/cardinal/
install -m 644 docs/*.md docs/*.png %buildroot%_datadir/doc/cardinal/docs/


%files
%_bindir/*

%files -n lv2-Cardinal-plugins
%_libdir/lv2/*

%files common
%_datadir/cardinal
%doc %_datadir/doc/cardinal

%changelog
* Thu Dec 29 2022 Ivan A. Melnikov <iv@altlinux.org> 22.12-alt1
- 22.12
- Link with system libfmt and libsamplerate.

* Mon Nov 28 2022 Ivan A. Melnikov <iv@altlinux.org> 22.11-alt1
- 22.11

* Sat Oct 15 2022 Ivan A. Melnikov <iv@altlinux.org> 22.10-alt1
- 22.10

* Mon Sep 19 2022 Ivan A. Melnikov <iv@altlinux.org> 22.09-alt1
- 22.09

* Wed Aug 10 2022 Ivan A. Melnikov <iv@altlinux.org> 22.07-alt2
- Fix build with LTO on certain systems

* Mon Aug 08 2022 Ivan A. Melnikov <iv@altlinux.org> 22.07-alt1
- Initial build for Sisyphus
