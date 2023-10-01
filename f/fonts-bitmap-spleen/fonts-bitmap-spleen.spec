%define cname spleen

Name: fonts-bitmap-%cname
Version: 2.0.0
Release: alt1

Summary: Monospaced bitmap fonts
License: BSD-2-Clause
Group: System/Fonts/X11 bitmap
Url: https://www.cambus.net/spleen-monospaced-bitmap-fonts/
Vcs: https://github.com/fcambus/spleen

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-fonts
BuildRequires: bdftopcf

%description
Spleen is a monospaced bitmap font available in 6 sizes:

- 5x8
- 6x12
- 8x16
- 12x24
- 16x32
- 32x64

Each size is provided in the Glyph Bitmap Distribution Format (BDF), and
release tarballs contain the fonts in the following formats: `PCF`, `PSF`
(for the Linux console), `OTB`, `OTF`, `.dfont` for macOS users, and `FON`
for Windows users.

All font sizes contain all ISO/IEC 8859-1 characters (Basic Latin and Latin-1
Supplement Unicode block), Latin Extended-A characters, as well as Box Drawing,
Block Elements, and Braille Patterns Unicode blocks, except for the 5x8 and the
6x12 versions.

Due to character size constraints, the 5x8 version only contains printable
ASCII characters, the Braille Patterns Unicode block, and light Box Drawing
characters. Please also note that there is no OpenType version for this size.

As of Spleen 1.8.0, there is now a 6x12 version containing the same Unicode
blocks as the 5x8 version and the Latin-1 Supplement Unicode block.

As of Spleen 2.0.0, the 8x16, 16x32 and 32x64 versions have full support for
Code page 437 (IBM PC).

Spleen also has support for Powerline symbols out of the box.

The font name is a reference to Baudelaire.

%prep
%setup

%build
for size in $(ls -1 spleen-*.bdf | grep -oE '[[:digit:]]+x[[:digit:]]+'); do
    %_bindir/bdftopcf -t -o spleen-${size}.pcf spleen-${size}.bdf
    gzip spleen-${size}.pcf
done

%install
%bitmap_fonts_install %cname

%files -f %cname.files
%doc LICENSE AUTHORS README.md

%changelog
* Sun Oct 01 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Built for ALT Sisyphus.

