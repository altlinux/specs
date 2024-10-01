Name:           deutex
Version:        5.2.2
Release:        alt1
Summary:        WAD composer for Doom and related games
License:        GPL-2.0-or-later
Group:          Editors
#Historic-URL:  http://www.teaser.fr/~amajorel/deutex/
URL:            https://github.com/Doom-Utils/deutex
Source:         %name-%version.tar
BuildRequires:  asciidoc asciidoc-a2x
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  zstd

%description
DeuTex is a .wad file composer for Doom, Heretic, Hexen and Strife.
It can be used to extract the lumps of a WAD and save them as
individual files. Conversely, it can also build a WAD from separate
files. When extracting a lump to a file, it does not just copy the
raw data, it converts it to an appropriate format (such as PNG for
graphics, WAVE for audio samples, etc.). Conversely, when it reads
files for inclusion in PWADs, it does the necessary conversions (for
example, from PPM to Doom picture format). In addition, DeuTex has
functions such as merging WADs.

%prep
%setup

%build
autoreconf -fiv
%configure --enable-man
%make_build

%install
%makeinstall_std

%files
%doc COPYING COPYING.LIB
%_bindir/*
%_man6dir/%name.6.xz

%changelog
* Tue Oct  1 2024 Artyom Bystrov <arbars@altlinux.org> 5.2.2-alt1
- Initial commit for Sisyphus.

* Thu Apr 29 2021 Ferdinand Thiessen <rpm@fthiessen.de>
- Update to new upstream release 5.2.2
  * Hexen graphics are now treated a bit more specially,
    the last entry in the palette no longer counting as a candidate
    to produce transparency in the output file.
* Fri Aug 23 2019 Jan Engelhardt <jengelh@inai.de>
- Update to new upstream release 5.2.1
  * DeuTex supports textures in TX_START and TX_END markers
    (introduced in ZDoom in 2003). These are used by certain
    editors/engines for textures, with support for storing PNG and
    JPEG files directly in the WAD. Extraction is likewise handled
    for all formats.
* Sun Sep 16 2018 Avindra Goolcharan <avindra@opensuse.org>
- update to 5.1.2
  * fix segfault with --help
- partial cleanup with spec-cleaner
* Tue Jan  9 2018 avindra@opensuse.org
- update to 5.1.1
  * Fixed: texture name array: the maximum possible string size is
    now supported.
  * Fixed: some warnings and errors with old versions of pkg-config
    and gcc
  * Fixed: Aliasing errors (caused crashes on some architectures,
    such as sparc64)
  * Can now build WADs with an arbitrary number of lumps. A warning
    is emitted when more than 4046 are included (vanilla Doom limit).
- remove 0001-increase-array-size-for-char-tname-variable-51.patch
  * upstreamed in 7024dd74a33780ef2dbdf614f4e52526cc3ab457
- remove 0001-Fix-strict-aliasing-violations.patch
  * upstreamed in 85d821dd3c145be1a998ca2a704930caaad73030
- remove deutex-proto.diff
  * upstreamed in 07bd0a5083fc15db20bee9056511bd3e10dd1362
- remove deutex-nolimit.diff
  * fixed in f8b1336bbcb7bc387d3e856cc7c9f75697cd0f0b
- remove deprecated BuildRoot option
* Mon Jan  1 2018 jengelh@inai.de
- Add 0001-increase-array-size-for-char-tname-variable-51.patch,
  0001-Fix-strict-aliasing-violations.patch
- Explain some changelog entries better.
* Mon Jan  1 2018 avindra@opensuse.org
- update to 5.1.0
  * The -overwrite option now works.
  * Levels are extracted/inserted in a way to preserve GL nodes.
  * Inserting pictures with a height of 1 pixel no longer causes
    a malloc error, and allows the operation of rebuilding a
    Doom 1 or 2 IWAD.
  * Texture lump file names can now be overridden.
  * Support reading and writing sprite offsets based on PNG
    "grAb" chunks (cf. grabpng package) in a manner compatible
    with SLADE and ZDoom. wadinfo.txt overrides these offsets
    unless -pngoffsets is used.
- includes 5.0.0
  * Removed DeuSF program mode.
  * Removed command line options used by WinTex.
  * Removed MS-DOS and OS/2 support code.
  * Removed the "-man" option from deutex.
  * Removed incomplete Rise of the Triad support.
  * PNG support added. This is the default extraction format now.
  * Sun Audio (.au) and Creative .voc sound file format support
    has been removed. RIFF WAVE is the only supported format.
  * Full sound lumps from the WAD are always extracted (-fullsnd
    option).
  * MIDI files can be included just by being named *.mid, and are
    extracted to the same file name extension.
  * Log file support has been removed, in favor of the user doing
    a shell redirection (e.g. with > or 2>) instead.
  * Arch-vile sprites are now extracted and inserted using
    literal names for sprites with the '[' and ']' characters in
    names (were illegal in DOS), and sprite names with '\' are
    now altered to use '^' on-disk, matching the ZDoom PK3
    standard.
  * Graphics with a height > 128 and < 256 are now inserted into
    Doom WAD files correctly.
  * UDMF (Universal Doom Map Format) support.
- remove patches obsoleted by upstream cleanup and refactoring
  * deutex-automake.diff
  * deutex-braces.diff
  * deutex-init-stdfp.diff
  - check_types removed (b76fafa6fee9a64929e7b1087ac36ea3ce39e27d)
  * deutex-soundbuf.diff
- rebase deutex-proto.diff
- rebase deutex-nolimit.diff
- renumber patches
* Fri Jul  7 2017 jengelh@inai.de
- Add deutex-nolimit.diff: raise limit for WAD directory reading
* Wed Feb 22 2012 jreidinger@suse.com
- add explicit buildrequires for autotools
- use license format conforming SPDX
* Tue Jun  7 2011 jengelh@medozas.de
- update to deutex-4.4.902
- start specfile afresh
* Mon Aug 23 2010 jengelh@medozas.de
- (imported changelog entry from non-Fedora based spec file)
  * deutex-4.4.0 package
  * fixed crash in check_types
  * fix types such that deutex works on 64-bit
* Sat Nov  8 2008 prusnak@suse.cz
- fix overflows (overflow.patch)
* Sun Dec 23 2007 claes.backstrom@fsfe.org
- Initial package built from Fedora package (4.4.0-6)
