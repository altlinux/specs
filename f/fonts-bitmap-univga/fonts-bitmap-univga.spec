%define cname univga
%define fdate 20021031
%define fontsdir %_datadir/fonts/bitmap/univga
%define charmapdir /usr/share/i18n/charmaps

Name: fonts-bitmap-univga
Version: 0.0.%fdate
Release: alt3.1
Summary: Unicode VGA font for X11
Summary(ru_RU.CP1251): Ўрифт Unicode VGA дл€ X11
License: X11
Group: System/Fonts/X11 bitmap
URL: http://www.inp.nsk.su/~bolkhov/files/fonts/univga/
BuildArch: noarch

# http://www.inp.nsk.su/~bolkhov/files/fonts/univga/uni-vga.tgz
Source0: uni-vga-%fdate.tar.bz2

# http://www.inp.nsk.su/~bolkhov/files/fonts/univga/
Source1: univga.html

Source2: uni-vga-utils-0.3.tar.bz2

Patch0: uni_vga-20021031-alt-fixnames.patch

PreReq: fontconfig mkfontdir

# for /usr/share/fonts/bitmap in default config
Requires: fontconfig >= 2.4.2

Obsoletes: univga-fonts-bitmap < %version-%release
Provides: univga-fonts-bitmap = %version-%release

Obsoletes: xfonts-uni-vga < %version-%release
Provides: xfonts-uni-vga = %version-%release

# Automatically added by buildreq on Sun May 21 2006
BuildRequires: bdftopcf glibc-i18ndata

%description
UNI-VGA is a constant-width Unicode font with VGA-style characters,
originally created to be a single source of fonts for console and
XDosEmu.  This package contains the X11 version of this font in both
8x16 and 9x16 sizes.  Fonts are available both in the Unicode encoding
(iso10646-1) and in the traditional 8-bit encodings
(iso8859-{1..10,13..16}, microsoft-cp{1250..1256}, koi8-r, koi8-u,
paratype-cp154).

%description -l ru_RU.CP1251
UNI-VGA - моноширинный шрифт Unicode с символами в стиле VGA, изначально
созданный как общий источник шрифтов дл€ консоли и XDosEmu. Ётот пакет
содержит версию этого шрифта дл€ X11 с размерами 8x16 и 9x16. Ўрифты
доступны как в кодировке Unicode (iso10646-1), так и в обычных 8-битовых
кодировках (iso8859-{1..10,13..16}, microsoft-cp{1250..1256}, koi8-r,
koi8-u, paratype-cp154).

%prep
%setup -q -n uni_vga -a 2
%patch0 -p1
subst 's/iso10646/ISO10646/i' u_vga16.bdf
cp -p %SOURCE1 univga.html

%build
perl bdf8to9.pl -f VGA9 -l linedraw.lst -o u_vga16_9.bdf u_vga16.bdf

encodings="
ISO-8859-1	iso8859-1
ISO-8859-2	iso8859-2
ISO-8859-3	iso8859-3
ISO-8859-4	iso8859-4
ISO-8859-5	iso8859-5
ISO-8859-6	iso8859-6
ISO-8859-7	iso8859-7
ISO-8859-8	iso8859-8
ISO-8859-9	iso8859-9
ISO-8859-10	iso8859-10
ISO-8859-13	iso8859-13
ISO-8859-14	iso8859-14
ISO-8859-15	iso8859-15
ISO-8859-16	iso8859-16
CP1250		microsoft-cp1250
CP1251		microsoft-cp1251
CP1252		microsoft-cp1252
CP1253		microsoft-cp1253
CP1254		microsoft-cp1254
CP1255		microsoft-cp1255
CP1256		microsoft-cp1256
CP1257		microsoft-cp1257
CP1258		microsoft-cp1258
KOI8-R		koi8-r
KOI8-U		koi8-u
PT154		paratype-cp154
"

for bdf in u_vga16.bdf u_vga16_9.bdf; do
	sh bdfconv.sh "$bdf" %charmapdir $encodings
done

for bdf in *.bdf; do
	bdftopcf "$bdf" | gzip -9f >"${bdf%.bdf}.pcf.gz"
done

%install
mkdir -p $RPM_BUILD_ROOT%fontsdir
install -p -m 444 *.pcf.gz $RPM_BUILD_ROOT%fontsdir/
touch $RPM_BUILD_ROOT%fontsdir/fonts.dir

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/X11/fontpath.d
ln -s ../../..%fontsdir $RPM_BUILD_ROOT%_sysconfdir/X11/fontpath.d/bitmap-%cname:unscaled:pri=20

%post
%_bindir/mkfontdir %fontsdir ||:
%_bindir/fc-cache %fontsdir ||:

%triggerun -- %name <= 0.0.20021031-alt3
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %fontsdir ||:
fi

%files
%doc univga.html
%_sysconfdir/X11/fontpath.d/*
%dir %fontsdir
%fontsdir/*.pcf.gz
%ghost %fontsdir/fonts.dir

%changelog
* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20021031-alt3.1
- NMU:
  + used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Sun May 21 2006 Sergey Vlasov <vsu@altlinux.ru> 0.0.20021031-alt3
- Renamed to fonts-bitmap-univga according to new fonts packaging conventions.
- Relocated fonts to /usr/share/fonts/bitmap/univga.
- Moved mkfontdir call from %%build to %%post, added mkfontdir to PreReq.
- Added fonts.dir to package as %%ghost.
- Now fontconfig >= 2.3.2-alt7 is required (previous releases did not have
  /usr/share/fonts/bitmap in the default config).
- Spec file cleanup (reordered header tags).
- Replaced sed usage in %%build with shell substitutions.
- Removed all %%__* macros from spec.
- Added "< %%version-%%release" to Obsoletes.
- Updated BuildRequires.

* Mon Jun 07 2004 Sergey Vlasov <vsu@altlinux.ru> 0.0.20021031-alt2
- Renamed to univga-fonts-bitmap according to the fonts packaging conventions.
- Relocated fonts to /usr/share/fonts/default/Bitmap-univga.
- Added fc-cache call to %%post, updated PreReq appropriately.
- Added fonts.cache-1 to package as %%ghost.
- Fixed permissions in src.rpm.
- Fixed uni-vga-utils/bdf8to9.pl for new perl.

* Sat Nov 09 2002 Sergey Vlasov <vsu@altlinux.ru> 0.0.20021031-alt1
- Version 20021031 (still no version number on the original file).
- Updated fix patch (only glyph name fixes now).
- Updated scripts to accept gzip/bzip2-compressed glibc charmap files.
- Added microsoft-cp1256 encoding (no more missing characters).
- Fixed description; added Russian description.
- Updated BuildRequires.

* Sun Nov 25 2001 Sergey Vlasov <vsu@altlinux.ru> 0.0.20010608-alt1
- First build for ALT Linux
