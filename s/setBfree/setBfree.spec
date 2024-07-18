
%define _unpackaged_files_terminate_build 1

Name: setBfree
Version: 0.8.13
Release: alt1
Summary: A DSP Tonewheel Organ emulator

License: GPLv2+ and GPLv3+ and ISC
Group: Sound
Url: http://setbfree.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: rpm-macros-fonts

# git grep -Eo -e '(--cflags|--exists|--libs)( [-+0-9a-z]+)+'  | tr ' ' '\n' | grep -v ':--' | sort -u
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(ftgl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(zlib)

# PKG_GL_LIBS
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)

BuildRequires: fonts-ttf-vera

Requires: fonts-ttf-vera

%description
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.

This package contains standalone (Jack) version.


%package -n lv2-setBfree-plugins
Summary: A DSP Tonewheel Organ emulator. LV2 version
Group: Sound
Requires: fonts-ttf-vera

%description -n lv2-setBfree-plugins
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.

This package contains setBfree build as LV2 plugin.


%prep
%setup
%autopatch -p1

%build
# Upstream adds x86-specific optimization flags by default.
# We're preserving most of them on x86_64, but we have other platforms.
%ifarch x86_64
%add_optflags -msse2 -mfpmath=sse -O3
%endif
%add_optflags -ffast-math -fno-finite-math-only

%make_build \
    OPTIMIZATIONS="%optflags" \
    VERSION=%version \
    FONTFILE=%_ttffontsdir/TrueType-vera/VeraBd.ttf \
    PREFIX=%prefix \
    INSTALL_EXTRA_LV2=yes \
    STRIP=: \
    lv2dir=%_libdir/lv2

%install
%makeinstall_std \
    OPTIMIZATIONS="%optflags" \
    VERSION=%version \
    FONTFILE=%_ttffontsdir/TrueType-vera/VeraBd.ttf \
    PREFIX=%prefix \
    INSTALL_EXTRA_LV2=yes \
    STRIP=: \
    lv2dir=%_libdir/lv2

mkdir -p %buildroot%_man1dir
install -Dm644 doc/*.1 %buildroot%_man1dir


%files
%doc AUTHORS ChangeLog README.md
%_bindir/setBfree
%_bindir/setBfreeUI
%_bindir/x42-whirl
%_datadir/%name
%_man1dir/*

%files -n lv2-setBfree-plugins
%doc AUTHORS ChangeLog README.md
%_libdir/lv2/*

%changelog
* Thu Jul 18 2024 Ivan A. Melnikov <iv@altlinux.org> 0.8.13-alt1
- 0.8.13

* Wed Jun 07 2023 Ivan A. Melnikov <iv@altlinux.org> 0.8.12-alt1
- 0.8.12

* Fri Jul 09 2021 Ivan A. Melnikov <iv@altlinux.org> 0.8.11-alt2.gitbdb2cc6
- install extra lv2 plugins
- avoid stripping binaries

* Wed Jun 02 2021 Ivan A. Melnikov <iv@altlinux.org> 0.8.11-alt1.gitbdb2cc6
- initial build for Sisyphus
  + build from snapshot for MIDINAM fixes
