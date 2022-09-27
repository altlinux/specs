
%define oname invada-studio-plugins-lv2

Name:    lv2-invada-plugins
Version: 1.2.0
Release: alt2

Group:   Sound
Summary: A collection of LV2 plugins from Invada Records

License: GPLv2-or-later
URL:     http://launchpad.net/invada-studio

Source: %oname-%version.tar

Patch101: 101-denormals-in-meters-and-phase-rename.patch
Patch103: 103-fixed_wrong_graph_in_compressor_gui.patch
Patch105: 105-denormal.patch
Patch106: 106-segfault-when-closing-gui.patch
Patch107: 107-ttl-fix.patch


BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(cairo)

%description
A collection of LV2 plugins:
* Delay Munge - two channel delay with non-linear feedback;
* Tube - valve warmth/distortion simulation;
* Compressor - peak/RMS softclipping compressor;
* ER Reverb - early reflection based reverb;
* Gentle low and high pass filters;
* Stereo Phaser;
* Meters - peak, VU, phase and spectrograph;
* Input Module - alter gain, balance, width, phase on a stereo signal;
* Test Tones - generates test tones at standard and muscial frequencies.

%prep
%setup -n %oname-%version
%autopatch -p0

# Make make more verbose and LTO-friendly; make it respect %%optflags
find . -name Makefile -exec sed -i \
    -e 's|@$(CC)|$(CC)|'  \
    -e 's|@$(LD)|$(LD)|'  \
    -e 's|@ar\b|gcc-ar|'  \
    -e '/^CFLAGS\s*=/ s|$| %optflags|'  \
    -e '/^LDFLAGS\s*=/ s|$| %optflags|' \
    '{}' ';'

%build
%make_build

%install
%make_install install-sys \
    DESTDIR=%buildroot \
    INSTALL_SYS_PLUGINS_DIR="%_libdir/lv2"

%files
%_libdir/lv2/*

%changelog
* Mon Aug 22 2022 Ivan A. Melnikov <iv@altlinux.org> 1.2.0-alt2
- applied latest fixes from upstream

* Fri Aug 12 2022 Ivan A. Melnikov <iv@altlinux.org> 1.2.0-alt1
- build for Sisyphus
