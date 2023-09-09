%define _unpackaged_files_terminate_build 1
%define libname libsfizz1

Name:     sfizz
Version:  1.2.2
Release:  alt2

Summary:  SFZ parser and synthesizer
License:  BSD-2-Clause
Group:    Sound
#Vcs:     https://github.com/sfztools/sfizz-ui
Url:      https://sfz.tools/sfizz/

ExcludeArch: %arm ppc64le


Source: %name-ui-%version.tar
Source1:  sub-merge.sources.txt
Source2:  sub-merge.unpack.sh

# https://github.com/sfztools/sfizz/issues/1180
Patch1: sfizz-alt-fix-assertion-failed.patch

# import sub-merge sources here
%(cat %SOURCE1)

BuildRequires: cmake gcc-c++
# BuildRequires: libabseil-cpp-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(gio-2.0)

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)


%description
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.


%package tools
Summary: SFZ parser and synthesizer tools
Group:   Sound

%description tools
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

This package includes the following tools:
- sfizz_render: render a midi file through an SFZ file;
- sfizz_jack: standalone synthesizer for Jack.


%package -n lv2-%name-plugin
Summary: SFZ parser and synthesizer as LV2 plugin
Group:   Sound

%description -n lv2-%name-plugin
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

This package includes LV2 plugins that enable use of
SFZ instruments in any LV2-compatible host.


%package -n %libname
Summary: SFZ parser and synthesizer library
Group:   Sound

%description  -n %libname
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.

This package includes its shared library.


%package -n %libname-devel
Summary: Development files for %libname
Group:   Development/C++

%description -n %libname-devel
sfizz is a sample-based musical synthesizer.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.

This package contains include files, libraries and other files
needed for developing applications that use libsfizz.

%prep
%setup -n %name-ui
sh '%SOURCE2'

%autopatch -p1

%build
# TODO: -DSFIZZ_USE_SYSTEM_ABSEIL=ON -- currently this way it does not build

%cmake \
    -DLV2_PLUGIN_INSTALL_DIR=%_libdir/lv2 \
    -DPLUGIN_LV2_PSA=ON \
    -DPLUGIN_VST2=OFF \
    -DPLUGIN_VST3=OFF \
    -DPLUGIN_PUREDATA=OFF \
    -DSFIZZ_USE_SNDFILE=OFF \
    -DSFIZZ_TESTS=ON \
    -DSFIZZ_DEVTOOLS=ON

%cmake_build

%install
%cmakeinstall_std

%check
binary=$(realpath "%_cmake__builddir/library/bin/sfizz_tests")
cd library/tests && "$binary"

%files tools
%_bindir/*
%_man1dir/*

%files -n lv2-%name-plugin
%_libdir/lv2/%{name}*

%files -n %libname
%_libdir/*.so.*
%doc README.md

%files -n %libname-devel
%_includedir/sfizz*
%_libdir/*.so
%_pkgconfigdir/sfizz*


%changelog
* Sat Sep 09 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.2-alt2
- fix assertion failure for sustained notes

* Sat Sep 09 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.2-alt1
- 1.2.2
- switch to sfizz-ui for main upstream git

* Wed May 10 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Jul 01 2022 Ivan A. Melnikov <iv@altlinux.org> 1.2.0-alt1.git77fbfa50
- 1.2.0
- build from the develop branch snapshot
  + voice-stealing fix
  + doap:name for sfizz-multi fix
- disable (broken) sndfile integration
  (https://github.com/sfztools/sfizz/issues/1090)
- fix building tests with recent glibc

* Wed Jul 07 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt2.git07260b13
- Build from develop branch snapshot
  + fixes crash with Ardour 6+ (https://github.com/sfztools/sfizz/issues/884).
- Enable PSA for LV2 plugin

* Fri May 28 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
