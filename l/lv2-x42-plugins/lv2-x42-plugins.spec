
%define _unpackaged_files_terminate_build 1
%define oname x42-plugins

Name: lv2-%oname
Version: 20221101
Release: alt1
Summary: Collection of LV2 plugins

License: GPLv2+ and ISC
Group: Sound

# https://x42-plugins.com/x42/ is more about binary builds
Url: https://github.com/x42/x42-plugins

# This package uses tarball from http://gareus.org/misc/x42-plugins.php
Source: %oname-%version.tar

BuildRequires: rpm-macros-fonts
BuildRequires: gcc-c++
BuildRequires: zita-convolver-devel

# git grep -Eo -e '(--cflags|--exists|--libs)( [-+0-9a-z]+)+'  | tr ' ' '\n' | grep -v -e '--' | sort -u
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(ftgl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(ltc)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(zlib)

BuildRequires: fonts-ttf-gnu-freefont-sans
Requires: fonts-ttf-gnu-freefont-sans

%description
A collection of lv2 plugins including stereo balance,
midi filter, delay, convolver, fader, parametric equalizer,
auto-tune, awesome meters collection and others.

%prep
%setup -n %oname-%version

%build
# Upstream adds x86-specific optimization flags by default.
# We're preserving most of them on x86_64, but we have other platforms.
%add_optflags -ffast-math -fno-finite-math-only -DNDEBUG
%ifarch x86_64
%add_optflags -msse2 -mfpmath=sse -O3
%endif

%make_build \
        LIBDIR=%_libdir LV2DIR=%_libdir/lv2 PREFIX=%prefix \
        FONTFILE="%_ttffontsdir/gnu-free/FreeSansBold.ttf" \
        STRIP=: OPTIMIZATIONS="%optflags" \
        VERSION=%version

%install
%makeinstall_std \
        LIBDIR=%_libdir LV2DIR=%_libdir/lv2 PREFIX=%prefix \
        FONTFILE="%_ttffontsdir/gnu-free/FreeSansBold.ttf" \
        STRIP=: OPTIMIZATIONS="%optflags" \
        VERSION=%version

%files
%doc plugin.versions plugin.list plugin.news
%_libdir/lv2/*.lv2
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 16 2022 Ivan A. Melnikov <iv@altlinux.org> 20221101-alt1
- 20221101

* Thu Sep 29 2022 Ivan A. Melnikov <iv@altlinux.org> 20220923-alt1
- 20220923

* Thu Aug 04 2022 Ivan A. Melnikov <iv@altlinux.org> 20220714-alt1
- 20220714

* Thu Jun 16 2022 Ivan A. Melnikov <iv@altlinux.org> 20220605-alt1
- 20220605

* Thu May 12 2022 Ivan A. Melnikov <iv@altlinux.org> 20220327-alt1
- 20220327

* Sat Jan 22 2022 Ivan A. Melnikov <iv@altlinux.org> 20220107-alt1
- 20220107

* Tue Nov 02 2021 Ivan A. Melnikov <iv@altlinux.org> 20211016-alt1
- 20211016

* Fri Jul 16 2021 Ivan A. Melnikov <iv@altlinux.org> 20210714-alt1
- 20210714

* Fri Jun 04 2021 Ivan A. Melnikov <iv@altlinux.org> 20210409-alt1
- Initial build for Sisyphus
